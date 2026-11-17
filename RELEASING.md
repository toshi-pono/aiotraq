# Releasing the maintained package lines

`main` is the current development line (0.3.x, Python 3.11+). `v0.2` is the
maintenance line (API Python 3.8+, Bot / Message Python 3.10+). Keep the three
packages on the same release number within each line. Backport selected fixes
to `v0.2`; do not merge `main` wholesale because that would raise its Python
requirements. Changes to shared CI should be applied to both branches.

## Prepare a reviewed commit

1. Make compatible fixes in the appropriate branch, including dependency floors
   in distribution metadata. Document residual risks on the maintenance branch.
2. Synchronize release metadata with `make write-version VERSION=0.3.0` (or
   `0.2.6`). Use Python 3.11+ for repository tooling on either branch.
3. Refresh Poetry locks using Poetry 2.4.1. `poetry lock` preserves unchanged
   resolutions; use targeted `poetry update PACKAGE --lock` or an explicitly
   reviewed full regeneration when dependency updates are intended. Refresh the
   root lock after changing local package versions. Never commit local file/path
   dependencies into a distributed library to make an unpublished version resolve.
4. Run CI: manifest/lock consistency, versions, lint, type checks, generator
   checks on main, all wheel/sdist builds, runtime tests and dependency audits.
   Include docs type checks, dependency integration tests and production build.
5. Review wheel `Requires-Python` / `Requires-Dist`, licenses and `py.typed`.
   Review exact audit exceptions and their expiry on `v0.2`.
6. Obtain maintainer approval for the exact release commit and release notes.
   Until approval, do not publish to TestPyPI/PyPI, create release tags or create
   a public GitHub Release.

The root project is a development workspace, not a fourth published package.
Internal dependency ranges may include published older compatible versions so
locks can resolve before release. CI installs all three newly built wheels in
one transaction. Security floors in Message also apply when older compatible
API/Bot packages are selected.

## GitHub Actions

The **Prepare or publish release** workflow accepts:

| Input | Value |
| --- | --- |
| Branch | `main` for 0.3.x, `v0.2` for 0.2.x |
| `version` | Exact committed version, e.g. `0.3.0` |
| `destination` | `prepare` (default), `testpypi`, or `pypi` |

`prepare` only validates and uploads a GitHub Actions artifact. It does not
publish distributions. Wrong branch/version combinations fail before publishing.
Every invocation rebuilds and validates its own artifacts from the invocation's
commit. Within that invocation, the publisher uses exactly those artifacts.
Review the commit again if it changes between preparation and publication.

Before the first approved publish, configure the `testpypi` and `pypi` GitHub
environments with required reviewers, restrict deployment branches to `main`
and `v0.2`, and verify Trusted Publishers for all three projects on both package
indexes. Match repository owner, repository, `release.yml` and environment name.
These settings are external to the repository and are not created by YAML.

TestPyPI and PyPI publication are separate explicit operations. There is no
automatic promotion from one to the other. Duplicate uploads fail rather than
being silently skipped. If publication stops halfway through the three packages,
inspect index files and their hashes before resuming; never rebuild and overwrite
the same version. Preserve the original validated artifact for recovery.

After approval and successful publication, create a Git tag matching the
existing convention (`0.2.6` or `0.3.0`) at the exact published commit, and a
GitHub Release with the reviewed notes. Test installation from PyPI in a clean
environment and record the package versions and dependency audit. Publish 0.2.6
before 0.3.0 when releasing both lines in the same maintenance window.

## Local validation

```bash
poetry install --with dev,api
make check-version
make lint
make test
python scripts/ci.py build
twine check --strict dist/*
python scripts/audit.py
```

`scripts/ci.py` and `scripts/audit.py` use a separate Python 3.11+ tooling
environment containing Poetry 2.4.1, packaging, Twine and pip-audit. For legacy
runtime tests, create an environment without bundled pip/setuptools and install
the wheels with modern host `uv pip --python` commands; this keeps build tools
separate from the library runtime under audit. The workflow defines the complete
Python matrix and commands.
