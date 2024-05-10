from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BotTokens")


@_attrs_define
class BotTokens:
    """BOTのトークン情報

    Attributes:
        verification_token (str): Verification Token
        access_token (str): BOTアクセストークン
    """

    verification_token: str
    access_token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verification_token = self.verification_token

        access_token = self.access_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verificationToken": verification_token,
                "accessToken": access_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        verification_token = d.pop("verificationToken")

        access_token = d.pop("accessToken")

        bot_tokens = cls(
            verification_token=verification_token,
            access_token=access_token,
        )

        bot_tokens.additional_properties = d
        return bot_tokens

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
