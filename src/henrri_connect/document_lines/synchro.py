"""
Sous-client pour les endpoints /v1/documents/{documentId}/lines.

Classes:
--------
- `henrri_connect.document_lines.synchro.SyncDocumentLinesClient`:
    Accès synchrone aux endpoints lignes de documents.

Notes:
-----
- Utiliser de préférence l'objet `henrri_connect.SyncHenrriClient` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..models import DocumentLine, ListResponse, DocumentLineListQueryParameters

if TYPE_CHECKING:
    from ..connect import SyncHenrriClient

DOCUMENT_ENDPOINT = "/v1/documents"

class SyncDocumentLinesClient:
    """
    Accès synchrone aux lignes de document.
    
    Arguments:
    - `client`: Objet `henrri_connect.SyncHenrriClient`.
    
    Methods:
    - `list_document_lines`: Liste les lignes d'un document.
    - `add`: Ajoute une ligne à un document.
    - `get`: Récupère une ligne de document par son identifiant.
    - `modify`: Met à jour une ligne de document.
    - `delete`: Supprime une ligne de document.
    - `move`: Déplace une ligne vers une position donnée.
    """

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    async def list_document_lines(
            self,
            document_id: int,
            query_params: Optional[DocumentLineListQueryParameters] = None,
        ) -> ListResponse[DocumentLine]:
        """
        Liste les lignes d'un document.
        
        Arguments:
        - `document_id`(int): Identifiant du document (min 1 et max 2 147 483 647).
        - `query_params`(DocumentLineListQueryParameters, optional): Paramètres de requête.
        
        Returns:
        - `ListResponse[DocumentLine]`: Liste de lignes de document.
        """
        if query_params:
            resp = self._c.request(
                "GET",
                f"{DOCUMENT_ENDPOINT}/{document_id}/lines",
                params=query_params.model_dump(
                    by_alias=True,
                    exclude_unset=True,
                    exclude_none=True
                ),
            )
        else:
            resp = self._c.request("GET", f"{DOCUMENT_ENDPOINT}/{document_id}/lines")
        return ListResponse[DocumentLine].model_validate(resp.json())

    def add(self, document_id: int, line: DocumentLine) -> DocumentLine:
        """
        Ajoute une ligne à un document.
        
        Arguments:
        - `document_id`: Identifiant du document.
        - `line`: Ligne de document.
        
        Returns:
        - `DocumentLine`: Ligne de document ajoutée.
        """
        resp = self._c.request(
            "POST",
            f"{DOCUMENT_ENDPOINT}/{document_id}/lines",
            json=line.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return DocumentLine.model_validate(resp.json())

    def get(self, document_id: int, line_id: int) -> DocumentLine:
        """
        Récupère une ligne de document par son identifiant.
        
        Arguments:
        - `document_id`: Identifiant du document.
        - `line_id`: Identifiant de la ligne de document.
        
        Returns:
        - `DocumentLine`: Ligne de document.
        """
        resp = self._c.request("GET", f"{DOCUMENT_ENDPOINT}/{document_id}/lines/{line_id}")
        return DocumentLine.model_validate(resp.json())

    def modify(self, document_id: int, line_id: int, line: DocumentLine) -> DocumentLine:
        """
        Met à jour une ligne de document.
        
        Arguments:
        - `document_id`: Identifiant du document.
        - `line_id`: Identifiant de la ligne de document.
        - `line`: Ligne de document.
        
        Returns:
        - `DocumentLine`: Ligne de document modifiée.
        """
        resp = self._c.request(
            "PUT",
            f"{DOCUMENT_ENDPOINT}/{document_id}/lines/{line_id}",
            json=line.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return DocumentLine.model_validate(resp.json())

    def delete(self, document_id: int, line_id: int) -> None:
        """
        Supprime une ligne de document.
        
        Arguments:
        - `document_id`: Identifiant du document.
        - `line_id`: Identifiant de la ligne de document.
        
        Returns:
        - `None`
        """
        self._c.request("DELETE", f"{DOCUMENT_ENDPOINT}/{document_id}/lines/{line_id}")

    def move(self, document_id: int, line_id: int, to: int) -> None:
        """
        Déplace une ligne vers une position donnée.
        
        Arguments:
        - `document_id`: Identifiant du document.
        - `line_id`: Identifiant de la ligne de document.
        - `to`: Position de destination.
        
        Returns:
        - `None`
        """
        self._c.request(
            "POST",
            f"{DOCUMENT_ENDPOINT}/{document_id}/lines/{line_id}/move",
            params={"to": to},
        )
