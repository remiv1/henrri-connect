"""Sous-client pour les endpoints /v1/revenues."""

from __future__ import annotations

from .synchro import SyncRevenuesClient
from .asynchro import AsyncRevenuesClient

__all__ = [
    "SyncRevenuesClient",
    "AsyncRevenuesClient",
]
