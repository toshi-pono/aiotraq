from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.thumbnail_type import ThumbnailType
from ...types import UNSET, Response, Unset


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


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
) -> Response[Any]:
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
        Response[Any]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, ThumbnailType] = UNSET,
) -> Response[Any]:
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
        Response[Any]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
