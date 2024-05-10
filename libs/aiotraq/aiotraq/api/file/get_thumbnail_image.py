from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.thumbnail_type import ThumbnailType
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    file_id: str,
    *,
    type: Union[Unset, ThumbnailType] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/files/{file_id}/thumbnail",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, File]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[Union[Any, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, ThumbnailType] = UNSET,
) -> Response[Union[Any, File]]:
    """サムネイル画像を取得

     指定したファイルのサムネイル画像を取得します。
    指定したファイルへのアクセス権限が必要です。

    Args:
        file_id (str):
        type (Union[Unset, ThumbnailType]): サムネイル画像のタイプ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, ThumbnailType] = UNSET,
) -> Optional[Union[Any, File]]:
    """サムネイル画像を取得

     指定したファイルのサムネイル画像を取得します。
    指定したファイルへのアクセス権限が必要です。

    Args:
        file_id (str):
        type (Union[Unset, ThumbnailType]): サムネイル画像のタイプ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return sync_detailed(
        file_id=file_id,
        client=client,
        type=type,
    ).parsed


async def asyncio_detailed(
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, ThumbnailType] = UNSET,
) -> Response[Union[Any, File]]:
    """サムネイル画像を取得

     指定したファイルのサムネイル画像を取得します。
    指定したファイルへのアクセス権限が必要です。

    Args:
        file_id (str):
        type (Union[Unset, ThumbnailType]): サムネイル画像のタイプ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, ThumbnailType] = UNSET,
) -> Optional[Union[Any, File]]:
    """サムネイル画像を取得

     指定したファイルのサムネイル画像を取得します。
    指定したファイルへのアクセス権限が必要です。

    Args:
        file_id (str):
        type (Union[Unset, ThumbnailType]): サムネイル画像のタイプ

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
            type=type,
        )
    ).parsed
