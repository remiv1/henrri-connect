"""
Sous-client pour les endpoints /v1/documenttypes.

Classes:
- ``henrri_connect.document_types.synchro.SyncDocumentTypesClient``
    Accès synchrone aux endpoints types de documents.

Notes:
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import DocumentType, ListResponse

if TYPE_CHECKING:
    from ..connect import SyncHenrriClient

DOCUMENTTYPE_ENDPOINT = "/v1/documenttypes"

class SyncDocumentTypesClient:  # pylint: disable=R0903
    """
    Accès synchrone aux types de documents.

    Arguments
    - ``client`` : Objet ``henrri_connect.SyncHenrriClient``.

    Methods
    - ``list_document_types`` : Liste tous les types de documents.
    """

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def list_document_types(self) -> ListResponse[DocumentType]:
        """
        Liste tous les types de documents.

        Arguments
        - ``None``

        Returns
        - ``ListResponse[DocumentType]`` : Liste de types de documents.
        """
        resp = self._c.request("GET", DOCUMENTTYPE_ENDPOINT)
        return ListResponse[DocumentType].model_validate(resp.json())
