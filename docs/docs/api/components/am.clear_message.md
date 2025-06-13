---
id: am.clear_message
title: am.clear_message
sidebar_label: am.clear_message
---

am.write などで追加した特定のメッセージを削除します。

### Parameters

| Name                | Description                |
| :------------------ | :------------------------- |
| **message_id** (`str`) | 削除するメッセージの UUID |

### Returns

なし

### Example

```python
from aiotraq_message import TraqMessage

async def component(am: TraqMessage):
    message_id = am.write("Hello!")
    am.clear_message(message_id)
```
