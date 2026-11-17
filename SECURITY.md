# Security maintenance

| Release line | Branch | Supported Python | Policy |
| --- | --- | --- | --- |
| 0.3.x | `main` | 3.11+ for every package | Current line; remediate known dependency vulnerabilities |
| 0.2.x | `v0.2` | `aiotraq`: 3.8+; Bot / Message: 3.10+ | Backport compatible security fixes without raising Python minimums |

The 0.2.6 release is a partial security update, not a guarantee that
legacy Python environments are free of known vulnerabilities. AnyIO fixes
require Python 3.10+, and Pillow 13 fixes require Python 3.11+. See the
[maintenance branch security report](https://github.com/toshi-pono/aiotraq/blob/v0.2/SECURITY.md)
for exact dependencies, advisories, mitigations and audit exceptions. Prefer
Python 3.11+ and the 0.3 line for new deployments.

## Dependency policy

Security minimums belong in the packages' `pyproject.toml` and resulting
`Requires-Dist` metadata, not only in `poetry.lock`. When an indirect dependency
needs a security floor that its parent does not enforce, add an explicit
constraint with a compatibility test. The Message package also enforces these
floors when used with compatible older API / Bot packages.

CI audits all versions in all four Python lock files, the dependencies selected
by clean wheel installations, and the documentation's npm dependency tree.
The 0.3 line has no audit exceptions. Maintenance exceptions name the exact
package version, audit source, advisory and review expiry date. New advisories,
unexpected versions, incomplete scans and expired exceptions fail CI.

Dependabot opens weekly updates for both branches. GitHub's security updates
target the default branch; the maintenance branch also relies on scheduled CI
audits and reviewed lockfile updates. A maintenance advisory requiring a new
dependency constraint must be backported manually; lockfile-only updates cannot
change the package's published minimum requirement.

An advisory withdrawn by its publisher is not an unresolved vulnerability.
Record that evidence when triaging GitHub alerts instead of introducing a broad
audit suppression. Dependency inclusion does not prove exploitability, but
unused features alone do not justify dismissing every advisory for a package.

## Deployed applications

Repository lock updates do not update applications already installed elsewhere.
After upgrading, re-resolve the application's dependencies, audit that resolved
environment, rebuild container images and restart processes. In particular,
certifi must be updated in the actual environment performing HTTPS requests.

## Reporting

Report suspected vulnerabilities privately to the repository maintainer before
publishing exploit details. Include affected versions, prerequisites and a
minimal reproducer that does not contain production credentials or user data.
