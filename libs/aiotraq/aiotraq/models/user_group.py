import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.user_group_member import UserGroupMember


T = TypeVar("T", bound="UserGroup")


@_attrs_define
class UserGroup:
    """ユーザーグループ

    Attributes:
        id (str): グループUUID
        name (str): グループ名
        description (str): グループ説明
        type (str): グループタイプ
        icon (str): グループアイコンUUID
        members (List['UserGroupMember']): グループメンバーの配列
        created_at (datetime.datetime): 作成日時
        updated_at (datetime.datetime): 更新日時
        admins (List[str]): グループ管理者のUUIDの配列
    """

    id: str
    name: str
    description: str
    type: str
    icon: str
    members: List["UserGroupMember"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    admins: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        type = self.type

        icon = self.icon

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        admins = self.admins

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "type": type,
                "icon": icon,
                "members": members,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "admins": admins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_group_member import UserGroupMember

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        type = d.pop("type")

        icon = d.pop("icon")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = UserGroupMember.from_dict(members_item_data)

            members.append(members_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        admins = cast(List[str], d.pop("admins"))

        user_group = cls(
            id=id,
            name=name,
            description=description,
            type=type,
            icon=icon,
            members=members,
            created_at=created_at,
            updated_at=updated_at,
            admins=admins,
        )

        user_group.additional_properties = d
        return user_group

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
