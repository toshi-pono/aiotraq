"""Audit every locked version or a clean wheel installation; exceptions are exact and expire."""

import argparse
from datetime import date
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]
INTERNAL = {"aiotraq", "aiotraq-bot", "aiotraq-message"}
LOCKS = ["poetry.lock", "libs/aiotraq/poetry.lock", "libs/bot/poetry.lock", "libs/message/poetry.lock"]


def normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def load_exceptions(path):
    entries = json.loads(path.read_text())["exceptions"]
    for entry in entries:
        for key in ("package", "versions", "sources", "ids", "reason", "expires_on"):
            if not entry.get(key):
                raise ValueError(f"Missing {key} in audit exception")
        if date.fromisoformat(entry["expires_on"]) < date.today():
            raise ValueError(f"Expired audit exception: {entry['package']}: {entry['reason']}")
    return entries


def excepted(dependency, vulnerability, source, exceptions):
    ids = {vulnerability["id"], *vulnerability.get("aliases", [])}
    return any(
        normalize(entry["package"]) == normalize(dependency["name"])
        and dependency["version"] in entry["versions"]
        and source in entry["sources"]
        and ids.intersection(entry["ids"])
        for entry in exceptions
    )


def audit(packages, source, exceptions, report_dir):
    # Internal distributions are the code under test, not index dependencies.
    pins = sorted({(normalize(p["name"]), p["version"]) for p in packages if normalize(p["name"]) not in INTERNAL})
    if not pins:
        raise ValueError(f"No dependencies collected for {source}")
    report = report_dir / (source.replace("/", "-").replace(":", "-") + ".json")
    # A Poetry lock may contain different versions for different Python markers.
    # pip-audit rejects repeated names; audit every version in separate batches.
    batches = []
    for name, version in pins:
        for batch in batches:
            if name not in batch:
                batch[name] = version
                break
        else:
            batches.append({name: version})
    data = {"dependencies": []}
    with tempfile.TemporaryDirectory() as temp:
        requirement = Path(temp) / "requirements.txt"
        batch_report = Path(temp) / "audit.json"
        for batch in batches:
            requirement.write_text("".join(f"{name}=={version}\n" for name, version in batch.items()))
            batch_report.unlink(missing_ok=True)
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip_audit",
                    "-r",
                    str(requirement),
                    "--no-deps",
                    "--disable-pip",
                    "--strict",
                    "--format=json",
                    "--aliases=on",
                    "--progress-spinner=off",
                    "--output",
                    str(batch_report),
                ]
            )
            if result.returncode not in (0, 1) or not batch_report.is_file():
                raise RuntimeError(f"Audit failed to complete for {source}")
            data["dependencies"].extend(json.loads(batch_report.read_text())["dependencies"])
    report.write_text(json.dumps(data, indent=2) + "\n")
    actual = {(normalize(d["name"]), d.get("version")) for d in data["dependencies"]}
    if set(pins) != actual or any(d.get("skip_reason") for d in data["dependencies"]):
        raise RuntimeError(f"Audit did not inspect every dependency in {source}")
    failures = []
    accepted = []
    for dependency in data["dependencies"]:
        for vulnerability in dependency.get("vulns", []):
            record = f"{dependency['name']}=={dependency['version']} {vulnerability['id']}"
            if excepted(dependency, vulnerability, source, exceptions):
                accepted.append(record)
            else:
                failures.append(record)
    print(f"{source}: {len(pins)} dependencies, {len(failures)} unresolved, {len(accepted)} documented exceptions")
    for record in accepted:
        print(f"  EXCEPTION: {record}")
    for record in failures:
        print(f"  FAIL: {record}")
    return bool(failures)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--installed", type=Path, help="JSON from target Python's pip list --format=json")
    parser.add_argument("--python-version", help="Target runtime version, e.g. 3.10")
    parser.add_argument("--exceptions", type=Path, default=ROOT / ".github/security-exceptions.json")
    parser.add_argument("--report-dir", type=Path, default=ROOT / "audit-reports")
    args = parser.parse_args()
    args.report_dir.mkdir(parents=True, exist_ok=True)
    exceptions = load_exceptions(args.exceptions)
    if args.installed:
        if not args.python_version:
            parser.error("--installed requires --python-version")
        groups = [(f"runtime:{args.python_version}", json.loads(args.installed.read_text()))]
    else:
        groups = [(path, tomllib.loads((ROOT / path).read_text())["package"]) for path in LOCKS]
    failed = False
    for source, packages in groups:
        failed = audit(packages, source, exceptions, args.report_dir) or failed
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
