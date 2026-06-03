"""Client HTTP Henrri : factory et implémentations synchrone/asynchrone."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload, Literal    # type: ignore[import]
from .asynchro import AsyncHenrriClient    # type: ignore[import]
from .synchro import SyncHenrriClient   # type: ignore[import]

_BASE_URL = "https://api-sandbox.henrri.io"
APP_VERSION = "application/json; X-Version=1.0"

__all__ = [
    "AsyncHenrriClient",
    "SyncHenrriClient",
]
