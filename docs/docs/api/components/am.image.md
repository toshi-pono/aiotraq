---
id: am.image
title: am.image
sidebar_label: am.image
---

traQ に画像を送信します

### Parameters

| Name                                                         | Description               |
| :----------------------------------------------------------- | :------------------------ |
| **image** `(str \| Image.Image \| io.BytesIO \| np.ndarray)` | traQ に送信する画像データ |

- `str`: 画像の base64 エンコードされた文字列を指定します。 `data:image/png;base64,xxxxx` のような形式で指定してください。
- `Image.Image`: PIL で読み込んだ画像を指定します。
- `io.BytesIO`: 画像のバイナリデータを指定します。
- `np.ndarray`: 画像の numpy 配列を指定します。内部的に、BGR から RGB に変換されます。OpenCV で読み込んだ画像をそのまま指定することができます。

### Returns

`message_id` (`str | None`): 追加した画像付きメッセージの UUID が返されます。これを使ってメッセージの削除ができます。送信に失敗した場合は `None` が返されます。

### Example

```python
from aiotraq_message import TraqMessage
from PIL import Image

async def component(am: TraqMessage):
    image = Image.open("image.png")
    am.write(image)
```

:::border
![am.write](./img/am.image.png)
:::
