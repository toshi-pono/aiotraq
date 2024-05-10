import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MessageStamp")


@_attrs_define
class MessageStamp:
    """メッセージに押されたスタンプ

    Attributes:
        user_id (str): ユーザーUUID
        stamp_id (str): スタンプUUID
        count (int): スタンプ数
        created_at (datetime.datetime): スタンプが最初に押された日時
        updated_at (datetime.datetime): スタンプが最後に押された日時
    """

    user_id: str
    stamp_id: str
    count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        stamp_id = self.stamp_id

        count = self.count

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "stampId": stamp_id,
                "count": count,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        stamp_id = d.pop("stampId")

        count = d.pop("count")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        message_stamp = cls(
            user_id=user_id,
            stamp_id=stamp_id,
            count=count,
            created_at=created_at,
            updated_at=updated_at,
        )

        message_stamp.additional_properties = d
        return message_stamp

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
