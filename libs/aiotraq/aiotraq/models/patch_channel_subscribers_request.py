from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchChannelSubscribersRequest")


@_attrs_define
class PatchChannelSubscribersRequest:
    """チャンネル購読者編集リクエスト

    Attributes:
        on (Union[Unset, List[str]]): 通知をオンにするユーザーのUUID配列
        off (Union[Unset, List[str]]): 通知をオフにするユーザーのUUID配列
    """

    on: Union[Unset, List[str]] = UNSET
    off: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        on: Union[Unset, List[str]] = UNSET
        if not isinstance(self.on, Unset):
            on = self.on

        off: Union[Unset, List[str]] = UNSET
        if not isinstance(self.off, Unset):
            off = self.off

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if on is not UNSET:
            field_dict["on"] = on
        if off is not UNSET:
            field_dict["off"] = off

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        on = cast(List[str], d.pop("on", UNSET))

        off = cast(List[str], d.pop("off", UNSET))

        patch_channel_subscribers_request = cls(
            on=on,
            off=off,
        )

        patch_channel_subscribers_request.additional_properties = d
        return patch_channel_subscribers_request

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
