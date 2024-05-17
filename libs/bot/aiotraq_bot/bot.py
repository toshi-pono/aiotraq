import inspect
from typing import Awaitable, Callable
from fastapi import FastAPI, Header, Response
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import uvicorn

from .models import EventModel, convert_json_to_model, model_to_event_type


EventHandlerType = Callable[..., Awaitable[None]]


class TraqHttpBot:
    """Create a new TraqHttpBot

    Args:
        verification_token (str): The verification token for the bot

    Examples:
    .. code-block:: python
        import os
        from aiotraq_bot import TraqHttpBot

        bot = TraqHttpBot(verification_token=os.getenv("BOT_VERIFICATION_TOKEN"))

        @bot.event()
        async def on_message(payload: MessageCreatedPayload):
            print(payload)

        if __name__ == "__main__":
            bot.run()
    """

    def __init__(self, verification_token: str | None):
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

    async def handle_event(self, json_data: dict, event: str, request_id: str) -> None:
        payload = convert_json_to_model(json_data, event)
        if event not in self.handlers:
            return

        for handler in self.handlers[event]:
            sig = inspect.signature(handler)
            # 変数名が payload または， dict もしくは eventPayload のアノテーション  の引数に payload を渡す
            # 変数名が event の引数に event を渡す
            # 変数名が id の引数に id を渡す
            params: dict[str, str | EventModel | None] = {}
            for param in sig.parameters.values():
                if param.name == "payload":
                    params[param.name] = payload
                elif param.name == "event":
                    params[param.name] = event
                elif param.name == "id":
                    params[param.name] = request_id
                elif param.annotation == dict or model_to_event_type(param.annotation) is not None:
                    params[param.name] = payload
                else:
                    params[param.name] = None

            await handler(**params)

    def _register_handler(self, event: str, func: EventHandlerType) -> None:
        self.handlers[event].append(func)

    def event(self, event: str | None = None) -> Callable[[EventHandlerType], EventHandlerType]:
        """Register an event handler

        Args:
            event (str | None): The event to handle

        Examples:
        .. code-block:: python
            @bot.event("MESSAGE_CREATED")
            async def on_message_created(payload):
                print(payload)

            @bot.event()
            async def on_ping(payload: MessageCreatedPayload):
                print(payload)
        """

        def decorator(func: EventHandlerType) -> EventHandlerType:
            if event is None:
                # func の引数の型を見て event を決定する
                sig = inspect.signature(func)
                if len(sig.parameters) == 0:
                    raise ValueError("cannot determine event type")

                params = list(sig.parameters.values())
                for param in params:
                    ev_type = model_to_event_type(param.annotation)
                    if ev_type is not None:
                        self._register_handler(ev_type, func)
                        return func
                raise ValueError("cannot determine event type")

            elif event in self.handlers:
                self._register_handler(event, func)
            else:
                raise ValueError(f"Invalid event: {event}")

            return func

        return decorator

    def run(self, hostname: str = "0.0.0.0", port: int = 8080) -> None:
        """Run the bot

        Args:
            hostname (str): The hostname to bind to (default: "0.0.0.0")
            port (int): The port to bind to (default: 8080)
        """
        self.server = TraqHttpBotServer(hostname, port, self)
        try:
            self.server.run()
        except KeyboardInterrupt:
            pass


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
        x_traq_bot_token: str | None = Header(default=None),
        x_traq_bot_event: str | None = Header(default=None),
        x_traq_bot_request_id: str | None = Header(default=None),
    ) -> Response:
        if x_traq_bot_token != self.bot.verification_token:
            print("Invalid verification token")
            return JSONResponse(status_code=401, content={"message": "Invalid verification token"})
        if x_traq_bot_event is None:
            print("No X-TRAQ-BOT-EVENT")
            return JSONResponse(status_code=400, content={"message": "No X-TRAQ-BOT-EVENT"})
        if x_traq_bot_request_id is None:
            print("No X-TRAQ-BOT-REQUEST-ID")
            return JSONResponse(status_code=400, content={"message": "No X-TRAQ-BOT-REQUEST-ID"})

        try:
            await self.bot.handle_event(json_data, x_traq_bot_event, x_traq_bot_request_id)
            return Response(status_code=204, content=None)
        except ValidationError as e:
            print(f"Validation error: {e}")
            return JSONResponse(status_code=400, content={"message": "Validation error"})
        except Exception as e:
            print(f"Error handling event: {e}")
            return JSONResponse(status_code=500, content={"message": "Error handling event"})

    def run(self) -> None:
        uvicorn.run(self.app, host=self.hostname, port=self.port)
