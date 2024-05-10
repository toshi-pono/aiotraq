from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.o_auth_2_prompt import OAuth2Prompt
from ...models.o_auth_2_response_type import OAuth2ResponseType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    response_type: Union[Unset, OAuth2ResponseType] = UNSET,
    client_id: str,
    redirect_uri: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    code_challenge: Union[Unset, str] = UNSET,
    code_challenge_method: Union[Unset, str] = UNSET,
    nonce: Union[Unset, str] = UNSET,
    prompt: Union[Unset, OAuth2Prompt] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_response_type: Union[Unset, str] = UNSET
    if not isinstance(response_type, Unset):
        json_response_type = response_type.value

    params["response_type"] = json_response_type

    params["client_id"] = client_id

    params["redirect_uri"] = redirect_uri

    params["scope"] = scope

    params["state"] = state

    params["code_challenge"] = code_challenge

    params["code_challenge_method"] = code_challenge_method

    params["nonce"] = nonce

    json_prompt: Union[Unset, str] = UNSET
    if not isinstance(prompt, Unset):
        json_prompt = prompt.value

    params["prompt"] = json_prompt

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/oauth2/authorize",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.FOUND:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
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
    *,
    client: Union[AuthenticatedClient, Client],
    response_type: Union[Unset, OAuth2ResponseType] = UNSET,
    client_id: str,
    redirect_uri: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    code_challenge: Union[Unset, str] = UNSET,
    code_challenge_method: Union[Unset, str] = UNSET,
    nonce: Union[Unset, str] = UNSET,
    prompt: Union[Unset, OAuth2Prompt] = UNSET,
) -> Response[Any]:
    """OAuth2 認可エンドポイント

     OAuth2 認可エンドポイント

    Args:
        response_type (Union[Unset, OAuth2ResponseType]):
        client_id (str):
        redirect_uri (Union[Unset, str]):
        scope (Union[Unset, str]):
        state (Union[Unset, str]):
        code_challenge (Union[Unset, str]):
        code_challenge_method (Union[Unset, str]):
        nonce (Union[Unset, str]):
        prompt (Union[Unset, OAuth2Prompt]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        response_type=response_type,
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        state=state,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        nonce=nonce,
        prompt=prompt,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    response_type: Union[Unset, OAuth2ResponseType] = UNSET,
    client_id: str,
    redirect_uri: Union[Unset, str] = UNSET,
    scope: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    code_challenge: Union[Unset, str] = UNSET,
    code_challenge_method: Union[Unset, str] = UNSET,
    nonce: Union[Unset, str] = UNSET,
    prompt: Union[Unset, OAuth2Prompt] = UNSET,
) -> Response[Any]:
    """OAuth2 認可エンドポイント

     OAuth2 認可エンドポイント

    Args:
        response_type (Union[Unset, OAuth2ResponseType]):
        client_id (str):
        redirect_uri (Union[Unset, str]):
        scope (Union[Unset, str]):
        state (Union[Unset, str]):
        code_challenge (Union[Unset, str]):
        code_challenge_method (Union[Unset, str]):
        nonce (Union[Unset, str]):
        prompt (Union[Unset, OAuth2Prompt]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        response_type=response_type,
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        state=state,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        nonce=nonce,
        prompt=prompt,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
