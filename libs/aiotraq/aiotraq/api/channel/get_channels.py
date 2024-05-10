from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.channel_list import ChannelList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_dm: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["include-dm"] = include_dm

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/channels",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ChannelList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ChannelList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ChannelList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_dm: Union[Unset, bool] = False,
) -> Response[ChannelList]:
    """チャンネルリストを取得

     チャンネルのリストを取得します。

    Args:
        include_dm (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChannelList]
    """

    kwargs = _get_kwargs(
        include_dm=include_dm,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    include_dm: Union[Unset, bool] = False,
) -> Optional[ChannelList]:
    """チャンネルリストを取得

     チャンネルのリストを取得します。

    Args:
        include_dm (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChannelList
    """

    return sync_detailed(
        client=client,
        include_dm=include_dm,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_dm: Union[Unset, bool] = False,
) -> Response[ChannelList]:
    """チャンネルリストを取得

     チャンネルのリストを取得します。

    Args:
        include_dm (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChannelList]
    """

    kwargs = _get_kwargs(
        include_dm=include_dm,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    include_dm: Union[Unset, bool] = False,
) -> Optional[ChannelList]:
    """チャンネルリストを取得

     チャンネルのリストを取得します。

    Args:
        include_dm (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChannelList
    """

    return (
        await asyncio_detailed(
            client=client,
            include_dm=include_dm,
        )
    ).parsed
