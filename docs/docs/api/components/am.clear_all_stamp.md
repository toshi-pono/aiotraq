---
id: am.clear_all_stamp
title: am.clear_all_stamp
sidebar_label: am.clear_all_stamp
---

traQ のメッセージからすべてのスタンプを消します。

### Parameters

なし

### Returns

なし

### Example

```python
from aiotraq_message import TraqMessage

async def component(am: TraqMessage):
    am.clear_all_stamp()
```
