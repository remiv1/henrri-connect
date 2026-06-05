"""
Sous-client pour les endpoints /v1/companies.

Classes:
- ``SyncCompaniesClient`` : Accès synchrone aux endpoints entreprises.
- ``AsyncCompaniesClient`` : Accès asynchrone aux endpoints entreprises.

Models:
- ``Address`` : Adresse.
- ``Company`` : Entreprise.

Notes:
Utiliser de préférence les objets suivants pour acceder aux endpoints:
- ``henrri_connect.SyncHenrriClient``
- ``henrri_connect.AsyncHenrriClient``
"""

from __future__ import annotations

from .synchro import SyncCompaniesClient
from .asynchro import AsyncCompaniesClient
from ..models import Address, Company

__all__ = [
    "Address",
    "AsyncCompaniesClient",
    "Company",
    "SyncCompaniesClient",
]
