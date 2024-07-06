from pydantic import BaseModel
import datetime


class BasePayload(BaseModel):
    """共通部分

    Attributes:
        eventTime (datetime.datetime): イベント発生日時
    """

    eventTime: datetime.datetime


class UserPayload(BaseModel):
    """ユーザー情報ペイロード

    Attributes:
        id (str): ユーザーUUID
        name (str): ユーザーのtraQ Id
        displayName (str): ユーザーの表示名
        iconId (str): ユーザーアイコンのファイルUUID
        bot (bool): ユーザーがBotかどうか
    """

    id: str
    name: str
    displayName: str
    iconId: str
    bot: bool


class ChannelPayload(BaseModel):
    """チャンネル情報ペイロード

    Attributes:
        id (str): チャンネルUUID
        name (str): チャンネル名
        path (str): チャンネルパス
        parentId (str): 親チャンネルのUUID, ルートチャンネルの場合は"00000000-0000-0000-0000-000000000000"
        creator (UserPayload): チャンネル作成者
        createdAt (datetime.datetime): チャンネル作成日時
        updatedAt (datetime.datetime): チャンネル更新日時
    """

    id: str
    name: str
    path: str
    parentId: str
    creator: UserPayload
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class EmbeddedInfoPayload(BaseModel):
    """メッセージ埋め込み情報

    Attributes:
        raw (str): 表示文字列
        type (str): タイプ
        id (str): 各種Id(タイプによる)
    """

    raw: str
    type: str
    id: str


class MessagePayload(BaseModel):
    """メッセージ情報ペイロード

    Attributes:
        id (str): メッセージUUID
        user (UserPayload): メッセージ投稿者
        channelId (str): 投稿先チャンネルUUID
        text (str): 生メッセージ本文
        plainText (str): メッセージ本文(埋め込み情報・改行なし)
        embedded (list[EmbeddedInfoPayload]): メッセージ埋め込み情報の配列
        createdAt (datetime.datetime): メッセージ投稿日時
        updatedAt (datetime.datetime): メッセージ更新日時
    """

    id: str
    user: UserPayload
    channelId: str
    text: str
    plainText: str
    embedded: list[EmbeddedInfoPayload]
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class MessageStampPayload(BaseModel):
    """メッセージスタンプ情報

    Attributes:
        stampId (str): スタンプUUID
        userId (str): スタンプを押したユーザーUUID
        count (int): このユーザーによって押されたこのスタンプの数
        createdAt (datetime.datetime): 最初にスタンプが押された日時
        updatedAt (datetime.datetime): 最後にスタンプが押された日時
    """

    stampId: str
    userId: str
    count: int
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class GroupMemberPayload(BaseModel):
    """グループメンバー情報ペイロード

    Attributes:
        groupId (str): グループUUID
        userId (str): ユーザーUUID
    """

    groupId: str
    userId: str


class UserGroupAdminPayload(GroupMemberPayload):
    """グループ管理者情報ペイロード

    Attributes:
        groupId (str): グループUUID
        userId (str): ユーザーUUID
    """

    pass


class UserGroupMemberPayload(BaseModel):
    """グループメンバー(のより詳細な)情報ペイロード

    Attributes:
        groupId (str): グループUUID
        userId (str): ユーザーUUID
        role (str): メンバーの役割
    """

    groupId: str
    userId: str
    role: str


class UserGroupPayload(BaseModel):
    """グループ情報ペイロード

    Attributes:
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

    id: str
    name: str
    description: str
    type: str
    icon: str
    admins: list[UserGroupAdminPayload]
    members: list[UserGroupMemberPayload]
    createdAt: datetime.datetime
    updatedAt: datetime.datetime
