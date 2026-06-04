"""
Sous-client pour les endpoints /v1/item-categories.

Classes:
--------
- ``henrri_connect.item_categories.synchro.SyncItemCategoriesClient`` :
    Accès synchrone aux endpoints categories d'articles.

- ``henrri_connect.item_categories.asynchro.AsyncItemCategoriesClient`` :
    Accès asynchrone aux endpoints categories d'articles.

Notes:
------
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
- Utiliser de préférence l'objet ``henrri_connect.AsyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from .synchro import SyncItemCategoriesClient
from .asynchro import AsyncItemCategoriesClient

__all__ = [
    "SyncItemCategoriesClient",
    "AsyncItemCategoriesClient",
]
