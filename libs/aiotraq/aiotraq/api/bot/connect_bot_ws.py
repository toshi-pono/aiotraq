from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/bots/ws",
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
    r"""WebSocket Mode BOT用通知ストリームに接続します

     # BOT WebSocketプロトコル

    ## 送信

    `コマンド:引数1:引数2:...` のような形式のTextMessageをサーバーに送信することで、このWebSocketセッションに対する設定が実行できます。

    ### `rtcstate`コマンド
    自分のWebRTC状態を変更します。
    他のコネクションが既に状態を保持している場合、変更することができません。

    `rtcstate:{チャンネルID}:({状態}:{セッションID})*`

    チャンネルIDにnullもしくは空文字を指定するか、状態にnullもしくは空文字を指定した場合、WebRTC状態はリセットされます。

    `rtcstate:null`, `rtcstate:`, `rtcstate:channelId:null`, `rtcstate:channelId:`

    コネクションが切断された場合、自分のWebRTC状態はリセットされます。

    ## 受信

    TextMessageとして各種イベントが`type`、`reqId`、`body`を持つJSONとして非同期に送られます。
    `body`の内容はHTTP Modeの場合のRequest Bodyと同様です。
    例外として`ERROR`イベントは`reqId`を持ちません。

    例: PINGイベント
    `{\"type\":\"PING\",\"reqId\":\"requestId\",\"body\":{\"eventTime\":\"2019-05-
    07T04:50:48.582586882Z\"}}`

    ### `ERROR`

    コマンドの引数が不正などの理由でコマンドが受理されなかった場合に送られます。
    非同期に送られるため、必ずしもコマンドとの対応関係を確定できないことに注意してください。
    本番環境ではERRORが送られないようにすることが望ましいです。

    `{\"type\":\"ERROR\",\"body\":\"message\"}`

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
    r"""WebSocket Mode BOT用通知ストリームに接続します

     # BOT WebSocketプロトコル

    ## 送信

    `コマンド:引数1:引数2:...` のような形式のTextMessageをサーバーに送信することで、このWebSocketセッションに対する設定が実行できます。

    ### `rtcstate`コマンド
    自分のWebRTC状態を変更します。
    他のコネクションが既に状態を保持している場合、変更することができません。

    `rtcstate:{チャンネルID}:({状態}:{セッションID})*`

    チャンネルIDにnullもしくは空文字を指定するか、状態にnullもしくは空文字を指定した場合、WebRTC状態はリセットされます。

    `rtcstate:null`, `rtcstate:`, `rtcstate:channelId:null`, `rtcstate:channelId:`

    コネクションが切断された場合、自分のWebRTC状態はリセットされます。

    ## 受信

    TextMessageとして各種イベントが`type`、`reqId`、`body`を持つJSONとして非同期に送られます。
    `body`の内容はHTTP Modeの場合のRequest Bodyと同様です。
    例外として`ERROR`イベントは`reqId`を持ちません。

    例: PINGイベント
    `{\"type\":\"PING\",\"reqId\":\"requestId\",\"body\":{\"eventTime\":\"2019-05-
    07T04:50:48.582586882Z\"}}`

    ### `ERROR`

    コマンドの引数が不正などの理由でコマンドが受理されなかった場合に送られます。
    非同期に送られるため、必ずしもコマンドとの対応関係を確定できないことに注意してください。
    本番環境ではERRORが送られないようにすることが望ましいです。

    `{\"type\":\"ERROR\",\"body\":\"message\"}`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
