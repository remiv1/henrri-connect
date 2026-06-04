"""Tests de la sous-cliente customers (asynchrone)."""
from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock

import pytest   # pylint: disable=W0611

from src.henrri_connect.models import CustomerRequest
from tests.conftest import CUSTOMER_JSON, PAGED_META, make_response


def _paged(elements: list[Any]) -> dict[str, Any]:
    return {"elements": elements, "meta": PAGED_META}


class TestAsyncCustomersExtra:
    """Tests de la sous-cliente customers (asynchrone)."""
    async def test_list_and_filters(self, async_client, mock_async_http: AsyncMock) -> None:
        """Test de la méthode list_customers()."""
        mock_async_http.request.return_value = make_response(_paged([CUSTOMER_JSON]))

        res = await async_client.customers.list_customers(
            request=CustomerRequest(
                search="",
                from_date="",
                to_date=""
            ),
            with_selected_fields=False
        )
        assert res.elements and res.elements[0].id == CUSTOMER_JSON["id"]

        mock_async_http.request.return_value = make_response(_paged([]))
        await async_client.customers.list_customers(
            request=CustomerRequest(
                search="x",
                page=2,
                limit=10,
                from_date="",
                to_date=""
            ),
            with_selected_fields=False
        )
        _, kwargs = mock_async_http.request.call_args
        params = kwargs["params"]
        assert params["search"] == "x"
        assert params["page"] == 2

    async def test_best_sales_and_last_used_and_address(
            self,
            async_client,
            mock_async_http: AsyncMock
        ) -> None:
        """Test de la méthode list_customers()."""
        mock_async_http.request.return_value = make_response(_paged([CUSTOMER_JSON]))
        best = await async_client.customers.get_best_sales(year=2025)
        assert best.elements and len(best.elements) == 1

        mock_async_http.request.return_value = make_response(CUSTOMER_JSON)
        last = await async_client.customers.get_last_used("Company", 5)
        assert last.id == CUSTOMER_JSON["id"]

        mock_async_http.request.return_value = make_response(
            {
                "id": 5,
                "city": "Lyon",
                "isPostCodeShared": False
            }
        )
        addr = await async_client.customers.get_address(1)
        assert addr.city == "Lyon"

    async def test_contacts_crud(self, async_client, mock_async_http: AsyncMock) -> None:
        """Test de la méthode list_contacts()."""
        contact_json = {"id": 1, "firstName": "Alice", "isPrimary": True, "showOnDocument": False}
        mock_async_http.request.return_value = make_response([contact_json])
        contacts = await async_client.customers.list_contacts(1)
        assert len(contacts) == 1

        mock_async_http.request.return_value = make_response(contact_json)
        from src.henrri_connect.models import Contact   # pylint: disable=C0415
        c = Contact()
        added = await async_client.customers.add_contact(1, c)
        assert added.id == 1

        mock_async_http.request.return_value = make_response({})
        await async_client.customers.delete_contact(1, 2)
        assert mock_async_http.request.call_args is not None
