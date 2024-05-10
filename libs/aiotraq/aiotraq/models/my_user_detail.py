import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_account_state import UserAccountState
from ..models.user_permission import UserPermission

if TYPE_CHECKING:
    from ..models.user_tag import UserTag


T = TypeVar("T", bound="MyUserDetail")


@_attrs_define
class MyUserDetail:
    """自分のユーザー詳細情報

    Attributes:
        id (str): ユーザーUUID
        bio (str): 自己紹介(biography)
        groups (List[str]): 所属グループのUUIDの配列
        tags (List['UserTag']): タグリスト
        updated_at (datetime.datetime): 更新日時
        last_online (Union[None, datetime.datetime]): 最終オンライン日時
        twitter_id (str): Twitter ID
        name (str): ユーザー名
        display_name (str): ユーザー表示名
        icon_file_id (str): アイコンファイルUUID
        bot (bool): BOTかどうか
        state (UserAccountState): ユーザーアカウント状態
            0: 停止
            1: 有効
            2: 一時停止
        permissions (List[UserPermission]): 所有している権限の配列
        home_channel (Union[None, str]): ホームチャンネル
    """

    id: str
    bio: str
    groups: List[str]
    tags: List["UserTag"]
    updated_at: datetime.datetime
    last_online: Union[None, datetime.datetime]
    twitter_id: str
    name: str
    display_name: str
    icon_file_id: str
    bot: bool
    state: UserAccountState
    permissions: List[UserPermission]
    home_channel: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        bio = self.bio

        groups = self.groups

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        updated_at = self.updated_at.isoformat()

        last_online: Union[None, str]
        if isinstance(self.last_online, datetime.datetime):
            last_online = self.last_online.isoformat()
        else:
            last_online = self.last_online

        twitter_id = self.twitter_id

        name = self.name

        display_name = self.display_name

        icon_file_id = self.icon_file_id

        bot = self.bot

        state = self.state.value

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)

        home_channel: Union[None, str]
        home_channel = self.home_channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bio": bio,
                "groups": groups,
                "tags": tags,
                "updatedAt": updated_at,
                "lastOnline": last_online,
                "twitterId": twitter_id,
                "name": name,
                "displayName": display_name,
                "iconFileId": icon_file_id,
                "bot": bot,
                "state": state,
                "permissions": permissions,
                "homeChannel": home_channel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_tag import UserTag

        d = src_dict.copy()
        id = d.pop("id")

        bio = d.pop("bio")

        groups = cast(List[str], d.pop("groups"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = UserTag.from_dict(tags_item_data)

            tags.append(tags_item)

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_last_online(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_online_type_0 = isoparse(data)

                return last_online_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_online = _parse_last_online(d.pop("lastOnline"))

        twitter_id = d.pop("twitterId")

        name = d.pop("name")

        display_name = d.pop("displayName")

        icon_file_id = d.pop("iconFileId")

        bot = d.pop("bot")

        state = UserAccountState(d.pop("state"))

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = UserPermission(permissions_item_data)

            permissions.append(permissions_item)

        def _parse_home_channel(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        home_channel = _parse_home_channel(d.pop("homeChannel"))

        my_user_detail = cls(
            id=id,
            bio=bio,
            groups=groups,
            tags=tags,
            updated_at=updated_at,
            last_online=last_online,
            twitter_id=twitter_id,
            name=name,
            display_name=display_name,
            icon_file_id=icon_file_id,
            bot=bot,
            state=state,
            permissions=permissions,
            home_channel=home_channel,
        )

        my_user_detail.additional_properties = d
        return my_user_detail

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
