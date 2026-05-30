"""Sous-client pour les endpoints /v1/items."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models import Item, PagedListResponse

if TYPE_CHECKING:
    from ..connect import (
        _AsyncHenrriClient,  # type: ignore[import]
    )

ITEMS_ENDPOINT = "/v1/items"

def _clean(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


class AsyncItemsClient:
    """Accès asynchrone aux endpoints articles."""

    def __init__(self, client: _AsyncHenrriClient) -> None:
        self._c = client

    async def list_items(
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
        resp = await self._c.request("GET", ITEMS_ENDPOINT, params=params)
        return PagedListResponse[Item].model_validate(resp.json())

    async def add(self, item: Item) -> Item:
        """Crée un nouvel article."""
        resp = await self._c.request(
            "POST",
            ITEMS_ENDPOINT,
            json=item.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Item.model_validate(resp.json())

    async def get(self, id: int) -> Item:
        """Récupère un article par son identifiant."""
        resp = await self._c.request("GET", f"{ITEMS_ENDPOINT}/{id}")
        return Item.model_validate(resp.json())

    async def modify(self, id: int, item: Item) -> Item:
        """Met à jour un article existant."""
        resp = await self._c.request(
            "PUT",
            f"{ITEMS_ENDPOINT}/{id}",
            json=item.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Item.model_validate(resp.json())

    async def delete(self, id: int) -> None:
        """Supprime un article."""
        await self._c.request("DELETE", f"{ITEMS_ENDPOINT}/{id}")

    async def get_most_used(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
    ) -> PagedListResponse[Item]:
        """Récupère les articles les plus utilisés."""
        params = _clean({"page": page, "limit": limit, "search": search})
        resp = await self._c.request("GET", f"{ITEMS_ENDPOINT}/most-used", params=params)
        return PagedListResponse[Item].model_validate(resp.json())

    async def get_best_sales(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
    ) -> PagedListResponse[Item]:
        """Récupère les articles les plus vendus."""
        params = _clean({"page": page, "limit": limit, "search": search})
        resp = await self._c.request("GET", f"{ITEMS_ENDPOINT}/best-sales", params=params)
        return PagedListResponse[Item].model_validate(resp.json())

    async def list_with_selected_fields(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        fields: str | None = None,
    ) -> PagedListResponse[Item]:
        """Liste les articles avec sélection de champs."""
        params = _clean({"page": page, "limit": limit, "fields": fields})
        resp = await self._c.request("GET", f"{ITEMS_ENDPOINT}/with-selected-fields", params=params)
        return PagedListResponse[Item].model_validate(resp.json())
