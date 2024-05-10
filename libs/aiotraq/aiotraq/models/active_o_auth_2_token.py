import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.o_auth_2_scope import OAuth2Scope

T = TypeVar("T", bound="ActiveOAuth2Token")


@_attrs_define
class ActiveOAuth2Token:
    """有効なOAuth2トークン情報

    Attributes:
        id (str): トークンUUID
        client_id (str): OAuth2クライアントUUID
        scopes (List[OAuth2Scope]): スコープ
        issued_at (datetime.datetime): 発行日時
    """

    id: str
    client_id: str
    scopes: List[OAuth2Scope]
    issued_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        client_id = self.client_id

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        issued_at = self.issued_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "clientId": client_id,
                "scopes": scopes,
                "issuedAt": issued_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        client_id = d.pop("clientId")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = OAuth2Scope(scopes_item_data)

            scopes.append(scopes_item)

        issued_at = isoparse(d.pop("issuedAt"))

        active_o_auth_2_token = cls(
            id=id,
            client_id=client_id,
            scopes=scopes,
            issued_at=issued_at,
        )

        active_o_auth_2_token.additional_properties = d
        return active_o_auth_2_token

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
