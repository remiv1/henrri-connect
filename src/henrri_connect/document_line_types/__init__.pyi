"""Stubs for the document line types client."""
from __future__ import annotations

from typing import Any

from ..models import DocumentLineType, ListResponse

class SyncDocumentLineTypesClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ... # pylint: disable=W0613
    def list_document_line_types(self) -> ListResponse[DocumentLineType]: ... # pylint: disable=C0116

class AsyncDocumentLineTypesClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ... # pylint: disable=W0613
    async def list_document_line_types(self) -> ListResponse[DocumentLineType]: ... # pylint: disable=C0116
