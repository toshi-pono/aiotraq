import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="ClippedMessage")


@_attrs_define
class ClippedMessage:
    """クリップされたメッセージ

    Attributes:
        message (Message): メッセージ
        clipped_at (datetime.datetime): クリップした日時
    """

    message: "Message"
    clipped_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message.to_dict()

        clipped_at = self.clipped_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "clippedAt": clipped_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message import Message

        d = src_dict.copy()
        message = Message.from_dict(d.pop("message"))

        clipped_at = isoparse(d.pop("clippedAt"))

        clipped_message = cls(
            message=message,
            clipped_at=clipped_at,
        )

        clipped_message.additional_properties = d
        return clipped_message

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
