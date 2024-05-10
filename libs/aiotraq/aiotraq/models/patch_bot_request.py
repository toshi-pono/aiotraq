from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bot_mode import BotMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchBotRequest")


@_attrs_define
class PatchBotRequest:
    """BOT情報変更リクエスト

    Attributes:
        display_name (Union[Unset, str]): BOTユーザー表示名
        description (Union[Unset, str]): BOTの説明
        privileged (Union[Unset, bool]): 特権
        mode (Union[Unset, BotMode]): BOT動作モード

            HTTP: HTTP Mode
            WebSocket: WebSocket Mode
        endpoint (Union[Unset, str]): BOTサーバーエンドポイント
        developer_id (Union[Unset, str]): 移譲先の開発者UUID
        subscribe_events (Union[Unset, List[str]]): 購読するイベント
    """

    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    privileged: Union[Unset, bool] = UNSET
    mode: Union[Unset, BotMode] = UNSET
    endpoint: Union[Unset, str] = UNSET
    developer_id: Union[Unset, str] = UNSET
    subscribe_events: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        description = self.description

        privileged = self.privileged

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        endpoint = self.endpoint

        developer_id = self.developer_id

        subscribe_events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subscribe_events, Unset):
            subscribe_events = self.subscribe_events

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if privileged is not UNSET:
            field_dict["privileged"] = privileged
        if mode is not UNSET:
            field_dict["mode"] = mode
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if developer_id is not UNSET:
            field_dict["developerId"] = developer_id
        if subscribe_events is not UNSET:
            field_dict["subscribeEvents"] = subscribe_events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        privileged = d.pop("privileged", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, BotMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = BotMode(_mode)

        endpoint = d.pop("endpoint", UNSET)

        developer_id = d.pop("developerId", UNSET)

        subscribe_events = cast(List[str], d.pop("subscribeEvents", UNSET))

        patch_bot_request = cls(
            display_name=display_name,
            description=description,
            privileged=privileged,
            mode=mode,
            endpoint=endpoint,
            developer_id=developer_id,
            subscribe_events=subscribe_events,
        )

        patch_bot_request.additional_properties = d
        return patch_bot_request

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
