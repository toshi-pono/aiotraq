import asyncio
import uuid
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum

from aiotraq import AuthenticatedClient
from aiotraq.api.file import post_file
from aiotraq.api.message import (add_message_stamp, edit_message,
                                 post_direct_message, post_message)
from aiotraq.api.user import get_user_dm_channel
from aiotraq.models.dm_channel import DMChannel
from aiotraq.models.file_info import FileInfo
from aiotraq.models.message import Message
from aiotraq.models.post_file_request import PostFileRequest
from aiotraq.models.post_message_request import PostMessageRequest
from aiotraq.models.post_message_stamp_request import PostMessageStampRequest
from aiotraq.types import File

WAIT_QUEUE = 0.01
REQUEST_RATE = 0.9


class MessageType(Enum):
    TEXT = 0
    FILE = 1


@dataclass
class InnerMessage:
    id: str
    message: str
    type: MessageType


class MessageEngine:
    def __init__(
        self,
        base_url: str,
        base_client_url: str,
        access_token: str,
        channel_id: str | None = None,
        user_id: str | None = None,
        embed: bool = False,
        request_rate: float = REQUEST_RATE,
    ):
        self._base_url = base_url
        self._base_client_url = base_client_url
        self._access_token = access_token
        self.updated_at: datetime | None = None
        self.messages: list[InnerMessage] = []
        self.stamps: list[str] = []
        self.sended_stamps: list[str] = []
        self.message_id: str | None = None
        self.user_id = user_id
        self.embed = embed
        self.request_rate = request_rate
        self.event = asyncio.Event()
        self.prev_message = ""
        self.is_loop = True

        if channel_id is not None:
            self.channel_id = channel_id
        elif user_id is not None:
            # user_idからchannel_idを取得
            client = AuthenticatedClient(base_url=self._base_url, token=self._access_token)
            with client as c:
                response = get_user_dm_channel.sync_detailed(
                    user_id=user_id,
                    client=c,
                )
                if response.status_code == 200:
                    if isinstance(response.parsed, DMChannel):
                        self.channel_id = response.parsed.id

            if self.channel_id is None:
                raise ValueError("Failed to get channel_id from user_id")
        else:
            raise ValueError("channel_id or user_id must be set")

    def add_message(self, message: str) -> str:
        """
        message を追加する
        """
        message_id = str(uuid.uuid4())
        self.messages.append(InnerMessage(id=message_id, message=message, type=MessageType.TEXT))
        self.request_update()
        return message_id

    def add_stamp(self, stamp_id: str) -> None:
        """
        stamp を追加する
        """
        self.stamps.append(stamp_id)
        self.request_update()

    def add_file(self, file: File) -> str:
        """
        file を追加する
        """
        message_id = str(uuid.uuid4())

        # TODO: ここも非同期にしたほうがいいかも
        client = AuthenticatedClient(base_url=self._base_url, token=self._access_token)
        with client as c:
            response = post_file.sync_detailed(
                client=c,
                body=PostFileRequest(
                    file=file,
                    channel_id=self.channel_id,
                ),
            )
            if response.status_code == 201:
                if isinstance(response.parsed, FileInfo):
                    self.messages.append(
                        InnerMessage(
                            id=message_id,
                            message=f"{self._base_client_url}/files/{response.parsed.id}",
                            type=MessageType.FILE,
                        )
                    )
                    self.request_update()
                else:
                    print("Failed to get file info")
            elif response.status_code == 411:
                raise ValueError("Failed to upload file: Length Required")
            elif response.status_code == 413:
                raise ValueError("Failed to upload file: Payload Too Large")
            else:
                raise ValueError("Failed to upload file")
        return message_id

    def remove_message(self, message_id: str) -> None:
        """
        message を削除する
        """
        self.messages = [msg for msg in self.messages if msg.id != message_id]
        self.request_update()

    def remove_all_message(self) -> None:
        """
        全ての message を削除する
        """
        self.messages = []
        self.request_update()

    async def end(self) -> None:
        self.is_loop = False

    def request_update(self) -> None:
        self.event.set()

    async def task(self) -> None:
        client = AuthenticatedClient(base_url=self._base_url, token=self._access_token)
        with client as c:
            while self.is_loop:
                await self.event.wait()
                self.event.clear()
                await self.__update_message(c)
                await self.__update_stamps(c)

            await self.__fflush(c)

    def __create_body(self) -> PostMessageRequest:
        # TEXTを最初に追加 -> FILEを後ろに追加
        text_content = "\n".join([str(msg.message) for msg in self.messages if msg.type == MessageType.TEXT])
        file_content = "\n".join([str(msg.message) for msg in self.messages if msg.type == MessageType.FILE])
        embed = self.embed

        return PostMessageRequest(
            content=text_content + "\n" + file_content,
            embed=embed,
        )

    async def __fflush(self, c: AuthenticatedClient) -> None:
        if self.updated_at is None:
            self.updated_at = datetime.now()
            await self.__init_send_message(c)
        else:
            self.updated_at = datetime.now()
            await self.__update_send_message(c)

    async def __update_message(self, c: AuthenticatedClient) -> None:
        if self.updated_at is None:
            await asyncio.sleep(WAIT_QUEUE)
            self.updated_at = datetime.now()
            await self.__init_send_message(c)
            return

        if datetime.now() - self.updated_at > timedelta(seconds=REQUEST_RATE):
            await self.__update_send_message(c)
            self.updated_at = datetime.now()
            return

    async def __update_stamps(self, c: AuthenticatedClient) -> None:
        unsent_stamps = self.stamps[len(self.sended_stamps):]
        if len(unsent_stamps) == 0:
            return
        if self.message_id is None:
            return

        counter = Counter(unsent_stamps)
        result = [(key, counter[key]) for key in dict.fromkeys(unsent_stamps)]
        for stamp_id, count in result:
            body = PostMessageStampRequest(count=count)
            await add_message_stamp.asyncio_detailed(
                message_id=self.message_id,
                stamp_id=stamp_id,
                client=c,
                body=body,
            )
        self.sended_stamps = self.stamps[:]

    async def __init_send_message(self, c: AuthenticatedClient) -> None:
        if self.channel_id is None and self.user_id is None:
            return

        body = self.__create_body()
        self.prev_message = body.content
        if self.user_id is not None:
            # DM
            response = await post_direct_message.asyncio(
                user_id=self.user_id,
                client=c,
                body=body,
            )
            if isinstance(response, Message):
                self.message_id = response.id
        elif self.channel_id is not None:
            # Channel
            response = await post_message.asyncio(
                channel_id=self.channel_id,
                client=c,
                body=body,
            )
            if isinstance(response, Message):
                self.message_id = response.id

    async def __update_send_message(self, c: AuthenticatedClient) -> None:
        if self.message_id is None:
            return

        body = self.__create_body()
        if self.prev_message == body.content:
            # No change
            return

        await edit_message.asyncio_detailed(
            message_id=self.message_id,
            client=c,
            body=body,
        )
