from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_timeline_message import ActivityTimelineMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 50,
    all_: Union[Unset, bool] = False,
    per_channel: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["all"] = all_

    params["per_channel"] = per_channel

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/activity/timeline",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["ActivityTimelineMessage"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ActivityTimelineMessage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["ActivityTimelineMessage"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    all_: Union[Unset, bool] = False,
    per_channel: Union[Unset, bool] = False,
) -> Response[Union[Any, List["ActivityTimelineMessage"]]]:
    """アクテビティタイムラインを取得

     パブリックチャンネルの直近の投稿メッセージを作成日時の降順で取得します。
    `all`が`true`でない場合、購読チャンネルのみのタイムラインを取得します

    Args:
        limit (Union[Unset, int]):  Default: 50.
        all_ (Union[Unset, bool]):  Default: False.
        per_channel (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ActivityTimelineMessage']]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        all_=all_,
        per_channel=per_channel,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    all_: Union[Unset, bool] = False,
    per_channel: Union[Unset, bool] = False,
) -> Optional[Union[Any, List["ActivityTimelineMessage"]]]:
    """アクテビティタイムラインを取得

     パブリックチャンネルの直近の投稿メッセージを作成日時の降順で取得します。
    `all`が`true`でない場合、購読チャンネルのみのタイムラインを取得します

    Args:
        limit (Union[Unset, int]):  Default: 50.
        all_ (Union[Unset, bool]):  Default: False.
        per_channel (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ActivityTimelineMessage']]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        all_=all_,
        per_channel=per_channel,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    all_: Union[Unset, bool] = False,
    per_channel: Union[Unset, bool] = False,
) -> Response[Union[Any, List["ActivityTimelineMessage"]]]:
    """アクテビティタイムラインを取得

     パブリックチャンネルの直近の投稿メッセージを作成日時の降順で取得します。
    `all`が`true`でない場合、購読チャンネルのみのタイムラインを取得します

    Args:
        limit (Union[Unset, int]):  Default: 50.
        all_ (Union[Unset, bool]):  Default: False.
        per_channel (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ActivityTimelineMessage']]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        all_=all_,
        per_channel=per_channel,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 50,
    all_: Union[Unset, bool] = False,
    per_channel: Union[Unset, bool] = False,
) -> Optional[Union[Any, List["ActivityTimelineMessage"]]]:
    """アクテビティタイムラインを取得

     パブリックチャンネルの直近の投稿メッセージを作成日時の降順で取得します。
    `all`が`true`でない場合、購読チャンネルのみのタイムラインを取得します

    Args:
        limit (Union[Unset, int]):  Default: 50.
        all_ (Union[Unset, bool]):  Default: False.
        per_channel (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ActivityTimelineMessage']]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            all_=all_,
            per_channel=per_channel,
        )
    ).parsed
