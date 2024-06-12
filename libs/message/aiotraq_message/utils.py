import base64
from io import BytesIO
import mimetypes
from aiotraq.types import File


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
        return None
    return File(BytesIO(data), f"image{extention}", mime)
