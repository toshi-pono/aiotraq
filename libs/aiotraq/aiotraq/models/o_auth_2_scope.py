from enum import Enum


class OAuth2Scope(str, Enum):
    MANAGE_BOT = "manage_bot"
    OPENID = "openid"
    PROFILE = "profile"
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
