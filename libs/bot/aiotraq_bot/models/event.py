from pydantic import BaseModel
from .common import (
    BasePayload,
    ChannelPayload,
    MessagePayload,
    MessageStampPayload,
    UserGroupAdminPayload,
    UserGroupPayload,
    UserPayload,
    GroupMemberPayload,
)


class PingPayload(BasePayload):
    """PINGイベントペイロード"""

    pass


class JoinedPayload(BasePayload):
    """JOINEDイベントペイロード

    Attributes:
        channel (ChannelPayload): 参加したチャンネル
    """

    channel: ChannelPayload


class LeftPayload(BasePayload):
    """LEFTイベントペイロード

    Attributes:
        channel (ChannelPayload): 退出したチャンネル
    """

    channel: ChannelPayload


class MessageCreatedPayload(BasePayload):
    """MESSAGE_CREATEDイベントペイロード

    Attributes:
        message (MessagePayload): 投稿されたメッセージ
    """

    message: MessagePayload


class MessageUpdatedPayload(BasePayload):
    """MESSAGE_UPDATEDイベントペイロード

    Attributes:
        message (MessagePayload): 更新されたメッセージ
    """

    message: MessagePayload


class DeletedMessage(BaseModel):
    """削除されたメッセージ

    Attributes:
        id (str): メッセージUUID
        channelId (str): 投稿先チャンネルUUID
    """

    id: str
    channelId: str


class MessageDeletedPayload(BasePayload):
    """MESSAGE_DELETEDイベントペイロード

    Attributes:
        message (DeletedMessage): 削除されたメッセージ
    """

    message: DeletedMessage


class BotMessageStampsUpdatedPayload(BasePayload):
    """BOT_MESSAGE_STAMPS_UPDATEDイベントペイロード

    Attributes:
        messageId (str): スタンプの更新があったメッセージUUID
        stamps (list[MessageStampPayload]): メッセージに現在ついている全てのスタンプ
    """

    messageId: str
    stamps: list[MessageStampPayload]


class DirectMessageCreatedPayload(BasePayload):
    """DIRECT_MESSAGE_CREATEDイベントペイロード

    Attributes:
        message (MessagePayload): 投稿されたメッセージ
    """

    message: MessagePayload


class DirectMessageUpdatedPayload(BasePayload):
    """DIRECT_MESSAGE_UPDATEDイベントペイロード

    Attributes:
        message (MessagePayload): 更新されたメッセージ
    """

    message: MessagePayload


class DeletedDirectMessage(BaseModel):
    """削除されたダイレクトメッセージ

    Attributes:
        id (str): メッセージUUID
        userId (str): DMの宛先ユーザーUUID
        channelId (str): 投稿先チャンネルUUID
    """

    id: str
    userId: str
    channelId: str


class DirectMessageDeletedPayload(BasePayload):
    """DIRECT_MESSAGE_DELETEDイベントペイロード

    Attributes:
        message (DeletedDirectMessage): 削除されたメッセージ
    """

    message: DeletedDirectMessage


class ChannelCreatedPayload(BasePayload):
    """CHANNEL_CREATEDイベントペイロード

    Attributes:
        channel (ChannelPayload): 作成されたチャンネル
    """

    channel: ChannelPayload


class ChannelTopicChangedPayload(BasePayload):
    """CHANNEL_TOPIC_CHANGEDイベントペイロード

    Attributes:
        channel (ChannelPayload): 変更されたチャンネル
        topic (str): 変更後のトピック
        updater (UserPayload): トピック更新者
    """

    channel: ChannelPayload
    topic: str
    updater: UserPayload


class UserCreatedPayload(BasePayload):
    """USER_CREATEDイベントペイロード

    Attributes:
        user (UserPayload): 作成されたユーザー
    """

    user: UserPayload


class StampCreatedPayload(BasePayload):
    """STAMP_CREATEDイベントペイロード

    Attributes:
        id (str): スタンプUUID
        name (str): スタンプ名
        fileId (str): スタンプ画像ファイルUUID
        creator (UserPayload): スタンプを作成したユーザー
    """

    id: str
    name: str
    fileId: str
    creator: UserPayload


class TagAddedPayload(BasePayload):
    """TAG_ADDEDイベントペイロード

    Attributes:
        tagId (str): タグUUID
        tag (str): タグ名
    """

    tagId: str
    tag: str


class TagRemovedPayload(BasePayload):
    """TAG_REMOVEDイベントペイロード

    Attributes:
        tagId (str): タグUUID
        tag (str): タグ名
    """

    tagId: str
    tag: str


class UserGroupCreatedPayload(BasePayload):
    """USER_GROUP_CREATEDイベントペイロード

    Attributes:
        group (UserGroupPayload): 作成されたグループ
    """

    group: UserGroupPayload


class UserGroupUpdatedPayload(BasePayload):
    """USER_GROUP_UPDATEDイベントペイロード

    Attributes:
        groupId (str): 更新されたグループUUID
    """

    groupId: str


class UserGroupDeletedPayload(BasePayload):
    """USER_GROUP_DELETEDイベントペイロード

    Attributes:
        groupId (str): 削除されたグループUUID
    """

    groupId: str


class UserGroupMemberAddedPayload(BasePayload):
    """USER_GROUP_MEMBER_ADDEDイベントペイロード

    Attributes:
        groupMember (GroupMemberPayload): 追加されたグループメンバー情報
    """

    groupMember: GroupMemberPayload


class UserGroupMemberUpdatedPayload(BasePayload):
    """USER_GROUP_MEMBER_UPDATEDイベントペイロード

    Attributes:
        groupMember (GroupMemberPayload): 更新されたグループメンバー情報
    """

    groupMember: GroupMemberPayload


class UserGroupMemberRemovedPayload(BasePayload):
    """USER_GROUP_MEMBER_REMOVEDイベントペイロード

    Attributes:
        groupMember (GroupMemberPayload): 削除されたグループメンバー情報
    """

    groupMember: GroupMemberPayload


class UserGroupAdminAddedPayload(BasePayload):
    """USER_GROUP_ADMIN_ADDEDイベントペイロード

    Attributes:
        groupMember (UserGroupAdminPayload): 追加されたグループ管理者情報
    """

    groupMember: UserGroupAdminPayload


class UserGroupAdminRemovedPayload(BasePayload):
    """USER_GROUP_ADMIN_REMOVEDイベントペイロード

    Attributes:
        groupMember (UserGroupAdminPayload): 削除されたグループ管理者情報
    """

    groupMember: UserGroupAdminPayload
