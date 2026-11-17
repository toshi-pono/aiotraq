"""Shared release checks. Run with the tooling Python (3.11 or newer)."""

import argparse
import email
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tomllib
import zipfile

from packaging.specifiers import SpecifierSet

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = {"aiotraq": "libs/aiotraq", "aiotraq-bot": "libs/bot", "aiotraq-message": "libs/message"}


def projects():
    return {
        name: tomllib.loads((ROOT / folder / "pyproject.toml").read_text())["tool"]["poetry"]
        for name, folder in PACKAGES.items()
    }


def metadata(release_branch=None):
    subprocess.run([sys.executable, str(ROOT / "scripts/version.py"), "--check"], check=True)
    root = tomllib.loads((ROOT / "pyproject.toml").read_text())["tool"]["poetry"]
    version = root["version"]
    legacy = version.startswith("0.2.")
    expected_branch = "v0.2" if legacy else "main"
    if release_branch and release_branch != expected_branch:
        raise ValueError(f"{version} must be released from {expected_branch}, not {release_branch}")
    if not legacy and not version.startswith("0.3."):
        raise ValueError(f"Unconfigured release series: {version}")
    for name, project in projects().items():
        if project["version"] != version:
            raise ValueError(f"{name} version does not match {version}")
        minimum = "3.8" if legacy and name == "aiotraq" else "3.10" if legacy else "3.11"
        supported = SpecifierSet(project["dependencies"]["python"])
        if minimum not in supported:
            raise ValueError(f"{name} must support Python {minimum}")
        previous = f"3.{int(minimum.split('.')[1]) - 1}"
        if previous in supported:
            raise ValueError(f"{name} must declare its Python {minimum} minimum")
    generator = (ROOT / "api-client-config.yaml").read_text()
    if f"package_version_override: {version}" not in generator:
        raise ValueError("API generator version is out of sync")
    matrix = [{"python": p, "api-only": False} for p in (["3.10"] if legacy else []) + ["3.11", "3.12", "3.14"]]
    if legacy:
        matrix += [{"python": p, "api-only": True} for p in ["3.8", "3.9"]]
    if output := os.environ.get("GITHUB_OUTPUT"):
        with open(output, "a") as stream:
            stream.write(f"version={version}\nmatrix={json.dumps({'include': matrix})}\n")
    print(f"Release {version}; runtime matrix: {json.dumps(matrix)}")
    return version


def build():
    metadata()
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    for pattern in ("*.whl", "*.tar.gz"):
        for old in dist.glob(pattern):
            old.unlink()
    for folder in PACKAGES.values():
        subprocess.run(["poetry", "-C", str(ROOT / folder), "build", "--output", str(dist)], check=True)
    artifacts()


def artifacts():
    version = metadata()
    dist = ROOT / "dist"
    for name, project in projects().items():
        module = name.replace("-", "_")
        wheels = list(dist.glob(f"{module}-{version}-*.whl"))
        sdists = list(dist.glob(f"{module}-{version}.tar.gz"))
        if len(wheels) != 1 or len(sdists) != 1:
            raise ValueError(f"Expected one wheel and sdist for {name} {version}")
        with zipfile.ZipFile(wheels[0]) as wheel:
            names = wheel.namelist()
            meta_name = next(p for p in names if p.endswith(".dist-info/METADATA"))
            meta = email.message_from_bytes(wheel.read(meta_name))
            if meta["Name"] != name or meta["Version"] != version:
                raise ValueError(f"Incorrect distribution metadata: {wheels[0]}")
            if SpecifierSet(meta["Requires-Python"]) != SpecifierSet(project["dependencies"]["python"]):
                raise ValueError(f"Incorrect Requires-Python: {name}")
            if f"{module}/py.typed" not in names:
                raise ValueError(f"Missing py.typed: {name}")
            if not any(Path(p).name.upper().startswith("LICENSE") for p in names):
                raise ValueError(f"Missing license in wheel: {name}")
            if any("file:" in r or " @ " in r for r in meta.get_all("Requires-Dist", [])):
                raise ValueError(f"Local/URL dependency leaked into {name}")
            print(f"{name}: {meta['Requires-Python']}; {meta.get_all('Requires-Dist', [])}")
        with tarfile.open(sdists[0]) as sdist:
            if not any(Path(p).name.upper().startswith("LICENSE") for p in sdist.getnames()):
                raise ValueError(f"Missing license in sdist: {name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["metadata", "build", "artifacts"])
    parser.add_argument("--release-branch")
    args = parser.parse_args()
    if args.command == "metadata":
        metadata(args.release_branch)
    elif args.command == "build":
        build()
    else:
        artifacts()
