from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostStampPaletteRequest")


@_attrs_define
class PostStampPaletteRequest:
    """スタンプパレット作成リクエスト

    Attributes:
        stamps (List[str]): パレット内のスタンプのUUID配列
        name (str): パレット名
        description (str): 説明
    """

    stamps: List[str]
    name: str
    description: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stamps = self.stamps

        name = self.name

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stamps": stamps,
                "name": name,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stamps = cast(List[str], d.pop("stamps"))

        name = d.pop("name")

        description = d.pop("description")

        post_stamp_palette_request = cls(
            stamps=stamps,
            name=name,
            description=description,
        )

        post_stamp_palette_request.additional_properties = d
        return post_stamp_palette_request

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
