import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Webhook")


@_attrs_define
class Webhook:
    """Webhook情報

    Attributes:
        id (str): WebhookUUID
        bot_user_id (str): WebhookユーザーUUID
        display_name (str): Webhookユーザー表示名
        description (str): 説明
        secure (bool): セキュアWebhookかどうか
        channel_id (str): デフォルトの投稿先チャンネルUUID
        owner_id (str): オーナーUUID
        created_at (datetime.datetime): 作成日時
        updated_at (datetime.datetime): 更新日時
    """

    id: str
    bot_user_id: str
    display_name: str
    description: str
    secure: bool
    channel_id: str
    owner_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        bot_user_id = self.bot_user_id

        display_name = self.display_name

        description = self.description

        secure = self.secure

        channel_id = self.channel_id

        owner_id = self.owner_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "botUserId": bot_user_id,
                "displayName": display_name,
                "description": description,
                "secure": secure,
                "channelId": channel_id,
                "ownerId": owner_id,
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

        display_name = d.pop("displayName")

        description = d.pop("description")

        secure = d.pop("secure")

        channel_id = d.pop("channelId")

        owner_id = d.pop("ownerId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        webhook = cls(
            id=id,
            bot_user_id=bot_user_id,
            display_name=display_name,
            description=description,
            secure=secure,
            channel_id=channel_id,
            owner_id=owner_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        webhook.additional_properties = d
        return webhook

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
