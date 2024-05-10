from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_bot_action_join_request import PostBotActionJoinRequest
from ...types import Response


def _get_kwargs(
    bot_id: str,
    *,
    body: PostBotActionJoinRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/bots/{bot_id}/actions/join",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
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
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostBotActionJoinRequest,
) -> Response[Any]:
    """BOTをチャンネルに参加させる

     指定したBOTを指定したチャンネルに参加させます。
    チャンネルに参加したBOTは、そのチャンネルの各種イベントを受け取るようになります。
    対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        body (PostBotActionJoinRequest): BOTチャンネル参加リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostBotActionJoinRequest,
) -> Response[Any]:
    """BOTをチャンネルに参加させる

     指定したBOTを指定したチャンネルに参加させます。
    チャンネルに参加したBOTは、そのチャンネルの各種イベントを受け取るようになります。
    対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        body (PostBotActionJoinRequest): BOTチャンネル参加リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
