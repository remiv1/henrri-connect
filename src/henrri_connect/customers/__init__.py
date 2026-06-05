"""
Sous-client pour les endpoints /v1/customers.

Classes:
- ``SyncCustomersClient`` : Accès synchrone aux endpoints clients.
- ``AsyncCustomersClient`` : Accès asynchrone aux endpoints clients.

Notes:
Utiliser de préférence les objets suivants pour acceder aux endpoints:
- ``henrri_connect.SyncHenrriClient``
- ``henrri_connect.AsyncHenrriClient``
"""

from __future__ import annotations

from .asynchro import AsyncCustomersClient
from .synchro import SyncCustomersClient
from ..models.base import CustomerType
from ..models import CustomerRequest

__all__ = [
    "AsyncCustomersClient",
    "CustomerRequest",
    "CustomerType",
    "SyncCustomersClient",
]
