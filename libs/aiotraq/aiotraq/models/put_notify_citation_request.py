from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutNotifyCitationRequest")


@_attrs_define
class PutNotifyCitationRequest:
    """メッセージ引用通知設定リクエスト

    Attributes:
        notify_citation (bool): メッセージ引用通知の設定情報
    """

    notify_citation: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notify_citation = self.notify_citation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notifyCitation": notify_citation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        notify_citation = d.pop("notifyCitation")

        put_notify_citation_request = cls(
            notify_citation=notify_citation,
        )

        put_notify_citation_request.additional_properties = d
        return put_notify_citation_request

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
