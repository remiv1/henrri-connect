"""Sous-client pour les endpoints /v1/documents."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from henrri_connect.models import (
    Document,
    ListResponse,
    PagedListResponse,
    PaymentMilestone,
    PdfUrlResponse,
    TaxDetailArray,
    ValidateDocumentRequest,
)

if TYPE_CHECKING:
    from henrri_connect.connect import (
        _SyncHenrriClient,   # type: ignore[import]
    )

DOCUMENTS_ENDPOINT = "/v1/documents"

def _clean(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


class SyncDocumentsClient:
    """Accès synchrone aux endpoints documents."""

    def __init__(self, client: _SyncHenrriClient) -> None:
        self._c = client

    def list_documents(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        document_type_id: int | None = None,
        customer_id: int | None = None,
        state: str | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        min_id: int | None = None,
    ) -> PagedListResponse[Document]:
        """
        Liste les documents avec pagination et filtres optionnels.

        Args:
            page (int): Numéro de la page à récupérer.
            limit (int): Nombre d'éléments par page.
            search (str | None): Terme de recherche.
            sort_by (str | None): Champ de tri.
            sort_order (str | None): Ordre de tri ("asc" ou "desc").
            document_type_id (int | None): Filtre par type de document.
            customer_id (int | None): Filtre par identifiant de client.
            state (str | None): Filtre par état du document.
            from_date (str | None): Filtre par date de début.
            to_date (str | None): Filtre par date de fin.
            min_id (int | None): Filtre par identifiant minimum.

        Returns:
            PagedListResponse[Document]: Liste paginée de documents.

        Raises:
            HTTPError: Si la requête échoue (code de statut 4xx ou 5xx).
        """
        params = _clean({
            "page": page,
            "limit": limit,
            "search": search,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "documentTypeId": document_type_id,
            "customerId": customer_id,
            "state": state,
            "fromDate": from_date,
            "toDate": to_date,
            "minId": min_id,
        })
        resp = self._c.request("GET", DOCUMENTS_ENDPOINT, params=params)
        return PagedListResponse[Document].model_validate(resp.json())

    def add(self, document: Document) -> Document:
        """
        Crée un nouveau document.
        Les champs unset ou None du document sont exclus de la requête.

        Args:
            document (Document): Document à créer.

        Returns:
            Document: Le document créé avec les données retournées par l'API.

        Raises:
            HTTPError: Si la requête échoue (code de statut 4xx ou 5xx).
        """
        resp = self._c.request(
            "POST",
            DOCUMENTS_ENDPOINT,
            json=document.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Document.model_validate(resp.json())

    def get(self, id: int) -> Document:
        """Récupère un document par son identifiant."""
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{id}")
        return Document.model_validate(resp.json())

    def get_with_all(self, id: int) -> Document:
        """Récupère un document avec toutes ses relations incluses."""
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{id}/with-all")
        return Document.model_validate(resp.json())

    def get_all_included(self, id: int) -> Document:
        """Récupère un document avec toutes ses données incluses."""
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{id}/all-included")
        return Document.model_validate(resp.json())

    def modify(self, id: int, document: Document) -> Document:
        """Met à jour un document existant."""
        resp = self._c.request(
            "PUT",
            f"{DOCUMENTS_ENDPOINT}/{id}",
            json=document.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Document.model_validate(resp.json())

    def delete(self, id: int) -> None:
        """Supprime un document."""
        self._c.request("DELETE", f"{DOCUMENTS_ENDPOINT}/{id}")

    def get_tax_details(self, id: int) -> TaxDetailArray:
        """Récupère le détail des taxes d'un document."""
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{id}/tax-details")
        return TaxDetailArray.model_validate(resp.json())

    def validate(self, id: int, request: ValidateDocumentRequest) -> Document:
        """Valide électroniquement un document."""
        resp = self._c.request(
            "POST",
            f"{DOCUMENTS_ENDPOINT}/{id}/validate",
            json=request.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Document.model_validate(resp.json())

    def get_pdf_url(self, id: int) -> PdfUrlResponse:
        """Génère une URL de téléchargement pour le PDF d'un document."""
        resp = self._c.request("POST", f"{DOCUMENTS_ENDPOINT}/{id}/pdf/url")
        return PdfUrlResponse.model_validate(resp.json())

    def get_pdf_bytes(self, id: int) -> bytes:
        """Télécharge le PDF d'un document (retourne les octets bruts)."""
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{id}/pdf")
        return resp.content

    def get_pdf_file(self, id: int, guid: str) -> bytes:
        """Télécharge un fichier PDF identifié par son GUID."""
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{id}/pdf/files/{guid}")
        return resp.content

    def get_display(self, id: int) -> Document:
        """Récupère les données d'affichage d'un document."""
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{id}/display")
        return Document.model_validate(resp.json())

    def get_payment_milestones(self, document_id: int) -> ListResponse[PaymentMilestone]:
        """Récupère les jalons de paiement d'un document."""
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{document_id}/paymentmilestones")
        return ListResponse[PaymentMilestone].model_validate(resp.json())

    def finalize(self, id: int) -> Document:
        """Finalise un document."""
        resp = self._c.request("POST", f"{DOCUMENTS_ENDPOINT}/{id}/finalize")
        return Document.model_validate(resp.json())

    def transform_to_invoice(self, id: int) -> Document:
        """Transforme un document (devis, bon de livraison…) en facture."""
        resp = self._c.request("POST", f"{DOCUMENTS_ENDPOINT}/{id}/transform-to-invoice")
        return Document.model_validate(resp.json())

    def get_next_quote_batch(self) -> object:
        """Récupère le prochain numéro de lot pour un devis."""
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
        """Liste les documents avec sélection de champs."""
        params = _clean({"page": page, "limit": limit, "fields": fields, **kwargs})
        resp = self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/with-selected-fields", params=params)
        return PagedListResponse[Document].model_validate(resp.json())

