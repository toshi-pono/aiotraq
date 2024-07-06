from .bot import TraqHttpBot
from importlib.metadata import version


__version__ = version(__package__)
__all__ = ["TraqHttpBot"]
