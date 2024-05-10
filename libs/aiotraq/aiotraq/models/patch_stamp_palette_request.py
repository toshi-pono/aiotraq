from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchStampPaletteRequest")


@_attrs_define
class PatchStampPaletteRequest:
    """スタンプパレット情報変更リクエスト

    Attributes:
        name (Union[Unset, str]): パレット名
        description (Union[Unset, str]): 説明
        stamps (Union[Unset, List[str]]): パレット内のスタンプUUIDの配列
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    stamps: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        stamps: Union[Unset, List[str]] = UNSET
        if not isinstance(self.stamps, Unset):
            stamps = self.stamps

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if stamps is not UNSET:
            field_dict["stamps"] = stamps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        stamps = cast(List[str], d.pop("stamps", UNSET))

        patch_stamp_palette_request = cls(
            name=name,
            description=description,
            stamps=stamps,
        )

        patch_stamp_palette_request.additional_properties = d
        return patch_stamp_palette_request

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
