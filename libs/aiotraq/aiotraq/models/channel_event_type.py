from enum import Enum


class ChannelEventType(str, Enum):
    CHILDCREATED = "ChildCreated"
    FORCEDNOTIFICATIONCHANGED = "ForcedNotificationChanged"
    NAMECHANGED = "NameChanged"
    PARENTCHANGED = "ParentChanged"
    PINADDED = "PinAdded"
    PINREMOVED = "PinRemoved"
    SUBSCRIBERSCHANGED = "SubscribersChanged"
    TOPICCHANGED = "TopicChanged"
    VISIBILITYCHANGED = "VisibilityChanged"

    def __str__(self) -> str:
        return str(self.value)
