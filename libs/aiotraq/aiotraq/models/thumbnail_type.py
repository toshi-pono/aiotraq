from enum import Enum


class ThumbnailType(str, Enum):
    IMAGE = "image"
    WAVEFORM = "waveform"

    def __str__(self) -> str:
        return str(self.value)
