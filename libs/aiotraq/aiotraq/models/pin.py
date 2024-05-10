import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="Pin")


@_attrs_define
class Pin:
    """ピン情報(メッセージ本体付き)

    Attributes:
        user_id (str): ピン留めしたユーザーUUID
        pinned_at (datetime.datetime): ピン留めされた日時
        message (Message): メッセージ
    """

    user_id: str
    pinned_at: datetime.datetime
    message: "Message"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        pinned_at = self.pinned_at.isoformat()

        message = self.message.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "pinnedAt": pinned_at,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message import Message

        d = src_dict.copy()
        user_id = d.pop("userId")

        pinned_at = isoparse(d.pop("pinnedAt"))

        message = Message.from_dict(d.pop("message"))

        pin = cls(
            user_id=user_id,
            pinned_at=pinned_at,
            message=message,
        )

        pin.additional_properties = d
        return pin

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
