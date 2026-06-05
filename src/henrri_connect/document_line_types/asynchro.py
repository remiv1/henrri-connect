"""
Sous-client pour les endpoints /v1/documentlinetypes.

Classes:
- ``henrri_connect.document_line_types.asynchro.AsyncDocumentLineTypesClient``
    Accès asynchrone aux endpoints types de lignes de documents.

Notes:
- Utiliser de préférence l'objet ``henrri_connect.AsyncHenrriClient`` pour acceder
aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import DocumentLineType, ListResponse

if TYPE_CHECKING:
    from ..connect import AsyncHenrriClient

DOCUMENTLINETYPES_ENDPOINT = "/v1/documentlinetypes"

class AsyncDocumentLineTypesClient: # pylint: disable=R0903
    """
    Accès asynchrone aux types de lignes de document.

    Arguments
    - ``client`` : Objet ``henrri_connect.AsyncHenrriClient``.

    Methods
    - ``list_document_line_types`` : Liste tous les types de lignes de document.
    """

    def __init__(self, client: AsyncHenrriClient) -> None:
        self._c = client

    async def list_document_line_types(self) -> ListResponse[DocumentLineType]:
        """
        Liste tous les types de lignes de document.

        Arguments
        - ``None``

        Returns
        - ``ListResponse[DocumentLineType]`` : Liste de types de lignes de document.
        """
        resp = await self._c.request("GET", DOCUMENTLINETYPES_ENDPOINT)
        return ListResponse[DocumentLineType].model_validate(resp.json())
