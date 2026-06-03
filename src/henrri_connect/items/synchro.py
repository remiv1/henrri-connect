"""Sous-client pour les endpoints /v1/items."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models import Item, PagedListResponse

if TYPE_CHECKING:
    from ..connect import (
        SyncHenrriClient,
    )

ITEMS_ENDPOINT = "/v1/items"

def _clean(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


class SyncItemsClient:
    """Accès synchrone aux endpoints articles."""

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def list_items(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        item_category_id: int | None = None,
        min_id: int | None = None,
    ) -> PagedListResponse[Item]:
        """Liste les articles avec pagination et filtres optionnels."""
        params = _clean({
            "page": page,
            "limit": limit,
            "search": search,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "itemCategoryId": item_category_id,
            "minId": min_id,
        })
        resp = self._c.request("GET", ITEMS_ENDPOINT, params=params)
        return PagedListResponse[Item].model_validate(resp.json())

    def add(self, item: Item) -> Item:
        """Crée un nouvel article."""
        resp = self._c.request(
            "POST",
            ITEMS_ENDPOINT,
            json=item.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Item.model_validate(resp.json())

    def get(self, item_id: int) -> Item:
        """Récupère un article par son identifiant."""
        resp = self._c.request("GET", f"{ITEMS_ENDPOINT}/{item_id}")
        return Item.model_validate(resp.json())

    def modify(self, item_id: int, item: Item) -> Item:
        """Met à jour un article existant."""
        resp = self._c.request(
            "PUT",
            f"{ITEMS_ENDPOINT}/{item_id}",
            json=item.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Item.model_validate(resp.json())

    def delete(self, item_id: int) -> None:
        """Supprime un article."""
        self._c.request("DELETE", f"{ITEMS_ENDPOINT}/{item_id}")

    def get_most_used(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
    ) -> PagedListResponse[Item]:
        """Récupère les articles les plus utilisés."""
        params = _clean({"page": page, "limit": limit, "search": search})
        resp = self._c.request("GET", f"{ITEMS_ENDPOINT}/most-used", params=params)
        return PagedListResponse[Item].model_validate(resp.json())

    def get_best_sales(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
    ) -> PagedListResponse[Item]:
        """Récupère les articles les plus vendus."""
        params = _clean({"page": page, "limit": limit, "search": search})
        resp = self._c.request("GET", f"{ITEMS_ENDPOINT}/best-sales", params=params)
        return PagedListResponse[Item].model_validate(resp.json())

    def list_with_selected_fields(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        fields: str | None = None,
    ) -> PagedListResponse[Item]:
        """Liste les articles avec sélection de champs."""
        params = _clean({"page": page, "limit": limit, "fields": fields})
        resp = self._c.request("GET", f"{ITEMS_ENDPOINT}/with-selected-fields", params=params)
        return PagedListResponse[Item].model_validate(resp.json())
