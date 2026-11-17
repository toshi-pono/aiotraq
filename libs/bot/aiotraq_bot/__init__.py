from importlib.metadata import version

from .bot import TraqHttpBot

__version__ = version(__package__)
__all__ = ["TraqHttpBot"]
