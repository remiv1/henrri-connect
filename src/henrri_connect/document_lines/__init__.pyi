"""Stubs for the document lines client."""
from __future__ import annotations

from typing import Any, Optional

from ..models import DocumentLine, ListResponse, DocumentLineListQueryParameters

class SyncDocumentLinesClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ... # pylint: disable=W0613
    def list_document_lines( # pylint: disable=C0116, W0613
        self,
        document_id: int,
        query_params: Optional[DocumentLineListQueryParameters] = None,
    ) -> ListResponse[DocumentLine]: ...
    def add(self, document_id: int, line: DocumentLine) -> DocumentLine: ... # pylint: disable=C0116, W0613
    def get(self, document_id: int, id: int) -> DocumentLine: ... # pylint: disable=C0116, W0613, W0622
    def modify(self, document_id: int, id: int, line: DocumentLine) -> DocumentLine: ... # pylint: disable=C0116, W0613, W0622
    def delete(self, document_id: int, id: int) -> None: ... # pylint: disable=C0116, W0613, W0622
    def move(self, document_id: int, id: int, to: int) -> None: ... # pylint: disable=C0116, W0613, W0622

class AsyncDocumentLinesClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ... # pylint: disable=W0613
    async def list_document_lines( # pylint: disable=C0116, W0613
        self,
        document_id: int,
        query_params: Optional[DocumentLineListQueryParameters] = None,
    ) -> ListResponse[DocumentLine]: ...
    async def add(self, document_id: int, line: DocumentLine) -> DocumentLine: ... # pylint: disable=C0116, W0613
    async def get(self, document_id: int, id: int) -> DocumentLine: ... # pylint: disable=C0116, W0613, W0622
    async def modify(self, document_id: int, id: int, line: DocumentLine) -> DocumentLine: ... # pylint: disable=C0116, W0613, W0622
    async def delete(self, document_id: int, id: int) -> None: ... # pylint: disable=C0116, W0613, W0622
    async def move(self, document_id: int, id: int, to: int) -> None: ... # pylint: disable=C0116, W0613, W0622
