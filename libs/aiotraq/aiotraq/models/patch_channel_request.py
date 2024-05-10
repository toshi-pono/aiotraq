from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchChannelRequest")


@_attrs_define
class PatchChannelRequest:
    """チャンネル情報変更リクエスト

    Attributes:
        name (Union[Unset, str]): チャンネル名
        archived (Union[Unset, bool]): アーカイブされているかどうか
        force (Union[Unset, bool]): 強制通知チャンネルかどうか
        parent (Union[Unset, str]): 親チャンネルUUID
    """

    name: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    force: Union[Unset, bool] = UNSET
    parent: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        archived = self.archived

        force = self.force

        parent = self.parent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if archived is not UNSET:
            field_dict["archived"] = archived
        if force is not UNSET:
            field_dict["force"] = force
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        archived = d.pop("archived", UNSET)

        force = d.pop("force", UNSET)

        parent = d.pop("parent", UNSET)

        patch_channel_request = cls(
            name=name,
            archived=archived,
            force=force,
            parent=parent,
        )

        patch_channel_request.additional_properties = d
        return patch_channel_request

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
