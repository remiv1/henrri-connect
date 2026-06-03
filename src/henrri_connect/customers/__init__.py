"""
Sous-client pour les endpoints /v1/customers.

Classes:
--------
- `henrri_connect.customers.synchro.SyncCustomersClient`:
    Accès synchrone aux endpoints clients.

- `henrri_connect.customers.asynchro.AsyncCustomersClient`:
    Accès asynchrone aux endpoints clients.

Notes:
-----
- Utiliser de préférence les objets suivants pour acceder aux endpoints:
    - `henrri_connect.SyncHenrriClient`
    - `henrri_connect.AsyncHenrriClient`
"""

from __future__ import annotations

from .asynchro import AsyncCustomersClient
from .synchro import SyncCustomersClient

__all__ = [
    "SyncCustomersClient",
    "AsyncCustomersClient",
]
