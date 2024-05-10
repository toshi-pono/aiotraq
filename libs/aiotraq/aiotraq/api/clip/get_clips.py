from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clipped_message import ClippedMessage
from ...models.get_clips_order import GetClipsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    folder_id: str,
    *,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    order: Union[Unset, GetClipsOrder] = GetClipsOrder.DESC,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/clip-folders/{folder_id}/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["ClippedMessage"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ClippedMessage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["ClippedMessage"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    folder_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    order: Union[Unset, GetClipsOrder] = GetClipsOrder.DESC,
) -> Response[Union[Any, List["ClippedMessage"]]]:
    """フォルダ内のクリップのリストを取得

     指定したフォルダ内のクリップのリストを取得します。
    `order`を指定しない場合、クリップした日時の新しい順で返されます。

    Args:
        folder_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.
        order (Union[Unset, GetClipsOrder]):  Default: GetClipsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ClippedMessage']]]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        limit=limit,
        offset=offset,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    folder_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    order: Union[Unset, GetClipsOrder] = GetClipsOrder.DESC,
) -> Optional[Union[Any, List["ClippedMessage"]]]:
    """フォルダ内のクリップのリストを取得

     指定したフォルダ内のクリップのリストを取得します。
    `order`を指定しない場合、クリップした日時の新しい順で返されます。

    Args:
        folder_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.
        order (Union[Unset, GetClipsOrder]):  Default: GetClipsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ClippedMessage']]
    """

    return sync_detailed(
        folder_id=folder_id,
        client=client,
        limit=limit,
        offset=offset,
        order=order,
    ).parsed


async def asyncio_detailed(
    folder_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    order: Union[Unset, GetClipsOrder] = GetClipsOrder.DESC,
) -> Response[Union[Any, List["ClippedMessage"]]]:
    """フォルダ内のクリップのリストを取得

     指定したフォルダ内のクリップのリストを取得します。
    `order`を指定しない場合、クリップした日時の新しい順で返されます。

    Args:
        folder_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.
        order (Union[Unset, GetClipsOrder]):  Default: GetClipsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ClippedMessage']]]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        limit=limit,
        offset=offset,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    folder_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    order: Union[Unset, GetClipsOrder] = GetClipsOrder.DESC,
) -> Optional[Union[Any, List["ClippedMessage"]]]:
    """フォルダ内のクリップのリストを取得

     指定したフォルダ内のクリップのリストを取得します。
    `order`を指定しない場合、クリップした日時の新しい順で返されます。

    Args:
        folder_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.
        order (Union[Unset, GetClipsOrder]):  Default: GetClipsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ClippedMessage']]
    """

    return (
        await asyncio_detailed(
            folder_id=folder_id,
            client=client,
            limit=limit,
            offset=offset,
            order=order,
        )
    ).parsed
