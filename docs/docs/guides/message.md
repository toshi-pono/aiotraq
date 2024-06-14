---
id: message-guide
title: メッセージ送信
sidebar_label: Message
---

このガイドでは、`AiotraQ`を用いたメッセージの送信方法について紹介します。

## メッセージの送信

`TraqMessageManager`を用いてメッセージ送信用のマネージャーを作成します。
メッセージの送信先は、`channel_id`または`user_id`を指定することで行います。

:::info
`user_id`を指定した場合、DM が送信されます
:::

```python
import os
import asyncio
from aiotraq_bot import TraqHttpBot
from aiotraq_message import TraqMessage

async def component(am: TraqMessage, payload: str):
    am.write("Hello, World!")
    am.write(payload)

    with am.spinner():
        # heavy task
        asyncio.sleep(3)

    am.write(":done: Done!")

bot = TraqHttpBot(verification_token=os.getenv("BOT_VERIFICATION_TOKEN"))
response = TraqMessageManager(bot, os.getenv("BOT_ACCESS_TOKEN"), "https://q.trap.jp/api/v3", "https://q.trap.jp")


@bot.event("MESSAGE_CREATED")
async def on_message_created(payload) -> None:
    channel_id = payload.message.channelId
    message = payload.message.plainText

    await response(component, channnel_id=channel_id, payload=message)

if __name__ == "__main__":
    bot.run(port=8080)
```

## コンポーネント

コンポーネントは、メッセージ送信時に平行に実行されます。
コンポーネントは、`TraqMessage`を引数に取り、メッセージの送信を行います。
また、コンポーネント登録時に渡した任意の`payload`を受け取ることができます。

:::tip
traQ の負荷を減らすため、メッセージ送信/更新は、最小で 1 秒間隔で行われます
:::

```python
async def component(am: TraqMessage, payload: str):
    am.write(payload)
```

コンポーネントの第一引数には、`TraqMessage`が渡されます。これを用いて、多様なメッセージ送信を行うことができます。
メソッドの詳細は、[Components](/docs/api/components/components-overview/)を参照してください。

```python
async def component(am: TraqMessage, payload: str):
    # テキストメッセージの送信
    am.write("Hello, World!")

    # 画像の送信
    image = Image.open("image.png")
    am.image(image)

    # loading spinner の表示
    with am.spinner():
        # 重い処理
        asyncio.sleep(3)

    # メッセージの全削除
    am.clear()
```
