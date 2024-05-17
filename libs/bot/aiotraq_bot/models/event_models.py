from typing import Any, Union
from .event import (
    BotMessageStampsUpdatedPayload,
    ChannelCreatedPayload,
    ChannelTopicChangedPayload,
    DirectMessageCreatedPayload,
    DirectMessageDeletedPayload,
    DirectMessageUpdatedPayload,
    JoinedPayload,
    LeftPayload,
    MessageCreatedPayload,
    MessageDeletedPayload,
    MessageUpdatedPayload,
    PingPayload,
    StampCreatedPayload,
    TagAddedPayload,
    TagRemovedPayload,
    UserCreatedPayload,
    UserGroupAdminAddedPayload,
    UserGroupAdminRemovedPayload,
    UserGroupCreatedPayload,
    UserGroupDeletedPayload,
    UserGroupMemberAddedPayload,
    UserGroupMemberRemovedPayload,
    UserGroupMemberUpdatedPayload,
    UserGroupUpdatedPayload,
)
from pydantic import ValidationError


# FIXME: うまく型出し分ける方法わからん
EventModel = Union[
    BotMessageStampsUpdatedPayload,
    ChannelCreatedPayload,
    ChannelTopicChangedPayload,
    DirectMessageCreatedPayload,
    DirectMessageDeletedPayload,
    DirectMessageUpdatedPayload,
    JoinedPayload,
    LeftPayload,
    MessageCreatedPayload,
    MessageDeletedPayload,
    MessageUpdatedPayload,
    PingPayload,
    StampCreatedPayload,
    TagAddedPayload,
    TagRemovedPayload,
    UserCreatedPayload,
    UserGroupAdminAddedPayload,
    UserGroupAdminRemovedPayload,
    UserGroupCreatedPayload,
    UserGroupDeletedPayload,
    UserGroupMemberAddedPayload,
    UserGroupMemberRemovedPayload,
    UserGroupMemberUpdatedPayload,
    UserGroupUpdatedPayload,
]
EventModelType = type[EventModel]


event_models: dict[str, EventModelType] = {
    "PING": PingPayload,
    "JOINED": JoinedPayload,
    "LEFT": LeftPayload,
    "MESSAGE_CREATED": MessageCreatedPayload,
    "MESSAGE_DELETED": MessageDeletedPayload,
    "MESSAGE_UPDATED": MessageUpdatedPayload,
    "DIRECT_MESSAGE_CREATED": DirectMessageCreatedPayload,
    "DIRECT_MESSAGE_DELETED": DirectMessageDeletedPayload,
    "DIRECT_MESSAGE_UPDATED": DirectMessageUpdatedPayload,
    "BOT_MESSAGE_STAMPS_UPDATED": BotMessageStampsUpdatedPayload,
    "CHANNEL_CREATED": ChannelCreatedPayload,
    "CHANNEL_TOPIC_CHANGED": ChannelTopicChangedPayload,
    "USER_CREATED": UserCreatedPayload,
    "STAMP_CREATED": StampCreatedPayload,
    "TAG_ADDED": TagAddedPayload,
    "TAG_REMOVED": TagRemovedPayload,
    "USER_GROUP_CREATED": UserGroupCreatedPayload,
    "USER_GROUP_UPDATED": UserGroupUpdatedPayload,
    "USER_GROUP_DELETED": UserGroupDeletedPayload,
    "USER_GROUP_MEMBER_ADDED": UserGroupMemberAddedPayload,
    "USER_GROUP_MEMBER_UPDATED": UserGroupMemberUpdatedPayload,
    "USER_GROUP_MEMBER_REMOVED": UserGroupMemberRemovedPayload,
    "USER_GROUP_ADMIN_ADDED": UserGroupAdminAddedPayload,
    "USER_GROUP_ADMIN_REMOVED": UserGroupAdminRemovedPayload,
}


def convert_json_to_model(json_data: dict, event: str) -> EventModel:
    if event not in event_models:
        raise ValidationError(f"Invalid event: {event}")

    return event_models[event].model_validate(json_data)


def model_to_event_type(model: Any) -> str | None:
    for event, model_type in event_models.items():
        if model == model_type:
            return event

    return None
