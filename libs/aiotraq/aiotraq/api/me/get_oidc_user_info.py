from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oidc_user_info import OIDCUserInfo
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/users/me/oidc",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[OIDCUserInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OIDCUserInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[OIDCUserInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OIDCUserInfo]:
    """自分のユーザー詳細を取得 (OIDC UserInfo)

     OIDCトークンを用いてユーザー詳細を取得します。
    OIDC UserInfo Endpointです。

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OIDCUserInfo]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OIDCUserInfo]:
    """自分のユーザー詳細を取得 (OIDC UserInfo)

     OIDCトークンを用いてユーザー詳細を取得します。
    OIDC UserInfo Endpointです。

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OIDCUserInfo
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[OIDCUserInfo]:
    """自分のユーザー詳細を取得 (OIDC UserInfo)

     OIDCトークンを用いてユーザー詳細を取得します。
    OIDC UserInfo Endpointです。

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OIDCUserInfo]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[OIDCUserInfo]:
    """自分のユーザー詳細を取得 (OIDC UserInfo)

     OIDCトークンを用いてユーザー詳細を取得します。
    OIDC UserInfo Endpointです。

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OIDCUserInfo
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
