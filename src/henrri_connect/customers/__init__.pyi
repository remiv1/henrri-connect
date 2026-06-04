"""Stub pour le module customers."""
from __future__ import annotations

from typing import Any, overload, Optional

from ..models import Address, Contact, Customer, PagedListResponse, CustomerRequest

class SyncCustomersClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...  # pylint: disable=W0613
    @overload
    def list_customers(
        self,
        *,
        request: CustomerRequest,
        with_selected_fields: bool = True,
        with_totals: bool = False,
        only_current_page: bool = True,
    ) -> PagedListResponse[Customer]: ...
    @overload
    def list_customers(
        self,
        *,
        request: CustomerRequest,
        with_selected_fields: bool = False,
        with_totals: None = None,
        only_current_page: None = None,
    ) -> PagedListResponse[Customer]: ...
    def list_customers( # pylint: disable=C0116, W0613
        self,
        *,
        request: CustomerRequest,
        with_selected_fields: bool = True,
        with_totals: Optional[bool] = False,
        only_current_page: Optional[bool] = True
    ):...
    def add(self, customer: Customer) -> Customer: ...  # pylint: disable=C0116, W0613
    def get_best_sales(self, *, year: int) -> PagedListResponse[Customer]: ...  # pylint: disable=C0116, W0613
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
    @overload
    async def list_customers(
        self,
        *,
        request: CustomerRequest,
        with_selected_fields: bool = True,
        with_totals: bool = False,
        only_current_page: bool = True
    ) -> PagedListResponse[Customer]:...
    @overload
    async def list_customers(
        self,
        *,
        request: CustomerRequest,
        with_selected_fields: bool = False,
        with_totals: None = None,
        only_current_page: None = None,
    ):...
    async def list_customers( # pylint: disable=C0116, W0613
        self,
        *,
        request: CustomerRequest,
        with_selected_fields: bool = True,
        with_totals: Optional[bool] = False,
        only_current_page: Optional[bool] = True
    ):...
    async def add(self, customer: Customer) -> Customer: ... # pylint: disable=C0116, W0613
    async def get_best_sales(self, *, year: int) -> PagedListResponse[Customer]: ... # pylint: disable=C0116, W0613
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
