"""Synchronize release metadata from the root pyproject (Python 3.11+ tooling)."""

import argparse
import json
from pathlib import Path
import re
import tomllib


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", nargs="?", help="Explicit release version, e.g. 0.3.0")
    parser.add_argument("--check", action="store_true", help="Check without modifying files")
    args = parser.parse_args()
    root = ROOT / "pyproject.toml"
    current = tomllib.loads(root.read_text())["tool"]["poetry"]["version"]
    version = args.version or current
    if not re.fullmatch(r"0\.[23]\.\d+(?:(?:a|b|rc)\d+)?", version):
        parser.error("Expected a 0.2.x or 0.3.x release version (optionally a/b/rc).")
    changes = {}
    for path in [root, *(ROOT / "libs" / p / "pyproject.toml" for p in ("aiotraq", "bot", "message"))]:
        before = path.read_text()
        after, count = re.subn(r'^version = "[^"]+"', f'version = "{version}"', before, count=1, flags=re.M)
        if count != 1:
            raise ValueError(f"Missing project version: {path}")
        if after != before:
            changes[path] = after
    config = ROOT / "api-client-config.yaml"
    before = config.read_text()
    after, count = re.subn(r"^package_version_override: .+$", f"package_version_override: {version}", before, flags=re.M)
    if count != 1:
        raise ValueError("Missing generator version override")
    if after != before:
        changes[config] = after
    package = ROOT / "docs/package.json"
    doc = json.loads(package.read_text())
    if doc["version"] != version:
        doc["version"] = version
        changes[package] = json.dumps(doc, indent=2) + "\n"
    lock = ROOT / "docs/package-lock.json"
    doc = json.loads(lock.read_text())
    if doc["version"] != version or doc["packages"][""]["version"] != version:
        doc["version"] = doc["packages"][""]["version"] = version
        changes[lock] = json.dumps(doc, indent=2) + "\n"
    if args.check and changes:
        parser.exit(1, "Version mismatch: " + ", ".join(str(p.relative_to(ROOT)) for p in changes) + "\n")
    for path, content in changes.items():
        path.write_text(content)
    print(f"Release metadata {'checked' if args.check else 'synchronized'}: {version}")
    if changes and not args.check:
        print("Refresh the root Poetry lock after changing local package versions.")


if __name__ == "__main__":
    main()
