from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_user_group_request import PostUserGroupRequest
from ...models.user_group import UserGroup
from ...types import Response


def _get_kwargs(
    *,
    body: PostUserGroupRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/groups",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UserGroup]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = UserGroup.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, UserGroup]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUserGroupRequest,
) -> Response[Union[Any, UserGroup]]:
    """ユーザーグループを作成

     ユーザーグループを作成します。
    作成者は自動的にグループ管理者になります。

    Args:
        body (PostUserGroupRequest): ユーザーグループ作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserGroup]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUserGroupRequest,
) -> Optional[Union[Any, UserGroup]]:
    """ユーザーグループを作成

     ユーザーグループを作成します。
    作成者は自動的にグループ管理者になります。

    Args:
        body (PostUserGroupRequest): ユーザーグループ作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserGroup]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUserGroupRequest,
) -> Response[Union[Any, UserGroup]]:
    """ユーザーグループを作成

     ユーザーグループを作成します。
    作成者は自動的にグループ管理者になります。

    Args:
        body (PostUserGroupRequest): ユーザーグループ作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserGroup]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUserGroupRequest,
) -> Optional[Union[Any, UserGroup]]:
    """ユーザーグループを作成

     ユーザーグループを作成します。
    作成者は自動的にグループ管理者になります。

    Args:
        body (PostUserGroupRequest): ユーザーグループ作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserGroup]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
