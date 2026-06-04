"""
Sous-client pour les endpoints /v1/revenues.

Classes:
--------
- `henrri_connect.revenues.asynchro.AsyncRevenuesClient`:
    Accès asynchrone aux endpoints revenus.

Notes:
-----
- Utiliser de préférence l'objet `henrri_connect.AsyncHenrriClient` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import MonthlyRevenueStatistics, RevenueStatistics

if TYPE_CHECKING:
    from ..connect import AsyncHenrriClient

REVENUES_ENDPOINT = "/v1/revenues"

class AsyncRevenuesClient:
    """
    Accès asynchrone aux statistiques de revenus.
    
    Parameters:
    - `client` (AsyncHenrriClient): Client HTTP.
    
    Methods:
    - `get_annual(self, year: int)`: Récupère les statistiques de revenus annuelles.
    - `get_monthly(self, year: int)`: Récupère les statistiques de revenus mensuelles
    pour une année.
    """

    def __init__(self, client: AsyncHenrriClient) -> None:
        self._c = client

    async def get_annual(self, year: int) -> RevenueStatistics:
        """
        Récupère les statistiques de revenus annuelles.
        
        Arguments:
        - `year` (int): Année de recherche.
        
        Returns:
        - `RevenueStatistics`: Statistiques de revenus annuelles.
        """
        resp = await self._c.request("GET", f"{REVENUES_ENDPOINT}/{year}")
        return RevenueStatistics.model_validate(resp.json())

    async def get_monthly(self, year: int) -> list[MonthlyRevenueStatistics]:
        """
        Récupère les statistiques de revenus mensuelles pour une année.
        
        Arguments:
        - `year` (int): Année de recherche.
        
        Returns:
        - `list[MonthlyRevenueStatistics]`: Statistiques de revenus mensuelles.
        """
        resp = await self._c.request("GET", f"{REVENUES_ENDPOINT}/{year}/months")
        return [MonthlyRevenueStatistics.model_validate(item) for item in resp.json()]
