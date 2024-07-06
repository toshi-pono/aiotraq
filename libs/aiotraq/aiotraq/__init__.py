"""A client library for accessing traQ v3"""

from importlib.metadata import version

from .client import AuthenticatedClient, Client

__version__ = version(__package__)
__all__ = (
    "AuthenticatedClient",
    "Client",
)
