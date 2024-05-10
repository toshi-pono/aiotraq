from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_link_external_account import PostLinkExternalAccount
from ...types import Response


def _get_kwargs(
    *,
    body: PostLinkExternalAccount,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/users/me/ex-accounts/link",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.FOUND:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
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
    body: PostLinkExternalAccount,
) -> Response[Any]:
    """外部ログインアカウントを紐付ける

     自分に外部ログインアカウントを紐付けます。
    指定した`providerName`がサーバー側で有効である必要があります。
    リクエストが受理された場合、外部サービスの認証画面にリダイレクトされ、認証される必要があります。

    Args:
        body (PostLinkExternalAccount): POST /users/me/ex-accounts/link 用リクエストボディ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostLinkExternalAccount,
) -> Response[Any]:
    """外部ログインアカウントを紐付ける

     自分に外部ログインアカウントを紐付けます。
    指定した`providerName`がサーバー側で有効である必要があります。
    リクエストが受理された場合、外部サービスの認証画面にリダイレクトされ、認証される必要があります。

    Args:
        body (PostLinkExternalAccount): POST /users/me/ex-accounts/link 用リクエストボディ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
