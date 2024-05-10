from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_info import FileInfo
from ...models.post_file_request import PostFileRequest
from ...types import Response


def _get_kwargs(
    *,
    body: PostFileRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/files",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, FileInfo]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = FileInfo.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.LENGTH_REQUIRED:
        response_411 = cast(Any, None)
        return response_411
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = cast(Any, None)
        return response_413
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, FileInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFileRequest,
) -> Response[Union[Any, FileInfo]]:
    """ファイルをアップロード

     指定したチャンネルにファイルをアップロードします。
    アーカイブされているチャンネルにはアップロード出来ません。

    Args:
        body (PostFileRequest): ファイルアップロードリクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FileInfo]]
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
    body: PostFileRequest,
) -> Optional[Union[Any, FileInfo]]:
    """ファイルをアップロード

     指定したチャンネルにファイルをアップロードします。
    アーカイブされているチャンネルにはアップロード出来ません。

    Args:
        body (PostFileRequest): ファイルアップロードリクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FileInfo]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFileRequest,
) -> Response[Union[Any, FileInfo]]:
    """ファイルをアップロード

     指定したチャンネルにファイルをアップロードします。
    アーカイブされているチャンネルにはアップロード出来ません。

    Args:
        body (PostFileRequest): ファイルアップロードリクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FileInfo]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFileRequest,
) -> Optional[Union[Any, FileInfo]]:
    """ファイルをアップロード

     指定したチャンネルにファイルをアップロードします。
    アーカイブされているチャンネルにはアップロード出来ません。

    Args:
        body (PostFileRequest): ファイルアップロードリクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FileInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
