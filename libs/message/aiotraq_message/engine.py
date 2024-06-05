import asyncio
from dataclasses import dataclass
from datetime import datetime, timedelta
from aiotraq import AuthenticatedClient
from aiotraq.api.message import post_message, post_direct_message, edit_message
from aiotraq.models.post_message_request import PostMessageRequest
from aiotraq.models.message import Message
import uuid


WAIT_QUEUE = 0.01
REQUEST_RATE = 0.9


@dataclass
class InnerMessage:
    id: str
    message: str


class MessageEngine:
    def __init__(
        self,
        client: AuthenticatedClient,
        channel_id: str | None = None,
        user_id: str | None = None,
        embed: bool = False,
        request_rate: float = REQUEST_RATE,
    ):
        self.client = client
        self.updated_at: datetime | None = None
        self.messages: list[InnerMessage] = []
        self.message_id: str | None = None
        self.channel_id = channel_id
        self.user_id = user_id
        self.embed = embed
        self.request_rate = request_rate
        self.event = asyncio.Event()
        self.prev_message = ""
        self.is_loop = True

    def add_message(self, message: str) -> str:
        """
        message を追加する
        """
        message_id = str(uuid.uuid4())
        self.messages.append(InnerMessage(id=message_id, message=message))
        self.request_update()
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
        with self.client as c:
            while self.is_loop:
                await self.event.wait()
                self.event.clear()
                await self.__update_message(c)

            await self.__fflush(c)

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

    async def __init_send_message(self, c: AuthenticatedClient) -> None:
        if self.channel_id is None and self.user_id is None:
            return

        body = PostMessageRequest(
            content="\n".join([msg.message for msg in self.messages]),
            embed=self.embed,
        )
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

        body = PostMessageRequest(
            content="\n".join([msg.message for msg in self.messages]),
            embed=self.embed,
        )
        if self.prev_message == body.content:
            # No change
            return

        await edit_message.asyncio_detailed(
            message_id=self.message_id,
            client=c,
            body=body,
        )
