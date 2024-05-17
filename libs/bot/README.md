# aiotraq-bot

Async ready traQ Bot library written in Python.

## Installation

TODO

## Usage

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
