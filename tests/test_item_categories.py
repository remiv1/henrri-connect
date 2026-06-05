"""Tests du sous-client item_categories (synchrone et asynchrone)."""

from __future__ import annotations

from typing import Any

from unittest.mock import AsyncMock, MagicMock

from henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient   # type: ignore[import]
)
from henrri_connect.models import ItemCategoryRequest
from tests.conftest import ITEM_CATEGORY_JSON, PAGED_META, make_response


def _paged(elements: list[Any]) -> dict[str, Any]:
    return {"elements": elements, "meta": PAGED_META}


class TestSyncItemCategories:
    """Tests du sous-client item_categories (synchrone)."""
    def test_list_retourne_categories(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode list_item_categories()."""
        mock_http.request.return_value = make_response(_paged([ITEM_CATEGORY_JSON]))

        result = sync_client.item_categories.list_item_categories(
            request=ItemCategoryRequest(search="", page=1, limit=50)
        )

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].label == "Services"
        assert "/v1/itemcategories" in mock_http.request.call_args.args[1]

    def test_list_passe_les_filtres(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode list_item_categories()."""
        mock_http.request.return_value = make_response(_paged([]))

        sync_client.item_categories.list_item_categories(
            request=ItemCategoryRequest(
                search="service",
                page=2,
                limit=10
            )
        )

        _, kwargs = mock_http.request.call_args
        params = kwargs["params"]
        assert params["search"] == "service"
        assert params["page"] == 2

    def test_list_exclut_params_none(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode list_item_categories()."""
        mock_http.request.return_value = make_response(_paged([]))

        sync_client.item_categories.list_item_categories(
            request=ItemCategoryRequest(
                search="",
                page=1,
                limit=50
            )
        )

        _, kwargs = mock_http.request.call_args
        params = kwargs["params"]
        assert params["search"] == ""


class TestAsyncItemCategories:
    """Tests du sous-client item_categories (asynchrone)."""
    async def test_list_retourne_categories(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode list_item_categories()."""
        mock_async_http.request.return_value = make_response(_paged([ITEM_CATEGORY_JSON]))

        result = await async_client.item_categories.list_item_categories(
            request=ItemCategoryRequest(
                search="",
                page=1,
                limit=50
            )
        )

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].label == "Services"
