from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.post_message_stamp_request import PostMessageStampRequest
from ...types import Response


def _get_kwargs(
    message_id: str,
    stamp_id: str,
    *,
    body: PostMessageStampRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/messages/{message_id}/stamps/{stamp_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Message]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Message.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Message]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    message_id: str,
    stamp_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessageStampRequest,
) -> Response[Union[Any, Message]]:
    """チャンネルにスタンプを押す

    指定したメッセージにスタンプを押します。

    Args:
        message_id (str):
        stamp_id (str):
        body (PostMessageRequest): メッセージ投稿リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Message]]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
        stamp_id=stamp_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    message_id: str,
    stamp_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessageStampRequest,
) -> Optional[Union[Any, Message]]:
    """メッセージにスタンプを押す

    指定したメッセージにスタンプを押します。

    Args:
        message_id (str):
        stamp_id (str):
        body (PostMessageRequest): メッセージ投稿リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Message]
    """

    return sync_detailed(
        message_id=message_id,
        stamp_id=stamp_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    message_id: str,
    stamp_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessageStampRequest,
) -> Response[Union[Any, Message]]:
    """チャンネルにスタンプを押す

    指定したメッセージにスタンプを押します。

    Args:
        message_id (str):
        stamp_id (str):
        body (PostMessageRequest): メッセージ投稿リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Message]]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
        stamp_id=stamp_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    message_id: str,
    stamp_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessageStampRequest,
) -> Optional[Union[Any, Message]]:
    """メッセージにスタンプを押す

    指定したメッセージにスタンプを押します。

    Args:
        message_id (str):
        stamp_id (str):
        body (PostMessageRequest): メッセージ投稿リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Message]
    """

    return (
        await asyncio_detailed(
            message_id=message_id,
            stamp_id=stamp_id,
            client=client,
            body=body,
        )
    ).parsed
