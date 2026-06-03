"""Sous-client pour les endpoints /v1/documenttypes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import DocumentType, ListResponse

if TYPE_CHECKING:
    from ..connect import (
        SyncHenrriClient,
    )

DOCUMENTTYPE_ENDPOINT = "/v1/documenttypes"

class SyncDocumentTypesClient:
    """Accès synchrone aux types de documents."""

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def list_document_types(self) -> ListResponse[DocumentType]:
        """Liste tous les types de documents."""
        resp = self._c.request("GET", DOCUMENTTYPE_ENDPOINT)
        return ListResponse[DocumentType].model_validate(resp.json())
