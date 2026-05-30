"""Sous-client pour les endpoints /v1/item-categories."""

from __future__ import annotations

from .synchro import SyncItemCategoriesClient
from .asynchro import AsyncItemCategoriesClient

__all__ = [
    "SyncItemCategoriesClient",
    "AsyncItemCategoriesClient",
]
