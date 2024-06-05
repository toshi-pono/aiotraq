import asyncio
import threading
from typing import Callable, Any, Coroutine
from aiotraq_bot import TraqHttpBot
from aiotraq import AuthenticatedClient
from .message import TraqMessage
from .engine import MessageEngine


class TraqMessageManager:
    """Create a new TraqMessageManager

    Args:
        bot (TraqHttpBot): TraqHttpBot instance
        access_token (str): The access token for the bot
        base_url (str): The base API URL for the bot

    Example:
    .. code-block:: python
        from aiotraq_bot import TraqHttpBot
        from aiotraq_message import TraqMessageManager

        bot = TraqHttpBot(verification_token=BOT_VERIFICATION_TOKEN)
        response = TraqMessageManager(bot, BOT_ACCESS_TOKEN, "https://q.trap.jp/api/v3")
    """

    def __init__(self, bot: TraqHttpBot, access_token: str, base_url: str):
        self.bot = bot
        self._access_token = access_token
        self._base_url = base_url

    async def __call__(
        self,
        component: Callable[[TraqMessage, tuple[Any, ...]], Coroutine[Any, Any, None]],
        channnel_id: str | None = None,
        user_id: str | None = None,
        *args: Any,
    ) -> None:
        t = threading.Thread(target=self.__run, args=(component, channnel_id, user_id, *args), daemon=True)
        t.start()
        # joinを待たずに返す
        return

    def __run(
        self,
        component: Callable[[TraqMessage, tuple[Any, ...]], Coroutine[Any, Any, None]],
        channnel_id: str | None = None,
        user_id: str | None = None,
        *args: Any,
    ) -> None:
        loop = asyncio.new_event_loop()
        client = AuthenticatedClient(base_url=self._base_url, token=self._access_token)
        asyncio.set_event_loop(loop)
        engine = MessageEngine(client, channel_id=channnel_id, user_id=user_id, embed=False)
        message = TraqMessage(engine)

        # engine.taskをバックグラウンドで実行 -> (componentを実行 -> engine.end)を実行
        async def component_task() -> None:
            await component(message, *args)
            await engine.end()

        loop.run_until_complete(asyncio.gather(engine.task(), component_task()))
        return
