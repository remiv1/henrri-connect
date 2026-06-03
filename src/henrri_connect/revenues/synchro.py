"""Sous-client pour les endpoints /v1/revenues."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import MonthlyRevenueStatistics, RevenueStatistics

if TYPE_CHECKING:
    from ..connect import (
        SyncHenrriClient,
    )


class SyncRevenuesClient:
    """Accès synchrone aux statistiques de revenus."""

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def get_annual(self, year: int) -> RevenueStatistics:
        """Récupère les statistiques de revenus annuelles."""
        resp = self._c.request("GET", f"/v1/revenues/{year}")
        return RevenueStatistics.model_validate(resp.json())

    def get_monthly(self, year: int) -> list[MonthlyRevenueStatistics]:
        """Récupère les statistiques de revenus mensuelles pour une année."""
        resp = self._c.request("GET", f"/v1/revenues/{year}/months")
        return [MonthlyRevenueStatistics.model_validate(item) for item in resp.json()]
