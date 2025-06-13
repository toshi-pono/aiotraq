---
id: am.pyplot
title: am.pyplot
sidebar_label: am.pyplot
---

Matplotlib の figure を画像として traQ に送信します。

### Parameters

| Name                | Description                |
| :------------------ | :------------------------- |
| **fig** (`Any`)     | 送信する Matplotlib figure |

### Returns

`message_id` (`str | None`): 追加した画像付きメッセージの UUID。送信に失敗した場合は `None`。

### Example

```python
from aiotraq_message import TraqMessage
import matplotlib.pyplot as plt

async def component(am: TraqMessage):
    fig, ax = plt.subplots()
    ax.plot([x for x in range(30)])
    am.pyplot(fig)
```

:::border
![am.pyplot](./img/am.pyplot.png)
:::