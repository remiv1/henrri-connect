"""
Sous-client pour les endpoints /v1/documenttypes.

Classes:
--------
- `henrri_connect.document_types.synchro.SyncDocumentTypesClient`:
    Accès synchrone aux endpoints types de documents.

- `henrri_connect.document_types.asynchro.AsyncDocumentTypesClient`:
    Accès asynchrone aux endpoints types de documents.

Notes:
-----
- Utiliser de préférence les objets suivants pour acceder aux endpoints:
    - `henrri_connect.SyncHenrriClient`
    - `henrri_connect.AsyncHenrriClient`
"""

from __future__ import annotations

from .synchro import SyncDocumentTypesClient
from .asynchro import AsyncDocumentTypesClient
from ..models import DocumentType, ListResponse

__all__ = [
    "AsyncDocumentTypesClient",
    "DocumentType",
    "ListResponse",
    "SyncDocumentTypesClient",
]
