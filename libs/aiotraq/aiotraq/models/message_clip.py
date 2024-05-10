import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MessageClip")


@_attrs_define
class MessageClip:
    """メッセージクリップ

    Attributes:
        folder_id (str): クリップされているフォルダのID
        clipped_at (datetime.datetime): クリップされた日時
    """

    folder_id: str
    clipped_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        folder_id = self.folder_id

        clipped_at = self.clipped_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folderId": folder_id,
                "clippedAt": clipped_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        folder_id = d.pop("folderId")

        clipped_at = isoparse(d.pop("clippedAt"))

        message_clip = cls(
            folder_id=folder_id,
            clipped_at=clipped_at,
        )

        message_clip.additional_properties = d
        return message_clip

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
