"""
Sous-client pour les endpoints /v1/secures.

Classes:
- ``henrri_connect.secures.synchro.SyncSecuresClient``
    Accès synchrone aux endpoints safeguards (santé).

Notes:
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..connect import SyncHenrriClient

SECURES_ENDPOINT = "/v1/secures"


class SyncSecuresClient:    # pylint: disable=R0903
    """
    Accès synchrone aux endpoints sécurisés (santé).

    Arguments
    - client : SyncHenrriClient
    Client synchrone pour acceder aux endpoints.

    Methods
    - hello_world()
    Vérifie la connexion authentifiée à l'API (endpoint de santé).
    """

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def hello_world(self) -> str:
        """
        Vérifie la connexion authentifiée à l'API (endpoint de santé).

        Arguments
        - None

        Returns
        - str : Texte de la réponse.
        """
        resp = self._c.request("GET", f"{SECURES_ENDPOINT}/hello-world")
        return resp.text
