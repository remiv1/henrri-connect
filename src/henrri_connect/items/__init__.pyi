"""Stubs de type pour le module items de henrri-connect."""
from __future__ import annotations

from typing import Any

from ..models import Item, PagedListResponse

class SyncItemsClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    def list_items( # pylint: disable=C0116, W0613
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
    def add(self, item: Item) -> Item: ...  # pylint: disable=C0116, W0613
    def get(self, item_id: int) -> Item: ... # pylint: disable=C0116, W0613
    def modify(self, item_id: int, item: Item) -> Item: ...  # pylint: disable=C0116, W0613
    def delete(self, item_id: int) -> None: ...  # pylint: disable=C0116, W0613
    def get_most_used(  # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
    ) -> PagedListResponse[Item]: ...
    def get_best_sales( # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
    ) -> PagedListResponse[Item]: ...
    def list_with_selected_fields(  # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        fields: str | None = ...,
    ) -> PagedListResponse[Item]: ...

class AsyncItemsClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    async def list_items(   # pylint: disable=C0116, W0613
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
    async def add(self, item: Item) -> Item: ...    # pylint: disable=C0116, W0613
    async def get(self, item_id: int) -> Item: ...   # pylint: disable=C0116, W0613
    async def modify(self, item_id: int, item: Item) -> Item: ...    # pylint: disable=C0116, W0613
    async def delete(self, item_id: int) -> None: ...    # pylint: disable=C0116, W0613
    async def get_most_used(    # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
    ) -> PagedListResponse[Item]: ...
    async def get_best_sales(   # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
    ) -> PagedListResponse[Item]: ...
    async def list_with_selected_fields(    # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        fields: str | None = ...,
    ) -> PagedListResponse[Item]: ...
