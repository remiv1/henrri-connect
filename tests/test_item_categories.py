"""Tests du sous-client item_categories (synchrone et asynchrone)."""

from __future__ import annotations

from typing import Any

from unittest.mock import AsyncMock, MagicMock

from src.henrri_connect.connect import (
    _AsyncHenrriClient, _SyncHenrriClient   # type: ignore[import]
)
from tests.conftest import ITEM_CATEGORY_JSON, PAGED_META, make_response


def _paged(elements: list[Any]) -> dict[str, Any]:
    return {"elements": elements, "meta": PAGED_META}


class TestSyncItemCategories:
    def test_list_retourne_categories(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(_paged([ITEM_CATEGORY_JSON]))

        result = sync_client.item_categories.list_item_categories()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].label == "Services"
        assert "/v1/itemcategories" in mock_http.request.call_args.args[1]

    def test_list_passe_les_filtres(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(_paged([]))

        sync_client.item_categories.list_item_categories(search="service", page=2, limit=10)

        _, kwargs = mock_http.request.call_args
        params = kwargs["params"]
        assert params["search"] == "service"
        assert params["page"] == 2

    def test_list_exclut_params_none(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(_paged([]))

        sync_client.item_categories.list_item_categories()

        _, kwargs = mock_http.request.call_args
        assert "search" not in kwargs["params"]


class TestAsyncItemCategories:
    async def test_list_retourne_categories(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response(_paged([ITEM_CATEGORY_JSON]))

        result = await async_client.item_categories.list_item_categories()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].label == "Services"
