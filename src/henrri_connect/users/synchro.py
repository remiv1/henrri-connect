"""
Sous-client pour les endpoints /v1/users.

Classes:
- ``henrri_connect.users.synchro.SyncUsersClient`` : Accès synchrone aux endpoints utilisateurs.

Notes:
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import Address, TokenResponse, User, UserAndCompany

if TYPE_CHECKING:
    from ..connect import SyncHenrriClient

USERS_ENDPOINT = "/v1/users"

class SyncUsersClient:
    """
    Accès synchrone aux endpoints utilisateurs.

    Arguments:
    - client (SyncHenrriClient) : Client synchrone pour acceder aux endpoints.

    Methods:
    - get(user_id: int) : Récupère un utilisateur par son identifiant.
    - get_address(user_id: int) : Récupère l'adresse d'un utilisateur.
    - get_companies() : Récupère les entreprises associées à l'utilisateur courant.
    - authenticate() : Authentifie via les identifiants du client.
    - refresh_token(refresh_token: str) : Rafraîchit le token d'accès.
    """

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def get(self, user_id: int) -> User:
        """
        Récupère un utilisateur par son identifiant.

        Arguments:
        - ``user_id`` (int) : Identifiant de l'utilisateur.

        Returns:
        - ``User`` : Utilisateur.
        """
        resp = self._c.request("GET", f"{USERS_ENDPOINT}/{user_id}")
        return User.model_validate(resp.json())

    def get_address(self, user_id: int) -> Address:
        """
        Récupère l'adresse d'un utilisateur.

        Arguments:
        - ``user_id`` (int) : Identifiant de l'utilisateur.

        Returns:
        - ``henrri_connect.models.Address`` : Adresse de l'utilisateur.
        """
        resp = self._c.request("GET", f"{USERS_ENDPOINT}/{user_id}/address")
        return Address.model_validate(resp.json())

    def get_companies(self) -> list[UserAndCompany]:
        """
        Récupère les entreprises associées à l'utilisateur courant.

        Returns:
        - ``list[UserAndCompany]`` : Entreprises.
        """
        resp = self._c.request("GET", f"{USERS_ENDPOINT}/companies")
        return [UserAndCompany.model_validate(item) for item in resp.json()]

    def authenticate(self) -> TokenResponse:
        """
        Authentifie via les identifiants du client.

        Returns:
        - ``henrri_connect.models.TokenResponse`` : Objet contenant access_token et refresh_token.
        """
        return self._c.authenticate()

    def refresh_token(self, refresh_token: str) -> TokenResponse:
        """
        Rafraîchit le token d'accès.

        Arguments:
        - ``refresh_token`` (str) : Token de rafraîchissement.

        Returns:
        - ``henrri_connect.models.TokenResponse`` : Objet contenant access_token et refresh_token.
        """
        resp = self._c.request(
            "POST",
            f"{USERS_ENDPOINT}/refresh-token",
            authenticated=False,
            json={"refreshToken": refresh_token},
        )
        token = TokenResponse.model_validate(resp.json())
        self._c._access_token = token.access_token  # pylint: disable=W0212
        if token.refresh_token:
            self._c._refresh_token_str = token.refresh_token    # pylint: disable=W0212
        return token
