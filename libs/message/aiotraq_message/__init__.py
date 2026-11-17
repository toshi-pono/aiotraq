from importlib.metadata import version

from .manager import TraqMessageManager
from .message import TraqMessage

__version__ = version(__package__)
__all__ = ["TraqMessage", "TraqMessageManager"]
