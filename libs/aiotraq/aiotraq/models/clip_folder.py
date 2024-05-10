import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ClipFolder")


@_attrs_define
class ClipFolder:
    """クリップフォルダ情報

    Attributes:
        id (str): フォルダUUID
        name (str): フォルダ名
        created_at (datetime.datetime): 作成日時
        owner_id (str): フォルダ所有者UUID
        description (str): 説明
    """

    id: str
    name: str
    created_at: datetime.datetime
    owner_id: str
    description: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        created_at = self.created_at.isoformat()

        owner_id = self.owner_id

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "createdAt": created_at,
                "ownerId": owner_id,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        created_at = isoparse(d.pop("createdAt"))

        owner_id = d.pop("ownerId")

        description = d.pop("description")

        clip_folder = cls(
            id=id,
            name=name,
            created_at=created_at,
            owner_id=owner_id,
            description=description,
        )

        clip_folder.additional_properties = d
        return clip_folder

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
