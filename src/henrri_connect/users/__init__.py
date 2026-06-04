"""
Sous-client pour les endpoints /v1/users.

Classes:
--------
- ``henrri_connect.users.asynchro.AsyncUsersClient`` :
    Accès asynchrone aux endpoints utilisateurs.
- ``henrri_connect.users.synchro.SyncUsersClient`` :
    Accès synchrone aux endpoints utilisateurs.

Notes:
------
- Utiliser de préférence l'objet ``henrri_connect.AsyncHenrriClient`` pour acceder aux endpoints.
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from .synchro import SyncUsersClient
from .asynchro import AsyncUsersClient
from ..models import Address, TokenResponse, User, UserAndCompany

__all__ = [
    "Address",
    "AsyncUsersClient",
    "SyncUsersClient",
    "TokenResponse",
    "User",
    "UserAndCompany",
]
