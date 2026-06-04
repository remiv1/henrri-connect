"""
Sous-client pour les endpoints /v1/documentlinetypes.

Classes:
--------
- ``henrri_connect.document_line_types.synchro.SyncDocumentLineTypesClient`` :
    Accès synchrone aux endpoints types de lignes de documents.

Notes:
------
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import DocumentLineType, ListResponse

if TYPE_CHECKING:
    from ..connect import SyncHenrriClient

DOCUMENTLINETYPES_ENDPOINT = "/v1/documentlinetypes"

class SyncDocumentLineTypesClient:  # pylint: disable=R0903
    """
    Accès synchrone aux types de lignes de document.
    
    Arguments:
    - ``client`` : Objet ``henrri_connect.SyncHenrriClient``.
    
    Methods:
    - ``list_document_line_types`` : Liste tous les types de lignes de document.
    """

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def list_document_line_types(self) -> ListResponse[DocumentLineType]:
        """
        Liste tous les types de lignes de document.
        
        Arguments:
        - ``None``
        
        Returns:
        - ``ListResponse[DocumentLineType]`` : Liste de types de lignes de document.
        """
        resp = self._c.request("GET", DOCUMENTLINETYPES_ENDPOINT)
        return ListResponse[DocumentLineType].model_validate(resp.json())
