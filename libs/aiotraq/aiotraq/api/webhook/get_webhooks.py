from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook import Webhook
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    all_: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["all"] = all_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/webhooks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["Webhook"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Webhook.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["Webhook"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    all_: Union[Unset, bool] = False,
) -> Response[List["Webhook"]]:
    """Webhook情報のリストを取得します

     Webhookのリストを取得します。
    allがtrueで無い場合は、自分がオーナーのWebhookのリストを返します。

    Args:
        all_ (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Webhook']]
    """

    kwargs = _get_kwargs(
        all_=all_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    all_: Union[Unset, bool] = False,
) -> Optional[List["Webhook"]]:
    """Webhook情報のリストを取得します

     Webhookのリストを取得します。
    allがtrueで無い場合は、自分がオーナーのWebhookのリストを返します。

    Args:
        all_ (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Webhook']
    """

    return sync_detailed(
        client=client,
        all_=all_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    all_: Union[Unset, bool] = False,
) -> Response[List["Webhook"]]:
    """Webhook情報のリストを取得します

     Webhookのリストを取得します。
    allがtrueで無い場合は、自分がオーナーのWebhookのリストを返します。

    Args:
        all_ (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Webhook']]
    """

    kwargs = _get_kwargs(
        all_=all_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    all_: Union[Unset, bool] = False,
) -> Optional[List["Webhook"]]:
    """Webhook情報のリストを取得します

     Webhookのリストを取得します。
    allがtrueで無い場合は、自分がオーナーのWebhookのリストを返します。

    Args:
        all_ (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Webhook']
    """

    return (
        await asyncio_detailed(
            client=client,
            all_=all_,
        )
    ).parsed
