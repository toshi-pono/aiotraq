from enum import Enum


class SearchMessagesSort(str, Enum):
    CREATEDAT = "createdAt"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-createdAt"
    VALUE_3 = "-updatedAt"

    def __str__(self) -> str:
        return str(self.value)
