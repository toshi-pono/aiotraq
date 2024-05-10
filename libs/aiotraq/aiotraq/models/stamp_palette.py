import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="StampPalette")


@_attrs_define
class StampPalette:
    """スタンプパレット情報

    Attributes:
        id (str): スタンプパレットUUID
        name (str): パレット名
        stamps (List[str]): パレット内のスタンプのUUID配列
        creator_id (str): 作成者UUID
        created_at (datetime.datetime): パレット作成日時
        updated_at (datetime.datetime): パレット更新日時
        description (str): パレット説明
    """

    id: str
    name: str
    stamps: List[str]
    creator_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        stamps = self.stamps

        creator_id = self.creator_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "stamps": stamps,
                "creatorId": creator_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        stamps = cast(List[str], d.pop("stamps"))

        creator_id = d.pop("creatorId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        description = d.pop("description")

        stamp_palette = cls(
            id=id,
            name=name,
            stamps=stamps,
            creator_id=creator_id,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
        )

        stamp_palette.additional_properties = d
        return stamp_palette

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
