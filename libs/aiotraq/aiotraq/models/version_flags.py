from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VersionFlags")


@_attrs_define
class VersionFlags:
    """
    Attributes:
        external_login (List[str]): 有効な外部ログインプロバイダ
        sign_up_allowed (bool): ユーザーが自身で新規登録(POST /api/v3/users)可能か
    """

    external_login: List[str]
    sign_up_allowed: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_login = self.external_login

        sign_up_allowed = self.sign_up_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalLogin": external_login,
                "signUpAllowed": sign_up_allowed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_login = cast(List[str], d.pop("externalLogin"))

        sign_up_allowed = d.pop("signUpAllowed")

        version_flags = cls(
            external_login=external_login,
            sign_up_allowed=sign_up_allowed,
        )

        version_flags.additional_properties = d
        return version_flags

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
