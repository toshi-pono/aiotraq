from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="SearchMessagesMessageSearchResult")


@_attrs_define
class SearchMessagesMessageSearchResult:
    """メッセージ検索結果

    Attributes:
        total_hits (int): 検索にヒットしたメッセージ件数
        hits (List['Message']): 検索にヒットしたメッセージの配列
    """

    total_hits: int
    hits: List["Message"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_hits = self.total_hits

        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()
            hits.append(hits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalHits": total_hits,
                "hits": hits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message import Message

        d = src_dict.copy()
        total_hits = d.pop("totalHits")

        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = Message.from_dict(hits_item_data)

            hits.append(hits_item)

        search_messages_message_search_result = cls(
            total_hits=total_hits,
            hits=hits,
        )

        search_messages_message_search_result.additional_properties = d
        return search_messages_message_search_result

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
