"""
Sous-client pour les endpoints /v1/revenues.

Classes:
- ``henrri_connect.revenues.synchro.SyncRevenuesClient`` : Accès synchrone aux endpoints revenus.
- ``henrri_connect.revenues.asynchro.AsyncRevenuesClient`` : Accès asynchrone aux endpoints revenus.

Notes:
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
- Utiliser de préférence l'objet ``henrri_connect.AsyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from .synchro import SyncRevenuesClient
from .asynchro import AsyncRevenuesClient
from ..models import MonthlyRevenueStatistics, RevenueStatistics

__all__ = [
    "AsyncRevenuesClient",
    "MonthlyRevenueStatistics",
    "RevenueStatistics",
    "SyncRevenuesClient",
]
