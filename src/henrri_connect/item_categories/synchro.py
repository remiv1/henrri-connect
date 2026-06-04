"""
Sous-client pour les endpoints /v1/itemcategories.

Classes:
--------
- `henrri_connect.item_categories.synchro.SyncItemCategoriesClient`:
    Accès synchrone aux endpoints categories d'articles.

Notes:
-----
- Utiliser de préférence l'objet `henrri_connect.SyncHenrriClient` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import ItemCategory, PagedListResponse, ItemCategoryRequest
from ..utils import clean

if TYPE_CHECKING:
    from ..connect import SyncHenrriClient

ITEMCATEGORIES_ENDPOINT = "/v1/itemcategories"


class SyncItemCategoriesClient:
    """
    Accès synchrone aux catégories d'articles.
    
    Arguments:
    - `client`: Objet `henrri_connect.SyncHenrriClient` pour acceder aux endpoints.
    
    Methodes:
    - `list_item_categories`: Liste les catégories d'articles avec pagination.
    """

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def list_item_categories(
        self,
        *,
        request: ItemCategoryRequest,
    ) -> PagedListResponse[ItemCategory]:
        """
        Liste les catégories d'articles avec pagination.
        
        Arguments:
        - `request` (ItemCategoryRequest): Paramètres de recherche.

        Returns:
        - `PagedListResponse[ItemCategory]`: Liste paginée de catégories d'articles.
        """
        params = clean(request.model_dump(by_alias=True))
        resp = self._c.request("GET", ITEMCATEGORIES_ENDPOINT, params=params)
        return PagedListResponse[ItemCategory].model_validate(resp.json())
