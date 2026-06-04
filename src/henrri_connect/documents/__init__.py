"""
Sous-client pour les endpoints /v1/documents.

Classes:
--------
- `henrri_connect.documents.synchro.SyncDocumentsClient`:
    Accès synchrone aux endpoints documents.

- `henrri_connect.documents.asynchro.AsyncDocumentsClient`:
    Accès asynchrone aux endpoints documents.

Notes:
-----
- Utiliser de préférence les objets suivants pour acceder aux endpoints:
    - `henrri_connect.SyncHenrriClient`
    - `henrri_connect.AsyncHenrriClient`
"""

from __future__ import annotations

from .synchro import SyncDocumentsClient
from .asynchro import AsyncDocumentsClient
from ..models import (
    Document,
    ListResponse,
    PagedListResponse,
    PaymentMilestone,
    PdfUrlResponse,
    TaxDetailArray,
    ValidateDocumentRequest,
)

__all__ = [
    "AsyncDocumentsClient",
    "Document",
    "ListResponse",
    "PagedListResponse",
    "PaymentMilestone",
    "PdfUrlResponse",
    "TaxDetailArray",
    "ValidateDocumentRequest",
    "SyncDocumentsClient",
]
