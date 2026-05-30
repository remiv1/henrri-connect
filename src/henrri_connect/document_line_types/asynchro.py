"""Sous-client pour les endpoints /v1/documentlinetypes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import DocumentLineType, ListResponse

if TYPE_CHECKING:
    from ..connect import (
        _AsyncHenrriClient,   # type: ignore[import]
    )

DOCUMENTLINETYPES_ENDPOINT = "/v1/documentlinetypes"

class AsyncDocumentLineTypesClient:
    """Accès asynchrone aux types de lignes de document."""

    def __init__(self, client: _AsyncHenrriClient) -> None:
        self._c = client

    async def list_document_line_types(self) -> ListResponse[DocumentLineType]:
        """Liste tous les types de lignes de document."""
        resp = await self._c.request("GET", DOCUMENTLINETYPES_ENDPOINT)
        return ListResponse[DocumentLineType].model_validate(resp.json())
