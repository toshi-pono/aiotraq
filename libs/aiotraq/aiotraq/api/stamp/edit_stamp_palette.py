from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_stamp_palette_request import PatchStampPaletteRequest
from ...types import Response


def _get_kwargs(
    palette_id: str,
    *,
    body: PatchStampPaletteRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/stamp-palettes/{palette_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
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
    palette_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchStampPaletteRequest,
) -> Response[Any]:
    """スタンプパレットを編集

     指定したスタンプパレットを編集します。
    リクエストのスタンプの配列の順番は保存されて変更されます。
    対象のスタンプパレットの管理権限が必要です。

    Args:
        palette_id (str):
        body (PatchStampPaletteRequest): スタンプパレット情報変更リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        palette_id=palette_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    palette_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchStampPaletteRequest,
) -> Response[Any]:
    """スタンプパレットを編集

     指定したスタンプパレットを編集します。
    リクエストのスタンプの配列の順番は保存されて変更されます。
    対象のスタンプパレットの管理権限が必要です。

    Args:
        palette_id (str):
        body (PatchStampPaletteRequest): スタンプパレット情報変更リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        palette_id=palette_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
