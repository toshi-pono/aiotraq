import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="StampHistoryEntry")


@_attrs_define
class StampHistoryEntry:
    """スタンプ履歴の1項目

    Attributes:
        stamp_id (str): スタンプUUID
        datetime_ (datetime.datetime): 使用日時
    """

    stamp_id: str
    datetime_: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stamp_id = self.stamp_id

        datetime_ = self.datetime_.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stampId": stamp_id,
                "datetime": datetime_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stamp_id = d.pop("stampId")

        datetime_ = isoparse(d.pop("datetime"))

        stamp_history_entry = cls(
            stamp_id=stamp_id,
            datetime_=datetime_,
        )

        stamp_history_entry.additional_properties = d
        return stamp_history_entry

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
