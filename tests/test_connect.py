"""Tests du client principal : authentification, refresh token et gestion des erreurs HTTP."""

from __future__ import annotations

import json
from unittest.mock import MagicMock

import pytest

from src.henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient,  # type: ignore[import]
)
from src.henrri_connect.exc import (
    HenrriAuthError,
    HenrriForbiddenError,
    HenrriNotFoundError,
    HenrriServerError,
    HenrriValidationError,
)
from tests.conftest import TOKEN_JSON, make_response


# ── Authentification synchrone ────────────────────────────────────────────────


class TestSyncAuthenticate:
    def test_stocke_access_token(self, mock_http: MagicMock) -> None:
        """Le token d'accès est stocké après authentification réussie."""
        mock_http.post.return_value = make_response(TOKEN_JSON)
        client = SyncHenrriClient.__new__(SyncHenrriClient)
        client._client_id = "id"
        client._client_secret = "secret"
        client._base_url = "https://api-sandbox.henrri.io"
        client._access_token = None
        client._refresh_token_str = None
        client._http = mock_http
        client._init_subclients()

        token = client.authenticate()

        assert token.access_token == "new_access_token"
        assert client._access_token == "new_access_token"
        assert client._refresh_token_str == "new_refresh_token"

    def test_auto_authenticate_avant_requete(self, mock_http: MagicMock) -> None:
        """La première requête déclenche automatiquement l'authentification."""
        mock_http.post.return_value = make_response(TOKEN_JSON)
        mock_http.request.return_value = make_response({"id": 1})

        client = SyncHenrriClient.__new__(SyncHenrriClient)
        client._client_id = "id"
        client._client_secret = "secret"
        client._base_url = "https://api-sandbox.henrri.io"
        client._access_token = None
        client._refresh_token_str = None
        client._http = mock_http
        client._init_subclients()

        client.request("GET", "/v1/companies/1")

        mock_http.post.assert_called_once()


# ── Refresh token synchrone ───────────────────────────────────────────────────


class TestSyncRefreshToken:
    def test_refresh_succes(self, sync_client: SyncHenrriClient, mock_http: MagicMock) -> None:
        """Le refresh token met à jour l'access token."""
        mock_http.post.return_value = make_response(TOKEN_JSON)

        sync_client._do_refresh()

        assert sync_client._access_token == "new_access_token"

    def test_refresh_echec_reauthentifie(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """En cas d'échec du refresh, le client se ré-authentifie."""
        mock_http.post.side_effect = [
            make_response({}, status_code=401),  # refresh échoue
            make_response(TOKEN_JSON),             # ré-authentification réussit
        ]

        sync_client._do_refresh()

        assert mock_http.post.call_count == 2


# ── Gestion des erreurs HTTP ──────────────────────────────────────────────────


class TestRaiseForStatus:
    @pytest.mark.parametrize(
        "status_code, exc_class",
        [
            (400, HenrriValidationError),
            (403, HenrriForbiddenError),
            (404, HenrriNotFoundError),
            (500, HenrriServerError),
            (503, HenrriServerError),
        ],
    )
    def test_leve_exception_selon_code_http(
        self,
        sync_client: SyncHenrriClient,
        mock_http: MagicMock,
        status_code: int,
        exc_class: type,
    ) -> None:
        """Chaque code HTTP d'erreur lève l'exception appropriée."""
        mock_http.request.return_value = make_response(
            {"detail": "erreur"}, status_code=status_code
        )
        with pytest.raises(exc_class):
            sync_client.request("GET", "/v1/companies/1")

    def test_leve_auth_error_apres_refresh_echec(
        self,
        sync_client: SyncHenrriClient,
        mock_http: MagicMock,
    ) -> None:
        """Un 401 persistant après refresh lève HenrriAuthError."""
        # Refresh réussit (retourne un token valide), mais la requête répond toujours 401
        mock_http.post.return_value = make_response(TOKEN_JSON)
        mock_http.request.return_value = make_response({"detail": "erreur"}, status_code=401)

        with pytest.raises(HenrriAuthError):
            sync_client.request("GET", "/v1/companies/1")

    def test_erreur_json_invalide_utilise_texte(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Si le corps de la réponse n'est pas du JSON valide, le texte brut est utilisé."""
        resp = make_response({}, status_code=400, text="Bad Request")
        resp.json.side_effect = json.JSONDecodeError("Expecting value", "", 0)
        mock_http.request.return_value = resp

        with pytest.raises(HenrriValidationError) as exc_info:
            sync_client.request("GET", "/v1/companies/1")

        assert "Bad Request" in str(exc_info.value)


# ── Authentification asynchrone ───────────────────────────────────────────────


class TestAsyncAuthenticate:
    async def test_stocke_access_token(self, mock_async_http: MagicMock) -> None:
        """Le token d'accès est stocké après authentification asynchrone réussie."""
        mock_async_http.post.return_value = make_response(TOKEN_JSON)

        client = AsyncHenrriClient.__new__(AsyncHenrriClient)
        client._client_id = "id"
        client._client_secret = "secret"
        client._base_url = "https://api-sandbox.henrri.io"
        client._access_token = None
        client._refresh_token_str = None
        client._http = mock_async_http
        client._init_subclients()   # type: ignore[union-attr]

        token = await client.authenticate()

        assert token.access_token == "new_access_token"
        assert client._access_token == "new_access_token"
