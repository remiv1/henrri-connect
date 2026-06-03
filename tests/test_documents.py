"""Tests du sous-client documents (synchrone et asynchrone)."""

from __future__ import annotations

from typing import Any

from unittest.mock import AsyncMock, MagicMock

import pytest   # type: ignore[import]

from src.henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient,  # type: ignore[import]
)
from src.henrri_connect.models import Document, ValidateDocumentRequest
from tests.conftest import DOCUMENT_JSON, PAGED_META, make_response


def _paged(elements: list[Any]) -> dict[str, Any]:
    return {"elements": elements, "meta": PAGED_META}


class TestSyncDocuments:
    def test_list_retourne_documents(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(_paged([DOCUMENT_JSON]))

        result = sync_client.documents.list_documents()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].id == 100

    def test_list_passe_les_filtres(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(_paged([]))

        sync_client.documents.list_documents(customer_id=5, document_type_id=1, state="Pending")

        _, kwargs = mock_http.request.call_args
        params = kwargs["params"]
        assert params["customerId"] == 5
        assert params["documentTypeId"] == 1
        assert params["state"] == "Pending"

    def test_add_cree_document(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({**DOCUMENT_JSON, "id": 200})
        doc = Document(document_type_id=1)  # type: ignore[call-arg]

        result = sync_client.documents.add(doc)

        assert result.id == 200
        assert mock_http.request.call_args.args[0] == "POST"

    def test_get_retourne_document(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(DOCUMENT_JSON)

        result = sync_client.documents.get(100)

        assert result.id == 100
        assert "/v1/documents/100" in mock_http.request.call_args.args[1]

    def test_modify_met_a_jour(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        updated: dict[str, Any] = {**DOCUMENT_JSON, "title": "Facture modifiée"}
        mock_http.request.return_value = make_response(updated)

        result = sync_client.documents.modify(100, Document(document_type_id=1))  # type: ignore[call-arg]

        assert result.title == "Facture modifiée"
        assert mock_http.request.call_args.args[0] == "PUT"

    def test_delete(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({})

        sync_client.documents.delete(100)

        assert mock_http.request.call_args.args[0] == "DELETE"

    def test_get_tax_details(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(
            {"taxDetailArray": [{"rate": 20.0, "priceBeforeTax": 100.0, "taxAmount": 20.0, "priceAfterTax": 120.0}]}
        )

        result = sync_client.documents.get_tax_details(100)

        assert result.tax_detail_array is not None
        assert len(result.tax_detail_array) == 1
        assert result.tax_detail_array[0].rate == pytest.approx(20.0)  # type: ignore[misc]

    def test_validate_document(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({**DOCUMENT_JSON, "validated": True})
        req = ValidateDocumentRequest(
            email="sign@example.com",
            first_name="Jean",
            last_name="Dupont",
            validation_date="2025-01-01",
            time_offset=60,
            ip="127.0.0.1",
        )

        result = sync_client.documents.validate(100, req)

        assert result.validated is True
        assert mock_http.request.call_args.args[0] == "POST"
        assert "/v1/documents/100/validate" in mock_http.request.call_args.args[1]

    def test_get_pdf_url(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(
            {"downloadUrl": "https://cdn.example.com/facture.pdf", "fileName": "facture.pdf"}
        )

        result = sync_client.documents.get_pdf_url(100)

        assert result.download_url == "https://cdn.example.com/facture.pdf"

    def test_get_pdf_bytes(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        pdf_bytes = b"%PDF-1.4 test"
        mock_http.request.return_value = make_response({}, content=pdf_bytes)

        result = sync_client.documents.get_pdf_bytes(100)

        assert result == pdf_bytes

    def test_finalize(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({**DOCUMENT_JSON, "finalized": True})

        result = sync_client.documents.finalize(100)

        assert result.finalized is True
        assert "/v1/documents/100/finalize" in mock_http.request.call_args.args[1]

    def test_transform_to_invoice(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({**DOCUMENT_JSON, "id": 101})

        result = sync_client.documents.transform_to_invoice(100)

        assert result.id == 101
        assert "/transform-to-invoice" in mock_http.request.call_args.args[1]

    def test_get_payment_milestones(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        milestone: dict[str, Any] = {
            "id": 1,
            "dueDate": "2025-06-30T00:00:00",
            "isPaid": False,
            "documentId": 100,
        }
        mock_http.request.return_value = make_response({"elements": [milestone]})

        result = sync_client.documents.get_payment_milestones(100)

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].document_id == 100

    def test_get_with_all(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(DOCUMENT_JSON)

        result = sync_client.documents.get_with_all(100)

        assert result.id == 100
        assert "/with-all" in mock_http.request.call_args.args[1]


class TestAsyncDocuments:
    async def test_list_retourne_documents(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response(_paged([DOCUMENT_JSON]))

        result = await async_client.documents.list()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].id == 100

    async def test_get_retourne_document(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response(DOCUMENT_JSON)

        result = await async_client.documents.get(100)

        assert result.id == 100

    async def test_finalize(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response({**DOCUMENT_JSON, "finalized": True})

        result = await async_client.documents.finalize(100)

        assert result.finalized is True

    async def test_get_pdf_bytes(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        pdf_bytes = b"%PDF-1.4 async"
        mock_async_http.request.return_value = make_response({}, content=pdf_bytes)

        result = await async_client.documents.get_pdf_bytes(100)

        assert result == pdf_bytes
