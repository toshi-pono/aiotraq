import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ActivityTimelineMessage")


@_attrs_define
class ActivityTimelineMessage:
    """Timelineアクテビティ用メッセージ

    Attributes:
        id (str): メッセージUUID
        user_id (str): 投稿者UUID
        channel_id (str): チャンネルUUID
        content (str): メッセージ本文
        created_at (datetime.datetime): 投稿日時
        updated_at (datetime.datetime): 編集日時
    """

    id: str
    user_id: str
    channel_id: str
    content: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        user_id = self.user_id

        channel_id = self.channel_id

        content = self.content

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
                "channelId": channel_id,
                "content": content,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        user_id = d.pop("userId")

        channel_id = d.pop("channelId")

        content = d.pop("content")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        activity_timeline_message = cls(
            id=id,
            user_id=user_id,
            channel_id=channel_id,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
        )

        activity_timeline_message.additional_properties = d
        return activity_timeline_message

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
