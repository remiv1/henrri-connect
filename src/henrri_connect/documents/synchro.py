"""
Sous-client pour les endpoints /v1/documents.

Classes:
- ``henrri_connect.documents.synchro.SyncDocumentsClient``
    Accès synchrone aux endpoints documents.

Notes:
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import (
    Document,
    DocumentQuery,
    ListResponse,
    PagedListResponse,
    PaymentMilestone,
    PdfUrlResponse,
    TaxDetailArray,
    ValidateDocumentRequest,
)
from ..utils import clean

if TYPE_CHECKING:
    from ..connect import SyncHenrriClient

DOCUMENTS_ENDPOINT = "/v1/documents"


class SyncDocumentsClient:
    """
    Accès synchrone aux endpoints documents.

    Arguments
    - ``client`` : Objet ``henrri_connect.AsyncHenrriClient``.

    Methods
    - ``list_documents`` : Liste tous les documents.
    - ``add`` : Ajoute un document.
    - ``get`` : Accès au document par son ID.
    - ``get_with_all`` : Accès au document par son ID avec toutes ses relations incluses.
    - ``get_all_included`` : Accès au document par son ID avec toutes ses données incluses.
    - ``modify`` : Modifie un document par son ID.
    - ``delete`` : Supprime un document par son ID.
    - ``get_tax_details`` : Accès aux taxes d'un document par son ID.
    - ``validate`` : Valide un document.
    - ``get_pdf_url`` : Accès au document par son ID et son GUID.
    - ``get_pdf_bytes`` : Accès au document par son ID et son GUID.
    - ``get_pdf_file`` : Accès au document par son ID et son GUID.
    - ``get_display`` : Accès aux données d'affichage d'un document par son ID.
    - ``get_payment_milestones`` : Accès aux milestones de paiement d'un document par son ID.
    - ``finalize`` : Finalise un document.
    - ``transform_to_invoice`` : Transforme un document (devis, bon de livraison...) en facture.
    - ``get_next_code_batch`` : Accès au code de batch suivant.
    - ``list_with_selected_fields`` : Liste les documents avec sélection de champs.
    """

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def list_documents(self, *, request: DocumentQuery) -> PagedListResponse[Document]:
        """
        Liste les documents avec pagination et filtres optionnels.

        Arguments
        - ``request`` (DocumentQuery) : Paramètres de recherche.

        Returns
        - ``PagedListResponse[Document]`` : Liste paginée de documents.
        """
        params = clean(request.model_dump(by_alias=True))
        resp = self._c.request("GET", DOCUMENTS_ENDPOINT, params=params)
        return PagedListResponse[Document].model_validate(resp.json())

    def add(self, document: Document) -> Document:
        """
        Crée un nouveau document.
        Les champs unset ou None du document sont exclus de la requête.

        Args
        - document (Document) : Document à créer.

        Returns
        - Document: Le document créé avec les données retournées par l'API.

        Raises
        - HTTPError: Si la requête échoue (code de statut 4xx ou 5xx).
        """
        resp = self._c.request(
            "POST",
            DOCUMENTS_ENDPOINT,
            json=document.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Document.model_validate(resp.json())

    def get(self, doc_id: int) -> Document:
        """
        Récupère un document par son identifiant.

        Arguments
        - doc_id (int) : Identifiant du document à reafficher.

        Returns
        - Document: Le document retourné par l'API.

        Raises
        - HTTPError: Si la requête échoue (code de statut 4xx ou 5xx).
        """
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}")
        return Document.model_validate(resp.json())

    def get_with_all(self, doc_id: int) -> Document:
        """
        Récupère un document avec toutes ses relations incluses.

        Arguments
        - doc_id (int) : Identifiant du document à reafficher.

        Returns
        - Document: Le document retourné par l'API.
        """
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/with-all")
        return Document.model_validate(resp.json())

    def get_all_included(self, doc_id: int) -> Document:
        """
        Récupère un document avec toutes ses données incluses.

        Arguments
        - doc_id (int) : Identifiant du document à reafficher.

        Returns
        - Document: Le document retourné par l'API.
        """
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/all-included")
        return Document.model_validate(resp.json())

    def modify(self, doc_id: int, document: Document) -> Document:
        """
        Met à jour un document existant.

        Arguments
        - doc_id (int) : Identifiant du document à mettre à jour.
        - document (Document) : Document à mettre à jour.

        Returns
        - Document: Le document mis à jour par l'API.
        """
        resp = self._c.request(
            "PUT",
            f"{DOCUMENTS_ENDPOINT}/{doc_id}",
            json=document.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Document.model_validate(resp.json())

    def delete(self, doc_id: int) -> None:
        """
        Supprime un document.

        Arguments
        - doc_id (int) : Identifiant du document à supprimer.
        """
        self._c.request("DELETE", f"{DOCUMENTS_ENDPOINT}/{doc_id}")

    def get_tax_details(self, doc_id: int) -> TaxDetailArray:
        """
        Récupère le détail des taxes d'un document.

        Arguments
        - doc_id (int) : Identifiant du document.

        Returns
        - TaxDetailArray: Le détail des taxes retourné par l'API.
        """
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/tax-details")
        return TaxDetailArray.model_validate(resp.json())

    def validate(self, doc_id: int, request: ValidateDocumentRequest) -> Document:
        """
        Valide électroniquement un document.

        Arguments
        - doc_id (int) : Identifiant du document à valider.
        - request (ValidateDocumentRequest) : La requête de validation du document.

        Returns
        - Document: Le document validé par l'API.
        """
        resp = self._c.request(
            "POST",
            f"{DOCUMENTS_ENDPOINT}/{doc_id}/validate",
            json=request.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Document.model_validate(resp.json())

    def get_pdf_url(self, doc_id: int) -> PdfUrlResponse:
        """
        Génère une URL de téléchargement pour le PDF d'un document.

        Arguments
        - doc_id (int) : Identifiant du document.

        Returns
        - PdfUrlResponse: L'URL de téléchargement du PDF retourné par l'API.
        """
        resp = self._c.request("POST", f"{DOCUMENTS_ENDPOINT}/{doc_id}/pdf/url")
        return PdfUrlResponse.model_validate(resp.json())

    def get_pdf_bytes(self, doc_id: int) -> bytes:
        """
        Télécharge le PDF d'un document (retourne les octets bruts).

        Arguments
        - doc_id (int) : Identifiant du document.

        Returns
        - bytes: Les octets bruts du PDF retourné par l'API.
        """
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/pdf")
        return resp.content

    def get_pdf_file(self, doc_id: int, guid: str) -> bytes:
        """
        Télécharge un fichier PDF identifié par son GUID.

        Arguments
        - doc_id (int) : Identifiant du document.
        - guid (str) : GUID du fichier PDF.

        Returns
        - bytes: Les octets bruts du fichier PDF retourné par l'API.
        """
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/pdf/files/{guid}")
        return resp.content

    def get_display(self, doc_id: int) -> Document:
        """
        Récupère les données d'affichage d'un document.

        Arguments
        - doc_id (int) : Identifiant du document.

        Returns
        - Document: Les données d'affichage du document retourné par l'API.
        """
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/display")
        return Document.model_validate(resp.json())

    def get_payment_milestones(self, doc_id: int) -> ListResponse[PaymentMilestone]:
        """
        Récupère les jalons de paiement d'un document.

        Arguments
        - doc_id (int) : Identifiant du document.

        Returns
        - ListResponse[PaymentMilestone]: La liste des jalons de paiement du document retourné
        par l'API.
        """
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/paymentmilestones")
        return ListResponse[PaymentMilestone].model_validate(resp.json())

    def finalize(self, doc_id: int) -> Document:
        """
        Finalise un document.

        Arguments
        - doc_id (int) : Identifiant du document à finaliser.

        Returns
        - Document: Le document finalisé par l'API.
        """
        resp = self._c.request("POST", f"{DOCUMENTS_ENDPOINT}/{doc_id}/finalize")
        return Document.model_validate(resp.json())

    def transform_to_invoice(self, doc_id: int) -> Document:
        """
        Transforme un document (devis, bon de livraison…) en facture.

        Arguments
        - doc_id (int) : Identifiant du document à transformer en facture.

        Returns
        - Document: Le document transformé en facture par l'API.
        """
        resp = self._c.request("POST", f"{DOCUMENTS_ENDPOINT}/{doc_id}/transform-to-invoice")
        return Document.model_validate(resp.json())

    def get_next_quote_batch(self) -> object:
        """
        Récupère le prochain numéro de lot pour un devis.

        Returns
        - object: Le numéro de lot retourné par l'API.
        """
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/next-quote-batch")
        return resp.json()

    def list_with_selected_fields(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        fields: str | None = None,
        **kwargs: object,
    ) -> PagedListResponse[Document]:
        """
        Liste les documents avec sélection de champs.

        Arguments
        - page (int) : Numéro de page.
        - limit (int) : Nombre d'articles par page.
        - fields (str | None) : Champs à retourner.

        Returns
        - PagedListResponse[Document]: La liste des documents retourné par l'API.
        """
        params = clean({"page": page, "limit": limit, "fields": fields, **kwargs})
        resp = self._c.request(
            "GET",
            f"{DOCUMENTS_ENDPOINT}/with-selected-fields",
            params=params
        )
        return PagedListResponse[Document].model_validate(resp.json())
