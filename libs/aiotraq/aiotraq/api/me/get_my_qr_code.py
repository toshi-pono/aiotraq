from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    token: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/users/me/qr-code",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[File]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    token: Union[Unset, bool] = False,
) -> Response[File]:
    """QRコードを取得

     自身のQRコードを取得します。
    返されたQRコードまたはトークンは、発行後の5分間のみ有効です

    Args:
        token (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    token: Union[Unset, bool] = False,
) -> Optional[File]:
    """QRコードを取得

     自身のQRコードを取得します。
    返されたQRコードまたはトークンは、発行後の5分間のみ有効です

    Args:
        token (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        client=client,
        token=token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    token: Union[Unset, bool] = False,
) -> Response[File]:
    """QRコードを取得

     自身のQRコードを取得します。
    返されたQRコードまたはトークンは、発行後の5分間のみ有効です

    Args:
        token (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    token: Union[Unset, bool] = False,
) -> Optional[File]:
    """QRコードを取得

     自身のQRコードを取得します。
    返されたQRコードまたはトークンは、発行後の5分間のみ有効です

    Args:
        token (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
        )
    ).parsed
