import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bot_mode import BotMode
from ..models.bot_state import BotState

T = TypeVar("T", bound="Bot")


@_attrs_define
class Bot:
    """BOT情報

    Attributes:
        id (str): BOT UUID
        bot_user_id (str): BOTユーザーUUID
        description (str): 説明
        developer_id (str): BOT開発者UUID
        subscribe_events (List[str]): BOTが購読しているイベントの配列
        mode (BotMode): BOT動作モード

            HTTP: HTTP Mode
            WebSocket: WebSocket Mode
        state (BotState): BOT状態
            0: 停止
            1: 有効
            2: 一時停止
        created_at (datetime.datetime): 作成日時
        updated_at (datetime.datetime): 更新日時
    """

    id: str
    bot_user_id: str
    description: str
    developer_id: str
    subscribe_events: List[str]
    mode: BotMode
    state: BotState
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        bot_user_id = self.bot_user_id

        description = self.description

        developer_id = self.developer_id

        subscribe_events = self.subscribe_events

        mode = self.mode.value

        state = self.state.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "botUserId": bot_user_id,
                "description": description,
                "developerId": developer_id,
                "subscribeEvents": subscribe_events,
                "mode": mode,
                "state": state,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        bot_user_id = d.pop("botUserId")

        description = d.pop("description")

        developer_id = d.pop("developerId")

        subscribe_events = cast(List[str], d.pop("subscribeEvents"))

        mode = BotMode(d.pop("mode"))

        state = BotState(d.pop("state"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        bot = cls(
            id=id,
            bot_user_id=bot_user_id,
            description=description,
            developer_id=developer_id,
            subscribe_events=subscribe_events,
            mode=mode,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
        )

        bot.additional_properties = d
        return bot

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
