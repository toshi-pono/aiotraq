"""Regression checks for the security audit gate."""

from datetime import date, timedelta
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import audit


class AuditPolicyTests(unittest.TestCase):
    def setUp(self):
        self.exception = {
            "package": "Pillow",
            "versions": ["12.3.0"],
            "sources": ["runtime:3.10"],
            "ids": ["GHSA-example"],
            "reason": "The fixed release requires Python 3.11; tracked in SECURITY.md.",
            "expires_on": str(date.today() + timedelta(days=30)),
        }
        self.dependency = {"name": "pillow", "version": "12.3.0"}
        self.vulnerability = {"id": "CVE-example", "aliases": ["GHSA-example"]}

    def test_exception_is_scoped_to_version_source_and_advisory(self):
        self.assertTrue(audit.excepted(self.dependency, self.vulnerability, "runtime:3.10", [self.exception]))
        self.assertFalse(audit.excepted(self.dependency, self.vulnerability, "runtime:3.11", [self.exception]))
        self.assertFalse(
            audit.excepted(
                {**self.dependency, "version": "12.2.0"}, self.vulnerability, "runtime:3.10", [self.exception]
            )
        )
        self.assertFalse(audit.excepted(self.dependency, {"id": "GHSA-new"}, "runtime:3.10", [self.exception]))

    def test_expired_exception_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "exceptions.json"
            entry = {**self.exception, "expires_on": str(date.today() - timedelta(days=1))}
            path.write_text(json.dumps({"exceptions": [entry]}))
            with self.assertRaisesRegex(ValueError, "Expired"):
                audit.load_exceptions(path)

    def test_every_marker_version_is_audited(self):
        batches = []

        def fake_audit(command):
            requirement = Path(command[command.index("-r") + 1])
            packages = [
                dict(zip(("name", "version"), line.split("=="))) for line in requirement.read_text().splitlines()
            ]
            self.assertEqual(len(packages), len({p["name"] for p in packages}))
            batches.extend(packages)
            output = Path(command[command.index("--output") + 1])
            output.write_text(json.dumps({"dependencies": [{**p, "vulns": []} for p in packages]}))
            return SimpleNamespace(returncode=0)

        packages = [{"name": "anyio", "version": "4.5.2"}, {"name": "anyio", "version": "4.14.2"}]
        with tempfile.TemporaryDirectory() as directory, patch("audit.subprocess.run", side_effect=fake_audit):
            self.assertFalse(audit.audit(packages, "poetry.lock", [], Path(directory)))
        self.assertCountEqual(batches, packages)

    def test_incomplete_audit_fails_closed(self):
        def incomplete(command):
            Path(command[command.index("--output") + 1]).write_text('{"dependencies": []}')
            return SimpleNamespace(returncode=0)

        with tempfile.TemporaryDirectory() as directory, patch("audit.subprocess.run", side_effect=incomplete):
            with self.assertRaisesRegex(RuntimeError, "every dependency"):
                audit.audit([self.dependency], "runtime:3.10", [], Path(directory))


if __name__ == "__main__":
    unittest.main()
