from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.o_auth_2_client import OAuth2Client
from ...models.o_auth_2_client_detail import OAuth2ClientDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    client_id: str,
    *,
    detail: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["detail"] = detail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/clients/{client_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Union["OAuth2Client", "OAuth2ClientDetail"]]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["OAuth2Client", "OAuth2ClientDetail"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = OAuth2Client.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = OAuth2ClientDetail.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Union[Any, Union["OAuth2Client", "OAuth2ClientDetail"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    detail: Union[Unset, bool] = False,
) -> Response[Union[Any, Union["OAuth2Client", "OAuth2ClientDetail"]]]:
    """OAuth2クライアント情報を取得

     指定したOAuth2クライアントの情報を取得します。
    詳細情報の取得には対象のクライアントの管理権限が必要です。

    Args:
        client_id (str):
        detail (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['OAuth2Client', 'OAuth2ClientDetail']]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        detail=detail,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    detail: Union[Unset, bool] = False,
) -> Optional[Union[Any, Union["OAuth2Client", "OAuth2ClientDetail"]]]:
    """OAuth2クライアント情報を取得

     指定したOAuth2クライアントの情報を取得します。
    詳細情報の取得には対象のクライアントの管理権限が必要です。

    Args:
        client_id (str):
        detail (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['OAuth2Client', 'OAuth2ClientDetail']]
    """

    return sync_detailed(
        client_id=client_id,
        client=client,
        detail=detail,
    ).parsed


async def asyncio_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    detail: Union[Unset, bool] = False,
) -> Response[Union[Any, Union["OAuth2Client", "OAuth2ClientDetail"]]]:
    """OAuth2クライアント情報を取得

     指定したOAuth2クライアントの情報を取得します。
    詳細情報の取得には対象のクライアントの管理権限が必要です。

    Args:
        client_id (str):
        detail (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['OAuth2Client', 'OAuth2ClientDetail']]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        detail=detail,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    detail: Union[Unset, bool] = False,
) -> Optional[Union[Any, Union["OAuth2Client", "OAuth2ClientDetail"]]]:
    """OAuth2クライアント情報を取得

     指定したOAuth2クライアントの情報を取得します。
    詳細情報の取得には対象のクライアントの管理権限が必要です。

    Args:
        client_id (str):
        detail (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['OAuth2Client', 'OAuth2ClientDetail']]
    """

    return (
        await asyncio_detailed(
            client_id=client_id,
            client=client,
            detail=detail,
        )
    ).parsed
