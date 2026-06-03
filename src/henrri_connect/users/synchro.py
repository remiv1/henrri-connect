"""Sous-client pour les endpoints /v1/users."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import Address, TokenResponse, User, UserAndCompany

if TYPE_CHECKING:
    from ..connect import (
        SyncHenrriClient,
    )

USERS_ENDPOINT = "/v1/users"

class SyncUsersClient:
    """Accès synchrone aux endpoints utilisateurs."""

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def get(self, user_id: int) -> User:
        """Récupère un utilisateur par son identifiant."""
        resp = self._c.request("GET", f"{USERS_ENDPOINT}/{user_id}")
        return User.model_validate(resp.json())

    def get_address(self, user_id: int) -> Address:
        """Récupère l'adresse d'un utilisateur."""
        resp = self._c.request("GET", f"{USERS_ENDPOINT}/{user_id}/address")
        return Address.model_validate(resp.json())

    def get_companies(self) -> list[UserAndCompany]:
        """Récupère les entreprises associées à l'utilisateur courant."""
        resp = self._c.request("GET", f"{USERS_ENDPOINT}/companies")
        return [UserAndCompany.model_validate(item) for item in resp.json()]

    def authenticate(self) -> TokenResponse:
        """Authentifie via les identifiants du client."""
        return self._c.authenticate()

    def refresh_token(self, refresh_token: str) -> TokenResponse:
        """Rafraîchit le token d'accès."""
        resp = self._c.request(
            "POST",
            "/v1/users/refresh-token",
            authenticated=False,
            json={"refreshToken": refresh_token},
        )
        token = TokenResponse.model_validate(resp.json())
        self._c._access_token = token.access_token  # pylint: disable=W0212
        if token.refresh_token:
            self._c._refresh_token_str = token.refresh_token    # pylint: disable=W0212
        return token
