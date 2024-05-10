from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OgpMedia")


@_attrs_define
class OgpMedia:
    """OGPに含まれる画像の情報

    Attributes:
        url (str):
        secure_url (Union[None, str]):
        type (Union[None, str]):
        width (Union[None, int]):
        height (Union[None, int]):
    """

    url: str
    secure_url: Union[None, str]
    type: Union[None, str]
    width: Union[None, int]
    height: Union[None, int]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        secure_url: Union[None, str]
        secure_url = self.secure_url

        type: Union[None, str]
        type = self.type

        width: Union[None, int]
        width = self.width

        height: Union[None, int]
        height = self.height

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "secureUrl": secure_url,
                "type": type,
                "width": width,
                "height": height,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        def _parse_secure_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        secure_url = _parse_secure_url(d.pop("secureUrl"))

        def _parse_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        type = _parse_type(d.pop("type"))

        def _parse_width(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        width = _parse_width(d.pop("width"))

        def _parse_height(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        height = _parse_height(d.pop("height"))

        ogp_media = cls(
            url=url,
            secure_url=secure_url,
            type=type,
            width=width,
            height=height,
        )

        ogp_media.additional_properties = d
        return ogp_media

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
