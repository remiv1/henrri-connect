"""
Sous-client pour les endpoints /v1/units.

Classes:
- ``henrri_connect.units.asynchro.AsyncUnitsClient`` : Accès asynchrone aux endpoints unités.
- ``henrri_connect.units.synchro.SyncUnitsClient`` : Accès synchrone aux endpoints unités.

Notes:
- Utiliser de préférence l'objet ``henrri_connect.AsyncHenrriClient`` pour acceder aux endpoints.
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from .synchro import SyncUnitsClient
from .asynchro import AsyncUnitsClient
from ..models import ListResponse, Unit

__all__ = [
    "AsyncUnitsClient",
    "ListResponse",
    "SyncUnitsClient",
    "Unit",
]
