---
id: bot-guide
title: Botサーバーの作成
sidebar_label: Bot
---

このガイドでは、traQ の Bot サーバーを作成する方法について紹介します。

:::note
Bot サーバーの作成には Python 3.10 以上が必要です。
現在のバージョンでは、HTTP リクエストを受け取る Bot サーバーのみサポートしています。
:::
:::info
BOT イベントの詳細については [BOT イベント](/docs/api/bot-event) を参照してください。
:::

## HTTPBot サーバーの作成

`aiotraq_bot` を使用して Bot サーバーを作成します。
BOT は bot-console から取得できる `BOT_VERIFICATION_TOKEN` を使用して traQ からのリクエストを検証します。

```python
import os
from aiotraq_bot import TraqHttpBot

bot = TraqHttpBot(verification_token=os.getenv("BOT_VERIFICATION_TOKEN"))

# 型ヒントを使用してイベントハンドラーを登録 (1)
@bot.event()
async def on_message(payload: MessageCreatedPayload):
    print(payload)

# イベント名を指定してイベントハンドラーを登録 (2)
@bot.event("MESSAGE_CREATED")
async def on_message2(payload):
    print(payload)

if __name__ == "__main__":
  bot.run()
```

`@bot.event()` デコレータを使用してイベントハンドラーを登録します。イベントハンドラーは非同期関数である必要があります。

イベントの登録は、以下のいずれかの方法で行うことができます。

- デコレータに与えるイベントハンドラーの型ヒントを使用する(1)
- デコレータの引数にイベントの文字列を指定する(2)

ここでは、型ヒント `MessageCreatedPayload` を使用してメッセージの受信イベントを処理するイベントハンドラーを登録しています。

:::info
イベントの種類とイベントハンドラーの型ヒントの一覧は [bot-event の一覧](/docs/api/bot-event) を参照してください。
:::

## イベントハンドラーの引数

イベントハンドラーは、リクエストのペイロードやイベント名、リクエスト ID を引数として受け取ることができます。

```python
@bot.event()
async def on_message(payload: MessageCreatedPayload, event: str, id: str):
    # Request Body
    print(payload)
    # Event Name (X-TRAQ-BOT-EVENT Header)
    print(event)
    # Request ID (X-TRAQ-BOT-REQUEST-ID Header)
    print(id)
```

## Bot サーバーの起動

Bot サーバーを起動するには、`run` メソッドを呼び出します。BOT サーバーは traQ からのリクエストを受け取り、イベントに応じてイベントハンドラーを呼び出します。

```python
if __name__ == "__main__":
  bot.run()
```

サーバーの待ち受けポートとホストはデフォルトで `0.0.0.0:8080` に設定されています。
`run` メソッドの引数に `host` と `port` を指定することで、ポートとホストを変更することができます。

```python
if __name__ == "__main__":
  bot.run(host="0.0.0.0", port=8080)
```

:::tip
BOT サーバーは内部的に [FastAPI](https://fastapi.tiangolo.com/) を使用して実装されています。リクエストごとに非同期にイベントハンドラーを呼び出します。
:::
