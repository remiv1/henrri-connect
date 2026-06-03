"""Client HTTP Henrri : factory et implémentations synchrone/asynchrone."""

from __future__ import annotations

from .asynchro import AsyncHenrriClient
from .synchro import SyncHenrriClient

_BASE_URL = "https://api-sandbox.henrri.io"
APP_VERSION = "application/json; X-Version=1.0"

__all__ = [
    "AsyncHenrriClient",
    "SyncHenrriClient",
]
