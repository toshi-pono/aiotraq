from enum import Enum


class GetStampsType(str, Enum):
    ORIGINAL = "original"
    UNICODE = "unicode"

    def __str__(self) -> str:
        return str(self.value)
