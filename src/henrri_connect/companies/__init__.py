"""
Sous-client pour les endpoints /v1/companies.

Classes:
--------
- `henrri_connect.companies.synchro.SyncCompaniesClient`:
    Accès synchrone aux endpoints entreprises.

- `henrri_connect.companies.asynchro.AsyncCompaniesClient`:
    Accès asynchrone aux endpoints entreprises.

Models:
-------
- `henrri_connect.companies.models.Address`:
    Adresse.

- `henrri_connect.companies.models.Company`:
    Entreprise.

Notes:
-----
- Utiliser de préférence les objets suivants pour acceder aux endpoints:
    - `henrri_connect.SyncHenrriClient`
    - `henrri_connect.AsyncHenrriClient`
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
