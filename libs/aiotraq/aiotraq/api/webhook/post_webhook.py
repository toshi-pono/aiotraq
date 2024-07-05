from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    webhook_id: str,
    *,
    body: str,
    embed: Union[Unset, int] = 0,
    x_traq_signature: Union[Unset, str] = UNSET,
    x_traq_channel_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_traq_signature, Unset):
        headers["X-TRAQ-Signature"] = x_traq_signature

    if not isinstance(x_traq_channel_id, Unset):
        headers["X-TRAQ-Channel-Id"] = x_traq_channel_id

    params: Dict[str, Any] = {}

    params["embed"] = embed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/webhooks/{webhook_id}",
        "params": params,
    }

    _body = body

    _kwargs["content"] = _body
    headers["Content-Type"] = "text/plain"

    _kwargs["headers"] = headers

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
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
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    embed: Union[Unset, int] = 0,
    x_traq_signature: Union[Unset, str] = UNSET,
    x_traq_channel_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Webhookを送信

    Webhookにメッセージを投稿します。
    secureなウェブフックに対しては`X-TRAQ-Signature`ヘッダーが必須です。
    アーカイブされているチャンネルには投稿できません。

    Args:
        webhook_id (str):
        embed (Union[Unset, int]):  Default: 0.
        x_traq_signature (Union[Unset, str]):
        x_traq_channel_id (Union[Unset, str]):
        body (str): メッセージ文字列

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
        embed=embed,
        x_traq_signature=x_traq_signature,
        x_traq_channel_id=x_traq_channel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    embed: Union[Unset, int] = 0,
    x_traq_signature: Union[Unset, str] = UNSET,
    x_traq_channel_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Webhookを送信

    Webhookにメッセージを投稿します。
    secureなウェブフックに対しては`X-TRAQ-Signature`ヘッダーが必須です。
    アーカイブされているチャンネルには投稿できません。

    Args:
        webhook_id (str):
        embed (Union[Unset, int]):  Default: 0.
        x_traq_signature (Union[Unset, str]):
        x_traq_channel_id (Union[Unset, str]):
        body (str): メッセージ文字列

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
        embed=embed,
        x_traq_signature=x_traq_signature,
        x_traq_channel_id=x_traq_channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
