import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.file_info_thumbnail_type_0 import FileInfoThumbnailType0
    from ..models.thumbnail_info import ThumbnailInfo


T = TypeVar("T", bound="FileInfo")


@_attrs_define
class FileInfo:
    """ファイル情報

    Attributes:
        id (str): ファイルUUID
        name (str): ファイル名
        mime (str): MIMEタイプ
        size (int): ファイルサイズ
        md5 (str): MD5ハッシュ
        is_animated_image (bool): アニメーション画像かどうか
        created_at (datetime.datetime): アップロード日時
        thumbnails (List['ThumbnailInfo']):
        thumbnail (Union['FileInfoThumbnailType0', None]): サムネイル情報
            サムネイルが存在しない場合はnullになります
            Deprecated: thumbnailsを参照してください
        channel_id (Union[None, str]): 属しているチャンネルUUID
        uploader_id (Union[None, str]): アップロード者UUID
    """

    id: str
    name: str
    mime: str
    size: int
    md5: str
    is_animated_image: bool
    created_at: datetime.datetime
    thumbnails: List["ThumbnailInfo"]
    thumbnail: Union["FileInfoThumbnailType0", None]
    channel_id: Union[None, str]
    uploader_id: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.file_info_thumbnail_type_0 import FileInfoThumbnailType0

        id = self.id

        name = self.name

        mime = self.mime

        size = self.size

        md5 = self.md5

        is_animated_image = self.is_animated_image

        created_at = self.created_at.isoformat()

        thumbnails = []
        for thumbnails_item_data in self.thumbnails:
            thumbnails_item = thumbnails_item_data.to_dict()
            thumbnails.append(thumbnails_item)

        thumbnail: Union[Dict[str, Any], None]
        if isinstance(self.thumbnail, FileInfoThumbnailType0):
            thumbnail = self.thumbnail.to_dict()
        else:
            thumbnail = self.thumbnail

        channel_id: Union[None, str]
        channel_id = self.channel_id

        uploader_id: Union[None, str]
        uploader_id = self.uploader_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "mime": mime,
                "size": size,
                "md5": md5,
                "isAnimatedImage": is_animated_image,
                "createdAt": created_at,
                "thumbnails": thumbnails,
                "thumbnail": thumbnail,
                "channelId": channel_id,
                "uploaderId": uploader_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_info_thumbnail_type_0 import FileInfoThumbnailType0
        from ..models.thumbnail_info import ThumbnailInfo

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        mime = d.pop("mime")

        size = d.pop("size")

        md5 = d.pop("md5")

        is_animated_image = d.pop("isAnimatedImage")

        created_at = isoparse(d.pop("createdAt"))

        thumbnails = []
        _thumbnails = d.pop("thumbnails")
        for thumbnails_item_data in _thumbnails:
            thumbnails_item = ThumbnailInfo.from_dict(thumbnails_item_data)

            thumbnails.append(thumbnails_item)

        def _parse_thumbnail(data: object) -> Union["FileInfoThumbnailType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                thumbnail_type_0 = FileInfoThumbnailType0.from_dict(data)

                return thumbnail_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FileInfoThumbnailType0", None], data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail"))

        def _parse_channel_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        channel_id = _parse_channel_id(d.pop("channelId"))

        def _parse_uploader_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        uploader_id = _parse_uploader_id(d.pop("uploaderId"))

        file_info = cls(
            id=id,
            name=name,
            mime=mime,
            size=size,
            md5=md5,
            is_animated_image=is_animated_image,
            created_at=created_at,
            thumbnails=thumbnails,
            thumbnail=thumbnail,
            channel_id=channel_id,
            uploader_id=uploader_id,
        )

        file_info.additional_properties = d
        return file_info

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
