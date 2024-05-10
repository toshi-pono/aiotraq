from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_account_state import UserAccountState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchUserRequest")


@_attrs_define
class PatchUserRequest:
    """ユーザー情報編集リクエスト

    Attributes:
        display_name (Union[Unset, str]): 新しい表示名
        twitter_id (Union[Unset, str]): TwitterID
        state (Union[Unset, UserAccountState]): ユーザーアカウント状態
            0: 停止
            1: 有効
            2: 一時停止
        role (Union[Unset, str]): ユーザーロール
    """

    display_name: Union[Unset, str] = UNSET
    twitter_id: Union[Unset, str] = UNSET
    state: Union[Unset, UserAccountState] = UNSET
    role: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        twitter_id = self.twitter_id

        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        role = self.role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if twitter_id is not UNSET:
            field_dict["twitterId"] = twitter_id
        if state is not UNSET:
            field_dict["state"] = state
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        twitter_id = d.pop("twitterId", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, UserAccountState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = UserAccountState(_state)

        role = d.pop("role", UNSET)

        patch_user_request = cls(
            display_name=display_name,
            twitter_id=twitter_id,
            state=state,
            role=role,
        )

        patch_user_request.additional_properties = d
        return patch_user_request

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
