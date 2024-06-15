import io
from contextlib import contextmanager
from typing import Any, Generator

import numpy as np
import pandas as pd
from PIL import Image

from aiotraq_message.utils import base64_to_file, bytes_to_file, cv2pil

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

    def stamp(self, stamp_id: str) -> None:
        """
        スタンプを押す

        Args:
            stamp_id (str): スタンプ ID
        """
        self.engine.add_stamp(stamp_id)

    def clear_stamp(self, stamp_id: str) -> None:
        """
        スタンプを消す

        Args:
            stamp_id (str): スタンプ ID
        """
        self.engine.remove_stamp(stamp_id)

    def clear_all_stamp(self) -> None:
        """
        全てのスタンプを消す
        """
        self.engine.remove_all_stamp()

    def image(self, image: str | Image.Image | io.BytesIO | np.ndarray) -> str | None:
        """
        画像を表示する

        Args:
            image (str | Image.Image | BytesIO | np.ndarray): 画像

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
        elif isinstance(image, io.BytesIO):
            file = bytes_to_file(image.getvalue(), "image.png", "image/png")
            return self.engine.add_file(file)
        elif isinstance(image, np.ndarray):
            image_pil = cv2pil(image)
            output = io.BytesIO()
            image_pil.save(output, format="PNG")
            file = bytes_to_file(output.getvalue(), "image.png", "image/png")
            return self.engine.add_file(file)
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

    def dataframe(self, df: pd.DataFrame | pd.Series, *, max_length: int = 10) -> str | None:
        """
        表を表示する

        Args:
            df (pd.DataFrame | pd.Series): 表
            max_length (int): 表示する最大行数
        """
        # markdown で表示する
        out_df = df
        if isinstance(df, pd.Series):
            out_df = df.to_frame()

        # 行数が多い場合は省略して最初と最後を表示 間には省略記号を入れる
        if len(df) > max_length:
            shortcut = pd.DataFrame(["..."] * len(df.columns), index=df.columns).T
            shortcut.index = ["..."]
            out_df = pd.concat([df.head(max_length // 2), shortcut, df.tail(max_length // 2)])

        markdown = out_df.to_markdown() + "\n"

        return self.engine.add_message(markdown)

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
