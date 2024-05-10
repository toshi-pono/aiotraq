import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Stamp")


@_attrs_define
class Stamp:
    """スタンプ情報

    Attributes:
        id (str): スタンプUUID
        name (str): スタンプ名
        creator_id (str): 作成者UUID
        created_at (datetime.datetime): 作成日時
        updated_at (datetime.datetime): 更新日時
        file_id (str): ファイルUUID
        is_unicode (bool): Unicode絵文字か
    """

    id: str
    name: str
    creator_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    file_id: str
    is_unicode: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        creator_id = self.creator_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        file_id = self.file_id

        is_unicode = self.is_unicode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "creatorId": creator_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "fileId": file_id,
                "isUnicode": is_unicode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        creator_id = d.pop("creatorId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        file_id = d.pop("fileId")

        is_unicode = d.pop("isUnicode")

        stamp = cls(
            id=id,
            name=name,
            creator_id=creator_id,
            created_at=created_at,
            updated_at=updated_at,
            file_id=file_id,
            is_unicode=is_unicode,
        )

        stamp.additional_properties = d
        return stamp

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
