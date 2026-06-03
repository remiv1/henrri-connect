"""Stubs pour les clients de l'API Documents."""
from __future__ import annotations

from typing import Any

from ..models import (
    Document,
    ListResponse,
    PagedListResponse,
    PaymentMilestone,
    PdfUrlResponse,
    TaxDetailArray,
    ValidateDocumentRequest,
)

class SyncDocumentsClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    def list_documents( # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
        document_type_id: int | None = ...,
        customer_id: int | None = ...,
        state: str | None = ...,
        from_date: str | None = ...,
        to_date: str | None = ...,
        min_id: int | None = ...,
    ) -> PagedListResponse[Document]: ...
    def add(self, document: Document) -> Document: ...  # pylint: disable=C0116, W0613
    def get(self, doc_id: int) -> Document: ... # pylint: disable=C0116, W0613
    def get_with_all(self, doc_id: int) -> Document: ...    # pylint: disable=C0116, W0613
    def get_all_included(self, doc_id: int) -> Document: ...    # pylint: disable=C0116, W0613
    def modify(self, doc_id: int, document: Document) -> Document: ...  # pylint: disable=C0116, W0613
    def delete(self, doc_id: int) -> None: ...  # pylint: disable=C0116, W0613
    def get_tax_details(self, doc_id: int) -> TaxDetailArray: ...   # pylint: disable=C0116, W0613
    def validate(self, doc_id: int, request: ValidateDocumentRequest) -> Document: ...  # pylint: disable=C0116, W0613
    def get_pdf_url(self, doc_id: int) -> PdfUrlResponse: ...   # pylint: disable=C0116, W0613
    def get_pdf_bytes(self, doc_id: int) -> bytes: ...  # pylint: disable=C0116, W0613
    def get_pdf_file(self, doc_id: int, guid: str) -> bytes: ...    # pylint: disable=C0116, W0613
    def get_display(self, doc_id: int) -> Document: ... # pylint: disable=C0116, W0613
    def get_payment_milestones(self, doc_id: int) -> ListResponse[PaymentMilestone]: ...   # pylint: disable=C0116, W0613
    def finalize(self, doc_id: int) -> Document: ...    # pylint: disable=C0116, W0613
    def transform_to_invoice(self, doc_id: int) -> Document: ...    # pylint: disable=C0116, W0613
    def get_next_quote_batch(self) -> object: ...   # pylint: disable=C0116
    def list_with_selected_fields(  # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        fields: str | None = ...,
        **kwargs: object,
    ) -> PagedListResponse[Document]: ...

class AsyncDocumentsClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    async def list_documents( # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
        document_type_id: int | None = ...,
        customer_id: int | None = ...,
        state: str | None = ...,
        from_date: str | None = ...,
        to_date: str | None = ...,
        min_id: int | None = ...,
    ) -> PagedListResponse[Document]: ...
    async def add(self, document: Document) -> Document: ...    # pylint: disable=C0116, W0613
    async def get(self, doc_id: int) -> Document: ...   # pylint: disable=C0116, W0613
    async def get_with_all(self, doc_id: int) -> Document: ...  # pylint: disable=C0116, W0613
    async def get_all_included(self, doc_id: int) -> Document: ...  # pylint: disable=C0116, W0613
    async def modify(self, doc_id: int, document: Document) -> Document: ...    # pylint: disable=C0116, W0613
    async def delete(self, doc_id: int) -> None: ...    # pylint: disable=C0116, W0613
    async def get_tax_details(self, doc_id: int) -> TaxDetailArray: ... # pylint: disable=C0116, W0613
    async def validate(self, doc_id: int, request: ValidateDocumentRequest) -> Document: ...    # pylint: disable=C0116, W0613
    async def get_pdf_url(self, doc_id: int) -> PdfUrlResponse: ... # pylint: disable=C0116, W0613
    async def get_pdf_bytes(self, doc_id: int) -> bytes: ...    # pylint: disable=C0116, W0613
    async def get_pdf_file(self, doc_id: int, guid: str) -> bytes: ...  # pylint: disable=C0116, W0613
    async def get_display(self, doc_id: int) -> Document: ...   # pylint: disable=C0116, W0613
    async def get_payment_milestones(self, doc_id: int) -> ListResponse[PaymentMilestone]: ... # pylint: disable=C0116, W0613
    async def finalize(self, doc_id: int) -> Document: ...  # pylint: disable=C0116, W0613
    async def transform_to_invoice(self, doc_id: int) -> Document: ...  # pylint: disable=C0116, W0613
    async def get_next_quote_batch(self) -> object: ... # pylint: disable=C0116
    async def list_with_selected_fields(    # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        fields: str | None = ...,
        **kwargs: object,
    ) -> PagedListResponse[Document]: ...
