# aiotraq-message

streamlit 風の構文を用いてインタラクティブなメッセージ送信に対応するプラグインです。

[![PyPI - Version](https://img.shields.io/pypi/v/aiotraq-message?label=aiotraq-message)](https://pypi.org/project/aiotraq-message/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/toshi-pono/aiotraq/blob/main/LICENSE)
[![CI](https://github.com/toshi-pono/aiotraq/actions/workflows/ci.yml/badge.svg)](https://github.com/toshi-pono/aiotraq/actions/workflows/ci.yml)

## Installation

```bash
pip install aiotraq-message
```

## Requirements

aiotraq-message は aiotraq に依存しています

- [aiotraq](https://github.com/toshi-pono/aiotraq/tree/main/libs/aiotraq)
- [aiotraq-bot](https://github.com/toshi-pono/aiotraq/tree/main/libs/bot)

## Usage

```python
import os
import asyncio
from aiotraq_bot import TraqHttpBot
from aiotraq_message import TraqMessage

async def component(am: TraqMessage, *args):
    am.write("Hello, World!")

    with am.spinner():
        # heavy task
        asyncio.sleep(3)

    am.write(":done: Done!")

bot = TraqHttpBot(verification_token=os.getenv("BOT_VERIFICATION_TOKEN"))
response = TraqMessageManager(bot, os.getenv("BOT_ACCESS_TOKEN"), "https://q.trap.jp/api/v3")


@bot.event("MESSAGE_CREATED")
async def on_message_created(payload) -> None:
    channel_id = payload.message.channelId

    await response(component, channnel_id=channel_id)

if __name__ == "__main__":
    bot.run()
```

### Component

write, spinner, clear などのメソッドを使うことができます

- write: メッセージを送信します
- spinner: スピナーを表示します
- clear: 送信したメッセージを空にします

## License

This project is licensed under the terms of the MIT license.
