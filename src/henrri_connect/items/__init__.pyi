from __future__ import annotations

from typing import Any

from ..models import Item, PagedListResponse

class SyncItemsClient:
    def __init__(self, client: Any) -> None: ...
    def list_items(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
        item_category_id: int | None = ...,
        min_id: int | None = ...,
    ) -> PagedListResponse[Item]: ...
    def add(self, item: Item) -> Item: ...
    def get(self, id: int) -> Item: ...
    def modify(self, id: int, item: Item) -> Item: ...
    def delete(self, id: int) -> None: ...
    def get_most_used(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
    ) -> PagedListResponse[Item]: ...
    def get_best_sales(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
    ) -> PagedListResponse[Item]: ...
    def list_with_selected_fields(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        fields: str | None = ...,
    ) -> PagedListResponse[Item]: ...

class AsyncItemsClient:
    def __init__(self, client: Any) -> None: ...
    async def list_items(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
        item_category_id: int | None = ...,
        min_id: int | None = ...,
    ) -> PagedListResponse[Item]: ...
    async def add(self, item: Item) -> Item: ...
    async def get(self, id: int) -> Item: ...
    async def modify(self, id: int, item: Item) -> Item: ...
    async def delete(self, id: int) -> None: ...
    async def get_most_used(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
    ) -> PagedListResponse[Item]: ...
    async def get_best_sales(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
    ) -> PagedListResponse[Item]: ...
    async def list_with_selected_fields(
        self,
        *,
        page: int = ...,
        limit: int = ...,
        fields: str | None = ...,
    ) -> PagedListResponse[Item]: ...
