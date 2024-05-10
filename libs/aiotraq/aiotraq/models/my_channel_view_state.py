from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_view_state import ChannelViewState

T = TypeVar("T", bound="MyChannelViewState")


@_attrs_define
class MyChannelViewState:
    """自身のチャンネル閲覧状態

    Attributes:
        key (str): WSセッションの識別子
        channel_id (str): チャンネルUUID
        state (ChannelViewState): 閲覧状態
    """

    key: str
    channel_id: str
    state: ChannelViewState
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        channel_id = self.channel_id

        state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "channelId": channel_id,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        channel_id = d.pop("channelId")

        state = ChannelViewState(d.pop("state"))

        my_channel_view_state = cls(
            key=key,
            channel_id=channel_id,
            state=state,
        )

        my_channel_view_state.additional_properties = d
        return my_channel_view_state

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
