"""Sous-client pour les endpoints /v1/documents."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models import (
    Document,
    ListResponse,
    PagedListResponse,
    PaymentMilestone,
    PdfUrlResponse,
    TaxDetailArray,
    ValidateDocumentRequest,
)

if TYPE_CHECKING:
    from ..connect import (
        AsyncHenrriClient,
    )

DOCUMENTS_ENDPOINT = "/v1/documents"

def _clean(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


class AsyncDocumentsClient:
    """Accès asynchrone aux endpoints documents."""

    def __init__(self, client: AsyncHenrriClient) -> None:
        self._c = client

    async def list(
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
        """Liste les documents avec pagination et filtres optionnels."""
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
        resp = await self._c.request("GET", DOCUMENTS_ENDPOINT, params=params)
        return PagedListResponse[Document].model_validate(resp.json())

    async def add(self, document: Document) -> Document:
        """Crée un nouveau document."""
        resp = await self._c.request(
            "POST",
            DOCUMENTS_ENDPOINT,
            json=document.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Document.model_validate(resp.json())

    async def get(self, doc_id: int) -> Document:
        """Récupère un document par son identifiant."""
        resp = await self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}")
        return Document.model_validate(resp.json())

    async def get_with_all(self, doc_id: int) -> Document:
        """Récupère un document avec toutes ses relations incluses."""
        resp = await self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/with-all")
        return Document.model_validate(resp.json())

    async def get_all_included(self, doc_id: int) -> Document:
        """Récupère un document avec toutes ses données incluses."""
        resp = await self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/all-included")
        return Document.model_validate(resp.json())

    async def modify(self, doc_id: int, document: Document) -> Document:
        """Met à jour un document existant."""
        resp = await self._c.request(
            "PUT",
            f"{DOCUMENTS_ENDPOINT}/{doc_id}",
            json=document.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Document.model_validate(resp.json())

    async def delete(self, doc_id: int) -> None:
        """Supprime un document."""
        await self._c.request("DELETE", f"{DOCUMENTS_ENDPOINT}/{doc_id}")

    async def get_tax_details(self, doc_id: int) -> TaxDetailArray:
        """Récupère le détail des taxes d'un document."""
        resp = await self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/tax-details")
        return TaxDetailArray.model_validate(resp.json())

    async def validate(self, doc_id: int, request: ValidateDocumentRequest) -> Document:
        """Valide électroniquement un document."""
        resp = await self._c.request(
            "POST",
            f"{DOCUMENTS_ENDPOINT}/{doc_id}/validate",
            json=request.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Document.model_validate(resp.json())

    async def get_pdf_url(self, doc_id: int) -> PdfUrlResponse:
        """Génère une URL de téléchargement pour le PDF d'un document."""
        resp = await self._c.request("POST", f"{DOCUMENTS_ENDPOINT}/{doc_id}/pdf/url")
        return PdfUrlResponse.model_validate(resp.json())

    async def get_pdf_bytes(self, doc_id: int) -> bytes:
        """Télécharge le PDF d'un document (retourne les octets bruts)."""
        resp = await self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/pdf")
        return resp.content

    async def get_pdf_file(self, doc_id: int, guid: str) -> bytes:
        """Télécharge un fichier PDF identifié par son GUID."""
        resp = await self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/pdf/files/{guid}")
        return resp.content

    async def get_display(self, doc_id: int) -> Document:
        """Récupère les données d'affichage d'un document."""
        resp = await self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/display")
        return Document.model_validate(resp.json())

    async def get_payment_milestones(self, doc_id: int) -> ListResponse[PaymentMilestone]:
        """Récupère les jalons de paiement d'un document."""
        resp = await self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/{doc_id}/paymentmilestones")
        return ListResponse[PaymentMilestone].model_validate(resp.json())

    async def finalize(self, doc_id: int) -> Document:
        """Finalise un document."""
        resp = await self._c.request("POST", f"{DOCUMENTS_ENDPOINT}/{doc_id}/finalize")
        return Document.model_validate(resp.json())

    async def transform_to_invoice(self, doc_id: int) -> Document:
        """Transforme un document (devis, bon de livraison…) en facture."""
        resp = await self._c.request("POST", f"{DOCUMENTS_ENDPOINT}/{doc_id}/transform-to-invoice")
        return Document.model_validate(resp.json())

    async def get_next_quote_batch(self) -> object:
        """Récupère le prochain numéro de lot pour un devis."""
        resp = await self._c.request("GET", f"{DOCUMENTS_ENDPOINT}/next-quote-batch")
        return resp.json()

    async def list_with_selected_fields(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        fields: str | None = None,
        **kwargs: object,
    ) -> PagedListResponse[Document]:
        """Liste les documents avec sélection de champs."""
        params = _clean({"page": page, "limit": limit, "fields": fields, **kwargs})
        resp = await self._c.request(
            "GET",
            f"{DOCUMENTS_ENDPOINT}/with-selected-fields",
            params=params
        )
        return PagedListResponse[Document].model_validate(resp.json())
