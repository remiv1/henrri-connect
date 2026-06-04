"""Tests du sous-client document_lines (synchrone et asynchrone)."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from src.henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient, # type: ignore[import]
)
from src.henrri_connect.models import DocumentLine

from tests.conftest import DOCUMENT_LINE_JSON, make_response


class TestSyncDocumentLines:
    """Tests du sous-client document_lines (synchrone)."""
    def test_list_retourne_lignes(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode list_document_lines()."""
        mock_http.request.return_value = make_response({"elements": [DOCUMENT_LINE_JSON]})

        result = sync_client.document_lines.list_document_lines(100)

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].id == 10
        assert "/v1/documents/100/lines" in mock_http.request.call_args.args[1]

    def test_add_ligne(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode add_document_line()."""
        mock_http.request.return_value = make_response({**DOCUMENT_LINE_JSON, "id": 20})
        line = DocumentLine(type_id=2)  # type: ignore[call-arg]

        result = sync_client.document_lines.add(100, line)

        assert result.id == 20
        assert mock_http.request.call_args.args[0] == "POST"

    def test_get_ligne(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode get_document_line()."""
        mock_http.request.return_value = make_response(DOCUMENT_LINE_JSON)

        result = sync_client.document_lines.get(100, 10)

        assert result.id == 10
        assert "/lines/10" in mock_http.request.call_args.args[1]

    def test_modify_ligne(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode modify_document_line()."""
        updated: dict[str, Any] = {**DOCUMENT_LINE_JSON, "quantity": 3.0}
        mock_http.request.return_value = make_response(updated)

        result = sync_client.document_lines.modify(
            100, 10, DocumentLine(type_id=2)  # type: ignore[call-arg]
            )

        assert result.quantity == pytest.approx(3.0)  # type: ignore[misc]
        assert mock_http.request.call_args.args[0] == "PUT"

    def test_delete_ligne(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode delete_document_line()."""
        mock_http.request.return_value = make_response({})

        sync_client.document_lines.delete(100, 10)

        assert mock_http.request.call_args.args[0] == "DELETE"
        assert "/lines/10" in mock_http.request.call_args.args[1]

    def test_move_ligne(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        """Test de la méthode move_document_line()."""
        mock_http.request.return_value = make_response({})

        sync_client.document_lines.move(100, 10, to=3)

        args = mock_http.request.call_args
        assert args.args[0] == "POST"
        assert "/lines/10/move" in args.args[1]
        assert args.kwargs["params"]["to"] == 3


class TestAsyncDocumentLines:
    """Tests du sous-client document_lines (asynchrone)."""
    async def test_list_retourne_lignes(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode list_document_lines()."""
        mock_async_http.request.return_value = make_response({"elements": [DOCUMENT_LINE_JSON]})

        result = await async_client.document_lines.list_document_lines(100)

        assert result.elements is not None
        assert len(result.elements) == 1

    async def test_add_ligne(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode add_document_line()."""
        mock_async_http.request.return_value = make_response({**DOCUMENT_LINE_JSON, "id": 30})
        line = DocumentLine(type_id=2)  # type: ignore[call-arg]

        result = await async_client.document_lines.add(100, line)

        assert result.id == 30

    async def test_delete_ligne(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        """Test de la méthode delete_document_line()."""
        mock_async_http.request.return_value = make_response({})

        await async_client.document_lines.delete(100, 10)

        assert mock_async_http.request.call_args.args[0] == "DELETE"
