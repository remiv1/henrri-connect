"""Sous-client pour les endpoints /v1/users."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import Address, TokenResponse, User, UserAndCompany

if TYPE_CHECKING:
    from ..connect import (
        _AsyncHenrriClient,   # type: ignore[import]
    )

USERS_ENDPOINT = "/v1/users"

class AsyncUsersClient:
    """Accès asynchrone aux endpoints utilisateurs."""

    def __init__(self, client: _AsyncHenrriClient) -> None:
        self._c = client

    async def get(self, id: int) -> User:
        """Récupère un utilisateur par son identifiant."""
        resp = await self._c.request("GET", f"/v1/users/{id}")
        return User.model_validate(resp.json())

    async def get_address(self, id: int) -> Address:
        """Récupère l'adresse d'un utilisateur."""
        resp = await self._c.request("GET", f"/v1/users/{id}/address")
        return Address.model_validate(resp.json())

    async def get_companies(self) -> list[UserAndCompany]:
        """Récupère les entreprises associées à l'utilisateur courant."""
        resp = await self._c.request("GET", "/v1/users/companies")
        return [UserAndCompany.model_validate(item) for item in resp.json()]

    async def authenticate(self) -> TokenResponse:
        """Authentifie via les identifiants du client."""
        return await self._c.authenticate()

    async def refresh_token(self, refresh_token: str) -> TokenResponse:
        """Rafraîchit le token d'accès."""
        resp = await self._c.request(
            "POST",
            "/v1/users/refresh-token",
            authenticated=False,
            json={"refreshToken": refresh_token},
        )
        token = TokenResponse.model_validate(resp.json())
        self._c._access_token = token.access_token
        if token.refresh_token:
            self._c._refresh_token_str = token.refresh_token
        return token
