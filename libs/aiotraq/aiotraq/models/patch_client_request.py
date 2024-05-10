from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchClientRequest")


@_attrs_define
class PatchClientRequest:
    """OAuth2クライアント情報変更リクエスト

    Attributes:
        name (Union[Unset, str]): クライアント名
        description (Union[Unset, str]): 説明
        callback_url (Union[Unset, str]): コールバックURL
        developer_id (Union[Unset, str]): クライアント開発者UUID
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    callback_url: Union[Unset, str] = UNSET
    developer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        callback_url = self.callback_url

        developer_id = self.developer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if callback_url is not UNSET:
            field_dict["callbackUrl"] = callback_url
        if developer_id is not UNSET:
            field_dict["developerId"] = developer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        callback_url = d.pop("callbackUrl", UNSET)

        developer_id = d.pop("developerId", UNSET)

        patch_client_request = cls(
            name=name,
            description=description,
            callback_url=callback_url,
            developer_id=developer_id,
        )

        patch_client_request.additional_properties = d
        return patch_client_request

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
