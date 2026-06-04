"""
Sous-client pour les endpoints /v1/document-lines.

Classes:
--------
- `henrri_connect.document_lines.synchro.SyncDocumentLinesClient`:
    Accès synchrone aux endpoints lignes de documents.

- `henrri_connect.document_lines.asynchro.AsyncDocumentLinesClient`:
    Accès asynchrone aux endpoints lignes de documents.

Notes:
-----
- Utiliser de préférence les objets suivants pour acceder aux endpoints:
    - `henrri_connect.SyncHenrriClient`
    - `henrri_connect.AsyncHenrriClient`
"""

from __future__ import annotations

from .synchro import SyncDocumentLinesClient
from .asynchro import AsyncDocumentLinesClient
from ..models import DocumentLine, ListResponse, DocumentLineListQueryParameters

__all__ = [
    "AsyncDocumentLinesClient",
    "DocumentLine",
    "DocumentLineListQueryParameters",
    "ListResponse",
    "SyncDocumentLinesClient",
]
