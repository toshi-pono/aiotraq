from enum import Enum


class OAuth2ResponseType(str, Enum):
    CODE = "code"
    NONE = "none"
    TOKEN = "token"

    def __str__(self) -> str:
        return str(self.value)
