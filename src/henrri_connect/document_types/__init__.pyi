"""Stubs for document types client."""
from __future__ import annotations

from typing import Any

from ..models import DocumentType, ListResponse

class SyncDocumentTypesClient:  # pylint: disable=C0115, R0903
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    def list_document_types(self) -> ListResponse[DocumentType]: ...    # pylint: disable=C0116

class AsyncDocumentTypesClient:  # pylint: disable=C0115, R0903
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    async def list_document_types(self) -> ListResponse[DocumentType]: ...  # pylint: disable=C0116
