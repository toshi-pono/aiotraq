from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.version_flags import VersionFlags


T = TypeVar("T", bound="Version")


@_attrs_define
class Version:
    """バージョン・サーバーフラグ情報

    Attributes:
        revision (str): traQ(サーバー)リビジョン
        version (str): traQ(サーバー)バージョン
        flags (VersionFlags):
    """

    revision: str
    version: str
    flags: "VersionFlags"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        revision = self.revision

        version = self.version

        flags = self.flags.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revision": revision,
                "version": version,
                "flags": flags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.version_flags import VersionFlags

        d = src_dict.copy()
        revision = d.pop("revision")

        version = d.pop("version")

        flags = VersionFlags.from_dict(d.pop("flags"))

        version = cls(
            revision=revision,
            version=version,
            flags=flags,
        )

        version.additional_properties = d
        return version

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
