"""Sous-client pour les endpoints /v1/documents."""

from __future__ import annotations

from .synchro import SyncDocumentsClient
from .asynchro import AsyncDocumentsClient

__all__ = [
    "SyncDocumentsClient",
    "AsyncDocumentsClient",
]
