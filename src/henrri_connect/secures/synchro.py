"""Sous-client pour les endpoints /v1/secures."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..connect import (
        SyncHenrriClient,
    )

SECURES_ENDPOINT = "/v1/secures"


class SyncSecuresClient:
    """Accès synchrone aux endpoints sécurisés (santé)."""

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def hello_world(self) -> str:
        """Vérifie la connexion authentifiée à l'API (endpoint de santé)."""
        resp = self._c.request("GET", f"{SECURES_ENDPOINT}/hello-world")
        return resp.text
