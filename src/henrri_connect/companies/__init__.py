"""Sous-client pour les endpoints /v1/companies."""

from __future__ import annotations

from .synchro import SyncCompaniesClient
from .asynchro import AsyncCompaniesClient

__all__ = [
    "SyncCompaniesClient",
    "AsyncCompaniesClient",
]
