from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchMeRequest")


@_attrs_define
class PatchMeRequest:
    """自分のユーザー情報変更リクエスト

    Attributes:
        display_name (Union[Unset, str]): 新しい表示名
        twitter_id (Union[Unset, str]): TwitterID
        bio (Union[Unset, str]): 自己紹介(biography)
        home_channel (Union[Unset, str]): ホームチャンネルのUUID
            `00000000-0000-0000-0000-000000000000`を指定すると、ホームチャンネルが`null`に設定されます
    """

    display_name: Union[Unset, str] = UNSET
    twitter_id: Union[Unset, str] = UNSET
    bio: Union[Unset, str] = UNSET
    home_channel: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        twitter_id = self.twitter_id

        bio = self.bio

        home_channel = self.home_channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if twitter_id is not UNSET:
            field_dict["twitterId"] = twitter_id
        if bio is not UNSET:
            field_dict["bio"] = bio
        if home_channel is not UNSET:
            field_dict["homeChannel"] = home_channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        twitter_id = d.pop("twitterId", UNSET)

        bio = d.pop("bio", UNSET)

        home_channel = d.pop("homeChannel", UNSET)

        patch_me_request = cls(
            display_name=display_name,
            twitter_id=twitter_id,
            bio=bio,
            home_channel=home_channel,
        )

        patch_me_request.additional_properties = d
        return patch_me_request

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
