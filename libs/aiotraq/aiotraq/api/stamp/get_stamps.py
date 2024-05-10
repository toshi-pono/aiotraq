from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_stamps_type import GetStampsType
from ...models.stamp_with_thumbnail import StampWithThumbnail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_unicode: Union[Unset, bool] = True,
    type: Union[Unset, GetStampsType] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["include-unicode"] = include_unicode

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/stamps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["StampWithThumbnail"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StampWithThumbnail.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["StampWithThumbnail"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_unicode: Union[Unset, bool] = True,
    type: Union[Unset, GetStampsType] = UNSET,
) -> Response[List["StampWithThumbnail"]]:
    """スタンプリストを取得

     スタンプのリストを取得します。

    Args:
        include_unicode (Union[Unset, bool]):  Default: True.
        type (Union[Unset, GetStampsType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['StampWithThumbnail']]
    """

    kwargs = _get_kwargs(
        include_unicode=include_unicode,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    include_unicode: Union[Unset, bool] = True,
    type: Union[Unset, GetStampsType] = UNSET,
) -> Optional[List["StampWithThumbnail"]]:
    """スタンプリストを取得

     スタンプのリストを取得します。

    Args:
        include_unicode (Union[Unset, bool]):  Default: True.
        type (Union[Unset, GetStampsType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['StampWithThumbnail']
    """

    return sync_detailed(
        client=client,
        include_unicode=include_unicode,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_unicode: Union[Unset, bool] = True,
    type: Union[Unset, GetStampsType] = UNSET,
) -> Response[List["StampWithThumbnail"]]:
    """スタンプリストを取得

     スタンプのリストを取得します。

    Args:
        include_unicode (Union[Unset, bool]):  Default: True.
        type (Union[Unset, GetStampsType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['StampWithThumbnail']]
    """

    kwargs = _get_kwargs(
        include_unicode=include_unicode,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    include_unicode: Union[Unset, bool] = True,
    type: Union[Unset, GetStampsType] = UNSET,
) -> Optional[List["StampWithThumbnail"]]:
    """スタンプリストを取得

     スタンプのリストを取得します。

    Args:
        include_unicode (Union[Unset, bool]):  Default: True.
        type (Union[Unset, GetStampsType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['StampWithThumbnail']
    """

    return (
        await asyncio_detailed(
            client=client,
            include_unicode=include_unicode,
            type=type,
        )
    ).parsed
