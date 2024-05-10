from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bot import Bot
from ...models.bot_detail import BotDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: str,
    *,
    detail: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["detail"] = detail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/bots/{bot_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Union["Bot", "BotDetail"]]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["Bot", "BotDetail"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = Bot.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = BotDetail.from_dict(data)

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
) -> Response[Union[Any, Union["Bot", "BotDetail"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    detail: Union[Unset, bool] = False,
) -> Response[Union[Any, Union["Bot", "BotDetail"]]]:
    """BOT情報を取得

     指定したBOTのBOT情報を取得します。
    BOT詳細情報を取得する場合は、対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        detail (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['Bot', 'BotDetail']]]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        detail=detail,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    detail: Union[Unset, bool] = False,
) -> Optional[Union[Any, Union["Bot", "BotDetail"]]]:
    """BOT情報を取得

     指定したBOTのBOT情報を取得します。
    BOT詳細情報を取得する場合は、対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        detail (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['Bot', 'BotDetail']]
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        detail=detail,
    ).parsed


async def asyncio_detailed(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    detail: Union[Unset, bool] = False,
) -> Response[Union[Any, Union["Bot", "BotDetail"]]]:
    """BOT情報を取得

     指定したBOTのBOT情報を取得します。
    BOT詳細情報を取得する場合は、対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        detail (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['Bot', 'BotDetail']]]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        detail=detail,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    detail: Union[Unset, bool] = False,
) -> Optional[Union[Any, Union["Bot", "BotDetail"]]]:
    """BOT情報を取得

     指定したBOTのBOT情報を取得します。
    BOT詳細情報を取得する場合は、対象のBOTの管理権限が必要です。

    Args:
        bot_id (str):
        detail (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['Bot', 'BotDetail']]
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            detail=detail,
        )
    ).parsed
