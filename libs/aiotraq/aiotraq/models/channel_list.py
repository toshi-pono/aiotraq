from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel import Channel
    from ..models.dm_channel import DMChannel


T = TypeVar("T", bound="ChannelList")


@_attrs_define
class ChannelList:
    """GET /channelsレスポンス

    Attributes:
        public (List['Channel']): パブリックチャンネルの配列
        dm (Union[Unset, List['DMChannel']]): ダイレクトメッセージチャンネルの配列
    """

    public: List["Channel"]
    dm: Union[Unset, List["DMChannel"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        public = []
        for public_item_data in self.public:
            public_item = public_item_data.to_dict()
            public.append(public_item)

        dm: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dm, Unset):
            dm = []
            for dm_item_data in self.dm:
                dm_item = dm_item_data.to_dict()
                dm.append(dm_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public": public,
            }
        )
        if dm is not UNSET:
            field_dict["dm"] = dm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.channel import Channel
        from ..models.dm_channel import DMChannel

        d = src_dict.copy()
        public = []
        _public = d.pop("public")
        for public_item_data in _public:
            public_item = Channel.from_dict(public_item_data)

            public.append(public_item)

        dm = []
        _dm = d.pop("dm", UNSET)
        for dm_item_data in _dm or []:
            dm_item = DMChannel.from_dict(dm_item_data)

            dm.append(dm_item)

        channel_list = cls(
            public=public,
            dm=dm,
        )

        channel_list.additional_properties = d
        return channel_list

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
