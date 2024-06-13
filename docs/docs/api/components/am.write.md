---
id: components-write
title: am.write
sidebar_label: am.write
---

traQ にメッセージを書き込みます

### Parameters

| Name                | Description                                                 |
| :------------------ | :---------------------------------------------------------- |
| **message** (`str`) | traQ に送信するメッセージ。末尾に改行が自動で追加されます。 |

### Returns

`message_id` (`str`): 追加したメッセージの UUID が返されます。これを使ってメッセージの削除ができます。

### Example

```python
from aiotraq_message import TraqMessage

async def component(am: TraqMessage):
    am.write("Hello World!")
```

:::border
![am.write](./img/am.write.png)
:::
