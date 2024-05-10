from enum import Enum


class BotEventResult(str, Enum):
    DP = "dp"
    NE = "ne"
    NG = "ng"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
