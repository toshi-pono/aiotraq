from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExternalProviderUser")


@_attrs_define
class ExternalProviderUser:
    """外部認証アカウントユーザー

    Attributes:
        provider_name (str): 外部サービス名
        linked_at (str): 紐付けた日時
        external_name (str): 外部アカウント名
    """

    provider_name: str
    linked_at: str
    external_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider_name = self.provider_name

        linked_at = self.linked_at

        external_name = self.external_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerName": provider_name,
                "linkedAt": linked_at,
                "externalName": external_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider_name = d.pop("providerName")

        linked_at = d.pop("linkedAt")

        external_name = d.pop("externalName")

        external_provider_user = cls(
            provider_name=provider_name,
            linked_at=linked_at,
            external_name=external_name,
        )

        external_provider_user.additional_properties = d
        return external_provider_user

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
