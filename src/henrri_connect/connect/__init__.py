"""Client HTTP Henrri : factory et implémentations synchrone/asynchrone."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any    # type: ignore[import]
from .asynchro import _AsyncHenrriClient    # type: ignore[import]
from .synchro import _SyncHenrriClient   # type: ignore[import]

_BASE_URL = "https://api-sandbox.henrri.io"
APP_VERSION = "application/json; X-Version=1.0"

class HenrriClient:
    """Factory pour créer un client synchrone ou asynchrone pour l'API Henrri.

    Usage:
        # Synchrone
        client = HenrriClient('client_id', 'client_secret')
        
        # Asynchrone
        client = HenrriClient('client_id', 'client_secret', async_mode=True)
    """

    def __new__(
        cls,
        client_id: str,
        client_secret: str,
        *,
        base_url: str = _BASE_URL,
        async_mode: bool = False,
    ) -> _SyncHenrriClient | _AsyncHenrriClient:
        """Crée un client pour l'API Henrri.

        Args:
            client_id: Identifiant client pour l'authentification.
            client_secret: Secret client pour l'authentification.
            base_url: URL de base de l'API (défaut : sandbox Henrri).
            async_mode: Si True, retourne un client asynchrone (httpx.AsyncClient).

        Returns:
            Instance synchrone (_SyncHenrriClient) ou asynchrone (_AsyncHenrriClient).
        """
        if async_mode:
            return _AsyncHenrriClient(client_id, client_secret, base_url=base_url)
        return _SyncHenrriClient(client_id, client_secret, base_url=base_url)
