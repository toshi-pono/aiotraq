# Changelog

## 0.3.0 — prepared, not yet released

- Require Python 3.11+ for API, Bot and Message packages.
- Enforce repaired dependency minimums in distribution metadata, including
  Pillow 13, AnyIO, certifi, idna, Starlette and python-dotenv. Update all locks.
- Support current NumPy / pandas versions and verify image and dataframe helpers.
- Upgrade the API generator to the patched 0.29.1 release. Use its escaped code
  templates instead of old copied templates; preserve the shipped generated
  client and manually maintained webhook endpoint in this release.
- Include MIT licenses and typing markers in each wheel and source distribution.
- Add clean-wheel runtime tests, dependency audits, weekly maintenance updates
  and a preparation-only default for release workflows.
- Update the documentation toolchain and verify its transitive dependency
  overrides with integration tests.

Migration: use Python 3.11+, upgrade the packages and re-resolve application
dependencies. Applications requiring Python 3.8–3.10 should use the compatible
0.2 line and read its residual-risk report. See [SECURITY.md](SECURITY.md).

## 0.2.6 — prepared separately on `v0.2`

- Preserve API Python 3.8+ and Bot / Message Python 3.10+.
- Backport compatible dependency security fixes. Select newer repaired
  dependencies on newer Python using environment markers.
- Document remaining AnyIO vulnerabilities on Python 3.8/3.9 and Pillow
  vulnerabilities on Python 3.10 with narrowly scoped, expiring audit exceptions.
- Backport distribution validation, runtime tests, CI and documentation fixes.
- Disable API regeneration on the maintenance branch; generate on main and
  backport reviewed Python-compatible code.

This is a partial security update for legacy environments. Prefer the 0.3 line
for deployments able to use Python 3.11+.
