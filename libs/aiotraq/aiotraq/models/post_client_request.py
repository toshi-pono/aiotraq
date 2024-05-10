from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_2_scope import OAuth2Scope

T = TypeVar("T", bound="PostClientRequest")


@_attrs_define
class PostClientRequest:
    """OAuth2クライアント作成リクエスト

    Attributes:
        name (str): クライアント名
        callback_url (str): コールバックURL
        scopes (List[OAuth2Scope]): 要求スコープの配列
        description (str): 説明
    """

    name: str
    callback_url: str
    scopes: List[OAuth2Scope]
    description: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        callback_url = self.callback_url

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "callbackUrl": callback_url,
                "scopes": scopes,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        callback_url = d.pop("callbackUrl")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = OAuth2Scope(scopes_item_data)

            scopes.append(scopes_item)

        description = d.pop("description")

        post_client_request = cls(
            name=name,
            callback_url=callback_url,
            scopes=scopes,
            description=description,
        )

        post_client_request.additional_properties = d
        return post_client_request

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
