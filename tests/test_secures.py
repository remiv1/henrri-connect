"""Tests du sous-client secures (synchrone et asynchrone)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from src.henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient, # type: ignore[import]
)
from tests.conftest import make_response


class TestSyncSecures:
    def test_hello_world_retourne_texte(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        resp = make_response({}, text="Hello World!")
        mock_http.request.return_value = resp

        result = sync_client.secures.hello_world()

        assert result == "Hello World!"
        assert "/v1/secures/hello-world" in mock_http.request.call_args.args[1]
        assert mock_http.request.call_args.args[0] == "GET"


class TestAsyncSecures:
    async def test_hello_world_retourne_texte(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        resp = make_response({}, text="Hello World!")
        mock_async_http.request.return_value = resp

        result = await async_client.secures.hello_world()

        assert result == "Hello World!"
        assert "/v1/secures/hello-world" in mock_async_http.request.call_args.args[1]
