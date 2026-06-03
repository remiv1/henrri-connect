"""
Sous-client pour les endpoints /v1/customers.

Classes:
--------
- `henrri_connect.customers.synchro.SyncCustomersClient`:
    Accès synchrone aux endpoints clients.

Notes:
-----
- Utiliser de préférence l'objet `henrri_connect.SyncHenrriClient` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..models import Address, Contact, Customer, PagedListResponse

if TYPE_CHECKING:
    from ..connect import SyncHenrriClient

BASE_CUSTOMERS = "/v1/customers"

def _clean(params: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in params.items() if v is not None}


class SyncCustomersClient:
    """
    Accès synchrone aux endpoints clients.
    
    Arguments:
    - `client` (SyncHenrriClient): Client HTTP.

    Methodes:
    - `list_customers`: Liste les clients avec pagination et filtres optionnels.
    - `add`: Crée un nouveau client.
    - `get_best_sales`: Récupère les meilleurs clients.
    - `get`: Récupère un client par son identifiant.
    - `modify`: Met à jour un client existant.
    - `delete`: Supprime un client.
    - `get_address`: Récupère l'adresse d'un client.
    - `list_contacts`: Liste les contacts d'un client avec pagination et filtres optionnels.
    - `add_contact`: Crée un nouveau contact.
    - `get_contact`: Récupère un contact d'un client.
    - `modify_contact`: Met à jour un contact existant.
    - `delete_contact`: Supprime un contact.
    """

    def __init__(self, client: SyncHenrriClient) -> None:
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
        """
        Liste les clients avec pagination et filtres optionnels.
        
        Arguments:
        - `page` (int): Numéro de page (par d&eacute;faut 1).
        - `limit` (int): Nombre de clients par page (par d&eacute;faut 50).
        - `search` (str): Chaine de recherche (par d&eacute;faut None).
        - `sort_by` (str): Champ de tri (par d&eacute;faut None).
        - `sort_order` (str): Ordre de tri (par d&eacute;faut None).
        - `min_id` (int): ID minimum (par d&eacute;faut None).
        - `from_date` (str): Date de d&eacute;but (par d&eacute;faut None).
        - `to_date` (str): Date de fin (par d&eacute;faut None).

        Returns:
        - `PagedListResponse[Customer]`: Liste de clients.
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
        resp = self._c.request("GET", BASE_CUSTOMERS, params=params)
        return PagedListResponse[Customer].model_validate(resp.json())

    def add(self, customer: Customer) -> Customer:
        """
        Crée un nouveau client.
        
        Arguments:
        - `customer` (Customer): Client à créer.

        Returns:
        - `Customer`: Client créé.
        """
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
        """
        Récupère les meilleurs clients.
        
        Arguments:
        - `page` (int): Numéro de page (par d&eacute;faut 1).
        - `limit` (int): Nombre de clients par page (par d&eacute;faut 50).
        - `search` (str): Chaine de recherche (par d&eacute;faut None).
        - `sort_by` (str): Champ de tri (par d&eacute;faut None).
        - `sort_order` (str): Ordre de tri (par d&eacute;faut None).

        Returns:
        - `PagedListResponse[Customer]`: Liste de clients.
        """
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
        """
        Récupère un client par son identifiant.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.

        Returns:
        - `Customer`: Client.
        """
        resp = self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}")
        return Customer.model_validate(resp.json())

    def modify(self, customer_id: int, customer: Customer) -> Customer:
        """
        Met à jour un client existant.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `customer` (Customer): Client à mettre à jour.

        Returns:
        - `Customer`: Client mis à jour.
        """
        resp = self._c.request(
            "PUT",
            f"{BASE_CUSTOMERS}/{customer_id}",
            json=customer.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Customer.model_validate(resp.json())

    def delete(self, customer_id: int) -> None:
        """
        Supprime un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.

        Returns:
        - `None`
        """
        self._c.request("DELETE", f"{BASE_CUSTOMERS}/{customer_id}")

    def get_address(self, customer_id: int) -> Address:
        """
        Récupère l'adresse d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.

        Returns:
        - `Address`: Adresse du client.
        """
        resp = self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/address")
        return Address.model_validate(resp.json())

    def list_contacts(self, customer_id: int) -> list[Contact]:
        """
        Liste les contacts d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.

        Returns:
        - `list[Contact]`: Liste de contacts.
        """
        resp = self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/contacts")
        return [Contact.model_validate(c) for c in resp.json()]

    def add_contact(self, customer_id: int, contact: Contact) -> Contact:
        """
        Ajoute un contact à un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `contact` (Contact): Contact à ajouter.

        Returns:
        - `Contact`: Contact ajouté.
        """
        resp = self._c.request(
            "POST",
            f"{BASE_CUSTOMERS}/{customer_id}/contacts",
            json=contact.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Contact.model_validate(resp.json())

    def get_contact(self, customer_id: int, contact_id: int) -> Contact:
        """
        Récupère un contact d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `contact_id` (int): Identifiant du contact.

        Returns:
        - `Contact`: Contact.
        """
        resp = self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}")
        return Contact.model_validate(resp.json())

    def modify_contact(self, customer_id: int, contact_id: int, contact: Contact) -> Contact:
        """
        Met à jour un contact d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `contact_id` (int): Identifiant du contact.
        - `contact` (Contact): Contact à mettre à jour.

        Returns:
        - `Contact`: Contact mis à jour.
        """
        resp = self._c.request(
            "PUT",
            f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}",
            json=contact.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Contact.model_validate(resp.json())

    def delete_contact(self, customer_id: int, contact_id: int) -> None:
        """
        Supprime un contact d'un client.
        
        Arguments:
        - `customer_id` (int): Identifiant du client.
        - `contact_id` (int): Identifiant du contact.

        Returns:
        - `None`
        """
        self._c.request("DELETE", f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}")
