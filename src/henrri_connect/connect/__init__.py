"""
Client HTTP Henrri : implémentations synchrone/asynchrone.

Constants:
----------
- ``henrri_connect.connect._BASE_URL`` :
  URL de base de l'API Henrri.
- ``henrri_connect.connect.APP_VERSION`` :
  Version de l'application.

Classes:
--------
- ``henrri_connect.connect.AsyncHenrriClient`` :
  Client HTTP Henrri asynchrone.
- ``henrri_connect.connect.SyncHenrriClient`` :
  Client HTTP Henrri synchrone.

Exemples:
---------
.. code-block:: python

   # Client synchrone
   from henrri_connect import SyncHenrriClient

   client = SyncHenrriClient("client_id", "client_secret")

   # Client asynchrone
   from henrri_connect import AsyncHenrriClient
   
   client = AsyncHenrriClient("client_id", "client_secret")
"""

from __future__ import annotations

from .asynchro import AsyncHenrriClient
from .synchro import SyncHenrriClient

_BASE_URL = "https://api-sandbox.henrri.io"
APP_VERSION = "application/json; X-Version=1.0"

__all__ = [
    "AsyncHenrriClient",
    "SyncHenrriClient",
]
