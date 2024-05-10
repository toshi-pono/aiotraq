from enum import Enum


class ChannelViewState(str, Enum):
    EDITING = "editing"
    MONITORING = "monitoring"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
