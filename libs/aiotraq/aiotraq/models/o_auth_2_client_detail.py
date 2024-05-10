from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_2_scope import OAuth2Scope

T = TypeVar("T", bound="OAuth2ClientDetail")


@_attrs_define
class OAuth2ClientDetail:
    """OAuth2クライアント詳細情報

    Attributes:
        id (str): クライアントUUID
        developer_id (str): クライアント開発者UUID
        description (str): 説明
        name (str): クライアント名
        scopes (List[OAuth2Scope]): 要求スコープの配列
        callback_url (str): コールバックURL
        secret (str): クライアントシークレット
    """

    id: str
    developer_id: str
    description: str
    name: str
    scopes: List[OAuth2Scope]
    callback_url: str
    secret: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        developer_id = self.developer_id

        description = self.description

        name = self.name

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        callback_url = self.callback_url

        secret = self.secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "developerId": developer_id,
                "description": description,
                "name": name,
                "scopes": scopes,
                "callbackUrl": callback_url,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        developer_id = d.pop("developerId")

        description = d.pop("description")

        name = d.pop("name")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = OAuth2Scope(scopes_item_data)

            scopes.append(scopes_item)

        callback_url = d.pop("callbackUrl")

        secret = d.pop("secret")

        o_auth_2_client_detail = cls(
            id=id,
            developer_id=developer_id,
            description=description,
            name=name,
            scopes=scopes,
            callback_url=callback_url,
            secret=secret,
        )

        o_auth_2_client_detail.additional_properties = d
        return o_auth_2_client_detail

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
