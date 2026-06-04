"""
Sous-client pour les endpoints /v1/items.

Classes:
--------
- `henrri_connect.items.asynchro.AsyncItemsClient`:
    Accès asynchrone aux endpoints articles.
- `henrri_connect.items.synchro.SyncItemsClient`:
    Accès synchrone aux endpoints articles.

Notes:
-----
- Utiliser de préférence l'objet `henrri_connect.SyncHenrriClient` pour acceder aux endpoints.
- Utiliser de préférence l'objet `henrri_connect.AsyncHenrriClient` pour acceder aux endpoints.
"""

from __future__ import annotations

from .synchro import SyncItemsClient
from .asynchro import AsyncItemsClient
from ..models import Item, PagedListResponse, ItemsQuery

__all__ = [
    "AsyncItemsClient",
    "Item",
    "ItemsQuery",
    "PagedListResponse",
    "SyncItemsClient",
]
