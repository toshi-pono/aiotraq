---
id: am.stamp
title: am.stamp
sidebar_label: am.stamp
---

traQ のメッセージにスタンプを押します。

### Parameters

| Name                | Description                |
| :------------------ | :------------------------- |
| **stamp_id** (`str`) | 押すスタンプの UUID         |

### Returns

なし

- スタンプの一括削除: [`am.clear_all_stamp`](./am.clear_all_stamp.md)
- 特定のスタンプの削除: [`am.clear_stamp`](./am.clear_stamp.md)

### Example

```python
from aiotraq_message import TraqMessage

async def component(am: TraqMessage):
    am.stamp("stamp_uuid")
```
