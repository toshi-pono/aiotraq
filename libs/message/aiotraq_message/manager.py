import asyncio
import inspect
import threading
from typing import Callable, Any, Coroutine
from aiotraq_bot import TraqHttpBot
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
        response = TraqMessageManager(bot, BOT_ACCESS_TOKEN, "https://q.trap.jp/api/v3", "https://q.trap.jp")
    """

    def __init__(self, bot: TraqHttpBot, access_token: str, base_url: str, base_client_url: str):
        self.bot = bot
        self._access_token = access_token
        self._base_url = base_url
        self._base_client_url = base_client_url

    async def __call__(
        self,
        component: Callable[
            ...,
            Coroutine[Any, Any, None],
        ],
        *,
        channnel_id: str | None = None,
        user_id: str | None = None,
        payload: Any | None = None,
    ) -> None:
        """
        Args:
            component (Callable[..., Coroutine[Any, Any, None]]): The component to run
            channnel_id (str, optional): The channel ID to run the component in. Defaults to None.
            user_id (str, optional): The user ID to run the component for. Defaults to None.
            payload (Any, optional): The payload to pass to the component. Defaults to None.
        """
        t = threading.Thread(target=self.__run, args=(component, channnel_id, user_id, payload), daemon=True)
        t.start()
        # joinを待たずに返す
        return

    def __run(
        self,
        component: Callable[..., Coroutine[Any, Any, None]],
        channnel_id: str | None = None,
        user_id: str | None = None,
        payload: Any | None = None,
    ) -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        engine = MessageEngine(
            base_url=self._base_url,
            base_client_url=self._base_client_url,
            access_token=self._access_token,
            channel_id=channnel_id,
            user_id=user_id,
            embed=False,
        )
        message = TraqMessage(engine)

        # engine.taskをバックグラウンドで実行 -> (componentを実行 -> engine.end)を実行
        async def component_task() -> None:
            sig = inspect.signature(component)
            if len(sig.parameters) == 0:
                await component()
            elif len(sig.parameters) == 1:
                await component(message)
            elif len(sig.parameters) == 2:
                await component(message, payload)
            else:
                raise ValueError("Invalid component signature")

            await engine.end()

        loop.run_until_complete(asyncio.gather(engine.task(), component_task()))
        return
