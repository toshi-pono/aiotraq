from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOAuth2Token")


@_attrs_define
class PostOAuth2Token:
    """
    Attributes:
        grant_type (str):
        code (Union[Unset, str]):
        redirect_uri (Union[Unset, str]):
        client_id (Union[Unset, str]):
        code_verifier (Union[Unset, str]):
        username (Union[Unset, str]):
        password (Union[Unset, str]):
        scope (Union[Unset, str]):
        refresh_token (Union[Unset, str]):
        client_secret (Union[Unset, str]):
    """

    grant_type: str
    code: Union[Unset, str] = UNSET
    redirect_uri: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    code_verifier: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grant_type = self.grant_type

        code = self.code

        redirect_uri = self.redirect_uri

        client_id = self.client_id

        code_verifier = self.code_verifier

        username = self.username

        password = self.password

        scope = self.scope

        refresh_token = self.refresh_token

        client_secret = self.client_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if code_verifier is not UNSET:
            field_dict["code_verifier"] = code_verifier
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if scope is not UNSET:
            field_dict["scope"] = scope
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grant_type = d.pop("grant_type")

        code = d.pop("code", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        client_id = d.pop("client_id", UNSET)

        code_verifier = d.pop("code_verifier", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        scope = d.pop("scope", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        post_o_auth_2_token = cls(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            client_id=client_id,
            code_verifier=code_verifier,
            username=username,
            password=password,
            scope=scope,
            refresh_token=refresh_token,
            client_secret=client_secret,
        )

        post_o_auth_2_token.additional_properties = d
        return post_o_auth_2_token

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
