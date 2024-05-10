from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutMyPasswordRequest")


@_attrs_define
class PutMyPasswordRequest:
    """パスワード変更リクエスト

    Attributes:
        password (str): 現在のパスワード
        new_password (str): 新しいパスワード
    """

    password: str
    new_password: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password

        new_password = self.new_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "newPassword": new_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password")

        new_password = d.pop("newPassword")

        put_my_password_request = cls(
            password=password,
            new_password=new_password,
        )

        put_my_password_request.additional_properties = d
        return put_my_password_request

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
