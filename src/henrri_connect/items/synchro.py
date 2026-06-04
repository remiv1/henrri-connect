"""
Sous-client pour les endpoints /v1/items.

Classes:
--------
- `henrri_connect.items.synchro.SyncItemsClient`:
    Accès synchrone aux endpoints articles.

Notes:
-----
- Utiliser de préférence l'objet `henrri_connect.SyncHenrriClient` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, overload, Optional

from ..models import Item, PagedListResponse, ItemsQuery
from ..utils import clean

if TYPE_CHECKING:
    from ..connect import SyncHenrriClient

ITEMS_ENDPOINT = "/v1/items"


class SyncItemsClient:
    """
    Accès synchrone aux endpoints articles.
    
    Arguments:
    - `client`: Objet `henrri_connect.SyncHenrriClient` pour acceder aux endpoints.

    Methods:
    - `list_items`: Liste les articles avec pagination et filtres optionnels.
    - `add`: Crée un nouvel article.
    - `get`: Récupère un article par son identifiant.
    - `modify`: Modifie un article par son identifiant.
    - `delete`: Supprime un article par son identifiant.
    - `get_most_used`: Récupère les articles les plus utilisés.
    - `get_best_sales`: Récupère les articles les plus vendus.
    - `list_with_selected_fields`: Liste les articles avec sélection de champs.
    """

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

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
    async def list_items(
            self,
            *,
            request: ItemsQuery,
            with_selected_fields: bool = True,
            with_totals: Optional[bool] = False,
            only_current_page: Optional[bool] = True
        ) -> PagedListResponse[Item]:
        """
        Liste les articles avec pagination et filtres optionnels.
        
        Arguments:
        - `request` (ItemsQuery): Paramètres de recherche.
        - `with_selected_fields` (bool): Si True, lance une requête de recherche avancée.
        - `with_totals` (bool): Si True, renvoie les totaux.
        - `only_current_page` (bool): Si True, renvoie uniquement les articles de la page actuelle.

        Returns:
        - `PagedListResponse[Item]`: Liste paginée d'articles.
        """
        params = clean(request.model_dump(by_alias=True))
        if with_selected_fields:
            if with_totals and only_current_page:
                params["with_totals"] = with_totals
                params["only_current_page"] = only_current_page
                resp = self._c.request(
                    "GET",
                    f"{ITEMS_ENDPOINT}/with-selected-fields",
                    params=params
                )
            else:
                raise ValueError(
                    "with_totals and only_current_page must be True if with_selected_fields is True"
                )
        else:
            resp = self._c.request("GET", ITEMS_ENDPOINT, params=params)
        return PagedListResponse[Item].model_validate(resp.json())

    def add(self, item: Item) -> Item:
        """
        Crée un nouvel article.
        
        Arguments:
        - `item` (Item): Article à créer.
        
        Returns:
        - `Item`: Article créé.
        """
        resp = self._c.request(
            "POST",
            ITEMS_ENDPOINT,
            json=item.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Item.model_validate(resp.json())

    def get(self, item_id: int) -> Item:
        """
        Récupère un article par son identifiant.
        
        Arguments:
        - `item_id` (int): Identifiant de l'article.
        
        Returns:
        - `Item`: Article rencontré.
        """
        resp = self._c.request("GET", f"{ITEMS_ENDPOINT}/{item_id}")
        return Item.model_validate(resp.json())

    def modify(self, item_id: int, item: Item) -> Item:
        """
        Met à jour un article existant.
        
        Arguments:
        - `item_id` (int): Identifiant de l'article.
        - `item` (Item): Article à mettre à jour.
        
        Returns:
        - `Item`: Article mis à jour.
        """
        resp = self._c.request(
            "PUT",
            f"{ITEMS_ENDPOINT}/{item_id}",
            json=item.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Item.model_validate(resp.json())

    def delete(self, item_id: int) -> None:
        """
        Supprime un article.
        
        Arguments:
        - `item_id` (int): Identifiant de l'article à supprimer.
        
        Returns:
        - `None`: Article supprimé.
        """
        self._c.request("DELETE", f"{ITEMS_ENDPOINT}/{item_id}")

    def get_most_used(self) -> PagedListResponse[Item]:
        """
        Récupère les articles les plus utilisés.
        
        Arguments:
        - None
        
        Returns:
        - `PagedListResponse[Item]`: Liste paginée d'articles.
        """
        resp = self._c.request("GET", f"{ITEMS_ENDPOINT}/most-used")
        return PagedListResponse[Item].model_validate(resp.json())

    def get_best_sales(self, *, year: int) -> PagedListResponse[Item]:
        """
        Récupère les articles les plus vendus.
        
        Arguments:
        - `year` (int): Année de recherche.
        
        Returns:
        - `PagedListResponse[Item]`: Liste paginée d'articles.
        """
        params = {
            "year": year
        }
        resp = self._c.request("GET", f"{ITEMS_ENDPOINT}/with-selected-fields", params=params)
        return PagedListResponse[Item].model_validate(resp.json())
