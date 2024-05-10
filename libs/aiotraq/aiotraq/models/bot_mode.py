from enum import Enum


class BotMode(str, Enum):
    HTTP = "HTTP"
    WEBSOCKET = "WebSocket"

    def __str__(self) -> str:
        return str(self.value)
