import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UserTag")


@_attrs_define
class UserTag:
    """ユーザータグ

    Attributes:
        tag_id (str): タグUUID
        tag (str): タグ文字列
        is_locked (bool): タグがロックされているか
        created_at (datetime.datetime): タグ付与日時
        updated_at (datetime.datetime): タグ更新日時
    """

    tag_id: str
    tag: str
    is_locked: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag_id = self.tag_id

        tag = self.tag

        is_locked = self.is_locked

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tagId": tag_id,
                "tag": tag,
                "isLocked": is_locked,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_id = d.pop("tagId")

        tag = d.pop("tag")

        is_locked = d.pop("isLocked")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        user_tag = cls(
            tag_id=tag_id,
            tag=tag,
            is_locked=is_locked,
            created_at=created_at,
            updated_at=updated_at,
        )

        user_tag.additional_properties = d
        return user_tag

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
