import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bot_mode import BotMode
from ..models.bot_state import BotState

if TYPE_CHECKING:
    from ..models.bot_tokens import BotTokens


T = TypeVar("T", bound="BotDetail")


@_attrs_define
class BotDetail:
    """BOT詳細情報

    Attributes:
        id (str): BOT UUID
        updated_at (datetime.datetime): 更新日時
        created_at (datetime.datetime): 作成日時
        mode (BotMode): BOT動作モード

            HTTP: HTTP Mode
            WebSocket: WebSocket Mode
        state (BotState): BOT状態
            0: 停止
            1: 有効
            2: 一時停止
        subscribe_events (List[str]): BOTが購読しているイベントの配列
        developer_id (str): BOT開発者UUID
        description (str): 説明
        bot_user_id (str): BOTユーザーUUID
        tokens (BotTokens): BOTのトークン情報
        endpoint (str): BOTサーバーエンドポイント
        privileged (bool): 特権BOTかどうか
        channels (List[str]): BOTが参加しているチャンネルのUUID配列
    """

    id: str
    updated_at: datetime.datetime
    created_at: datetime.datetime
    mode: BotMode
    state: BotState
    subscribe_events: List[str]
    developer_id: str
    description: str
    bot_user_id: str
    tokens: "BotTokens"
    endpoint: str
    privileged: bool
    channels: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        mode = self.mode.value

        state = self.state.value

        subscribe_events = self.subscribe_events

        developer_id = self.developer_id

        description = self.description

        bot_user_id = self.bot_user_id

        tokens = self.tokens.to_dict()

        endpoint = self.endpoint

        privileged = self.privileged

        channels = self.channels

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "mode": mode,
                "state": state,
                "subscribeEvents": subscribe_events,
                "developerId": developer_id,
                "description": description,
                "botUserId": bot_user_id,
                "tokens": tokens,
                "endpoint": endpoint,
                "privileged": privileged,
                "channels": channels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bot_tokens import BotTokens

        d = src_dict.copy()
        id = d.pop("id")

        updated_at = isoparse(d.pop("updatedAt"))

        created_at = isoparse(d.pop("createdAt"))

        mode = BotMode(d.pop("mode"))

        state = BotState(d.pop("state"))

        subscribe_events = cast(List[str], d.pop("subscribeEvents"))

        developer_id = d.pop("developerId")

        description = d.pop("description")

        bot_user_id = d.pop("botUserId")

        tokens = BotTokens.from_dict(d.pop("tokens"))

        endpoint = d.pop("endpoint")

        privileged = d.pop("privileged")

        channels = cast(List[str], d.pop("channels"))

        bot_detail = cls(
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            mode=mode,
            state=state,
            subscribe_events=subscribe_events,
            developer_id=developer_id,
            description=description,
            bot_user_id=bot_user_id,
            tokens=tokens,
            endpoint=endpoint,
            privileged=privileged,
            channels=channels,
        )

        bot_detail.additional_properties = d
        return bot_detail

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
