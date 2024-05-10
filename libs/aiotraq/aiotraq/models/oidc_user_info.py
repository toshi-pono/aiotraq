from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oidc_traq_user_info import OIDCTraqUserInfo


T = TypeVar("T", bound="OIDCUserInfo")


@_attrs_define
class OIDCUserInfo:
    """自分のユーザー詳細情報

    Attributes:
        sub (str): ユーザーUUID
        name (str): ユーザー名
        preferred_username (str): ユーザー名
        picture (str): アイコン画像URL
        updated_at (Union[Unset, int]): 更新日時
        traq (Union[Unset, OIDCTraqUserInfo]): traQ特有のユーザー詳細情報
    """

    sub: str
    name: str
    preferred_username: str
    picture: str
    updated_at: Union[Unset, int] = UNSET
    traq: Union[Unset, "OIDCTraqUserInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub = self.sub

        name = self.name

        preferred_username = self.preferred_username

        picture = self.picture

        updated_at = self.updated_at

        traq: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.traq, Unset):
            traq = self.traq.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sub": sub,
                "name": name,
                "preferred_username": preferred_username,
                "picture": picture,
            }
        )
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if traq is not UNSET:
            field_dict["traq"] = traq

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.oidc_traq_user_info import OIDCTraqUserInfo

        d = src_dict.copy()
        sub = d.pop("sub")

        name = d.pop("name")

        preferred_username = d.pop("preferred_username")

        picture = d.pop("picture")

        updated_at = d.pop("updated_at", UNSET)

        _traq = d.pop("traq", UNSET)
        traq: Union[Unset, OIDCTraqUserInfo]
        if isinstance(_traq, Unset):
            traq = UNSET
        else:
            traq = OIDCTraqUserInfo.from_dict(_traq)

        oidc_user_info = cls(
            sub=sub,
            name=name,
            preferred_username=preferred_username,
            picture=picture,
            updated_at=updated_at,
            traq=traq,
        )

        oidc_user_info.additional_properties = d
        return oidc_user_info

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
