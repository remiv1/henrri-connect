"""Tests du sous-client items (synchrone et asynchrone)."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient, # type: ignore[import]
)
from henrri_connect.models import Item, ItemsQuery
from tests.conftest import ITEM_JSON, PAGED_META, make_response


def _paged(elements: list[Any]) -> dict[str, Any]:
    return {"elements": elements, "meta": PAGED_META}


class TestSyncItems:
    """Tests du sous-client items (synchrone)."""
    def test_list_retourne_articles(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode list_items()."""
        mock_http.request.return_value = make_response(_paged([ITEM_JSON]))

        result = sync_client.items.list_items(
            request=ItemsQuery(
                min_id=0,
                from_date="",
                to_date=""
            ),
            with_selected_fields=False
        )

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].id == 5
        assert result.elements[0].vat_percent == pytest.approx(20.0)  # type: ignore[misc]

    def test_list_passe_les_filtres(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode list_items()."""
        mock_http.request.return_value = make_response(_paged([]))

        sync_client.items.list_items(
            request=ItemsQuery(
                search="conseil",
                min_id=3,
                from_date="",
                to_date=""
            ),
            with_selected_fields=False
        )

        _, kwargs = mock_http.request.call_args
        params = kwargs["params"]
        assert params["search"] == "conseil"
        assert params["minId"] == 3

    def test_add_cree_article(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode add_item()."""
        mock_http.request.return_value = make_response({**ITEM_JSON, "id": 99})
        item = Item(vat_percent=20.0, creation_date="2025-01-01")  # type: ignore[call-arg]

        result = sync_client.items.add(item)

        assert result.id == 99
        assert mock_http.request.call_args.args[0] == "POST"

    def test_get_retourne_article(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode get_item()."""
        mock_http.request.return_value = make_response(ITEM_JSON)

        result = sync_client.items.get(5)

        assert result.id == 5
        assert "/v1/items/5" in mock_http.request.call_args.args[1]

    def test_modify_met_a_jour(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode modify_item()."""
        updated: dict[str, Any] = {**ITEM_JSON, "description": "Conseil modifié"}
        mock_http.request.return_value = make_response(updated)

        result = sync_client.items.modify(
            5,
            Item(  # type: ignore[call-arg]
                vat_percent=20.0,
                creation_date="2025-01-01"
            )
        )

        assert result.description == "Conseil modifié"
        assert mock_http.request.call_args.args[0] == "PUT"

    def test_delete_article(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode delete_item()."""
        mock_http.request.return_value = make_response({})

        sync_client.items.delete(5)

        assert mock_http.request.call_args.args[0] == "DELETE"
        assert "/v1/items/5" in mock_http.request.call_args.args[1]

    def test_get_most_used(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode get_most_used()."""
        mock_http.request.return_value = make_response(_paged([ITEM_JSON]))

        result = sync_client.items.get_most_used()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert "/items/most-used" in mock_http.request.call_args.args[1]

    def test_get_best_sales(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode get_best_sales()."""
        mock_http.request.return_value = make_response(_paged([ITEM_JSON]))

        result = sync_client.items.get_best_sales(year=2025)

        assert result.elements is not None
        assert len(result.elements) == 1
        assert "/with-selected-fields" in mock_http.request.call_args.args[1]


class TestAsyncItems:
    """Test de la classe AsyncItems."""
    async def test_list_retourne_articles(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode list_items()."""
        mock_async_http.request.return_value = make_response(_paged([ITEM_JSON]))

        result = await async_client.items.list_items(
            request=ItemsQuery(
                min_id=0,
                from_date="",
                to_date=""
            ),
            with_selected_fields=False
        )

        assert result.elements is not None
        assert len(result.elements) == 1

    async def test_get_retourne_article(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode get_item()."""
        mock_async_http.request.return_value = make_response(ITEM_JSON)

        result = await async_client.items.get(5)

        assert result.id == 5

    async def test_delete_article(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode delete_item()."""
        mock_async_http.request.return_value = make_response({})

        await async_client.items.delete(5)

        assert mock_async_http.request.call_args.args[0] == "DELETE"
