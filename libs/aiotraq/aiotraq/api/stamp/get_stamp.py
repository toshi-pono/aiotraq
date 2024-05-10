from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stamp import Stamp
from ...types import Response


def _get_kwargs(
    stamp_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/stamps/{stamp_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Stamp]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Stamp.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Stamp]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stamp_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Stamp]]:
    """スタンプ情報を取得

     指定したスタンプの情報を取得します。

    Args:
        stamp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Stamp]]
    """

    kwargs = _get_kwargs(
        stamp_id=stamp_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stamp_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Stamp]]:
    """スタンプ情報を取得

     指定したスタンプの情報を取得します。

    Args:
        stamp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Stamp]
    """

    return sync_detailed(
        stamp_id=stamp_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    stamp_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Stamp]]:
    """スタンプ情報を取得

     指定したスタンプの情報を取得します。

    Args:
        stamp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Stamp]]
    """

    kwargs = _get_kwargs(
        stamp_id=stamp_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stamp_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Stamp]]:
    """スタンプ情報を取得

     指定したスタンプの情報を取得します。

    Args:
        stamp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Stamp]
    """

    return (
        await asyncio_detailed(
            stamp_id=stamp_id,
            client=client,
        )
    ).parsed
