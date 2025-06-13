---
id: components-spinner
title: am.spinner
sidebar_label: am.spinner
---

ローディングスピナーを表示します。

### Parameters

| Name                | Description                |
| :------------------ | :------------------------- |
| **message** (`str`, optional) | 表示するメッセージ（デフォルト: `:loading: loading...`） |

### Returns

`message_id` (`str`): ローディングメッセージの UUID。

### Example

```python
from aiotraq_message import TraqMessage
import asyncio

async def component(am: TraqMessage):
    async with am.spinner():
        await asyncio.sleep(5)
```

:::border
![am.spinner](./img/am.spinner.png)
:::
