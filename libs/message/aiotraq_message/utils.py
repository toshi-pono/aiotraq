import base64
from io import BytesIO
import mimetypes
from aiotraq.types import File
import numpy as np
from PIL import Image


def bytes_to_file(bytes_: bytes, file_name: str | None = None, mime_type: str | None = None) -> File:
    """Convert bytes to a file object"""
    return File(BytesIO(bytes_), file_name, mime_type)


def base64_to_file(string: str) -> File | None:
    """Convert base64 encoded string to a file object
    format: data:image/png;base64,xxxxxxxxxxxx
    """

    if not string.startswith("data:") or ";base64," not in string:
        return None

    data = base64.b64decode(string.split(",")[-1])
    mime = string.split(",")[0].split(":")[-1].split(";")[0]

    extention = mimetypes.guess_extension(mime)
    if extention is None:
        mime = "application/octet-stream"
        extention = ""
    return File(BytesIO(data), f"image{extention}", mime)


def cv2pil(image: np.ndarray) -> Image.Image:
    """OpenCV型 -> PIL型"""
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = new_image[:, :, ::-1]
    elif new_image.shape[2] == 4:  # 透過
        new_image = new_image[:, :, [2, 1, 0, 3]]

    # FIXME: typeerrorを直す
    return Image.fromarray(new_image)  # type: ignore
