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
    """PINGイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
    """

    pass


class JoinedPayload(BasePayload):
    """JOINEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        channel (ChannelPayload): 参加したチャンネル
            id (str): チャンネルUUID
            name (str): チャンネル名
            path (str): チャンネルパス
            parentId (str): 親チャンネルのUUID, ルートチャンネルは"00000000-0000-0000-0000-000000000000"
            creator (UserPayload): チャンネル作成者
            createdAt (datetime.datetime): チャンネル作成日時
            updatedAt (datetime.datetime): チャンネル更新日時
    """

    channel: ChannelPayload


class LeftPayload(BasePayload):
    """LEFTイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        channel (ChannelPayload): 退出したチャンネル
            id (str): チャンネルUUID
            name (str): チャンネル名
            path (str): チャンネルパス
            parentId (str): 親チャンネルのUUID, ルートチャンネルは"00000000-0000-0000-0000-000000000000"
            creator (UserPayload): チャンネル作成者
            createdAt (datetime.datetime): チャンネル作成日時
            updatedAt (datetime.datetime): チャンネル更新日時
    """

    channel: ChannelPayload


class MessageCreatedPayload(BasePayload):
    """MESSAGE_CREATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        message (MessagePayload): 投稿されたメッセージ
            id (str): メッセージUUID
            user (UserPayload): メッセージ投稿者
            channelId (str): 投稿先チャンネルUUID
            text (str): 生メッセージ本文
            plainText (str): メッセージ本文(埋め込み情報・改行なし)
            embedded (list[EmbeddedInfoPayload]): メッセージ埋め込み情報の配列
            createdAt (datetime.datetime): メッセージ投稿日時
            updatedAt (datetime.datetime): メッセージ更新日時
    """

    message: MessagePayload


class MessageUpdatedPayload(BasePayload):
    """MESSAGE_UPDATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        message (MessagePayload): 更新されたメッセージ
            id (str): メッセージUUID
            user (UserPayload): メッセージ投稿者
            channelId (str): 投稿先チャンネルUUID
            text (str): 生メッセージ本文
            plainText (str): メッセージ本文(埋め込み情報・改行なし)
            embedded (list[EmbeddedInfoPayload]): メッセージ埋め込み情報の配列
            createdAt (datetime.datetime): メッセージ投稿日時
            updatedAt (datetime.datetime): メッセージ更新日時
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
        eventTime (datetime.datetime): イベント発生日時
        message (DeletedMessage): 削除されたメッセージ
            id (str): メッセージUUID
            channelId (str): 投稿先チャンネルUUID
    """

    message: DeletedMessage


class BotMessageStampsUpdatedPayload(BasePayload):
    """BOT_MESSAGE_STAMPS_UPDATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        messageId (str): スタンプの更新があったメッセージUUID
        stamps (list[MessageStampPayload]): メッセージに現在ついている全てのスタンプ
            stampId (str): スタンプUUID
            userId (str): スタンプを押したユーザーUUID
            count (int): このユーザーによって押されたこのスタンプの数
            createdAt (datetime.datetime): 最初にスタンプが押された日時
            updatedAt (datetime.datetime): 最後にスタンプが押された日時
    """

    messageId: str
    stamps: list[MessageStampPayload]


class DirectMessageCreatedPayload(BasePayload):
    """DIRECT_MESSAGE_CREATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        message (MessagePayload): 投稿されたメッセージ
            id (str): メッセージUUID
            user (UserPayload): メッセージ投稿者
            channelId (str): 投稿先チャンネルUUID
            text (str): 生メッセージ本文
            plainText (str): メッセージ本文(埋め込み情報・改行なし)
            embedded (list[EmbeddedInfoPayload]): メッセージ埋め込み情報の配列
            createdAt (datetime.datetime): メッセージ投稿日時
            updatedAt (datetime.datetime): メッセージ更新日時
    """

    message: MessagePayload


class DirectMessageUpdatedPayload(BasePayload):
    """DIRECT_MESSAGE_UPDATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        message (MessagePayload): 更新されたメッセージ
            id (str): メッセージUUID
            user (UserPayload): メッセージ投稿者
            channelId (str): 投稿先チャンネルUUID
            text (str): 生メッセージ本文
            plainText (str): メッセージ本文(埋め込み情報・改行なし)
            embedded (list[EmbeddedInfoPayload]): メッセージ埋め込み情報の配列
            createdAt (datetime.datetime): メッセージ投稿日時
            updatedAt (datetime.datetime): メッセージ更新日時
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
        eventTime (datetime.datetime): イベント発生日時
        message (DeletedDirectMessage): 削除されたメッセージ
            id (str): メッセージUUID
            userId (str): DMの宛先ユーザーUUID
            channelId (str): 投稿先チャンネルUUID
    """

    message: DeletedDirectMessage


class ChannelCreatedPayload(BasePayload):
    """CHANNEL_CREATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        channel (ChannelPayload): 作成されたチャンネル
            id (str): チャンネルUUID
            name (str): チャンネル名
            path (str): チャンネルパス
            parentId (str): 親チャンネルのUUID, ルートチャンネルは"00000000-0000-0000-0000-000000000000"
            creator (UserPayload): チャンネル作成者
            createdAt (datetime.datetime): チャンネル作成日時
            updatedAt (datetime.datetime): チャンネル更新日時
    """

    channel: ChannelPayload


class ChannelTopicChangedPayload(BasePayload):
    """CHANNEL_TOPIC_CHANGEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        channel (ChannelPayload): 変更されたチャンネル
            id (str): チャンネルUUID
            name (str): チャンネル名
            path (str): チャンネルパス
            parentId (str): 親チャンネルのUUID, ルートチャンネルは"00000000-0000-0000-0000-000000000000"
            creator (UserPayload): チャンネル作成者
            createdAt (datetime.datetime): チャンネル作成日時
            updatedAt (datetime.datetime): チャンネル更新日時
        topic (str): 変更後のトピック
        updater (UserPayload): トピック更新者
            id (str): ユーザーUUID
            name (str): ユーザーのtraQ Id
            displayName (str): ユーザーの表示名
            iconId (str): ユーザーアイコンのファイルUUID
            bot (bool): ユーザーがBotかどうか
    """

    channel: ChannelPayload
    topic: str
    updater: UserPayload


class UserCreatedPayload(BasePayload):
    """USER_CREATEDイベントペイロード
    ユーザーが作成された

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        user (UserPayload): 作成されたユーザー
            id (str): ユーザーUUID
            name (str): ユーザーのtraQ Id
            displayName (str): ユーザーの表示名
            iconId (str): ユーザーアイコンのファイルUUID
            bot (bool): ユーザーがBotかどうか
    """

    user: UserPayload


class UserActivatedPayload(BasePayload):
    """USER_ACTIVATEDイベントペイロード
    ユーザーの凍結が解除された

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        user (UserPayload): 凍結解除されたユーザー
            id (str): ユーザーUUID
            name (str): ユーザーのtraQ Id
            displayName (str): ユーザーの表示名
            iconId (str): ユーザーアイコンのファイルUUID
            bot (bool): ユーザーがBotかどうか
    """

    user: UserPayload


class StampCreatedPayload(BasePayload):
    """STAMP_CREATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        id (str): スタンプUUID
        name (str): スタンプ名
        fileId (str): スタンプ画像ファイルUUID
        creator (UserPayload): スタンプを作成したユーザー
            id (str): ユーザーUUID
            name (str): ユーザーのtraQ Id
            displayName (str): ユーザーの表示名
            iconId (str): ユーザーアイコンのファイルUUID
            bot (bool): ユーザーがBotかどうか
    """

    id: str
    name: str
    fileId: str
    creator: UserPayload


class TagAddedPayload(BasePayload):
    """TAG_ADDEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        tagId (str): タグUUID
        tag (str): タグ名
    """

    tagId: str
    tag: str


class TagRemovedPayload(BasePayload):
    """TAG_REMOVEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        tagId (str): タグUUID
        tag (str): タグ名
    """

    tagId: str
    tag: str


class UserGroupCreatedPayload(BasePayload):
    """USER_GROUP_CREATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        group (UserGroupPayload): 作成されたグループ
            id (str): グループUUID
            name (str): グループ名
            description (str): グループの説明
            type (str): グループの種類
            icon (str): グループアイコンのファイルUUID
            admins (list[UserGroupAdminPayload]): グループ管理者の配列
            members (list[UserGroupMemberPayload]): グループメンバーの配列
            createdAt (datetime.datetime): グループ作成日時
            updatedAt (datetime.datetime): グループ更新日時
    """

    group: UserGroupPayload


class UserGroupUpdatedPayload(BasePayload):
    """USER_GROUP_UPDATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        groupId (str): 更新されたグループUUID
    """

    groupId: str


class UserGroupDeletedPayload(BasePayload):
    """USER_GROUP_DELETEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        groupId (str): 削除されたグループUUID
    """

    groupId: str


class UserGroupMemberAddedPayload(BasePayload):
    """USER_GROUP_MEMBER_ADDEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        groupMember (GroupMemberPayload): 追加されたグループメンバー情報
            groupId (str): グループUUID
            userId (str): ユーザーUUID
    """

    groupMember: GroupMemberPayload


class UserGroupMemberUpdatedPayload(BasePayload):
    """USER_GROUP_MEMBER_UPDATEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        groupMember (GroupMemberPayload): 更新されたグループメンバー情報
            groupId (str): グループUUID
            userId (str): ユーザーUUID
    """

    groupMember: GroupMemberPayload


class UserGroupMemberRemovedPayload(BasePayload):
    """USER_GROUP_MEMBER_REMOVEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        groupMember (GroupMemberPayload): 削除されたグループメンバー情報
            groupId (str): グループUUID
            userId (str): ユーザーUUID
    """

    groupMember: GroupMemberPayload


class UserGroupAdminAddedPayload(BasePayload):
    """USER_GROUP_ADMIN_ADDEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        groupMember (UserGroupAdminPayload): 追加されたグループ管理者情報
            groupId (str): グループUUID
            userId (str): ユーザーUUID
    """

    groupMember: UserGroupAdminPayload


class UserGroupAdminRemovedPayload(BasePayload):
    """USER_GROUP_ADMIN_REMOVEDイベントペイロード

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
        groupMember (UserGroupAdminPayload): 削除されたグループ管理者情報
            groupId (str): グループUUID
            userId (str): ユーザーUUID
    """

    groupMember: UserGroupAdminPayload
