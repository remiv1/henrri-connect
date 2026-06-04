"""
Sous-client pour les endpoints /v1/customers.

Classes:
--------
- ``henrri_connect.customers.asynchro.AsyncCustomersClient`` :
    Accès asynchrone aux endpoints clients.

Notes:
------
- Utiliser de préférence l'objet ``henrri_connect.AsyncHenrriClient`` pour acceder
aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, overload, Optional

from ..models import Address, Contact, Customer, CustomerRequest, PagedListResponse
from ..models.base import CustomerType
from ..utils import clean

if TYPE_CHECKING:
    from ..connect import AsyncHenrriClient

BASE_CUSTOMERS = "/v1/customers"

class AsyncCustomersClient:
    """
    Accès asynchrone aux endpoints clients.

    Arguments
    - ``client`` (AsyncHenrriClient) : Client HTTP.

    Methods
    - ``delete`` : Supprime un client.
    - ``delete_contact`` : Supprime un contact.
    - ``list_customers`` : Liste les clients avec pagination et filtres optionnels.
    - ``get_best_sales`` : Récupère les meilleurs clients.
    - ``get_last_used`` : Récupère le dernier client utilisé.
    - ``add`` : Crée un nouveau client.
    - ``get`` : Récupère un client par son identifiant.
    - ``modify`` : Met à jour un client.
    - ``get_address`` : Récupère l'adresse d'un client.
    - ``list_contacts`` : Liste les contacts d'un client.
    - ``add_contact`` : Crée un nouveau contact.
    - ``get_contact`` : Récupère un contact d'un client.
    - ``modify_contact`` : Met à jour un contact.
    """

    def __init__(self, client: AsyncHenrriClient) -> None:
        self._c = client

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
    async def list_customers(
        self,
        *,
        request: CustomerRequest,
        with_selected_fields: bool = True,
        with_totals: Optional[bool] = False,
        only_current_page: Optional[bool] = True
    ):
        """
        Liste les clients avec pagination et filtres optionnels.
        
        Arguments
        - ``request`` (CustomerRequest) : Paramètres de recherche.
        - ``with_selected_fields`` (bool) : Si True, lance une requête de recherche avancée.
        - ``with_totals`` (bool) : Si True, renvoie les totaux.
        - ``only_current_page`` (bool) : Si True, renvoie uniquement les clients de la page actuelle.

        Returns
        - ``PagedListResponse[Customer]`` : Liste paginée de clients.
        """
        params = clean(request.model_dump(by_alias=True))
        if with_selected_fields:
            if with_totals and only_current_page:
                params["with_totals"] = with_totals
                params["only_current_page"] = only_current_page
                resp = await self._c.request(
                    "GET",
                    f"{BASE_CUSTOMERS}/with-selected-fields",
                    params=params
                )
            else:
                raise ValueError(
                    "with_totals and only_current_page must be True if with_selected_fields is True"
                )
        else:
            resp = await self._c.request("GET", BASE_CUSTOMERS, params=params)
        return PagedListResponse[Customer].model_validate(resp.json())

    async def add(self, customer: Customer) -> Customer:
        """
        Crée un nouveau client.
        
        Arguments
        - ``customer`` (Customer) : Client à créer.

        Returns
        - ``Customer`` : Client créé.
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
        year: int,
    ) -> PagedListResponse[Customer]:
        """
        Récupère les meilleurs clients.
        
        Arguments
        - ``year`` (int) : Année concerne (minimum 2000, maximum 2100).

        Returns
        - ``PagedListResponse[Customer]`` : Liste paginée de clients.
        """
        params = {
            "year": year
        }
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/best-sales", params=params)
        return PagedListResponse[Customer].model_validate(resp.json())

    async def get_last_used(self, customer_type: CustomerType, limit: int) -> Customer:
        """
        Récupère les derniers clients utilisés.

        Arguments
        - ``customer_type`` (CustomerType) : Type de client.
        - ``limit`` (int) : Nombre de clients maximum.
        
        Returns
        - ``Customer`` : Derniers clients utilisés.
        """
        params = {
            "Types": customer_type,
            "Limit": limit,
        }
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/last-used", params=params)
        return Customer.model_validate(resp.json())

    async def get(self, customer_id: int) -> Customer:
        """
        Récupère un client par son identifiant.
        
        Arguments:
        - ``customer_id`` (int) : Identifiant du client.

        Returns:
        - ``Customer`` : Client.
        """
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}")
        return Customer.model_validate(resp.json())

    async def modify(self, customer_id: int, customer: Customer) -> Customer:
        """
        Met à jour un client existant.
        
        Arguments:
        - ``customer_id`` (int) : Identifiant du client.
        - ``customer`` (Customer) : Client à mettre à jour.

        Returns:
        - ``Customer`` : Client mis à jour.
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
        - ``customer_id`` (int) : Identifiant du client.
        
        Returns:
        - ``None``.
        """
        await self._c.request("DELETE", f"{BASE_CUSTOMERS}/{customer_id}")

    async def get_address(self, customer_id: int) -> Address:
        """
        Récupère l'adresse d'un client.
        
        Arguments:
        - ``customer_id`` (int) : Identifiant du client.
        
        Returns:
        - ``henrri_connect.models.Address`` : Adresse du client.
        """
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/address")
        return Address.model_validate(resp.json())

    async def list_contacts(self, customer_id: int) -> list[Contact]:
        """
        Liste les contacts d'un client.
        
        Arguments:
        - ``customer_id`` (int) : Identifiant du client.
        
        Returns:
        - ``list[Contact]`` : Liste de contacts.
        """
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/contacts")
        return [Contact.model_validate(c) for c in resp.json()]

    async def add_contact(self, customer_id: int, contact: Contact) -> Contact:
        """
        Ajoute un contact à un client.
        
        Arguments:
        - ``customer_id`` (int) : Identifiant du client.
        - ``contact`` (Contact) : Contact à ajouter.

        Returns:
        - ``Contact`` : Contact ajouté.
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
        - ``customer_id`` (int) : Identifiant du client.
        - ``contact_id`` (int) : Identifiant du contact.

        Returns:
        - ``Contact`` : Contact.
        """
        resp = await self._c.request("GET", f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}")
        return Contact.model_validate(resp.json())

    async def modify_contact(self, customer_id: int, contact_id: int, contact: Contact) -> Contact:
        """
        Met à jour un contact d'un client.
        
        Arguments:
        - ``customer_id`` (int) : Identifiant du client.
        - ``contact_id`` (int) : Identifiant du contact.
        - ``contact`` (Contact) : Contact à mettre à jour.

        Returns:
        - ``Contact`` : Contact mis à jour.
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
        - ``customer_id`` (int) : Identifiant du client.
        - ``contact_id`` (int) : Identifiant du contact.
        
        Returns:
        - ``None``.
        """
        await self._c.request("DELETE", f"{BASE_CUSTOMERS}/{customer_id}/contacts/{contact_id}")
