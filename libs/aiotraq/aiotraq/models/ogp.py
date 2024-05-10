from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ogp_media import OgpMedia


T = TypeVar("T", bound="Ogp")


@_attrs_define
class Ogp:
    """OGPの情報

    Attributes:
        type (str):
        title (str):
        url (str):
        images (List['OgpMedia']):
        description (str):
        videos (List['OgpMedia']):
    """

    type: str
    title: str
    url: str
    images: List["OgpMedia"]
    description: str
    videos: List["OgpMedia"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        title = self.title

        url = self.url

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        description = self.description

        videos = []
        for videos_item_data in self.videos:
            videos_item = videos_item_data.to_dict()
            videos.append(videos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "title": title,
                "url": url,
                "images": images,
                "description": description,
                "videos": videos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ogp_media import OgpMedia

        d = src_dict.copy()
        type = d.pop("type")

        title = d.pop("title")

        url = d.pop("url")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = OgpMedia.from_dict(images_item_data)

            images.append(images_item)

        description = d.pop("description")

        videos = []
        _videos = d.pop("videos")
        for videos_item_data in _videos:
            videos_item = OgpMedia.from_dict(videos_item_data)

            videos.append(videos_item)

        ogp = cls(
            type=type,
            title=title,
            url=url,
            images=images,
            description=description,
            videos=videos,
        )

        ogp.additional_properties = d
        return ogp

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
