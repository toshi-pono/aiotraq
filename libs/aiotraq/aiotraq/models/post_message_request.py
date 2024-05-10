from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMessageRequest")


@_attrs_define
class PostMessageRequest:
    """メッセージ投稿リクエスト

    Attributes:
        content (str): メッセージ本文
        embed (Union[Unset, bool]): メンション・チャンネルリンクを自動埋め込みするか Default: False.
    """

    content: str
    embed: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        embed = self.embed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if embed is not UNSET:
            field_dict["embed"] = embed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        embed = d.pop("embed", UNSET)

        post_message_request = cls(
            content=content,
            embed=embed,
        )

        post_message_request.additional_properties = d
        return post_message_request

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
