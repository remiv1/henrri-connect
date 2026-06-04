"""
Sous-client pour les endpoints /v1/document-line-types.

Classes:
--------
- ``henrri_connect.document_line_types.synchro.SyncDocumentLineTypesClient`` :
    Accès synchrone aux endpoints types de lignes de documents.

- ``henrri_connect.document_line_types.asynchro.AsyncDocumentLineTypesClient`` :
    Accès asynchrone aux endpoints types de lignes de documents.

Notes:
------
- Utiliser de préférence les objets suivants pour acceder aux endpoints:
    - ``henrri_connect.SyncHenrriClient``
    - ``henrri_connect.AsyncHenrriClient``
"""

from __future__ import annotations

from .synchro import SyncDocumentLineTypesClient
from .asynchro import AsyncDocumentLineTypesClient
from ..models import DocumentLineType, ListResponse

__all__ = [
    "AsyncDocumentLineTypesClient",
    "DocumentLineType",
    "ListResponse",
    "SyncDocumentLineTypesClient",
]
