import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.user_stats_stamp import UserStatsStamp


T = TypeVar("T", bound="UserStats")


@_attrs_define
class UserStats:
    """ユーザー統計情報

    Attributes:
        total_message_count (int): ユーザーの総投稿メッセージ数(削除されたものも含む)
        stamps (List['UserStatsStamp']): ユーザーのスタンプ統計情報
        datetime_ (datetime.datetime): 統計情報日時
    """

    total_message_count: int
    stamps: List["UserStatsStamp"]
    datetime_: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_message_count = self.total_message_count

        stamps = []
        for stamps_item_data in self.stamps:
            stamps_item = stamps_item_data.to_dict()
            stamps.append(stamps_item)

        datetime_ = self.datetime_.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalMessageCount": total_message_count,
                "stamps": stamps,
                "datetime": datetime_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_stats_stamp import UserStatsStamp

        d = src_dict.copy()
        total_message_count = d.pop("totalMessageCount")

        stamps = []
        _stamps = d.pop("stamps")
        for stamps_item_data in _stamps:
            stamps_item = UserStatsStamp.from_dict(stamps_item_data)

            stamps.append(stamps_item)

        datetime_ = isoparse(d.pop("datetime"))

        user_stats = cls(
            total_message_count=total_message_count,
            stamps=stamps,
            datetime_=datetime_,
        )

        user_stats.additional_properties = d
        return user_stats

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
