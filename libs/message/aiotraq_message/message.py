from contextlib import contextmanager
from typing import Any, Generator
from .engine import MessageEngine


class TraqMessage:
    def __init__(self, engine: MessageEngine):
        self.engine = engine
        self.buttons: list[str] = []

    def write(self, message: str) -> str:
        """
        message を追加する

        Args:
            message (str): メッセージ

        Returns:
            str: メッセージ ID

        Examples:
        .. code-block:: python
            message_id = am.write("Hello, world!")
        """
        return self.engine.add_message(message)

    def clear(self) -> None:
        """
        メッセージをすべて削除する
        """
        self.engine.remove_all_message()

    def clear_message(self, message_id: str) -> None:
        """
        メッセージを削除する
        """
        self.engine.remove_message(message_id)

    @contextmanager
    def spinner(self, message: str = ":loading: loading...") -> Generator[str, Any, None]:
        """
        loading spinner を表示する

        Args:
            message (str): メッセージ

        Yields:
            str: ローディングメッセージ ID

        Examples:
        .. code-block:: python
            with am.spinner():
                # heavy process
                await asyncio.sleep(5)
        """
        loading_id = self.engine.add_message(message)
        try:
            yield loading_id
        finally:
            self.engine.remove_message(loading_id)
