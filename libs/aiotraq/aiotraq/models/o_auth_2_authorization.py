from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_2_prompt import OAuth2Prompt
from ..models.o_auth_2_response_type import OAuth2ResponseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2Authorization")


@_attrs_define
class OAuth2Authorization:
    """
    Attributes:
        client_id (str):
        response_type (Union[Unset, OAuth2ResponseType]):
        redirect_uri (Union[Unset, str]):
        scope (Union[Unset, str]):
        state (Union[Unset, str]):
        code_challenge (Union[Unset, str]):
        code_challenge_method (Union[Unset, str]):
        nonce (Union[Unset, str]):
        prompt (Union[Unset, OAuth2Prompt]):
    """

    client_id: str
    response_type: Union[Unset, OAuth2ResponseType] = UNSET
    redirect_uri: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    code_challenge: Union[Unset, str] = UNSET
    code_challenge_method: Union[Unset, str] = UNSET
    nonce: Union[Unset, str] = UNSET
    prompt: Union[Unset, OAuth2Prompt] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id

        response_type: Union[Unset, str] = UNSET
        if not isinstance(self.response_type, Unset):
            response_type = self.response_type.value

        redirect_uri = self.redirect_uri

        scope = self.scope

        state = self.state

        code_challenge = self.code_challenge

        code_challenge_method = self.code_challenge_method

        nonce = self.nonce

        prompt: Union[Unset, str] = UNSET
        if not isinstance(self.prompt, Unset):
            prompt = self.prompt.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
            }
        )
        if response_type is not UNSET:
            field_dict["response_type"] = response_type
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if scope is not UNSET:
            field_dict["scope"] = scope
        if state is not UNSET:
            field_dict["state"] = state
        if code_challenge is not UNSET:
            field_dict["code_challenge"] = code_challenge
        if code_challenge_method is not UNSET:
            field_dict["code_challenge_method"] = code_challenge_method
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if prompt is not UNSET:
            field_dict["prompt"] = prompt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("client_id")

        _response_type = d.pop("response_type", UNSET)
        response_type: Union[Unset, OAuth2ResponseType]
        if isinstance(_response_type, Unset):
            response_type = UNSET
        else:
            response_type = OAuth2ResponseType(_response_type)

        redirect_uri = d.pop("redirect_uri", UNSET)

        scope = d.pop("scope", UNSET)

        state = d.pop("state", UNSET)

        code_challenge = d.pop("code_challenge", UNSET)

        code_challenge_method = d.pop("code_challenge_method", UNSET)

        nonce = d.pop("nonce", UNSET)

        _prompt = d.pop("prompt", UNSET)
        prompt: Union[Unset, OAuth2Prompt]
        if isinstance(_prompt, Unset):
            prompt = UNSET
        else:
            prompt = OAuth2Prompt(_prompt)

        o_auth_2_authorization = cls(
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            nonce=nonce,
            prompt=prompt,
        )

        o_auth_2_authorization.additional_properties = d
        return o_auth_2_authorization

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
