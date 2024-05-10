import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_messages_message_search_result import SearchMessagesMessageSearchResult
from ...models.search_messages_sort import SearchMessagesSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    word: Union[Unset, str] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    in_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    citation: Union[Unset, str] = UNSET,
    bot: Union[Unset, bool] = UNSET,
    has_url: Union[Unset, bool] = UNSET,
    has_attachments: Union[Unset, bool] = UNSET,
    has_image: Union[Unset, bool] = UNSET,
    has_video: Union[Unset, bool] = UNSET,
    has_audio: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, SearchMessagesSort] = SearchMessagesSort.VALUE_1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["word"] = word

    json_after: Union[Unset, str] = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    json_before: Union[Unset, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params["in"] = in_

    params["to"] = to

    params["from"] = from_

    params["citation"] = citation

    params["bot"] = bot

    params["hasURL"] = has_url

    params["hasAttachments"] = has_attachments

    params["hasImage"] = has_image

    params["hasVideo"] = has_video

    params["hasAudio"] = has_audio

    params["limit"] = limit

    params["offset"] = offset

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SearchMessagesMessageSearchResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchMessagesMessageSearchResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, SearchMessagesMessageSearchResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    word: Union[Unset, str] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    in_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    citation: Union[Unset, str] = UNSET,
    bot: Union[Unset, bool] = UNSET,
    has_url: Union[Unset, bool] = UNSET,
    has_attachments: Union[Unset, bool] = UNSET,
    has_image: Union[Unset, bool] = UNSET,
    has_video: Union[Unset, bool] = UNSET,
    has_audio: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, SearchMessagesSort] = SearchMessagesSort.VALUE_1,
) -> Response[Union[Any, SearchMessagesMessageSearchResult]]:
    """メッセージを検索

     メッセージを検索します。

    Args:
        word (Union[Unset, str]):
        after (Union[Unset, datetime.datetime]):
        before (Union[Unset, datetime.datetime]):
        in_ (Union[Unset, str]):
        to (Union[Unset, str]):
        from_ (Union[Unset, str]):
        citation (Union[Unset, str]):
        bot (Union[Unset, bool]):
        has_url (Union[Unset, bool]):
        has_attachments (Union[Unset, bool]):
        has_image (Union[Unset, bool]):
        has_video (Union[Unset, bool]):
        has_audio (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, SearchMessagesSort]):  Default: SearchMessagesSort.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SearchMessagesMessageSearchResult]]
    """

    kwargs = _get_kwargs(
        word=word,
        after=after,
        before=before,
        in_=in_,
        to=to,
        from_=from_,
        citation=citation,
        bot=bot,
        has_url=has_url,
        has_attachments=has_attachments,
        has_image=has_image,
        has_video=has_video,
        has_audio=has_audio,
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    word: Union[Unset, str] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    in_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    citation: Union[Unset, str] = UNSET,
    bot: Union[Unset, bool] = UNSET,
    has_url: Union[Unset, bool] = UNSET,
    has_attachments: Union[Unset, bool] = UNSET,
    has_image: Union[Unset, bool] = UNSET,
    has_video: Union[Unset, bool] = UNSET,
    has_audio: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, SearchMessagesSort] = SearchMessagesSort.VALUE_1,
) -> Optional[Union[Any, SearchMessagesMessageSearchResult]]:
    """メッセージを検索

     メッセージを検索します。

    Args:
        word (Union[Unset, str]):
        after (Union[Unset, datetime.datetime]):
        before (Union[Unset, datetime.datetime]):
        in_ (Union[Unset, str]):
        to (Union[Unset, str]):
        from_ (Union[Unset, str]):
        citation (Union[Unset, str]):
        bot (Union[Unset, bool]):
        has_url (Union[Unset, bool]):
        has_attachments (Union[Unset, bool]):
        has_image (Union[Unset, bool]):
        has_video (Union[Unset, bool]):
        has_audio (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, SearchMessagesSort]):  Default: SearchMessagesSort.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SearchMessagesMessageSearchResult]
    """

    return sync_detailed(
        client=client,
        word=word,
        after=after,
        before=before,
        in_=in_,
        to=to,
        from_=from_,
        citation=citation,
        bot=bot,
        has_url=has_url,
        has_attachments=has_attachments,
        has_image=has_image,
        has_video=has_video,
        has_audio=has_audio,
        limit=limit,
        offset=offset,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    word: Union[Unset, str] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    in_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    citation: Union[Unset, str] = UNSET,
    bot: Union[Unset, bool] = UNSET,
    has_url: Union[Unset, bool] = UNSET,
    has_attachments: Union[Unset, bool] = UNSET,
    has_image: Union[Unset, bool] = UNSET,
    has_video: Union[Unset, bool] = UNSET,
    has_audio: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, SearchMessagesSort] = SearchMessagesSort.VALUE_1,
) -> Response[Union[Any, SearchMessagesMessageSearchResult]]:
    """メッセージを検索

     メッセージを検索します。

    Args:
        word (Union[Unset, str]):
        after (Union[Unset, datetime.datetime]):
        before (Union[Unset, datetime.datetime]):
        in_ (Union[Unset, str]):
        to (Union[Unset, str]):
        from_ (Union[Unset, str]):
        citation (Union[Unset, str]):
        bot (Union[Unset, bool]):
        has_url (Union[Unset, bool]):
        has_attachments (Union[Unset, bool]):
        has_image (Union[Unset, bool]):
        has_video (Union[Unset, bool]):
        has_audio (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, SearchMessagesSort]):  Default: SearchMessagesSort.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SearchMessagesMessageSearchResult]]
    """

    kwargs = _get_kwargs(
        word=word,
        after=after,
        before=before,
        in_=in_,
        to=to,
        from_=from_,
        citation=citation,
        bot=bot,
        has_url=has_url,
        has_attachments=has_attachments,
        has_image=has_image,
        has_video=has_video,
        has_audio=has_audio,
        limit=limit,
        offset=offset,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    word: Union[Unset, str] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    in_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    citation: Union[Unset, str] = UNSET,
    bot: Union[Unset, bool] = UNSET,
    has_url: Union[Unset, bool] = UNSET,
    has_attachments: Union[Unset, bool] = UNSET,
    has_image: Union[Unset, bool] = UNSET,
    has_video: Union[Unset, bool] = UNSET,
    has_audio: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort: Union[Unset, SearchMessagesSort] = SearchMessagesSort.VALUE_1,
) -> Optional[Union[Any, SearchMessagesMessageSearchResult]]:
    """メッセージを検索

     メッセージを検索します。

    Args:
        word (Union[Unset, str]):
        after (Union[Unset, datetime.datetime]):
        before (Union[Unset, datetime.datetime]):
        in_ (Union[Unset, str]):
        to (Union[Unset, str]):
        from_ (Union[Unset, str]):
        citation (Union[Unset, str]):
        bot (Union[Unset, bool]):
        has_url (Union[Unset, bool]):
        has_attachments (Union[Unset, bool]):
        has_image (Union[Unset, bool]):
        has_video (Union[Unset, bool]):
        has_audio (Union[Unset, bool]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, SearchMessagesSort]):  Default: SearchMessagesSort.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SearchMessagesMessageSearchResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            word=word,
            after=after,
            before=before,
            in_=in_,
            to=to,
            from_=from_,
            citation=citation,
            bot=bot,
            has_url=has_url,
            has_attachments=has_attachments,
            has_image=has_image,
            has_video=has_video,
            has_audio=has_audio,
            limit=limit,
            offset=offset,
            sort=sort,
        )
    ).parsed
