from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_stamp_palette_request import PostStampPaletteRequest
from ...models.stamp_palette import StampPalette
from ...types import Response


def _get_kwargs(
    *,
    body: PostStampPaletteRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/stamp-palettes",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, StampPalette]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = StampPalette.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, StampPalette]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStampPaletteRequest,
) -> Response[Union[Any, StampPalette]]:
    """スタンプパレットを作成

     スタンプパレットを作成します。

    Args:
        body (PostStampPaletteRequest): スタンプパレット作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StampPalette]]
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
    body: PostStampPaletteRequest,
) -> Optional[Union[Any, StampPalette]]:
    """スタンプパレットを作成

     スタンプパレットを作成します。

    Args:
        body (PostStampPaletteRequest): スタンプパレット作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StampPalette]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStampPaletteRequest,
) -> Response[Union[Any, StampPalette]]:
    """スタンプパレットを作成

     スタンプパレットを作成します。

    Args:
        body (PostStampPaletteRequest): スタンプパレット作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StampPalette]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStampPaletteRequest,
) -> Optional[Union[Any, StampPalette]]:
    """スタンプパレットを作成

     スタンプパレットを作成します。

    Args:
        body (PostStampPaletteRequest): スタンプパレット作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StampPalette]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
