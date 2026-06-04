"""Stubs de type pour le module items de henrri-connect."""
from __future__ import annotations

from typing import Any, overload, Optional

from ..models import Item, PagedListResponse, ItemsQuery

class SyncItemsClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    @overload
    def list_items(
        self,
        *,
        request: ItemsQuery,
        with_selected_fields: bool = True,
        with_totals: bool = False,
        only_current_page: bool = True
    ) -> PagedListResponse[Item]:...
    @overload
    def list_items(
        self,
        *,
        request: ItemsQuery,
        with_selected_fields: bool = False,
        with_totals: None = None,
        only_current_page: None = None,
    ) -> PagedListResponse[Item]:...
    def list_items(    # pylint: disable=C0116, W0613
            self,
            *,
            request: ItemsQuery,
            with_selected_fields: bool = True,
            with_totals: Optional[bool] = False,
            only_current_page: Optional[bool] = True
        ) -> PagedListResponse[Item]:...
    def add(self, item: Item) -> Item: ...  # pylint: disable=C0116, W0613
    def get(self, item_id: int) -> Item: ... # pylint: disable=C0116, W0613
    def modify(self, item_id: int, item: Item) -> Item: ...  # pylint: disable=C0116, W0613
    def delete(self, item_id: int) -> None: ...  # pylint: disable=C0116, W0613
    def get_most_used(self) -> PagedListResponse[Item]: ...  # pylint: disable=C0116
    def get_best_sales(self, *, year: int) -> PagedListResponse[Item]: ... # pylint: disable=C0116, W0613

class AsyncItemsClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    @overload
    async def list_items(
        self,
        *,
        request: ItemsQuery,
        with_selected_fields: bool = True,
        with_totals: bool = False,
        only_current_page: bool = True
    ) -> PagedListResponse[Item]:...
    @overload
    async def list_items(
        self,
        *,
        request: ItemsQuery,
        with_selected_fields: bool = False,
        with_totals: None = None,
        only_current_page: None = None,
    ) -> PagedListResponse[Item]:...
    async def list_items(    # pylint: disable=C0116, W0613
            self,
            *,
            request: ItemsQuery,
            with_selected_fields: bool = True,
            with_totals: Optional[bool] = False,
            only_current_page: Optional[bool] = True
        ) -> PagedListResponse[Item]:...
    async def add(self, item: Item) -> Item: ...    # pylint: disable=C0116, W0613
    async def get(self, item_id: int) -> Item: ...   # pylint: disable=C0116, W0613
    async def modify(self, item_id: int, item: Item) -> Item: ...    # pylint: disable=C0116, W0613
    async def delete(self, item_id: int) -> None: ...    # pylint: disable=C0116, W0613
    async def get_most_used(self) -> PagedListResponse[Item]: ...  # pylint: disable=C0116
    async def get_best_sales(self, *, year: int) -> PagedListResponse[Item]: ... # pylint: disable=C0116, W0613
