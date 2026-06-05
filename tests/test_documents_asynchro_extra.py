"""Tests de la sous-cliente documents (asynchrone)."""
from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock

import pytest   # pylint: disable=W0611

from henrri_connect.models import Document, PdfUrlResponse
from tests.conftest import DOCUMENT_JSON, PAGED_META, make_response


def _paged(elements: list[Any]) -> dict[str, Any]:
    return {"elements": elements, "meta": PAGED_META}


class TestAsyncDocumentsExtra:
    """Tests de la sous-cliente documents (asynchrone)."""
    async def test_add_and_modify_and_get_with_all(
        self, async_client, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode add()."""
        mock_async_http.request.return_value = make_response({**DOCUMENT_JSON, "id": 200})
        doc = Document(
            document_type_id=1,
            customer_id=1,
            finalized=True,
            price_before_tax=10.0,
            price_after_tax=12.0,
            tax_amount=20.0,
            validated=True,
            user_can_validate=True,
            )

        res = await async_client.documents.add(doc)
        assert res.id == 200

        mock_async_http.request.return_value = make_response({**DOCUMENT_JSON, "title": "t"})
        res2 = await async_client.documents.modify(
            100,
            Document(
                document_type_id=1,
                customer_id=1,
                finalized=True,
                price_before_tax=10.0,
                price_after_tax=12.0,
                tax_amount=20.0,
                validated=True,
                user_can_validate=True,
            )
        )
        assert res2.title == "t"

        mock_async_http.request.return_value = make_response(DOCUMENT_JSON)
        res3 = await async_client.documents.get_with_all(100)
        assert res3.id == 100

    async def test_pdf_endpoints(self, async_client, mock_async_http: AsyncMock) -> None:
        """Test de la méthode get_pdf_url()."""
        mock_async_http.request.return_value = make_response(
            {"downloadUrl": "u", "fileName": "f.pdf"}
        )
        url = await async_client.documents.get_pdf_url(100)
        assert isinstance(url, PdfUrlResponse)
        assert url.download_url == "u"

        pdf_bytes = b"%PDF-async"
        mock_async_http.request.return_value = make_response({}, content=pdf_bytes)
        got = await async_client.documents.get_pdf_bytes(100)
        assert got == pdf_bytes

        mock_async_http.request.return_value = make_response({}, content=pdf_bytes)
        got2 = await async_client.documents.get_pdf_file(100, "guid")
        assert got2 == pdf_bytes

    async def test_finalize_transform_payment_milestones_next_quote(
        self, async_client, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode finalize()."""
        mock_async_http.request.return_value = make_response({**DOCUMENT_JSON, "finalized": True})
        f = await async_client.documents.finalize(100)
        assert f.finalized is True

        mock_async_http.request.return_value = make_response({**DOCUMENT_JSON, "id": 101})
        t = await async_client.documents.transform_to_invoice(100)
        assert t.id == 101

        milestone = {"id": 1, "dueDate": "2025-06-30T00:00:00", "isPaid": False, "documentId": 100}
        mock_async_http.request.return_value = make_response({"elements": [milestone]})
        lst = await async_client.documents.get_payment_milestones(100)
        assert lst.elements and lst.elements[0].document_id == 100

        mock_async_http.request.return_value = make_response({"next": 5})
        nq = await async_client.documents.get_next_quote_batch()
        assert nq == {"next": 5}

    async def test_list_with_selected_fields(
            self,
            async_client,
            mock_async_http: AsyncMock
        ) -> None:
        """Test de la méthode list_with_selected_fields()."""
        mock_async_http.request.return_value = make_response(_paged([DOCUMENT_JSON]))
        res = await async_client.documents.list_with_selected_fields(
            page=2,
            limit=10,
            fields="id,title"
        )
        assert res.elements and len(res.elements) == 1
        _, kwargs = mock_async_http.request.call_args
        params = kwargs["params"]
        assert params["page"] == 2
        assert params["fields"] == "id,title"
