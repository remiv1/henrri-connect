"""Stub pour le module customers."""
from __future__ import annotations

from typing import Any

from ..models import Address, Contact, Customer, PagedListResponse

class SyncCustomersClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...  # pylint: disable=W0613
    def list_customers( # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
        min_id: int | None = ...,
        from_date: str | None = ...,
        to_date: str | None = ...,
    ) -> PagedListResponse[Customer]: ...
    def add(self, customer: Customer) -> Customer: ...  # pylint: disable=C0116, W0613
    def get_best_sales(  # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
    ) -> PagedListResponse[Customer]: ...
    def get(self, customer_id: int) -> Customer: ...  # pylint: disable=C0116, W0613
    def modify(self, customer_id: int, customer: Customer) -> Customer: ...  # pylint: disable=C0116, W0613
    def delete(self, customer_id: int) -> None: ...  # pylint: disable=C0116, W0613
    def get_address(self, customer_id: int) -> Address: ...  # pylint: disable=C0116, W0613
    def list_contacts(self, customer_id: int) -> list[Contact]: ...  # pylint: disable=C0116, W0613
    def add_contact(self, customer_id: int, contact: Contact) -> Contact: ...  # pylint: disable=C0116, W0613
    def get_contact(self, customer_id: int, contact_id: int) -> Contact: ...  # pylint: disable=C0116, W0613
    def modify_contact(self, customer_id: int, contact_id: int, contact: Contact) -> Contact: ...  # pylint: disable=C0116, W0613
    def delete_contact(self, customer_id: int, contact_id: int) -> None: ... # pylint: disable=C0116, W0613

class AsyncCustomersClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ... # pylint: disable=W0613
    async def list_customers( # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
        min_id: int | None = ...,
        from_date: str | None = ...,
        to_date: str | None = ...,
    ) -> PagedListResponse[Customer]: ...
    async def add(self, customer: Customer) -> Customer: ... # pylint: disable=C0116, W0613
    async def get_best_sales( # pylint: disable=C0116, W0613
        self,
        *,
        page: int = ...,
        limit: int = ...,
        search: str | None = ...,
        sort_by: str | None = ...,
        sort_order: str | None = ...,
    ) -> PagedListResponse[Customer]: ...
    async def get(self, customer_id: int) -> Customer: ... # pylint: disable=C0116, W0613
    async def modify(self, customer_id: int, customer: Customer) -> Customer: ... # pylint: disable=C0116, W0613
    async def delete(self, customer_id: int) -> None: ... # pylint: disable=C0116, W0613
    async def get_address(self, customer_id: int) -> Address: ... # pylint: disable=C0116, W0613
    async def list_contacts(self, customer_id: int) -> list[Contact]: ... # pylint: disable=C0116, W0613
    async def add_contact(self, customer_id: int, contact: Contact) -> Contact: ... # pylint: disable=C0116, W0613
    async def get_contact(self, customer_id: int, contact_id: int) -> Contact: ... # pylint: disable=C0116, W0613
    async def modify_contact( # pylint: disable=C0116, W0613
        self, customer_id: int, contact_id: int, contact: Contact
    ) -> Contact: ...
    async def delete_contact(self, customer_id: int, contact_id: int) -> None: ... # pylint: disable=C0116, W0613
