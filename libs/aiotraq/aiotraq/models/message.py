import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.message_stamp import MessageStamp


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """メッセージ

    Attributes:
        id (str): メッセージUUID
        user_id (str): 投稿者UUID
        channel_id (str): チャンネルUUID
        content (str): メッセージ本文
        created_at (datetime.datetime): 投稿日時
        updated_at (datetime.datetime): 編集日時
        pinned (bool): ピン留めされているかどうか
        stamps (List['MessageStamp']): 押されているスタンプの配列
        thread_id (Union[None, str]): スレッドUUID
    """

    id: str
    user_id: str
    channel_id: str
    content: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    pinned: bool
    stamps: List["MessageStamp"]
    thread_id: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        user_id = self.user_id

        channel_id = self.channel_id

        content = self.content

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        pinned = self.pinned

        stamps = []
        for stamps_item_data in self.stamps:
            stamps_item = stamps_item_data.to_dict()
            stamps.append(stamps_item)

        thread_id: Union[None, str]
        thread_id = self.thread_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
                "channelId": channel_id,
                "content": content,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "pinned": pinned,
                "stamps": stamps,
                "threadId": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_stamp import MessageStamp

        d = src_dict.copy()
        id = d.pop("id")

        user_id = d.pop("userId")

        channel_id = d.pop("channelId")

        content = d.pop("content")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        pinned = d.pop("pinned")

        stamps = []
        _stamps = d.pop("stamps")
        for stamps_item_data in _stamps:
            stamps_item = MessageStamp.from_dict(stamps_item_data)

            stamps.append(stamps_item)

        def _parse_thread_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        thread_id = _parse_thread_id(d.pop("threadId"))

        message = cls(
            id=id,
            user_id=user_id,
            channel_id=channel_id,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
            pinned=pinned,
            stamps=stamps,
            thread_id=thread_id,
        )

        message.additional_properties = d
        return message

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
