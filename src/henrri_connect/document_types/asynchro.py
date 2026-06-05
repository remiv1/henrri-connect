"""
Sous-client pour les endpoints /v1/documenttypes.

Classes:
- ``henrri_connect.document_types.asynchro.AsyncDocumentTypesClient``
    Accès asynchrone aux endpoints types de documents.

Notes:
- Utiliser de préférence l'objet ``henrri_connect.AsyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import DocumentType, ListResponse

if TYPE_CHECKING:
    from ..connect import AsyncHenrriClient

DOCUMENTTYPE_ENDPOINT = "/v1/documenttypes"

class AsyncDocumentTypesClient: # pylint: disable=R0903
    """
    Accès asynchrone aux types de documents.

    Arguments
    - ``client`` : Objet ``henrri_connect.AsyncHenrriClient``.

    Methods
    - ``list_document_types`` : Liste tous les types de documents.
    """

    def __init__(self, client: AsyncHenrriClient) -> None:
        self._c = client

    async def list_document_types(self) -> ListResponse[DocumentType]:
        """
        Liste tous les types de documents.

        Arguments
        - ``None``

        Returns
        - ``ListResponse[DocumentType]`` : Liste de types de documents.
        """
        resp = await self._c.request("GET", DOCUMENTTYPE_ENDPOINT)
        return ListResponse[DocumentType].model_validate(resp.json())
