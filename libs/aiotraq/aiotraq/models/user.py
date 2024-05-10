import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_account_state import UserAccountState

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """ユーザー情報

    Attributes:
        id (str): ユーザーUUID
        name (str): ユーザー名
        display_name (str): ユーザー表示名
        icon_file_id (str): アイコンファイルUUID
        bot (bool): BOTかどうか
        state (UserAccountState): ユーザーアカウント状態
            0: 停止
            1: 有効
            2: 一時停止
        updated_at (datetime.datetime): 更新日時
    """

    id: str
    name: str
    display_name: str
    icon_file_id: str
    bot: bool
    state: UserAccountState
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        display_name = self.display_name

        icon_file_id = self.icon_file_id

        bot = self.bot

        state = self.state.value

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "displayName": display_name,
                "iconFileId": icon_file_id,
                "bot": bot,
                "state": state,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        display_name = d.pop("displayName")

        icon_file_id = d.pop("iconFileId")

        bot = d.pop("bot")

        state = UserAccountState(d.pop("state"))

        updated_at = isoparse(d.pop("updatedAt"))

        user = cls(
            id=id,
            name=name,
            display_name=display_name,
            icon_file_id=icon_file_id,
            bot=bot,
            state=state,
            updated_at=updated_at,
        )

        user.additional_properties = d
        return user

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
