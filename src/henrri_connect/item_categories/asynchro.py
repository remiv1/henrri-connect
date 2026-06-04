"""
Sous-client pour les endpoints /v1/itemcategories.

Classes:
--------
- ``henrri_connect.item_categories.asynchro.AsyncItemCategoriesClient`` :
    Accès asynchrone aux endpoints categories d'articles.

Notes:
------
- Utiliser de préférence l'objet ``henrri_connect.AsyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import ItemCategory, PagedListResponse, ItemCategoryRequest
from ..utils import clean

if TYPE_CHECKING:
    from ..connect import AsyncHenrriClient

ITEMCATEGORIES_ENDPOINT = "/v1/itemcategories"


class AsyncItemCategoriesClient:
    """
    Accès asynchrone aux catégories d'articles.
    
    Arguments:
    - ``client`` : Objet ``henrri_connect.AsyncHenrriClient`` pour acceder aux endpoints.
    
    Methodes:
    - ``list_item_categories`` : Liste les catégories d'articles avec pagination.
    """

    def __init__(self, client: AsyncHenrriClient) -> None:
        self._c = client

    async def list_item_categories(
        self,
        *,
        request: ItemCategoryRequest,
    ) -> PagedListResponse[ItemCategory]:
        """
        Liste les catégories d'articles avec pagination.
        
        Arguments:
        - ``request`` (ItemCategoryRequest) : Paramètres de recherche.

        Returns:
        - ``PagedListResponse[ItemCategory]`` : Liste paginée de catégories d'articles.
        """
        params = clean(request.model_dump(by_alias=True))
        resp = await self._c.request("GET", ITEMCATEGORIES_ENDPOINT, params=params)
        return PagedListResponse[ItemCategory].model_validate(resp.json())
