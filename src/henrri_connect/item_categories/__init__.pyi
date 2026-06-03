"""Stubs de type pour le module item_categories de henrri-connect."""
from __future__ import annotations

from typing import Any

from ..models import ItemCategory, PagedListResponse

class SyncItemCategoriesClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    def list_item_categories(   # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
    ) -> PagedListResponse[ItemCategory]: ...

class AsyncItemCategoriesClient:    # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    async def list_item_categories( # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
    ) -> PagedListResponse[ItemCategory]: ...
