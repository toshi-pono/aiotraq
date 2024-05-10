from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bot_event_log import BotEventLog
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: str,
    *,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/bots/{bot_id}/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["BotEventLog"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BotEventLog.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["BotEventLog"]]]:
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
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Response[Union[Any, List["BotEventLog"]]]:
    """BOTのイベントログを取得

     指定したBOTのイベントログを取得します。
    対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['BotEventLog']]]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[Any, List["BotEventLog"]]]:
    """BOTのイベントログを取得

     指定したBOTのイベントログを取得します。
    対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['BotEventLog']]
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Response[Union[Any, List["BotEventLog"]]]:
    """BOTのイベントログを取得

     指定したBOTのイベントログを取得します。
    対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['BotEventLog']]]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[Any, List["BotEventLog"]]]:
    """BOTのイベントログを取得

     指定したBOTのイベントログを取得します。
    対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['BotEventLog']]
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
