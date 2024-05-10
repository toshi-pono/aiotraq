from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebRTCAuthenticateResult")


@_attrs_define
class WebRTCAuthenticateResult:
    """skyway用認証リクエストリザルト

    Attributes:
        peer_id (str): ピアID
        ttl (int): TTL
        timestamp (int): タイムスタンプ
        auth_token (str): 認証トークン
    """

    peer_id: str
    ttl: int
    timestamp: int
    auth_token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        peer_id = self.peer_id

        ttl = self.ttl

        timestamp = self.timestamp

        auth_token = self.auth_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "peerId": peer_id,
                "ttl": ttl,
                "timestamp": timestamp,
                "authToken": auth_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        peer_id = d.pop("peerId")

        ttl = d.pop("ttl")

        timestamp = d.pop("timestamp")

        auth_token = d.pop("authToken")

        web_rtc_authenticate_result = cls(
            peer_id=peer_id,
            ttl=ttl,
            timestamp=timestamp,
            auth_token=auth_token,
        )

        web_rtc_authenticate_result.additional_properties = d
        return web_rtc_authenticate_result

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
