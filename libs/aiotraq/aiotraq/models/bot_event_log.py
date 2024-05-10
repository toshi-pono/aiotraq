import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bot_event_result import BotEventResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="BotEventLog")


@_attrs_define
class BotEventLog:
    """BOTイベントログ

    Attributes:
        bot_id (str): BOT UUID
        request_id (str): リクエストUUID
        event (str): イベントタイプ
        code (int): ステータスコード
        datetime_ (datetime.datetime): イベント日時
        result (Union[Unset, BotEventResult]): イベント配送結果
    """

    bot_id: str
    request_id: str
    event: str
    code: int
    datetime_: datetime.datetime
    result: Union[Unset, BotEventResult] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bot_id = self.bot_id

        request_id = self.request_id

        event = self.event

        code = self.code

        datetime_ = self.datetime_.isoformat()

        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "botId": bot_id,
                "requestId": request_id,
                "event": event,
                "code": code,
                "datetime": datetime_,
            }
        )
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bot_id = d.pop("botId")

        request_id = d.pop("requestId")

        event = d.pop("event")

        code = d.pop("code")

        datetime_ = isoparse(d.pop("datetime"))

        _result = d.pop("result", UNSET)
        result: Union[Unset, BotEventResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = BotEventResult(_result)

        bot_event_log = cls(
            bot_id=bot_id,
            request_id=request_id,
            event=event,
            code=code,
            datetime_=datetime_,
            result=result,
        )

        bot_event_log.additional_properties = d
        return bot_event_log

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
