"""Sous-client pour les endpoints /v1/itemcategories."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models import ItemCategory, PagedListResponse

if TYPE_CHECKING:
    from ..connect import (
        _AsyncHenrriClient,   # type: ignore[import]
    )

ITEMCATEGORIES_ENDPOINT = "/v1/itemcategories"

def _clean(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


class AsyncItemCategoriesClient:
    """Accès asynchrone aux catégories d'articles."""

    def __init__(self, client: _AsyncHenrriClient) -> None:
        self._c = client

    async def list_item_categories(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
    ) -> PagedListResponse[ItemCategory]:
        """Liste les catégories d'articles avec pagination."""
        params = _clean({
            "page": page,
            "limit": limit,
            "search": search,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        })
        resp = await self._c.request("GET", ITEMCATEGORIES_ENDPOINT, params=params)
        return PagedListResponse[ItemCategory].model_validate(resp.json())
