"""Sous-client pour les endpoints /v1/secures."""

from __future__ import annotations

from .synchro import SyncSecuresClient
from .asynchro import AsyncSecuresClient

__all__ = [
    "SyncSecuresClient",
    "AsyncSecuresClient",
]
