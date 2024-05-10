from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchStampRequest")


@_attrs_define
class PatchStampRequest:
    """スタンプ情報変更リクエスト

    Attributes:
        name (Union[Unset, str]): スタンプ名
        creator_id (Union[Unset, str]): 作成者UUID
    """

    name: Union[Unset, str] = UNSET
    creator_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        creator_id = self.creator_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if creator_id is not UNSET:
            field_dict["creatorId"] = creator_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        creator_id = d.pop("creatorId", UNSET)

        patch_stamp_request = cls(
            name=name,
            creator_id=creator_id,
        )

        patch_stamp_request.additional_properties = d
        return patch_stamp_request

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
