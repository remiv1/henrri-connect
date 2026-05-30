"""Sous-client pour les endpoints /v1/documents/{documentId}/lines."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import DocumentLine, ListResponse

if TYPE_CHECKING:
    from ..connect import (
        _SyncHenrriClient,  # type: ignore[import]
    )

DOCUMENT_ENDPOINT = "/v1/documents"

class SyncDocumentLinesClient:
    """Accès synchrone aux lignes de document."""

    def __init__(self, client: _SyncHenrriClient) -> None:
        self._c = client

    def list_document_lines(self, document_id: int) -> ListResponse[DocumentLine]:
        """Liste les lignes d'un document."""
        resp = self._c.request("GET", f"{DOCUMENT_ENDPOINT}/{document_id}/lines")
        return ListResponse[DocumentLine].model_validate(resp.json())

    def add(self, document_id: int, line: DocumentLine) -> DocumentLine:
        """Ajoute une ligne à un document."""
        resp = self._c.request(
            "POST",
            f"{DOCUMENT_ENDPOINT}/{document_id}/lines",
            json=line.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return DocumentLine.model_validate(resp.json())

    def get(self, document_id: int, line_id: int) -> DocumentLine:
        """Récupère une ligne de document par son identifiant."""
        resp = self._c.request("GET", f"{DOCUMENT_ENDPOINT}/{document_id}/lines/{line_id}")
        return DocumentLine.model_validate(resp.json())

    def modify(self, document_id: int, line_id: int, line: DocumentLine) -> DocumentLine:
        """Met à jour une ligne de document."""
        resp = self._c.request(
            "PUT",
            f"{DOCUMENT_ENDPOINT}/{document_id}/lines/{line_id}",
            json=line.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return DocumentLine.model_validate(resp.json())

    def delete(self, document_id: int, line_id: int) -> None:
        """Supprime une ligne de document."""
        self._c.request("DELETE", f"{DOCUMENT_ENDPOINT}/{document_id}/lines/{line_id}")

    def move(self, document_id: int, line_id: int, to: int) -> None:
        """Déplace une ligne vers une position donnée."""
        self._c.request(
            "POST",
            f"{DOCUMENT_ENDPOINT}/{document_id}/lines/{line_id}/move",
            params={"to": to},
        )
