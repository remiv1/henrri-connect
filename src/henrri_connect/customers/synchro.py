"""Sous-client pour les endpoints /v1/customers."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models import Address, Contact, Customer, PagedListResponse

if TYPE_CHECKING:
    from ..connect import (
        _SyncHenrriClient,    # type: ignore[import]
    )

BASE_CUSTOMERS = "/v1/customers"

def _clean(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


class SyncCustomersClient:
    """Accès synchrone aux endpoints clients."""

    def __init__(self, client: _SyncHenrriClient) -> None:
        self._c = client

    def list_customers(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        min_id: int | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> PagedListResponse[Customer]:
        """Liste les clients avec pagination et filtres optionnels."""
        params = _clean({
            "page": page,
            "limit": limit,
            "search": search,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "minId": min_id,
            "fromDate": from_date,
            "toDate": to_date,
        })
        resp = self._c.request("GET", BASE_CUSTOMERS, params=params)
        return PagedListResponse[Customer].model_validate(resp.json())

    def add(self, customer: Customer) -> Customer:
        """Crée un nouveau client."""
        resp = self._c.request(
            "POST",
            BASE_CUSTOMERS,
            json=customer.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Customer.model_validate(resp.json())

    def get_best_sales(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
    ) -> PagedListResponse[Customer]:
        """Récupère les meilleurs clients."""
        params = _clean({
            "page": page,
            "limit": limit,
            "search": search,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        })
        resp = self._c.request("GET", f"{BASE_CUSTOMERS}/best-sales", params=params)
        return PagedListResponse[Customer].model_validate(resp.json())

    def get(self, customer_id: int) -> Customer:
        """Récupère un client par son identifiant."""
        resp = self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}")
        return Customer.model_validate(resp.json())

    def modify(self, customer_id: int, customer: Customer) -> Customer:
        """Met à jour un client existant."""
        resp = self._c.request(
            "PUT",
            f"{BASE_CUSTOMERS}/{customer_id}",
            json=customer.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Customer.model_validate(resp.json())

    def delete(self, customer_id: int) -> None:
        """Supprime un client."""
        self._c.request("DELETE", f"{BASE_CUSTOMERS}/{customer_id}")

    def get_address(self, customer_id: int) -> Address:
        """Récupère l'adresse d'un client."""
        resp = self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/address")
        return Address.model_validate(resp.json())

    def list_contacts(self, customer_id: int) -> list[Contact]:
        """Liste les contacts d'un client."""
        resp = self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/contacts")
        return [Contact.model_validate(c) for c in resp.json()]

    def add_contact(self, customer_id: int, contact: Contact) -> Contact:
        """Ajoute un contact à un client."""
        resp = self._c.request(
            "POST",
            f"{BASE_CUSTOMERS}/{customer_id}/contacts",
            json=contact.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Contact.model_validate(resp.json())

    def get_contact(self, customer_id: int, contact_id: int) -> Contact:
        """Récupère un contact d'un client."""
        resp = self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}")
        return Contact.model_validate(resp.json())

    def modify_contact(self, customer_id: int, contact_id: int, contact: Contact) -> Contact:
        """Met à jour un contact d'un client."""
        resp = self._c.request(
            "PUT",
            f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}",
            json=contact.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Contact.model_validate(resp.json())

    def delete_contact(self, customer_id: int, contact_id: int) -> None:
        """Supprime un contact d'un client."""
        self._c.request("DELETE", f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}")
