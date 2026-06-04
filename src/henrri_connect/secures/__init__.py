"""
Sous-client pour les endpoints /v1/secures.

Classes:
--------
- `henrri_connect.secures.asynchro.AsyncSecuresClient`:
    Accès asynchrone aux endpoints safeguards (santé).
- `henrri_connect.secures.synchro.SyncSecuresClient`:
    Accès synchrone aux endpoints safeguards (santé).

Notes:
-----
- Utiliser de préférence l'objet `henrri_connect.AsyncHenrriClient` pour acceder aux endpoints.
- Utiliser de préférence l'objet `henrri_connect.SyncHenrriClient` pour acceder aux endpoints.
"""

from __future__ import annotations

from .synchro import SyncSecuresClient
from .asynchro import AsyncSecuresClient

__all__ = [
    "AsyncSecuresClient",
    "SyncSecuresClient",
]
