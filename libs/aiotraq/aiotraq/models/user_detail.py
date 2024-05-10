import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_account_state import UserAccountState

if TYPE_CHECKING:
    from ..models.user_tag import UserTag


T = TypeVar("T", bound="UserDetail")


@_attrs_define
class UserDetail:
    """ユーザー詳細情報

    Attributes:
        id (str): ユーザーUUID
        state (UserAccountState): ユーザーアカウント状態
            0: 停止
            1: 有効
            2: 一時停止
        bot (bool): BOTかどうか
        icon_file_id (str): アイコンファイルUUID
        display_name (str): ユーザー表示名
        name (str): ユーザー名
        twitter_id (str): Twitter ID
        last_online (Union[None, datetime.datetime]): 最終オンライン日時
        updated_at (datetime.datetime): 更新日時
        tags (List['UserTag']): タグリスト
        groups (List[str]): 所属グループのUUIDの配列
        bio (str): 自己紹介(biography)
        home_channel (Union[None, str]): ホームチャンネル
    """

    id: str
    state: UserAccountState
    bot: bool
    icon_file_id: str
    display_name: str
    name: str
    twitter_id: str
    last_online: Union[None, datetime.datetime]
    updated_at: datetime.datetime
    tags: List["UserTag"]
    groups: List[str]
    bio: str
    home_channel: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        state = self.state.value

        bot = self.bot

        icon_file_id = self.icon_file_id

        display_name = self.display_name

        name = self.name

        twitter_id = self.twitter_id

        last_online: Union[None, str]
        if isinstance(self.last_online, datetime.datetime):
            last_online = self.last_online.isoformat()
        else:
            last_online = self.last_online

        updated_at = self.updated_at.isoformat()

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        groups = self.groups

        bio = self.bio

        home_channel: Union[None, str]
        home_channel = self.home_channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "state": state,
                "bot": bot,
                "iconFileId": icon_file_id,
                "displayName": display_name,
                "name": name,
                "twitterId": twitter_id,
                "lastOnline": last_online,
                "updatedAt": updated_at,
                "tags": tags,
                "groups": groups,
                "bio": bio,
                "homeChannel": home_channel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_tag import UserTag

        d = src_dict.copy()
        id = d.pop("id")

        state = UserAccountState(d.pop("state"))

        bot = d.pop("bot")

        icon_file_id = d.pop("iconFileId")

        display_name = d.pop("displayName")

        name = d.pop("name")

        twitter_id = d.pop("twitterId")

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

        updated_at = isoparse(d.pop("updatedAt"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = UserTag.from_dict(tags_item_data)

            tags.append(tags_item)

        groups = cast(List[str], d.pop("groups"))

        bio = d.pop("bio")

        def _parse_home_channel(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        home_channel = _parse_home_channel(d.pop("homeChannel"))

        user_detail = cls(
            id=id,
            state=state,
            bot=bot,
            icon_file_id=icon_file_id,
            display_name=display_name,
            name=name,
            twitter_id=twitter_id,
            last_online=last_online,
            updated_at=updated_at,
            tags=tags,
            groups=groups,
            bio=bio,
            home_channel=home_channel,
        )

        user_detail.additional_properties = d
        return user_detail

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
