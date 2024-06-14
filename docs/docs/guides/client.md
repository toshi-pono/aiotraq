---
id: api-guide
title: APIクライアントの利用
sidebar_label: API Client
---

このガイドでは、`AiotraQ`を用いた API クライアントの利用方法について紹介します。

## API Client の作成

`AuthenticatedClient`を用いて API クライアントを作成し API を叩くことができます。
一度 with を使ってクラアントを使用すると、終了後に自動でクライアントが閉じられます。再度利用する場合は、`AuthenticatedClient`を再度作成してください。

```python
import os
from aiotraq import AuthenticatedClient
from aiotraq.api.channel import get_channels

BOT_ACCESS_TOKEN = os.getenv("BOT_ACCESS_TOKEN")
assert BOT_ACCESS_TOKEN is not None

client = AuthenticatedClient(base_url="https://q.trap.jp/api/v3", token=BOT_ACCESS_TOKEN)

with client as  client:
    channels = get_channels.sync_detailed(client=client)
    print(channels.status_code)
```

API の利用例: チャンネル一覧の取得

```python
with client as client:
    channels: ChannelList = get_channels.sync(client=client)
    # status_code などの情報も利用したい場合
    response: Response[ChannelList] = get_channels.sync_detailed(client=client)
```

:::info
`sync_detailed`/`async_detailed`を利用することで、レスポンスの情報も取得することができます。
ステータスコードやヘッダー情報などを取得したい場合は、`_detailed`付きのメソッドを利用してください。
:::

## 非同期 API の利用

`asyncio`または`asyncio_detailed`を利用することで、非同期で API を叩くことができます。

```python
with client as client:
    channels: ChannelList = await get_channels.asyncio(client=client)
    response: Response[ChannelList] = await get_channels.asyncio_detailed(client=client)
```

### 各メソッドの違い

以下に各メソッドの違いを示します。
API のエンドポイントによって、`sync`/`asyncio`を持たず、`detailed`付きの関数のみを持つ場合もあります。

1. `sync`: 成功した場合に解析済みデータを返し、そうでない場合は `None` を返すブロッキングリクエスト
1. `sync_detailed`: 成功した場合にはオプションで `parsed` を持つ `Request`型 を返すブロッキングリクエスト
1. `asyncio`: ブロッキングではなく非同期で動作する。`sync` と同様のリクエスト
1. `asyncio_detailed`: ブロッキングではなく非同期で動作する。`sync_detailed` と同様のリクエスト
