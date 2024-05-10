from enum import Enum


class OAuth2Prompt(str, Enum):
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
