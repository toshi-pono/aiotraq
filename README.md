# AiotraQ

async ready API wrapper and bot library for [traQ](https://github.com/traPtitech/traQ) written in Python.

[![PyPI - Version](https://img.shields.io/pypi/v/aiotraq?label=aiotraq)](https://pypi.org/project/aiotraq/)
[![PyPI - Version](https://img.shields.io/pypi/v/aiotraq-bot?label=aiotraq-bot)](https://pypi.org/project/aiotraq-bot/)
[![PyPI - Version](https://img.shields.io/pypi/v/aiotraq-message?label=aiotraq-message)](https://pypi.org/project/aiotraq-message/)
[![CI](https://github.com/toshi-pono/aiotraq/actions/workflows/ci.yml/badge.svg)](https://github.com/toshi-pono/aiotraq/actions/workflows/ci.yml)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/toshi-pono/aiotraq/blob/main/LICENSE)

![teaser](docs/static/img/aiotraq.png)

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

### aiotraq

API Client の更新: monorepo のプロジェクトルートで以下を実行してください

```bash
poetry install
make api_update
```

## License

This project is licensed under the terms of the MIT license.
