from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_2_scope import OAuth2Scope

T = TypeVar("T", bound="OAuth2Client")


@_attrs_define
class OAuth2Client:
    """OAuth2クライアント情報

    Attributes:
        id (str): クライアントUUID
        name (str): クライアント名
        description (str): 説明
        developer_id (str): クライアント開発者UUID
        scopes (List[OAuth2Scope]): 要求スコープの配列
    """

    id: str
    name: str
    description: str
    developer_id: str
    scopes: List[OAuth2Scope]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        developer_id = self.developer_id

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "developerId": developer_id,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        developer_id = d.pop("developerId")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = OAuth2Scope(scopes_item_data)

            scopes.append(scopes_item)

        o_auth_2_client = cls(
            id=id,
            name=name,
            description=description,
            developer_id=developer_id,
            scopes=scopes,
        )

        o_auth_2_client.additional_properties = d
        return o_auth_2_client

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
