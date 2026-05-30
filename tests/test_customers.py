"""Tests du sous-client customers (synchrone et asynchrone)."""

from __future__ import annotations

from typing import Any

from unittest.mock import AsyncMock, MagicMock

import pytest   # type: ignore[import]

from src.henrri_connect.connect import (
    _AsyncHenrriClient, _SyncHenrriClient,  # type: ignore[import]
)
from src.henrri_connect.models import Contact, Customer
from tests.conftest import CUSTOMER_JSON, PAGED_META, make_response


def _paged(elements: list[Any]) -> dict[str, Any]:
    return {"elements": elements, "meta": PAGED_META}


class TestSyncCustomers:
    def test_list_retourne_clients(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(_paged([CUSTOMER_JSON]))

        result = sync_client.customers.list_customers(page=1, limit=50)

        assert len(result.elements or []) == 1
        assert (result.elements[0].name if result.elements else None) == "Acme Corp"
        assert (result.meta.total_count if result.meta else 0) == 1

    def test_list_passe_les_filtres(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(_paged([]))

        sync_client.customers.list_customers(search="acme", page=2, limit=10)

        _, kwargs = mock_http.request.call_args
        params = kwargs["params"]
        assert params["search"] == "acme"
        assert params["page"] == 2
        assert params["limit"] == 10

    def test_list_exclut_params_none(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(_paged([]))

        sync_client.customers.list_customers()

        _, kwargs = mock_http.request.call_args
        params = kwargs["params"]
        assert "search" not in params
        assert "sortBy" not in params

    def test_add_cree_client(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({**CUSTOMER_JSON, "id": 99})
        customer = Customer(name="Nouveau", type="Company")

        result = sync_client.customers.add(customer)

        assert result.id == 99
        args = mock_http.request.call_args
        assert args.args[0] == "POST"

    def test_get_retourne_client(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(CUSTOMER_JSON)

        result = sync_client.customers.get(1)

        assert result.id == 1
        assert "/v1/customers/1" in mock_http.request.call_args.args[1]

    def test_modify_met_a_jour(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        updated = {**CUSTOMER_JSON, "name": "Acme Updated"}
        mock_http.request.return_value = make_response(updated)
        customer = Customer(name="Acme Updated", type="Company")

        result = sync_client.customers.modify(1, customer)

        assert result.name == "Acme Updated"
        assert mock_http.request.call_args.args[0] == "PUT"

    def test_delete_envoie_delete(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({})

        sync_client.customers.delete(1)

        assert mock_http.request.call_args.args[0] == "DELETE"
        assert "/v1/customers/1" in mock_http.request.call_args.args[1]

    def test_get_best_sales(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(_paged([CUSTOMER_JSON]))

        result = sync_client.customers.get_best_sales()

        assert len(result.elements) == 1
        assert "/customers/best-sales" in mock_http.request.call_args.args[1]

    def test_get_address(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(
            {"id": 5, "city": "Paris", "isPostCodeShared": False}
        )

        address = sync_client.customers.get_address(1)

        assert address.city == "Paris"
        assert "/v1/customers/1/address" in mock_http.request.call_args.args[1]

    def test_list_contacts(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        contact_json = {"id": 1, "firstName": "Alice", "isPrimary": True, "showOnDocument": False}
        mock_http.request.return_value = make_response([contact_json])

        contacts = sync_client.customers.list_contacts(1)

        assert len(contacts) == 1
        assert contacts[0].first_name == "Alice"

    def test_add_contact(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        contact_json = {"id": 2, "firstName": "Bob", "isPrimary": False, "showOnDocument": False}
        mock_http.request.return_value = make_response(contact_json)
        contact = Contact()

        result = sync_client.customers.add_contact(1, contact)

        assert result.id == 2
        assert mock_http.request.call_args.args[0] == "POST"

    def test_delete_contact(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({})

        sync_client.customers.delete_contact(1, 2)

        assert mock_http.request.call_args.args[0] == "DELETE"
        assert "/contacts/2" in mock_http.request.call_args.args[1]


class TestAsyncCustomers:
    async def test_list_retourne_clients(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response(_paged([CUSTOMER_JSON]))

        result = await async_client.customers.list_customers()

        assert len(result.elements) == 1
        assert result.elements[0].name == "Acme Corp"

    async def test_get_retourne_client(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response(CUSTOMER_JSON)

        result = await async_client.customers.get(1)

        assert result.id == 1

    async def test_add_cree_client(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response({**CUSTOMER_JSON, "id": 88})
        customer = Customer(name="Async Corp", type="Company")

        result = await async_client.customers.add(customer)

        assert result.id == 88

    async def test_delete_envoie_delete(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response({})

        await async_client.customers.delete(1)

        assert mock_async_http.request.call_args.args[0] == "DELETE"
