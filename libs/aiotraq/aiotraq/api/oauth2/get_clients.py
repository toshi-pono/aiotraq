from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.o_auth_2_client import OAuth2Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    all_: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["all"] = all_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/clients",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["OAuth2Client"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OAuth2Client.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["OAuth2Client"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    all_: Union[Unset, bool] = False,
) -> Response[List["OAuth2Client"]]:
    """OAuth2クライアントのリストを取得

     自身が開発者のOAuth2クライアントのリストを取得します。
    `all`が`true`の場合、全開発者の全クライアントのリストを返します。

    Args:
        all_ (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['OAuth2Client']]
    """

    kwargs = _get_kwargs(
        all_=all_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    all_: Union[Unset, bool] = False,
) -> Optional[List["OAuth2Client"]]:
    """OAuth2クライアントのリストを取得

     自身が開発者のOAuth2クライアントのリストを取得します。
    `all`が`true`の場合、全開発者の全クライアントのリストを返します。

    Args:
        all_ (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['OAuth2Client']
    """

    return sync_detailed(
        client=client,
        all_=all_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    all_: Union[Unset, bool] = False,
) -> Response[List["OAuth2Client"]]:
    """OAuth2クライアントのリストを取得

     自身が開発者のOAuth2クライアントのリストを取得します。
    `all`が`true`の場合、全開発者の全クライアントのリストを返します。

    Args:
        all_ (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['OAuth2Client']]
    """

    kwargs = _get_kwargs(
        all_=all_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    all_: Union[Unset, bool] = False,
) -> Optional[List["OAuth2Client"]]:
    """OAuth2クライアントのリストを取得

     自身が開発者のOAuth2クライアントのリストを取得します。
    `all`が`true`の場合、全開発者の全クライアントのリストを返します。

    Args:
        all_ (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['OAuth2Client']
    """

    return (
        await asyncio_detailed(
            client=client,
            all_=all_,
        )
    ).parsed
