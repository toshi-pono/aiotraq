import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.channel_view_state import ChannelViewState

T = TypeVar("T", bound="ChannelViewer")


@_attrs_define
class ChannelViewer:
    """チャンネル閲覧者情報

    Attributes:
        user_id (str): ユーザーUUID
        state (ChannelViewState): 閲覧状態
        updated_at (datetime.datetime): 更新日時
    """

    user_id: str
    state: ChannelViewState
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        state = self.state.value

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "state": state,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        state = ChannelViewState(d.pop("state"))

        updated_at = isoparse(d.pop("updatedAt"))

        channel_viewer = cls(
            user_id=user_id,
            state=state,
            updated_at=updated_at,
        )

        channel_viewer.additional_properties = d
        return channel_viewer

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
