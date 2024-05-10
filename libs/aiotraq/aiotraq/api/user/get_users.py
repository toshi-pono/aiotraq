from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_suspended: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["include-suspended"] = include_suspended

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["User"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = User.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["User"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_suspended: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["User"]]]:
    r"""ユーザーのリストを取得

     ユーザーのリストを取得します。
    `include-suspended`を指定しない場合、レスポンスにはユーザーアカウント状態が\"1: 有効\"であるユーザーのみが含まれます。
    `include-suspended`と`name`を同時に指定することはできません。

    Args:
        include_suspended (Union[Unset, bool]):  Default: False.
        name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['User']]]
    """

    kwargs = _get_kwargs(
        include_suspended=include_suspended,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    include_suspended: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["User"]]]:
    r"""ユーザーのリストを取得

     ユーザーのリストを取得します。
    `include-suspended`を指定しない場合、レスポンスにはユーザーアカウント状態が\"1: 有効\"であるユーザーのみが含まれます。
    `include-suspended`と`name`を同時に指定することはできません。

    Args:
        include_suspended (Union[Unset, bool]):  Default: False.
        name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['User']]
    """

    return sync_detailed(
        client=client,
        include_suspended=include_suspended,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_suspended: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["User"]]]:
    r"""ユーザーのリストを取得

     ユーザーのリストを取得します。
    `include-suspended`を指定しない場合、レスポンスにはユーザーアカウント状態が\"1: 有効\"であるユーザーのみが含まれます。
    `include-suspended`と`name`を同時に指定することはできません。

    Args:
        include_suspended (Union[Unset, bool]):  Default: False.
        name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['User']]]
    """

    kwargs = _get_kwargs(
        include_suspended=include_suspended,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    include_suspended: Union[Unset, bool] = False,
    name: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["User"]]]:
    r"""ユーザーのリストを取得

     ユーザーのリストを取得します。
    `include-suspended`を指定しない場合、レスポンスにはユーザーアカウント状態が\"1: 有効\"であるユーザーのみが含まれます。
    `include-suspended`と`name`を同時に指定することはできません。

    Args:
        include_suspended (Union[Unset, bool]):  Default: False.
        name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['User']]
    """

    return (
        await asyncio_detailed(
            client=client,
            include_suspended=include_suspended,
            name=name,
        )
    ).parsed
