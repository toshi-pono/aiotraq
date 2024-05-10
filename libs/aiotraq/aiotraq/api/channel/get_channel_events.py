import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx
from dateutil.parser import isoparse

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.channel_event import ChannelEvent
from ...models.get_channel_events_order import GetChannelEventsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    since: Union[Unset, datetime.datetime] = isoparse("0001-01-01T00:00:00.000000Z"),
    until: Union[Unset, datetime.datetime] = UNSET,
    inclusive: Union[Unset, bool] = False,
    order: Union[Unset, GetChannelEventsOrder] = GetChannelEventsOrder.DESC,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_since: Union[Unset, str] = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    json_until: Union[Unset, str] = UNSET
    if not isinstance(until, Unset):
        json_until = until.isoformat()
    params["until"] = json_until

    params["inclusive"] = inclusive

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/channels/{channel_id}/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["ChannelEvent"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChannelEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
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
) -> Response[Union[Any, List["ChannelEvent"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    since: Union[Unset, datetime.datetime] = isoparse("0001-01-01T00:00:00.000000Z"),
    until: Union[Unset, datetime.datetime] = UNSET,
    inclusive: Union[Unset, bool] = False,
    order: Union[Unset, GetChannelEventsOrder] = GetChannelEventsOrder.DESC,
) -> Response[Union[Any, List["ChannelEvent"]]]:
    """チャンネルイベントのリストを取得

     指定したチャンネルのイベントリストを取得します。

    Args:
        channel_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.
        since (Union[Unset, datetime.datetime]):  Default:
            isoparse('0001-01-01T00:00:00.000000Z').
        until (Union[Unset, datetime.datetime]):
        inclusive (Union[Unset, bool]):  Default: False.
        order (Union[Unset, GetChannelEventsOrder]):  Default: GetChannelEventsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ChannelEvent']]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        limit=limit,
        offset=offset,
        since=since,
        until=until,
        inclusive=inclusive,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    since: Union[Unset, datetime.datetime] = isoparse("0001-01-01T00:00:00.000000Z"),
    until: Union[Unset, datetime.datetime] = UNSET,
    inclusive: Union[Unset, bool] = False,
    order: Union[Unset, GetChannelEventsOrder] = GetChannelEventsOrder.DESC,
) -> Optional[Union[Any, List["ChannelEvent"]]]:
    """チャンネルイベントのリストを取得

     指定したチャンネルのイベントリストを取得します。

    Args:
        channel_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.
        since (Union[Unset, datetime.datetime]):  Default:
            isoparse('0001-01-01T00:00:00.000000Z').
        until (Union[Unset, datetime.datetime]):
        inclusive (Union[Unset, bool]):  Default: False.
        order (Union[Unset, GetChannelEventsOrder]):  Default: GetChannelEventsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ChannelEvent']]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        limit=limit,
        offset=offset,
        since=since,
        until=until,
        inclusive=inclusive,
        order=order,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    since: Union[Unset, datetime.datetime] = isoparse("0001-01-01T00:00:00.000000Z"),
    until: Union[Unset, datetime.datetime] = UNSET,
    inclusive: Union[Unset, bool] = False,
    order: Union[Unset, GetChannelEventsOrder] = GetChannelEventsOrder.DESC,
) -> Response[Union[Any, List["ChannelEvent"]]]:
    """チャンネルイベントのリストを取得

     指定したチャンネルのイベントリストを取得します。

    Args:
        channel_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.
        since (Union[Unset, datetime.datetime]):  Default:
            isoparse('0001-01-01T00:00:00.000000Z').
        until (Union[Unset, datetime.datetime]):
        inclusive (Union[Unset, bool]):  Default: False.
        order (Union[Unset, GetChannelEventsOrder]):  Default: GetChannelEventsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ChannelEvent']]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        limit=limit,
        offset=offset,
        since=since,
        until=until,
        inclusive=inclusive,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
    since: Union[Unset, datetime.datetime] = isoparse("0001-01-01T00:00:00.000000Z"),
    until: Union[Unset, datetime.datetime] = UNSET,
    inclusive: Union[Unset, bool] = False,
    order: Union[Unset, GetChannelEventsOrder] = GetChannelEventsOrder.DESC,
) -> Optional[Union[Any, List["ChannelEvent"]]]:
    """チャンネルイベントのリストを取得

     指定したチャンネルのイベントリストを取得します。

    Args:
        channel_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.
        since (Union[Unset, datetime.datetime]):  Default:
            isoparse('0001-01-01T00:00:00.000000Z').
        until (Union[Unset, datetime.datetime]):
        inclusive (Union[Unset, bool]):  Default: False.
        order (Union[Unset, GetChannelEventsOrder]):  Default: GetChannelEventsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ChannelEvent']]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            limit=limit,
            offset=offset,
            since=since,
            until=until,
            inclusive=inclusive,
            order=order,
        )
    ).parsed
