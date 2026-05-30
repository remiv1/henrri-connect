from __future__ import annotations

from typing import Any

from ..models import ItemCategory, PagedListResponse

class SyncItemCategoriesClient:
    def __init__(self, client: Any) -> None: ...
    def list_item_categories(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
    ) -> PagedListResponse[ItemCategory]: ...

class AsyncItemCategoriesClient:
    def __init__(self, client: Any) -> None: ...
    async def list_item_categories(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
    ) -> PagedListResponse[ItemCategory]: ...
