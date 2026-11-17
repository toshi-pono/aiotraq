import io
import unittest
from unittest.mock import Mock

import numpy as np
import pandas as pd
from PIL import Image

from aiotraq_message import TraqMessage


class MessageTests(unittest.TestCase):
    def setUp(self):
        self.engine = Mock()
        self.engine.add_file.return_value = "file-id"
        self.message = TraqMessage(self.engine)

    def test_pillow_image_is_uploaded_as_png(self):
        result = self.message.image(Image.new("RGB", (2, 3), (10, 20, 30)))
        self.assertEqual(result, "file-id")
        file = self.engine.add_file.call_args.args[0]
        self.assertEqual(file.mime_type, "image/png")
        with Image.open(file.payload) as image:
            self.assertEqual(image.format, "PNG")
            self.assertEqual(image.size, (2, 3))
            self.assertEqual(image.getpixel((0, 0)), (10, 20, 30))

    def test_numpy_bgr_image_retains_correct_colors(self):
        image = np.array([[[30, 20, 10]]], dtype=np.uint8)
        self.message.image(image)
        file = self.engine.add_file.call_args.args[0]
        with Image.open(file.payload) as uploaded:
            self.assertEqual(uploaded.getpixel((0, 0)), (10, 20, 30))
        self.assertEqual(image.tolist(), [[[30, 20, 10]]])

    def test_bytes_image_is_forwarded(self):
        self.message.image(io.BytesIO(b"image-bytes"))
        file = self.engine.add_file.call_args.args[0]
        self.assertEqual(file.payload.read(), b"image-bytes")

    def test_dataframe_renders_table(self):
        self.message.dataframe(pd.DataFrame({"name": ["Alice"], "value": [3]}))
        rendered = self.engine.add_message.call_args.args[0]
        self.assertIn("Alice", rendered)
        self.assertIn("name", rendered)
