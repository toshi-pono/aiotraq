"""A client library for accessing traQ v3"""

from .client import AuthenticatedClient, Client
from importlib.metadata import version

__version__ = version(__package__)
__all__ = (
    "AuthenticatedClient",
    "Client",
)
