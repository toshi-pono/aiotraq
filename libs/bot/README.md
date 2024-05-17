# aiotraq-bot

Async ready traQ Bot library written in Python.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/toshi-pono/aiotraq/blob/main/LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/aiotraq-bot)](https://pypi.org/project/aiotraq-bot/)

## Requirements

aiotraq-bot は以下のライブラリを使用しています。

- [FastAPI](https://fastapi.tiangolo.com/): サーバーの実装
- [Uvicorn](https://www.uvicorn.org/): サーバーの実行
- [Pydantic](https://docs.pydantic.dev/latest/): データのバリデーション

## Installation

```bash
pip install aiotraq-bot
```

## Usage

`TraqHttpBot` を使って http bot を作成することができます。

`traQ->BOTサーバー`へのイベント受け取り部分を補助します。
`BOTサーバー->traQ`へのイベント送信は [aiotraq](https://github.com/toshi-pono/aiotraq/tree/main/libs/aiotraq) 等を利用してください。

```python
import os
from aiotraq_bot import TraqHttpBot

bot = TraqHttpBot(verification_token=os.getenv("BOT_VERIFICATION_TOKEN"))

@bot.event()
async def on_message(payload: MessageCreatedPayload):
    print(payload)

if __name__ == "__main__":
  bot.run()
```

### Event handler の登録

イベントの登録は `@bot.event()` デコレータを使って行うことができます。
event の引数として対象のイベントを指定するか、関数の型ヒントを使って指定することができます。

`MESSAGE_CREATED` イベントを型ヒントを使って指定する場合

```python
@bot.event()
async def on_message(payload: MessageCreatedPayload):
    print(payload)
```

`MESSAGE_CREATED`イベントを引数を用いて指定する場合

```python
@bot.event("MESSAGE_CREATED")
async def on_message(payload):
    print(payload)
```

## Acknowledgements

This project is inspired by [python-traq-bot](https://github.com/eyemono-moe/python-traq-bot).

## License

This project is licensed under the terms of the MIT license.
