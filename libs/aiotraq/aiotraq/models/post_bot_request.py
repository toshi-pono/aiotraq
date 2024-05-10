from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bot_mode import BotMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostBotRequest")


@_attrs_define
class PostBotRequest:
    """BOT作成リクエスト

    Attributes:
        name (str): BOTユーザーID
            自動的に接頭辞"BOT_"が付与されます
        display_name (str): BOTユーザー表示名
        description (str): BOTの説明
        mode (BotMode): BOT動作モード

            HTTP: HTTP Mode
            WebSocket: WebSocket Mode
        endpoint (Union[Unset, str]): BOTサーバーエンドポイント
            BOT動作モードがHTTPの場合必須です
    """

    name: str
    display_name: str
    description: str
    mode: BotMode
    endpoint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        display_name = self.display_name

        description = self.description

        mode = self.mode.value

        endpoint = self.endpoint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "description": description,
                "mode": mode,
            }
        )
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("displayName")

        description = d.pop("description")

        mode = BotMode(d.pop("mode"))

        endpoint = d.pop("endpoint", UNSET)

        post_bot_request = cls(
            name=name,
            display_name=display_name,
            description=description,
            mode=mode,
            endpoint=endpoint,
        )

        post_bot_request.additional_properties = d
        return post_bot_request

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
