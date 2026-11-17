# Security maintenance for v0.2

`v0.2` is the maintenance branch. `main` develops the current release line.
Version 0.2.6 preserves Python >=3.8 for `aiotraq` and Python >=3.10 for
`aiotraq-bot` / `aiotraq-message`. The 0.3 release line requires Python >=3.11.

## What 0.2.6 changes

Security minimums are recorded in the distributed package metadata, not only
in development lock files: certifi >=2026.10.19, idna >=3.15,
Starlette >=1.3.1, and python-dotenv >=1.2.2 where used. FastAPI is updated
alongside Starlette. Python >=3.10 uses AnyIO >=4.14.2; Python >=3.11 uses
Pillow >=13.0.0.

The API source distribution uses Poetry Core 1.9.1 when built on Python 3.8/3.9
and 2.4.0 on newer Python, so source installs preserve the declared compatibility.
Both backend versions had no published PyPI advisories at verification time.

All four Poetry lock files are refreshed. Each package includes the MIT license
and its `py.typed` marker in both wheel and source distributions. API generation is deliberately disabled on this branch and its generator
dependency is removed. Generate API updates on `main` with the patched generator,
then backport reviewed Python 3.8-compatible code. Running `make api_update` or
`make api_generate` here fails with this instruction. The existing generated
client is preserved; updating a generator alone would not repair previously
generated code.

## Known residual vulnerabilities on older Python

**0.2.6 is a partial security update. It does not make old Python environments
free of known vulnerabilities.** The exceptions below keep the explicitly
supported Python versions installable; they are not assertions that the
vulnerabilities are harmless or unreachable in applications using this library.

| Environment | Dependency | Remaining risk | Upgrade path |
| --- | --- | --- | --- |
| API client on Python 3.8 | AnyIO 4.5.2 | GHSA-82r6-8w77-94w6 (IDN TLS validation), GHSA-5p39-cfhj-2xmp (process-worker stderr deadlock) | Python >=3.10 and AnyIO >=4.14.2 |
| API client on Python 3.9 | AnyIO 4.12.1 | Same two advisories | Python >=3.10 and AnyIO >=4.14.2 |
| Message library on Python 3.10 | Pillow 12.3.0 | Multiple image parser / encoder memory safety, information disclosure and denial-of-service advisories; fixes require Pillow 13 | Python >=3.11 and Pillow >=13.0.0, preferably the 0.3 release line |

The complete version-, source-, and advisory-specific exception list lives in
[.github/security-exceptions.json](.github/security-exceptions.json). It expires
on **2027-02-17** and must be reviewed rather than extended automatically. The
2026-11-17 runtime audit reported 42 Pillow advisories on Python 3.10 and two
AnyIO advisories on each of Python 3.8 and 3.9. GitHub also lists
GHSA-rfgq-q3w2-pmv2 for Pillow 12.3.0; databases can differ in coverage. The
same clean installation on Python 3.11 had no known dependency vulnerabilities
at the time of this audit. Newly published advisories still require review.

Do not process untrusted images on the Python 3.10 compatibility environment.
Avoid untrusted internationalized hostnames and AnyIO process-pool tasks on
Python 3.8/3.9. These restrictions reduce exposure; upgrading is the remediation.
The library's own image helper writes PNG, and the built-in Bot endpoint accepts
JSON, but downstream applications can use additional Pillow and Starlette
features. Feature usage alone is not a reason to dismiss every related alert.

## Updating installations

Updating this repository's locks does not update deployed applications.
Re-resolve application dependencies after upgrading, audit the resulting
installation, and rebuild images / restart processes to use the repaired
libraries. Prefer Python >=3.11 and the latest release line for new deployments.

## Maintenance rules

Backport security and compatibility fixes to `v0.2` without raising its declared
Python minimums. Keep security exceptions narrow and time-limited. Do not
silently use an old vulnerable dependency on newer Python: environment markers
must select the repaired version wherever it is supported.

Releases are prepared and tested separately for each branch. Publishing to
TestPyPI or PyPI, creating release tags, and GitHub releases require maintainer
review of the exact commits and the residual-risk report first.
