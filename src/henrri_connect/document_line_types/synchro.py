"""Sous-client pour les endpoints /v1/documentlinetypes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import DocumentLineType, ListResponse

if TYPE_CHECKING:
    from ..connect import (
        _SyncHenrriClient,   # type: ignore[import]
    )

DOCUMENTLINETYPES_ENDPOINT = "/v1/documentlinetypes"

class SyncDocumentLineTypesClient:
    """Accès synchrone aux types de lignes de document."""

    def __init__(self, client: _SyncHenrriClient) -> None:
        self._c = client

    def list_document_line_types(self) -> ListResponse[DocumentLineType]:
        """Liste tous les types de lignes de document."""
        resp = self._c.request("GET", DOCUMENTLINETYPES_ENDPOINT)
        return ListResponse[DocumentLineType].model_validate(resp.json())

