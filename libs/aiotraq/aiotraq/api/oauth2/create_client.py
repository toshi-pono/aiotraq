from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.o_auth_2_client_detail import OAuth2ClientDetail
from ...models.post_client_request import PostClientRequest
from ...types import Response


def _get_kwargs(
    *,
    body: PostClientRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/clients",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, OAuth2ClientDetail]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = OAuth2ClientDetail.from_dict(response.json())

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
) -> Response[Union[Any, OAuth2ClientDetail]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostClientRequest,
) -> Response[Union[Any, OAuth2ClientDetail]]:
    """OAuth2クライアントを作成

     OAuth2クライアントを作成します。

    Args:
        body (PostClientRequest): OAuth2クライアント作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth2ClientDetail]]
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
    body: PostClientRequest,
) -> Optional[Union[Any, OAuth2ClientDetail]]:
    """OAuth2クライアントを作成

     OAuth2クライアントを作成します。

    Args:
        body (PostClientRequest): OAuth2クライアント作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OAuth2ClientDetail]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostClientRequest,
) -> Response[Union[Any, OAuth2ClientDetail]]:
    """OAuth2クライアントを作成

     OAuth2クライアントを作成します。

    Args:
        body (PostClientRequest): OAuth2クライアント作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth2ClientDetail]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostClientRequest,
) -> Optional[Union[Any, OAuth2ClientDetail]]:
    """OAuth2クライアントを作成

     OAuth2クライアントを作成します。

    Args:
        body (PostClientRequest): OAuth2クライアント作成リクエスト

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OAuth2ClientDetail]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
