import inspect
from typing import Awaitable, Callable
from aiotraq_bot.models.event_models import convert_json_to_model
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import uvicorn
from fastapi import FastAPI, Header, Response

from aiotraq_bot.models.event import JoinedPayload

EventHandlerType = Callable[..., Awaitable[None]]


class TraqHttpBot:
    def __init__(self, verification_token: str):
        self.verification_token = verification_token
        self.handlers: dict[str, list[EventHandlerType]] = {
            "PING": [],
            "JOINED": [],
            "LEFT": [],
            "MESSAGE_CREATED": [],
            "MESSAGE_DELETED": [],
            "MESSAGE_UPDATED": [],
            "DIRECT_MESSAGE_CREATED": [],
            "DIRECT_MESSAGE_DELETED": [],
            "DIRECT_MESSAGE_UPDATED": [],
            "BOT_MESSAGE_STAMPS_UPDATED": [],
            "CHANNEL_CREATED": [],
            "CHANNEL_TOPIC_CHANGED": [],
            "USER_CREATED": [],
            "STAMP_CREATED": [],
            "TAG_ADDED": [],
            "TAG_REMOVED": [],
            "USER_GROUP_CREATED": [],
            "USER_GROUP_UPDATED": [],
            "USER_GROUP_DELETED": [],
            "USER_GROUP_MEMBER_ADDED": [],
            "USER_GROUP_MEMBER_UPDATED": [],
            "USER_GROUP_MEMBER_REMOVED": [],
            "USER_GROUP_ADMIN_ADDED": [],
            "USER_GROUP_ADMIN_REMOVED": [],
        }

    async def handle_event(self, json_data: dict, event: str) -> None:
        payload = convert_json_to_model(json_data, event)
        if event not in self.handlers:
            return

        for handler in self.handlers[event]:
            sig = inspect.signature(handler)
            if len(sig.parameters) == 0:
                await handler()
            elif len(sig.parameters) == 1:
                # TODO: check if the handler expects the correct payload type (?)
                await handler(payload)
            else:
                raise ValueError("Invalid handler signature: must be 0 or 1 arguments")

    def _register_handler(self, event: str, func: EventHandlerType) -> None:
        self.handlers[event].append(func)

    def joind(
        self, func: Callable[[JoinedPayload | None], Awaitable[None]]
    ) -> Callable[[JoinedPayload | None], Awaitable[None]]:
        """Register a handler for the JOINED event.

        Args:
            func (Callable[[JoinedPayload | None], Awaitable[None]]): The handler function.

        Returns:
            Callable[[JoinedPayload | None], Awaitable[None]]: The handler function.
        """
        self._register_handler("JOINED", func)
        return func


class TraqHttpBotServer:
    def __init__(self, hostname: str, port: int, bot: TraqHttpBot):
        self.hostname = hostname
        self.port = port
        self.bot = bot
        self.app = FastAPI()

        self.app.add_api_route("/", self.handle_bot_request, methods=["POST"])

    async def handle_bot_request(
        self,
        json_data: dict,
        x_traq_verification_token: str | None = Header(default=None),
        x_traq_bot_event: str | None = Header(default=None),
        x_traq_bot_request_id: str | None = Header(default=None),
    ) -> Response:
        if x_traq_verification_token != self.bot.verification_token:
            print("Invalid verification token")
            return JSONResponse(status_code=401, content={"message": "Invalid verification token"})
        if x_traq_bot_event is None:
            print("No X-TRAQ-BOT-EVENT")
            return JSONResponse(status_code=400, content={"message": "No X-TRAQ-BOT-EVENT"})
        if x_traq_bot_request_id is None:
            print("No X-TRAQ-BOT-REQUEST-ID")
            return JSONResponse(status_code=400, content={"message": "No X-TRAQ-BOT-REQUEST-ID"})

        try:
            await self.bot.handle_event(json_data, x_traq_bot_event)
            return JSONResponse(status_code=204, content={})
        except ValidationError as e:
            print(f"Validation error: {e}")
            return JSONResponse(status_code=400, content={"message": "Validation error"})
        except Exception as e:
            print(f"Error handling event: {e}")
            return JSONResponse(status_code=500, content={"message": "Error handling event"})

    def run(self) -> None:
        uvicorn.run(self.app, host=self.hostname, port=self.port)
