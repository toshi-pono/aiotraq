import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UnreadChannel")


@_attrs_define
class UnreadChannel:
    """未読チャンネル情報

    Attributes:
        channel_id (str): チャンネルUUID
        count (int): 未読メッセージ数
        noticeable (bool): 自分宛てメッセージが含まれているかどうか
        since (datetime.datetime): チャンネルの最古の未読メッセージの日時
        updated_at (datetime.datetime): チャンネルの最新の未読メッセージの日時
        oldest_message_id (str): そのチャンネルの未読の中で最も古いメッセージのid
    """

    channel_id: str
    count: int
    noticeable: bool
    since: datetime.datetime
    updated_at: datetime.datetime
    oldest_message_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id

        count = self.count

        noticeable = self.noticeable

        since = self.since.isoformat()

        updated_at = self.updated_at.isoformat()

        oldest_message_id = self.oldest_message_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
                "count": count,
                "noticeable": noticeable,
                "since": since,
                "updatedAt": updated_at,
                "oldestMessageId": oldest_message_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channelId")

        count = d.pop("count")

        noticeable = d.pop("noticeable")

        since = isoparse(d.pop("since"))

        updated_at = isoparse(d.pop("updatedAt"))

        oldest_message_id = d.pop("oldestMessageId")

        unread_channel = cls(
            channel_id=channel_id,
            count=count,
            noticeable=noticeable,
            since=since,
            updated_at=updated_at,
            oldest_message_id=oldest_message_id,
        )

        unread_channel.additional_properties = d
        return unread_channel

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
