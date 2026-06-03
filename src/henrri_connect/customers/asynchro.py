"""
Sous-client pour les endpoints /v1/customers.

Classes:
--------
- `henrri_connect.customers.asynchro.AsyncCustomersClient`:
    Accès asynchrone aux endpoints clients.

Notes:
-----
- Utiliser de préférence l'objet `henrri_connect.AsyncHenrriClient` pour acceder
aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models import Address, Contact, Customer, PagedListResponse

if TYPE_CHECKING:
    from ..connect import (
        AsyncHenrriClient,
    )

BASE_CUSTOMERS = "/v1/customers"

def _clean(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}

class AsyncCustomersClient:
    """
    Accès asynchrone aux endpoints clients.

    Arguments:
    - `client` (AsyncHenrriClient): Client HTTP.

    Methods:
    - `list_customers`: Liste les clients avec pagination et filtres optionnels.
    - `add`: Crée un nouveau client.
    - `get_best_sales`: Récupère les meilleurs clients.
    - `get`: Récupère un client par son identifiant.
    - `modify`: Met à jour un client.
    - `delete`: Supprime un client.
    - `get_address`: Récupère l'adresse d'un client.
    - `list_contacts`: Liste les contacts d'un client.
    - `add_contact`: Crée un nouveau contact.
    - `get_contact`: Récupère un contact d'un client.
    - `modify_contact`: Met à jour un contact.
    - `delete_contact`: Supprime un contact.
    """

    def __init__(self, client: AsyncHenrriClient) -> None:
        self._c = client

    async def list_customers(
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
        """
        Liste les clients avec pagination et filtres optionnels.
        
        Arguments:
        - `page` (int): Numéro de page (par d&eacute;faut 1).
        - `limit` (int): Nombre d'articles par page (par d&eacute;faut 50).
        - `search` (str | None): Chaine de recherche.
        - `sort_by` (str | None): Champ de tri.
        - `sort_order` (str | None): Ordre de tri (ascendant ou descendant).
        - `min_id` (int | None): Filtre par identifiant minimum.
        - `from_date` (str | None): Filtre par date de debut.
        - `to_date` (str | None): Filtre par date de fin.

        Returns:
        - `PagedListResponse[Customer]`: Liste paginée de clients.
        """
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
        resp = await self._c.request("GET", BASE_CUSTOMERS, params=params)
        return PagedListResponse[Customer].model_validate(resp.json())

    async def add(self, customer: Customer) -> Customer:
        """
        Crée un nouveau client.
        
        Arguments:
        - `customer` (Customer): Client à créer.

        Returns:
        - `Customer`: Client créé.
        """
        resp = await self._c.request(
            "POST",
            BASE_CUSTOMERS,
            json=customer.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Customer.model_validate(resp.json())

    async def get_best_sales(
        self,
        *,
        page: int = 1,
        limit: int = 50,
        search: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
    ) -> PagedListResponse[Customer]:
        """
        Récupère les meilleurs clients.
        
        Arguments:
        - `page` (int): Numéro de page (par d&eacute;faut 1).
        - `limit` (int): Nombre d'articles par page (par d&eacute;faut 50).
        - `search` (str | None): Chaine de recherche.
        - `sort_by` (str | None): Champ de tri.
        - `sort_order` (str | None): Ordre de tri (ascendant ou descendant).

        Returns:
        - `PagedListResponse[Customer]`: Liste paginée de clients.
        """
        params = _clean({
            "page": page,
            "limit": limit,
            "search": search,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        })
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/best-sales", params=params)
        return PagedListResponse[Customer].model_validate(resp.json())

    async def get(self, customer_id: int) -> Customer:
        """
        Récupère un client par son identifiant.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.

        Returns:
        - `Customer`: Client.
        """
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}")
        return Customer.model_validate(resp.json())

    async def modify(self, customer_id: int, customer: Customer) -> Customer:
        """
        Met à jour un client existant.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `customer` (Customer): Client à mettre à jour.

        Returns:
        - `Customer`: Client mis à jour.
        """
        resp = await self._c.request(
            "PUT",
            f"{BASE_CUSTOMERS}/{customer_id}",
            json=customer.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Customer.model_validate(resp.json())

    async def delete(self, customer_id: int) -> None:
        """
        Supprime un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        
        Returns:
        - `None`.
        """
        await self._c.request("DELETE", f"{BASE_CUSTOMERS}/{customer_id}")

    async def get_address(self, customer_id: int) -> Address:
        """
        Récupère l'adresse d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        
        Returns:
        - `henrri_connect.models.Address`: Adresse du client.
        """
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/address")
        return Address.model_validate(resp.json())

    async def list_contacts(self, customer_id: int) -> list[Contact]:
        """
        Liste les contacts d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        
        Returns:
        - `list[Contact]`: Liste de contacts.
        """
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/contacts")
        return [Contact.model_validate(c) for c in resp.json()]

    async def add_contact(self, customer_id: int, contact: Contact) -> Contact:
        """
        Ajoute un contact à un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `contact` (Contact): Contact à ajouter.

        Returns:
        - `Contact`: Contact ajouté.
        """
        resp = await self._c.request(
            "POST",
            f"{BASE_CUSTOMERS}/{customer_id}/contacts",
            json=contact.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Contact.model_validate(resp.json())

    async def get_contact(self, customer_id: int, contact_id: int) -> Contact:
        """
        Récupère un contact d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `contact_id` (int): Identifiant du contact.

        Returns:
        - `Contact`: Contact.
        """
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}")
        return Contact.model_validate(resp.json())

    async def modify_contact(self, customer_id: int, contact_id: int, contact: Contact) -> Contact:
        """
        Met à jour un contact d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `contact_id` (int): Identifiant du contact.
        - `contact` (Contact): Contact à mettre à jour.

        Returns:
        - `Contact`: Contact mis à jour.
        """
        resp = await self._c.request(
            "PUT",
            f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}",
            json=contact.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Contact.model_validate(resp.json())

    async def delete_contact(self, customer_id: int, contact_id: int) -> None:
        """
        Supprime un contact d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `contact_id` (int): Identifiant du contact.
        
        Returns:
        - `None`.
        """
        await self._c.request("DELETE", f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}")
