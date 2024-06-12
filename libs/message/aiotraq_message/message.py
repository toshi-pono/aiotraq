from contextlib import contextmanager
import io
from PIL import Image
from aiotraq.types import File
from aiotraq_message.utils import base64_to_file, bytes_to_file
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
        write等で追加したメッセージを削除する

        Args:
            message_id (str): メッセージ ID
        """
        self.engine.remove_message(message_id)

    def image(self, image: str | Image.Image | File) -> str | None:
        """
        画像を表示する

        Args:
            image (str | Image.Image | File): 画像

        Returns:
            str: 画像 ID (送信に失敗した場合はNone)

        Examples:
        .. code-block:: python
            image_id = am.image("data:image/png;base64,xxxxxxxxxxxx")
        """
        if isinstance(image, str):
            # base64 encoded image
            # format: data:image/png;base64,xxxxxxxxxxxx
            file = base64_to_file(image)
            if file is None:
                return None
            return self.engine.add_file(file)
        elif isinstance(image, Image.Image):
            output = io.BytesIO()
            image.save(output, format="PNG")
            file = bytes_to_file(output.getvalue(), "image.png", "image/png")
            return self.engine.add_file(file)
        elif isinstance(image, File):
            return self.engine.add_file(image)
        else:
            return None

    def pyplot(self, fig: Any) -> str | None:
        """
        Matplotlib の figure を表示する

        Args:
            fig (Any): Matplotlib の figure

        Returns:
            str: 画像 ID (送信に失敗した場合はNone)

        Examples:
        .. code-block:: python
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()
            ax.plot([1, 2, 3, 4])
            am.pyplot(fig)
        """
        output = io.BytesIO()
        fig.savefig(output, format="PNG")
        file = bytes_to_file(output.getvalue(), "image.png", "image/png")
        return self.engine.add_file(file)

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
