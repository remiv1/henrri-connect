"""
Façade principale du package henrri_connect.

Classes:
--------
- ``henrri_connect.AsyncHenrriClient`` :
  Client HTTP Henrri asynchrone.
- ``henrri_connect.SyncHenrriClient`` :
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
from .connect import AsyncHenrriClient, SyncHenrriClient

__all__ = [
    "AsyncHenrriClient",
    "SyncHenrriClient",
]
