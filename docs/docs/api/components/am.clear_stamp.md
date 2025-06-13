---
id: components-clear-stamp
title: am.clear_stamp
sidebar_label: am.clear_stamp
---

traQ のメッセージから特定のスタンプを消します。

### Parameters

| Name                | Description                |
| :------------------ | :------------------------- |
| **stamp_id** (`str`) | 消すスタンプの UUID         |

### Returns

なし

### Example

```python
from aiotraq_message import TraqMessage

async def component(am: TraqMessage):
    am.clear_stamp("stamp_id")
```
