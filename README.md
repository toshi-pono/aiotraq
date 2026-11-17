# AiotraQ

async ready API wrapper and bot library for [traQ](https://github.com/traPtitech/traQ) written in Python.

[![PyPI - Version](https://img.shields.io/pypi/v/aiotraq?label=aiotraq)](https://pypi.org/project/aiotraq/)
[![PyPI - Version](https://img.shields.io/pypi/v/aiotraq-bot?label=aiotraq-bot)](https://pypi.org/project/aiotraq-bot/)
[![PyPI - Version](https://img.shields.io/pypi/v/aiotraq-message?label=aiotraq-message)](https://pypi.org/project/aiotraq-message/)
[![CI](https://github.com/toshi-pono/aiotraq/actions/workflows/ci.yml/badge.svg)](https://github.com/toshi-pono/aiotraq/actions/workflows/ci.yml)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/toshi-pono/aiotraq/blob/main/LICENSE)

![teaser](docs/static/img/aiotraq.png)

## Maintenance release line

This is the `v0.2` maintenance branch. Version **0.2.6** preserves Python >=3.8
for `aiotraq` and Python >=3.10 for `aiotraq-bot` / `aiotraq-message`.
`main` contains the Python >=3.11 release line.

**Older Python environments retain known dependency vulnerabilities.** Read
[SECURITY.md](SECURITY.md) before using 0.2.6, and prefer Python >=3.11 for
new deployments. Backports keep the existing Python minimums; features and
Python support changes belong on `main`.

## Installation

```bash
pip install aiotraq
pip install aiotraq-bot
pip install aiotraq-message
```

## Projects

詳細は各リンク先を参照してください。

| Name                                                                            | Description                              | Version                                                                                                                             |
| ------------------------------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| [AiotraQ](https://github.com/toshi-pono/aiotraq/tree/main/libs/aiotraq)         | 非同期リクエスト対応の traQ API ラッパー | [![PyPI - Version](https://img.shields.io/pypi/v/aiotraq?label=aiotraq)](https://pypi.org/project/aiotraq/)                         |
| [AiotraQ-Bot](https://github.com/toshi-pono/aiotraq/tree/main/libs/bot)         | FastAPI を使った traQ Bot ライブラリ     | [![PyPI - Version](https://img.shields.io/pypi/v/aiotraq-bot?label=aiotraq-bot)](https://pypi.org/project/aiotraq-bot/)             |
| [AiotraQ-Message](https://github.com/toshi-pono/aiotraq/tree/main/libs/message) | traQ Bot のメッセージ送信ライブラリ      | [![PyPI - Version](https://img.shields.io/pypi/v/aiotraq-message?label=aiotraq-message)](https://pypi.org/project/aiotraq-message/) |

![overview](docs/docs/overview.svg)

ドキュメントは [こちら](https://toshi-pono.github.io/aiotraq/docs/intro/)

## Development

### API client maintenance

API generation is disabled on `v0.2`. Generate updates on `main` with its patched
generator, review the changes, and backport only Python 3.8-compatible code.
`make api_update` and `make api_generate` fail intentionally on this branch.
The hand-maintained `post_webhook` implementation must be preserved when
backporting API changes.

## Release preparation

Use Poetry 2.4.1. Run `python scripts/version.py <version>` from the repository
root, refresh all affected locks, then validate the built wheel / sdist and
runtime tests before release. `make write-version` synchronizes the version
from the root `pyproject.toml`, including the API generator and docs metadata.

The release workflow is dispatched for the reviewed branch and commit only.
Do not publish while tests or dependency audits have unexplained failures.
For `v0.2`, review the scoped security exceptions in [SECURITY.md](SECURITY.md).
The maintainer must approve the final release before publishing either series.

## License

This project is licensed under the terms of the MIT license.
