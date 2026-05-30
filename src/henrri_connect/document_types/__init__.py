"""Sous-client pour les endpoints /v1/documenttypes."""

from __future__ import annotations

from .synchro import SyncDocumentTypesClient
from .asynchro import AsyncDocumentTypesClient

__all__ = [
    "SyncDocumentTypesClient",
    "AsyncDocumentTypesClient",
]
