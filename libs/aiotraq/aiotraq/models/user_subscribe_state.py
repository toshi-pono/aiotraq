from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_subscribe_level import ChannelSubscribeLevel

T = TypeVar("T", bound="UserSubscribeState")


@_attrs_define
class UserSubscribeState:
    """ユーザーのチャンネル購読状態

    Attributes:
        channel_id (str): チャンネルUUID
        level (ChannelSubscribeLevel): チャンネル購読レベル
            0：無し
            1：未読管理
            2：未読管理+通知
    """

    channel_id: str
    level: ChannelSubscribeLevel
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id

        level = self.level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
                "level": level,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channelId")

        level = ChannelSubscribeLevel(d.pop("level"))

        user_subscribe_state = cls(
            channel_id=channel_id,
            level=level,
        )

        user_subscribe_state.additional_properties = d
        return user_subscribe_state

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
