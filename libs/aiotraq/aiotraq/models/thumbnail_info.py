from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.thumbnail_type import ThumbnailType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ThumbnailInfo")


@_attrs_define
class ThumbnailInfo:
    """
    Attributes:
        type (ThumbnailType): サムネイル画像のタイプ
        mime (str): MIMEタイプ
        width (Union[Unset, int]): サムネイル幅
        height (Union[Unset, int]): サムネイル高さ
    """

    type: ThumbnailType
    mime: str
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        mime = self.mime

        width = self.width

        height = self.height

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "mime": mime,
            }
        )
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ThumbnailType(d.pop("type"))

        mime = d.pop("mime")

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        thumbnail_info = cls(
            type=type,
            mime=mime,
            width=width,
            height=height,
        )

        thumbnail_info.additional_properties = d
        return thumbnail_info

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
