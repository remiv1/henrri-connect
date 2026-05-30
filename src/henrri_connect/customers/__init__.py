"""Sous-client pour les endpoints /v1/customers."""

from __future__ import annotations

from .asynchro import AsyncCustomersClient
from .synchro import SyncCustomersClient

__all__ = [
    "SyncCustomersClient",
    "AsyncCustomersClient",
]
