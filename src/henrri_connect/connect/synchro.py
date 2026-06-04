"""
Client HTTP Henrri synchrone.

Constants:
----------
- `henrri_connect.connect.synchro._BASE_URL`:
     URL de base de l'API Henrri.
- `henrri_connect.connect.synchro.APP_VERSION`:
     Version de l'application.
- `henrri_connect.connect.synchro.APP_X_VERSION`:
     Version de l'application.

Classes:
--------
- `henrri_connect.connect.synchro.SyncHenrriClient`:
     Client HTTP Henrri synchrone.

Exemples:
---------
.. code-block:: python

    # Client synchrone
    from henrri_connect import SyncHenrriClient

    client = SyncHenrriClient("client_id", "client_secret", base_url=<URL de base de l'API>)

Exceptions:
----------
- `henrri_connect.exc.HenrriAuthError`:
     Erreur d'authentification (HTTP 401).
"""

from __future__ import annotations

import logging
from typing import Any, TYPE_CHECKING   # pylint: disable=W0611 # type: ignore[import]
import httpx
from ..exc import HenrriAuthError
from ..models import TokenResponse
from ..utils import raise_for_status
if TYPE_CHECKING:
    from ..companies import SyncCompaniesClient
    from ..customers import SyncCustomersClient
    from ..document_line_types import SyncDocumentLineTypesClient
    from ..document_lines import SyncDocumentLinesClient
    from ..document_types import SyncDocumentTypesClient
    from ..documents import SyncDocumentsClient
    from ..item_categories import SyncItemCategoriesClient
    from ..items import SyncItemsClient
    from ..revenues import SyncRevenuesClient
    from ..secures import SyncSecuresClient
    from ..units import SyncUnitsClient
    from ..users import SyncUsersClient

logger = logging.getLogger(__name__)

_BASE_URL = "https://api-sandbox.henrri.io"
APP_VERSION = "application/json"
APP_X_VERSION = "1.0"


class SyncHenrriClient:
    """
    Client HTTP synchrone pour l'API Henrri.
    Gère l'authentification, le refresh-token et les erreurs HTTP.
    Fournit des sous-clients pour chaque groupe d'endpoints (users, companies, etc.)
    Authentification automatique avec gestion du refresh token
    Gestion centralisée des erreurs HTTP avec exceptions personnalisées

    Arguments:
    - client_id: Identifiant client pour l'authentification.
    - client_secret: Secret client pour l'authentification.
    - base_url: URL de base de l'API (défaut : sandbox Henrri).

    Methodes:
    - authenticate: Authentifie le client.
    - request: Effectue une requête HTTP authentifiée.
    - close: Ferme le client HTTP sous-jacent.
    """

    users: "SyncUsersClient"
    companies: "SyncCompaniesClient"
    customers: "SyncCustomersClient"
    documents: "SyncDocumentsClient"
    document_lines: "SyncDocumentLinesClient"
    document_line_types: "SyncDocumentLineTypesClient"
    document_types: "SyncDocumentTypesClient"
    items: "SyncItemsClient"
    item_categories: "SyncItemCategoriesClient"
    units: "SyncUnitsClient"
    revenues: "SyncRevenuesClient"
    secures: "SyncSecuresClient"

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
        self._http = httpx.Client()
        self._init_subclients()

    def _init_subclients(self) -> None:
        from ..companies import SyncCompaniesClient    # pylint: disable=C0415
        from ..customers import SyncCustomersClient    # pylint: disable=C0415
        from ..document_line_types import SyncDocumentLineTypesClient    # pylint: disable=C0415
        from ..document_lines import SyncDocumentLinesClient    # pylint: disable=C0415
        from ..document_types import SyncDocumentTypesClient    # pylint: disable=C0415
        from ..documents import SyncDocumentsClient    # pylint: disable=C0415
        from ..item_categories import SyncItemCategoriesClient    # pylint: disable=C0415
        from ..items import SyncItemsClient    # pylint: disable=C0415
        from ..revenues import SyncRevenuesClient    # pylint: disable=C0415
        from ..secures import SyncSecuresClient    # pylint: disable=C0415
        from ..units import SyncUnitsClient    # pylint: disable=C0415
        from ..users import SyncUsersClient    # pylint: disable=C0415

        self.users = SyncUsersClient(self)
        self.companies = SyncCompaniesClient(self)
        self.customers = SyncCustomersClient(self)
        self.documents = SyncDocumentsClient(self)
        self.document_lines = SyncDocumentLinesClient(self)
        self.document_line_types = SyncDocumentLineTypesClient(self)
        self.document_types = SyncDocumentTypesClient(self)
        self.items = SyncItemsClient(self)
        self.item_categories = SyncItemCategoriesClient(self)
        self.units = SyncUnitsClient(self)
        self.revenues = SyncRevenuesClient(self)
        self.secures = SyncSecuresClient(self)

    def _url(self, path: str) -> str:
        return f"{self._base_url}{path}"

    def _headers(self, *, authenticated: bool = True) -> dict[str, str]:
        headers: dict[str, str] = {
            "Content-Type": APP_VERSION,
            "Accept": APP_VERSION,
            "X-Version": APP_X_VERSION,
        }
        logger.debug("Construction des headers (authentifié=%s)", authenticated)
        if authenticated:
            if not self._access_token:
                logger.error("Tentative de requête authentifiée sans token d'accès.")
                raise HenrriAuthError(
                    401,
                    "Non authentifié. Appelez authenticate() avant toute requête."
                )
            headers["Authorization"] = f"Bearer {self._access_token}"
            logger.debug("Headers avec token d'accès ajouté.")
        return headers

    def authenticate(self) -> TokenResponse:
        """
        Authentifie le client et stocke le token d'accès.

        Arguments:
        - None

        Returns:
        - TokenResponse : objet contenant access_token et refresh_token.
        """
        resp: httpx.Response = self._http.post(
            self._url("/v1/users/authenticate"),
            headers=self._headers(authenticated=False),
            json={"clientId": self._client_id, "clientSecret": self._client_secret},
        )
        raise_for_status(resp)
        token: TokenResponse = TokenResponse.model_validate(resp.json())
        self._access_token = token.access_token
        self._refresh_token_str = token.refresh_token
        logger.debug("Authentification réussie, token d'accès obtenu.")
        logger.info(
            "Authentification réussie. Access token valide pour %d secondes.",
            token.expires_in
        )
        return token

    def _do_refresh(self) -> None:
        """
        Rafraîchit le token via le refresh token, ou ré-authentifie en cas d'échec.
        
        Arguments:
        - None
        
        Returns:
        - None
        """
        resp: httpx.Response = self._http.post(
            self._url("/v1/users/refresh-token"),
            headers=self._headers(authenticated=False),
            json={"refreshToken": self._refresh_token_str},
        )
        if resp.is_success:
            logger.debug("Rafraîchissement du token via le refresh token.")
            token: TokenResponse = TokenResponse.model_validate(resp.json())
            self._access_token = token.access_token
            if token.refresh_token:
                logger.debug("Nouveau refresh token reçu, mise à jour du refresh token stocké.")
                self._refresh_token_str = token.refresh_token
        else:
            self.authenticate()

    def _request(
        self,
        method: str,
        path: str,
        *,
        authenticated: bool = True,
        **kwargs: Any,
    ) -> httpx.Response:
        """
        Effectue une requête HTTP avec gestion automatique de l'authentification.
        
        Arguments:
        - method (str) : Le type de la requête (GET, POST, etc.).
        - path (str) : L'URL de la requête.
        - authenticated (bool, optional) : Indique si la requête doit быть authentifiée.
        - kwargs (dict, optional) : Dictionnaire de paramètres supplémentaires pour la requête.
        
        Returns:
        - httpx.Response : La réponse de la requête.
        
        Raises:
        - HenrriAuthError : Erreur d'authentification.
        """
        if authenticated and not self._access_token:
            self.authenticate()

        logger.debug(
            "Envoi de la requête %s %s (authentifié=%s)",
            method,
            path,
            authenticated,
        )
        resp: httpx.Response = self._http.request(
            method,
            self._url(path),
            headers=self._headers(authenticated=authenticated),
            **kwargs,
        )

        if resp.status_code == 401 and authenticated:
            logger.debug("Réponse 401 reçue, tentative de rafraîchissement du token.")
            if self._refresh_token_str:
                self._do_refresh()
            else:
                self.authenticate()
            resp: httpx.Response = self._http.request(
                method,
                self._url(path),
                headers=self._headers(authenticated=True),
                **kwargs,
            )

        raise_for_status(resp)
        return resp

    def request(self, method: str, endpoint: str, **kwargs: Any) -> httpx.Response:
        """
        Effectue une requête HTTP authentifiée (synchrone).
        
        Args:
            method: Méthode HTTP (GET, POST, etc.).
            endpoint: Chemin relatif (ex: '/v1/companies/42').
            **kwargs: Arguments supplémentaires pour httpx.request().
        
        Returns:
            Réponse HTTP.
        """
        return self._request(method, endpoint, **kwargs)

    def close(self) -> None:
        """
        Ferme le client HTTP sous-jacent.
        
        Args:
        - None
        
        Returns:
        - None
        """
        logger.info("Fermeture du client HTTP.")
        self._http.close()

    def __enter__(self) -> SyncHenrriClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
