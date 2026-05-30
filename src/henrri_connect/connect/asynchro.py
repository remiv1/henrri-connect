"""Client HTTP Henrri : factory et implémentations synchrone/asynchrone."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any    # type: ignore[import]
import httpx
from ..exc import (
    HenrriAuthError,
)
from ..models import TokenResponse
from ..utils import raise_for_status

logger = logging.getLogger(__name__)

_BASE_URL = "https://api-sandbox.henrri.io"
APP_VERSION = "application/json; X-Version=1.0"

class _AsyncHenrriClient:
    """
    Client HTTP asynchrone pour l'API Henrri.
    Gère l'authentification, le refresh-token et les erreurs HTTP.
    Fournit des sous-clients pour chaque groupe d'endpoints (users, companies, etc.)
    Authentification automatique avec gestion du refresh token
    Gestion centralisée des erreurs HTTP avec exceptions personnalisées
    Args:
    - client_id: Identifiant client pour l'authentification.
    - client_secret: Secret client pour l'authentification.
    - base_url: URL de base de l'API (défaut : sandbox Henrri).
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        *,
        base_url: str = _BASE_URL,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = base_url.rstrip("/")
        self._access_token: str | None = None
        self._refresh_token_str: str | None = None
        self._http = httpx.AsyncClient(timeout=30.0)
        self._init_subclients()

    def _init_subclients(self) -> None:
        from ..companies import AsyncCompaniesClient
        from ..customers import AsyncCustomersClient
        from ..document_line_types import AsyncDocumentLineTypesClient
        from ..document_lines import AsyncDocumentLinesClient
        from ..document_types import AsyncDocumentTypesClient
        from ..documents import AsyncDocumentsClient
        from ..item_categories import AsyncItemCategoriesClient
        from ..items import AsyncItemsClient
        from ..revenues import AsyncRevenuesClient
        from ..secures import AsyncSecuresClient
        from ..units import AsyncUnitsClient
        from ..users import AsyncUsersClient

        self.users = AsyncUsersClient(self)
        self.companies = AsyncCompaniesClient(self)
        self.customers = AsyncCustomersClient(self)
        self.documents = AsyncDocumentsClient(self)
        self.document_lines = AsyncDocumentLinesClient(self)
        self.document_line_types = AsyncDocumentLineTypesClient(self)
        self.document_types = AsyncDocumentTypesClient(self)
        self.items = AsyncItemsClient(self)
        self.item_categories = AsyncItemCategoriesClient(self)
        self.units = AsyncUnitsClient(self)
        self.revenues = AsyncRevenuesClient(self)
        self.secures = AsyncSecuresClient(self)

    def _url(self, path: str) -> str:
        return f"{self._base_url}{path}"

    def _headers(self, *, authenticated: bool = True) -> dict[str, str]:
        headers: dict[str, str] = {
            "Content-Type": APP_VERSION,
            "Accept": APP_VERSION,
        }
        logger.debug("Construction des headers (authentifié=%s)", authenticated)
        if authenticated:
            if not self._access_token:
                logger.error("Tentative de requête authentifiée sans token d'accès.")
                raise HenrriAuthError(
                    401,
                    "Non authentifié. Appelez await authenticate() avant toute requête."
                )
            headers["Authorization"] = f"Bearer {self._access_token}"
            logger.debug("Headers avec token d'accès ajouté.")
        return headers

    async def authenticate(self) -> TokenResponse:
        """Authentifie le client et stocke le token d'accès."""
        resp = await self._http.post(
            self._url("/v1/users/authenticate"),
            headers=self._headers(authenticated=False),
            json={"clientId": self._client_id, "clientSecret": self._client_secret},
        )
        raise_for_status(resp)
        token = TokenResponse.model_validate(resp.json())
        self._access_token = token.access_token
        self._refresh_token_str = token.refresh_token
        logger.debug("Authentification réussie, token d'accès obtenu.")
        logger.info(
            "Authentification réussie. Access token valide pour %d secondes.",
            token.expires_in
        )
        return token

    async def _do_refresh(self) -> None:
        """Rafraîchit le token via le refresh token, ou ré-authentifie en cas d'échec."""
        resp = await self._http.post(
            self._url("/v1/users/refresh-token"),
            headers=self._headers(authenticated=False),
            json={"refreshToken": self._refresh_token_str},
        )
        if resp.is_success:
            logger.debug("Rafraîchissement du token via le refresh token.")
            token = TokenResponse.model_validate(resp.json())
            self._access_token = token.access_token
            if token.refresh_token:
                logger.debug("Nouveau refresh token reçu, mise à jour du refresh token stocké.")
                self._refresh_token_str = token.refresh_token
        else:
            await self.authenticate()

    async def _request(
        self,
        method: str,
        path: str,
        *,
        authenticated: bool = True,
        **kwargs: Any,
    ) -> httpx.Response:
        """Effectue une requête HTTP avec gestion automatique de l'authentification."""
        if authenticated and not self._access_token:
            await self.authenticate()

        logger.debug(
            "Envoi de la requête %s %s (authentifié=%s)",
            method,
            path,
            authenticated,
        )
        resp = await self._http.request(
            method,
            self._url(path),
            headers=self._headers(authenticated=authenticated),
            **kwargs,
        )

        if resp.status_code == 401 and authenticated:
            logger.debug("Réponse 401 reçue, tentative de rafraîchissement du token.")
            if self._refresh_token_str:
                await self._do_refresh()
            else:
                await self.authenticate()
            resp = await self._http.request(
                method,
                self._url(path),
                headers=self._headers(authenticated=True),
                **kwargs,
            )

        raise_for_status(resp)
        return resp

    async def request(self, method: str, endpoint: str, **kwargs: Any) -> httpx.Response:
        """Effectue une requête HTTP authentifiée (asynchrone).
        
        Args:
            method: Méthode HTTP (GET, POST, etc.).
            endpoint: Chemin relatif (ex: '/v1/companies/42').
            **kwargs: Arguments supplémentaires pour httpx.request().
        
        Returns:
            Réponse HTTP.
        """
        return await self._request(method, endpoint, **kwargs)

    async def close(self) -> None:
        """
        Ferme le client HTTP sous-jacent.
        - Arguments:
            - None
        - Returns:
            - None
        """
        logger.info("Fermeture du client HTTP.")
        await self._http.aclose()

    async def __aenter__(self) -> _AsyncHenrriClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
