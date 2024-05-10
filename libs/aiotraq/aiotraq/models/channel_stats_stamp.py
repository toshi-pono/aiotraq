from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChannelStatsStamp")


@_attrs_define
class ChannelStatsStamp:
    """チャンネル上の特定スタンプ統計情報

    Attributes:
        id (str): スタンプID
        count (int): スタンプ数(同一メッセージ上のものは複数カウントしない)
        total (int): スタンプ数(同一メッセージ上のものも複数カウントする)
    """

    id: str
    count: int
    total: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        count = self.count

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "count": count,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        count = d.pop("count")

        total = d.pop("total")

        channel_stats_stamp = cls(
            id=id,
            count=count,
            total=total,
        )

        channel_stats_stamp.additional_properties = d
        return channel_stats_stamp

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
