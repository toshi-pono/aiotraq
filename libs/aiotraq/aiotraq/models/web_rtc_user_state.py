from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.web_rtc_user_state_sessions_item import WebRTCUserStateSessionsItem


T = TypeVar("T", bound="WebRTCUserState")


@_attrs_define
class WebRTCUserState:
    """WebRTC状態

    Attributes:
        user_id (str): ユーザーUUID
        channel_id (str): チャンネルUUID
        sessions (List['WebRTCUserStateSessionsItem']): セッションの配列
    """

    user_id: str
    channel_id: str
    sessions: List["WebRTCUserStateSessionsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        channel_id = self.channel_id

        sessions = []
        for sessions_item_data in self.sessions:
            sessions_item = sessions_item_data.to_dict()
            sessions.append(sessions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "channelId": channel_id,
                "sessions": sessions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.web_rtc_user_state_sessions_item import WebRTCUserStateSessionsItem

        d = src_dict.copy()
        user_id = d.pop("userId")

        channel_id = d.pop("channelId")

        sessions = []
        _sessions = d.pop("sessions")
        for sessions_item_data in _sessions:
            sessions_item = WebRTCUserStateSessionsItem.from_dict(sessions_item_data)

            sessions.append(sessions_item)

        web_rtc_user_state = cls(
            user_id=user_id,
            channel_id=channel_id,
            sessions=sessions,
        )

        web_rtc_user_state.additional_properties = d
        return web_rtc_user_state

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
