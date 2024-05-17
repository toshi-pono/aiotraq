# aiotraq

Async ready traQ API Client for Python

## Installation

TODO

## Usage

`AuthenticatedClient`を用いて API クライアントを作成し API を叩くことができます。

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

非同期版も利用可能です:

```python
with client as client:
    channels: ChannelList = await get_channels.asyncio(client=client)
    response: Response[ChannelList] = await get_channels.asyncio_detailed(client=client)
```

## Advanced customizations

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl=False
)
```

Things to know:

1. Every path/method combo becomes a Python module with four functions:

   1. `sync`: Blocking request that returns parsed data (if successful) or `None`
   1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
   1. `asyncio`: Like `sync` but async instead of blocking
   1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `aiotraq.api.default`

### Customizing the client

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from aiotraq import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from aiotraq import Client

client = Client(
    base_url="https://api.example.com",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://api.example.com", proxies="http://localhost:8030"))
```

## Acknowledgements

This project is generated using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
