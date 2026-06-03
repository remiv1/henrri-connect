"""Stub de type pour le module de revenus de Henrri Connect."""
from __future__ import annotations

from typing import Any

from ..models import MonthlyRevenueStatistics, RevenueStatistics

class SyncRevenuesClient:   # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    def get_annual(self, year: int) -> RevenueStatistics: ...   # pylint: disable=C0116, W0613
    def get_monthly(self, year: int) -> list[MonthlyRevenueStatistics]: ... # pylint: disable=C0116, W0613

class AsyncRevenuesClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    async def get_annual(self, year: int) -> RevenueStatistics: ... # pylint: disable=C0116, W0613
    async def get_monthly(self, year: int) -> list[MonthlyRevenueStatistics]: ...   # pylint: disable=C0116, W0613
