"""Tests du sous-client users (synchrone et asynchrone)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from src.henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient, # type: ignore[import]
)
from tests.conftest import TOKEN_JSON, USER_JSON, make_response


class TestSyncUsers:
    """Tests du sous-client users (synchrone)."""
    def test_get_retourne_utilisateur(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode get_user()."""
        mock_http.request.return_value = make_response(USER_JSON)

        user = sync_client.users.get(7)

        assert user.id == 7
        assert user.email == "user@example.com"
        assert "/v1/users/7" in mock_http.request.call_args.args[1]

    def test_get_address(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode get_address()."""
        mock_http.request.return_value = make_response(
            {"id": 1, "city": "Paris", "isPostCodeShared": False}
        )

        address = sync_client.users.get_address(7)

        assert address.city == "Paris"
        assert "/v1/users/7/address" in mock_http.request.call_args.args[1]

    def test_get_companies(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode get_companies()."""
        mock_http.request.return_value = make_response(
            [
                {
                    "user": USER_JSON,
                    "company": {"id": 42, "name": "Ma Société", "isSelfEmployed": False},
                }
            ]
        )

        result = sync_client.users.get_companies()

        assert len(result) == 1
        assert result[0].company.name == "Ma Société"
        assert "/v1/users/companies" in mock_http.request.call_args.args[1]

    def test_refresh_token(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode refresh_token()."""
        mock_http.request.return_value = make_response(TOKEN_JSON)

        token = sync_client.users.refresh_token("old_refresh")

        assert token.access_token == "new_access_token"
        assert sync_client._access_token == "new_access_token"  # pylint: disable=W0212


class TestAsyncUsers:
    """Tests du sous-client users (asynchrone)."""
    async def test_get_retourne_utilisateur(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode get_user()."""
        mock_async_http.request.return_value = make_response(USER_JSON)

        user = await async_client.users.get(7)

        assert user.id == 7
        assert user.email == "user@example.com"

    async def test_get_companies(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode get_companies()."""
        mock_async_http.request.return_value = make_response(
            [
                {
                    "user": USER_JSON,
                    "company": {"id": 5, "name": "Async SA", "isSelfEmployed": True},
                }
            ]
        )

        result = await async_client.users.get_companies()

        assert result[0].company.name == "Async SA"

    async def test_refresh_token(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode refresh_token()."""
        mock_async_http.request.return_value = make_response(TOKEN_JSON)

        token = await async_client.users.refresh_token("old_refresh")

        assert token.access_token == "new_access_token"
