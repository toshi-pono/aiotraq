from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ws",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.SWITCHING_PROTOCOLS:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    r"""WebSocket通知ストリームに接続します

     # WebSocketプロトコル
    ## 送信
    `コマンド:引数1:引数2:...`のような形式のTextMessageをサーバーに送信することで、このWebSocketセッションに対する設定が実行できる。
    ### `viewstate`コマンド
    このWebSocketセッションが見ているチャンネル(イベントを受け取るチャンネル)を設定する。
    現時点では1つのセッションに対して1つのチャンネルしか設定できない。

    `viewstate:{チャンネルID}:{閲覧状態}`
    + チャンネルID: 対象のチャンネルID
    + 閲覧状態: `none`, `monitoring`, `editing`

    最初の`viewstate`コマンドを送る前、または`viewstate:null`, `viewstate:`を送信した後は、このセッションはどこのチャンネルも見ていないことになる。

    ### `rtcstate`コマンド
    自分のWebRTC状態を変更する。
    他のコネクションが既に状態を保持している場合、変更することができません。

    `rtcstate:{チャンネルID}:({状態}:{セッションID})*`

    コネクションが切断された場合、自分のWebRTC状態はリセットされます。

    ### `timeline_streaming`コマンド
    全てのパブリックチャンネルの`MESSAGE_CREATED`イベントを受け取るかどうかを設定する。
    初期状態は`off`です。

    `timeline_streaming:(on|off|true|false)`

    ## 受信
    TextMessageとして各種イベントが`type`と`body`を持つJSONとして非同期に送られます。

    例:
    ```json
    {\"type\":\"USER_ONLINE\",\"body\":{\"id\":\"7dd8e07f-7f5d-4331-9176-b56a4299768b\"}}
    ```

    ## イベント一覧

    ### `USER_JOINED`
    ユーザーが新規登録された。

    対象: 全員

    + `id`: 登録されたユーザーのId

    ### `USER_UPDATED`
    ユーザーの情報が更新された。

    対象: 全員

    + `id`: 情報が更新されたユーザーのId

    ### `USER_TAGS_UPDATED`
    ユーザーのタグが更新された。

    対象: 全員

    + `id`: タグが更新されたユーザーのId
    + `tag_id`: 更新されたタグのId

    ### `USER_ICON_UPDATED`
    ユーザーのアイコンが更新された。

    対象: 全員

    + `id`: アイコンが更新されたユーザーのId

    ### `USER_WEBRTC_STATE_CHANGED`
    ユーザーのWebRTCの状態が変化した

    対象: 全員

    + `user_id`: 変更があったユーザーのId
    + `channel_id`: ユーザーの変更後の接続チャンネルのId
    + `sessions`: ユーザーの変更後の状態(配列)
      + `state`: 状態
      + `sessionId`: セッションID

    ### `USER_VIEWSTATE_CHANGED`
    ユーザーのチャンネルの閲覧状態が変化した

    対象: 変化したWSセッションを含めた、該当ユーザーのWSセッション全て

    + `view_states`: 変化したWSセッションを含めた、該当ユーザーの変更後の状態(配列)
      + `key`: WSセッションの識別子
      + `channel_id`: 閲覧しているチャンネルId
      + `state`: 閲覧状態

    ### `USER_ONLINE`
    ユーザーがオンラインになった。

    対象: 全員

    + `id`: オンラインになったユーザーのId

    ### `USER_OFFLINE`
    ユーザーがオフラインになった。

    対象: 全員

    + `id`: オフラインになったユーザーのId

    ### `USER_GROUP_CREATED`
    ユーザーグループが作成された

    対象: 全員

    + `id`: 作成されたユーザーグループのId

    ### `USER_GROUP_UPDATED`
    ユーザーグループが更新された

    対象: 全員

    + `id`: 作成されたユーザーグループのId

    ### `USER_GROUP_DELETED`
    ユーザーグループが削除された

    対象: 全員

    + `id`: 削除されたユーザーグループのId

    ### `CHANNEL_CREATED`
    チャンネルが新規作成された。

    対象: 該当チャンネルを閲覧可能な全員

    + `id`: 作成されたチャンネルのId
    + `dm_user_id`: (DMの場合のみ) DM相手のユーザーId

    ### `CHANNEL_UPDATED`
    チャンネルの情報が変更された。

    対象: 該当チャンネルを閲覧可能な全員

    + `id`: 変更があったチャンネルのId
    + `dm_user_id`: (DMの場合のみ) DM相手のユーザーId

    ### `CHANNEL_DELETED`
    チャンネルが削除された。

    対象: 該当チャンネルを閲覧可能な全員

    + `id`: 削除されたチャンネルのId
    + `dm_user_id`: (DMの場合のみ) DM相手のユーザーId

    ### `CHANNEL_STARED`
    自分がチャンネルをスターした。

    対象: 自分

    + `id`: スターしたチャンネルのId

    ### `CHANNEL_UNSTARED`
    自分がチャンネルのスターを解除した。

    対象: 自分

    + `id`: スターしたチャンネルのId

    ### `CHANNEL_VIEWERS_CHANGED`
    チャンネルの閲覧者が変化した。

    対象: 該当チャンネルを閲覧しているユーザー

    + `id`: 変化したチャンネルのId
    + `viewers`: 変化後の閲覧者(配列)
      + `userId`: ユーザーId
      + `state`: 閲覧状態
      + `updatedAt`: 閲覧状態の更新日時

    ### `CHANNEL_SUBSCRIBERS_CHANGED`
    チャンネルの購読者が変化した。

    対象: 該当チャンネルを閲覧しているユーザー

    + `id`: 変化したチャンネルのId

    ### `MESSAGE_CREATED`
    メッセージが投稿された。

    対象: 投稿チャンネルを閲覧しているユーザー・投稿チャンネルに通知をつけているユーザー・メンションを受けたユーザー

    + `id`: 投稿されたメッセージのId
    + `is_citing`: 投稿されたメッセージがWebSocketを接続しているユーザーの投稿を引用しているかどうか

    ### `MESSAGE_UPDATED`
    メッセージが更新された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `id`: 更新されたメッセージのId

    ### `MESSAGE_DELETED`
    メッセージが削除された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `id`: 削除されたメッセージのId

    ### `MESSAGE_STAMPED`
    メッセージにスタンプが押された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `message_id`: メッセージId
    + `user_id`: スタンプを押したユーザーのId
    + `stamp_id`: スタンプのId
    + `count`: そのユーザーが押した数
    + `created_at`: そのユーザーがそのスタンプをそのメッセージに最初に押した日時

    ### `MESSAGE_UNSTAMPED`
    メッセージからスタンプが外された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `message_id`: メッセージId
    + `user_id`: スタンプを押したユーザーのId
    + `stamp_id`: スタンプのId

    ### `MESSAGE_PINNED`
    メッセージがピン留めされた。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `message_id`: ピンされたメッセージのID
    + `channel_id`: ピンされたメッセージのチャンネルID

    ### `MESSAGE_UNPINNED`
    ピン留めされたメッセージのピンが外された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `message_id`: ピンが外されたメッセージのID
    + `channel_id`: ピンが外されたメッセージのチャンネルID

    ### `MESSAGE_READ`
    自分があるチャンネルのメッセージを読んだ。

    対象: 自分

    + `id`: 読んだチャンネルId

    ### `STAMP_CREATED`
    スタンプが新しく追加された。

    対象: 全員

    + `id`: 作成されたスタンプのId

    ### `STAMP_UPDATED`
    スタンプが修正された。

    対象: 全員

    + `id`: 修正されたスタンプのId

    ### `STAMP_DELETED`
    スタンプが削除された。

    対象: 全員

    + `id`: 削除されたスタンプのId

    ### `STAMP_PALETTE_CREATED`
    スタンプパレットが新しく追加された。

    対象: 自分

    + `id`: 作成されたスタンプパレットのId

    ### `STAMP_PALETTE_UPDATED`
    スタンプパレットが修正された。

    対象: 自分

    + `id`: 修正されたスタンプパレットのId

    ### `STAMP_PALETTE_DELETED`
    スタンプパレットが削除された。

    対象: 自分

    + `id`: 削除されたスタンプパレットのId

    ### `CLIP_FOLDER_CREATED`
    クリップフォルダーが作成された。

    対象：自分

    + `id`: 作成されたクリップフォルダーのId

    ### `CLIP_FOLDER_UPDATED`
    クリップフォルダーが修正された。

    対象: 自分

    + `id`: 更新されたクリップフォルダーのId

    ### `CLIP_FOLDER_DELETED`
    クリップフォルダーが削除された。

    対象: 自分

    + `id`: 削除されたクリップフォルダーのId

    ### `CLIP_FOLDER_MESSAGE_DELETED`
    クリップフォルダーからメッセージが除外された。

    対象: 自分

    + `folder_id`: メッセージが除外されたクリップフォルダーのId
    + `message_id`: クリップフォルダーから除外されたメッセージのId

    ### `CLIP_FOLDER_MESSAGE_ADDED`
    クリップフォルダーにメッセージが追加された。

    対象: 自分

    + `folder_id`: メッセージが追加されたクリップフォルダーのId
    + `message_id`: クリップフォルダーに追加されたメッセージのId

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    r"""WebSocket通知ストリームに接続します

     # WebSocketプロトコル
    ## 送信
    `コマンド:引数1:引数2:...`のような形式のTextMessageをサーバーに送信することで、このWebSocketセッションに対する設定が実行できる。
    ### `viewstate`コマンド
    このWebSocketセッションが見ているチャンネル(イベントを受け取るチャンネル)を設定する。
    現時点では1つのセッションに対して1つのチャンネルしか設定できない。

    `viewstate:{チャンネルID}:{閲覧状態}`
    + チャンネルID: 対象のチャンネルID
    + 閲覧状態: `none`, `monitoring`, `editing`

    最初の`viewstate`コマンドを送る前、または`viewstate:null`, `viewstate:`を送信した後は、このセッションはどこのチャンネルも見ていないことになる。

    ### `rtcstate`コマンド
    自分のWebRTC状態を変更する。
    他のコネクションが既に状態を保持している場合、変更することができません。

    `rtcstate:{チャンネルID}:({状態}:{セッションID})*`

    コネクションが切断された場合、自分のWebRTC状態はリセットされます。

    ### `timeline_streaming`コマンド
    全てのパブリックチャンネルの`MESSAGE_CREATED`イベントを受け取るかどうかを設定する。
    初期状態は`off`です。

    `timeline_streaming:(on|off|true|false)`

    ## 受信
    TextMessageとして各種イベントが`type`と`body`を持つJSONとして非同期に送られます。

    例:
    ```json
    {\"type\":\"USER_ONLINE\",\"body\":{\"id\":\"7dd8e07f-7f5d-4331-9176-b56a4299768b\"}}
    ```

    ## イベント一覧

    ### `USER_JOINED`
    ユーザーが新規登録された。

    対象: 全員

    + `id`: 登録されたユーザーのId

    ### `USER_UPDATED`
    ユーザーの情報が更新された。

    対象: 全員

    + `id`: 情報が更新されたユーザーのId

    ### `USER_TAGS_UPDATED`
    ユーザーのタグが更新された。

    対象: 全員

    + `id`: タグが更新されたユーザーのId
    + `tag_id`: 更新されたタグのId

    ### `USER_ICON_UPDATED`
    ユーザーのアイコンが更新された。

    対象: 全員

    + `id`: アイコンが更新されたユーザーのId

    ### `USER_WEBRTC_STATE_CHANGED`
    ユーザーのWebRTCの状態が変化した

    対象: 全員

    + `user_id`: 変更があったユーザーのId
    + `channel_id`: ユーザーの変更後の接続チャンネルのId
    + `sessions`: ユーザーの変更後の状態(配列)
      + `state`: 状態
      + `sessionId`: セッションID

    ### `USER_VIEWSTATE_CHANGED`
    ユーザーのチャンネルの閲覧状態が変化した

    対象: 変化したWSセッションを含めた、該当ユーザーのWSセッション全て

    + `view_states`: 変化したWSセッションを含めた、該当ユーザーの変更後の状態(配列)
      + `key`: WSセッションの識別子
      + `channel_id`: 閲覧しているチャンネルId
      + `state`: 閲覧状態

    ### `USER_ONLINE`
    ユーザーがオンラインになった。

    対象: 全員

    + `id`: オンラインになったユーザーのId

    ### `USER_OFFLINE`
    ユーザーがオフラインになった。

    対象: 全員

    + `id`: オフラインになったユーザーのId

    ### `USER_GROUP_CREATED`
    ユーザーグループが作成された

    対象: 全員

    + `id`: 作成されたユーザーグループのId

    ### `USER_GROUP_UPDATED`
    ユーザーグループが更新された

    対象: 全員

    + `id`: 作成されたユーザーグループのId

    ### `USER_GROUP_DELETED`
    ユーザーグループが削除された

    対象: 全員

    + `id`: 削除されたユーザーグループのId

    ### `CHANNEL_CREATED`
    チャンネルが新規作成された。

    対象: 該当チャンネルを閲覧可能な全員

    + `id`: 作成されたチャンネルのId
    + `dm_user_id`: (DMの場合のみ) DM相手のユーザーId

    ### `CHANNEL_UPDATED`
    チャンネルの情報が変更された。

    対象: 該当チャンネルを閲覧可能な全員

    + `id`: 変更があったチャンネルのId
    + `dm_user_id`: (DMの場合のみ) DM相手のユーザーId

    ### `CHANNEL_DELETED`
    チャンネルが削除された。

    対象: 該当チャンネルを閲覧可能な全員

    + `id`: 削除されたチャンネルのId
    + `dm_user_id`: (DMの場合のみ) DM相手のユーザーId

    ### `CHANNEL_STARED`
    自分がチャンネルをスターした。

    対象: 自分

    + `id`: スターしたチャンネルのId

    ### `CHANNEL_UNSTARED`
    自分がチャンネルのスターを解除した。

    対象: 自分

    + `id`: スターしたチャンネルのId

    ### `CHANNEL_VIEWERS_CHANGED`
    チャンネルの閲覧者が変化した。

    対象: 該当チャンネルを閲覧しているユーザー

    + `id`: 変化したチャンネルのId
    + `viewers`: 変化後の閲覧者(配列)
      + `userId`: ユーザーId
      + `state`: 閲覧状態
      + `updatedAt`: 閲覧状態の更新日時

    ### `CHANNEL_SUBSCRIBERS_CHANGED`
    チャンネルの購読者が変化した。

    対象: 該当チャンネルを閲覧しているユーザー

    + `id`: 変化したチャンネルのId

    ### `MESSAGE_CREATED`
    メッセージが投稿された。

    対象: 投稿チャンネルを閲覧しているユーザー・投稿チャンネルに通知をつけているユーザー・メンションを受けたユーザー

    + `id`: 投稿されたメッセージのId
    + `is_citing`: 投稿されたメッセージがWebSocketを接続しているユーザーの投稿を引用しているかどうか

    ### `MESSAGE_UPDATED`
    メッセージが更新された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `id`: 更新されたメッセージのId

    ### `MESSAGE_DELETED`
    メッセージが削除された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `id`: 削除されたメッセージのId

    ### `MESSAGE_STAMPED`
    メッセージにスタンプが押された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `message_id`: メッセージId
    + `user_id`: スタンプを押したユーザーのId
    + `stamp_id`: スタンプのId
    + `count`: そのユーザーが押した数
    + `created_at`: そのユーザーがそのスタンプをそのメッセージに最初に押した日時

    ### `MESSAGE_UNSTAMPED`
    メッセージからスタンプが外された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `message_id`: メッセージId
    + `user_id`: スタンプを押したユーザーのId
    + `stamp_id`: スタンプのId

    ### `MESSAGE_PINNED`
    メッセージがピン留めされた。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `message_id`: ピンされたメッセージのID
    + `channel_id`: ピンされたメッセージのチャンネルID

    ### `MESSAGE_UNPINNED`
    ピン留めされたメッセージのピンが外された。

    対象: 投稿チャンネルを閲覧しているユーザー

    + `message_id`: ピンが外されたメッセージのID
    + `channel_id`: ピンが外されたメッセージのチャンネルID

    ### `MESSAGE_READ`
    自分があるチャンネルのメッセージを読んだ。

    対象: 自分

    + `id`: 読んだチャンネルId

    ### `STAMP_CREATED`
    スタンプが新しく追加された。

    対象: 全員

    + `id`: 作成されたスタンプのId

    ### `STAMP_UPDATED`
    スタンプが修正された。

    対象: 全員

    + `id`: 修正されたスタンプのId

    ### `STAMP_DELETED`
    スタンプが削除された。

    対象: 全員

    + `id`: 削除されたスタンプのId

    ### `STAMP_PALETTE_CREATED`
    スタンプパレットが新しく追加された。

    対象: 自分

    + `id`: 作成されたスタンプパレットのId

    ### `STAMP_PALETTE_UPDATED`
    スタンプパレットが修正された。

    対象: 自分

    + `id`: 修正されたスタンプパレットのId

    ### `STAMP_PALETTE_DELETED`
    スタンプパレットが削除された。

    対象: 自分

    + `id`: 削除されたスタンプパレットのId

    ### `CLIP_FOLDER_CREATED`
    クリップフォルダーが作成された。

    対象：自分

    + `id`: 作成されたクリップフォルダーのId

    ### `CLIP_FOLDER_UPDATED`
    クリップフォルダーが修正された。

    対象: 自分

    + `id`: 更新されたクリップフォルダーのId

    ### `CLIP_FOLDER_DELETED`
    クリップフォルダーが削除された。

    対象: 自分

    + `id`: 削除されたクリップフォルダーのId

    ### `CLIP_FOLDER_MESSAGE_DELETED`
    クリップフォルダーからメッセージが除外された。

    対象: 自分

    + `folder_id`: メッセージが除外されたクリップフォルダーのId
    + `message_id`: クリップフォルダーから除外されたメッセージのId

    ### `CLIP_FOLDER_MESSAGE_ADDED`
    クリップフォルダーにメッセージが追加された。

    対象: 自分

    + `folder_id`: メッセージが追加されたクリップフォルダーのId
    + `message_id`: クリップフォルダーに追加されたメッセージのId

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
