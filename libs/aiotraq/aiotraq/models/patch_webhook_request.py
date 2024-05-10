from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchWebhookRequest")


@_attrs_define
class PatchWebhookRequest:
    """Webhook情報変更リクエスト

    Attributes:
        name (Union[Unset, str]): Webhookユーザー表示名
        description (Union[Unset, str]): 説明
        channel_id (Union[Unset, str]): デフォルトの投稿先チャンネルUUID
        secret (Union[Unset, str]): Webhookシークレット
        owner_id (Union[Unset, str]): 移譲先のユーザーUUID
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    channel_id: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        channel_id = self.channel_id

        secret = self.secret

        owner_id = self.owner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if secret is not UNSET:
            field_dict["secret"] = secret
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        channel_id = d.pop("channelId", UNSET)

        secret = d.pop("secret", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        patch_webhook_request = cls(
            name=name,
            description=description,
            channel_id=channel_id,
            secret=secret,
            owner_id=owner_id,
        )

        patch_webhook_request.additional_properties = d
        return patch_webhook_request

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
