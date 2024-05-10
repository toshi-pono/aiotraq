from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Channel")


@_attrs_define
class Channel:
    """チャンネル

    Attributes:
        id (str): チャンネルUUID
        parent_id (Union[None, str]): 親チャンネルUUID
        archived (bool): チャンネルがアーカイブされているかどうか
        force (bool): 強制通知チャンネルかどうか
        topic (str): チャンネルトピック
        name (str): チャンネル名
        children (List[str]): 子チャンネルのUUID配列
    """

    id: str
    parent_id: Union[None, str]
    archived: bool
    force: bool
    topic: str
    name: str
    children: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        parent_id: Union[None, str]
        parent_id = self.parent_id

        archived = self.archived

        force = self.force

        topic = self.topic

        name = self.name

        children = self.children

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "parentId": parent_id,
                "archived": archived,
                "force": force,
                "topic": topic,
                "name": name,
                "children": children,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        def _parse_parent_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        parent_id = _parse_parent_id(d.pop("parentId"))

        archived = d.pop("archived")

        force = d.pop("force")

        topic = d.pop("topic")

        name = d.pop("name")

        children = cast(List[str], d.pop("children"))

        channel = cls(
            id=id,
            parent_id=parent_id,
            archived=archived,
            force=force,
            topic=topic,
            name=name,
            children=children,
        )

        channel.additional_properties = d
        return channel

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
