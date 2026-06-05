"""
Sous-client pour les endpoints /v1/secures.

Classes:
- ``henrri_connect.secures.asynchro.AsyncSecuresClient``
    Accès asynchrone aux endpoints safeguards (santé).

Notes:
- Utiliser de préférence l'objet ``henrri_connect.AsyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..connect import AsyncHenrriClient

SECURES_ENDPOINT = "/v1/secures"


class AsyncSecuresClient:   # pylint: disable=R0903
    """
    Accès asynchrone aux endpoints sécurisés (santé).

    Arguments
        client : AsyncHenrriClient
        Client asynchrone pour acceder aux endpoints.

    Methods
        hello_world()
        Vérifie la connexion authentifiée à l'API (endpoint de santé).
    """

    def __init__(self, client: AsyncHenrriClient) -> None:
        self._c = client

    async def hello_world(self) -> str:
        """
        Vérifie la connexion authentifiée à l'API (endpoint de santé).

        Arguments
            None

        Returns
            str : Texte de la réponse.
        """
        resp = await self._c.request("GET", f"{SECURES_ENDPOINT}/hello-world")
        return resp.text
