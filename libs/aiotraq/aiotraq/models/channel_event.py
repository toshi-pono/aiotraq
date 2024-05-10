import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.channel_event_type import ChannelEventType

if TYPE_CHECKING:
    from ..models.child_created_event import ChildCreatedEvent
    from ..models.forced_notification_changed_event import ForcedNotificationChangedEvent
    from ..models.name_changed_event import NameChangedEvent
    from ..models.parent_changed_event import ParentChangedEvent
    from ..models.pin_added_event import PinAddedEvent
    from ..models.pin_removed_event import PinRemovedEvent
    from ..models.subscribers_changed_event import SubscribersChangedEvent
    from ..models.topic_changed_event import TopicChangedEvent
    from ..models.visibility_changed_event import VisibilityChangedEvent


T = TypeVar("T", bound="ChannelEvent")


@_attrs_define
class ChannelEvent:
    """チャンネルイベント

    Attributes:
        type (ChannelEventType): イベントタイプ
        datetime_ (datetime.datetime): イベント日時
        detail (Union['ChildCreatedEvent', 'ForcedNotificationChangedEvent', 'NameChangedEvent', 'ParentChangedEvent',
            'PinAddedEvent', 'PinRemovedEvent', 'SubscribersChangedEvent', 'TopicChangedEvent', 'VisibilityChangedEvent']):
            イベント内容
    """

    type: ChannelEventType
    datetime_: datetime.datetime
    detail: Union[
        "ChildCreatedEvent",
        "ForcedNotificationChangedEvent",
        "NameChangedEvent",
        "ParentChangedEvent",
        "PinAddedEvent",
        "PinRemovedEvent",
        "SubscribersChangedEvent",
        "TopicChangedEvent",
        "VisibilityChangedEvent",
    ]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.forced_notification_changed_event import ForcedNotificationChangedEvent
        from ..models.name_changed_event import NameChangedEvent
        from ..models.parent_changed_event import ParentChangedEvent
        from ..models.pin_added_event import PinAddedEvent
        from ..models.pin_removed_event import PinRemovedEvent
        from ..models.subscribers_changed_event import SubscribersChangedEvent
        from ..models.topic_changed_event import TopicChangedEvent
        from ..models.visibility_changed_event import VisibilityChangedEvent

        type = self.type.value

        datetime_ = self.datetime_.isoformat()

        detail: Dict[str, Any]
        if isinstance(self.detail, TopicChangedEvent):
            detail = self.detail.to_dict()
        elif isinstance(self.detail, SubscribersChangedEvent):
            detail = self.detail.to_dict()
        elif isinstance(self.detail, PinAddedEvent):
            detail = self.detail.to_dict()
        elif isinstance(self.detail, PinRemovedEvent):
            detail = self.detail.to_dict()
        elif isinstance(self.detail, NameChangedEvent):
            detail = self.detail.to_dict()
        elif isinstance(self.detail, ParentChangedEvent):
            detail = self.detail.to_dict()
        elif isinstance(self.detail, VisibilityChangedEvent):
            detail = self.detail.to_dict()
        elif isinstance(self.detail, ForcedNotificationChangedEvent):
            detail = self.detail.to_dict()
        else:
            detail = self.detail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "datetime": datetime_,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.child_created_event import ChildCreatedEvent
        from ..models.forced_notification_changed_event import ForcedNotificationChangedEvent
        from ..models.name_changed_event import NameChangedEvent
        from ..models.parent_changed_event import ParentChangedEvent
        from ..models.pin_added_event import PinAddedEvent
        from ..models.pin_removed_event import PinRemovedEvent
        from ..models.subscribers_changed_event import SubscribersChangedEvent
        from ..models.topic_changed_event import TopicChangedEvent
        from ..models.visibility_changed_event import VisibilityChangedEvent

        d = src_dict.copy()
        type = ChannelEventType(d.pop("type"))

        datetime_ = isoparse(d.pop("datetime"))

        def _parse_detail(
            data: object,
        ) -> Union[
            "ChildCreatedEvent",
            "ForcedNotificationChangedEvent",
            "NameChangedEvent",
            "ParentChangedEvent",
            "PinAddedEvent",
            "PinRemovedEvent",
            "SubscribersChangedEvent",
            "TopicChangedEvent",
            "VisibilityChangedEvent",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail_type_0 = TopicChangedEvent.from_dict(data)

                return detail_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail_type_1 = SubscribersChangedEvent.from_dict(data)

                return detail_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail_type_2 = PinAddedEvent.from_dict(data)

                return detail_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail_type_3 = PinRemovedEvent.from_dict(data)

                return detail_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail_type_4 = NameChangedEvent.from_dict(data)

                return detail_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail_type_5 = ParentChangedEvent.from_dict(data)

                return detail_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail_type_6 = VisibilityChangedEvent.from_dict(data)

                return detail_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail_type_7 = ForcedNotificationChangedEvent.from_dict(data)

                return detail_type_7
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            detail_type_8 = ChildCreatedEvent.from_dict(data)

            return detail_type_8

        detail = _parse_detail(d.pop("detail"))

        channel_event = cls(
            type=type,
            datetime_=datetime_,
            detail=detail,
        )

        channel_event.additional_properties = d
        return channel_event

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
