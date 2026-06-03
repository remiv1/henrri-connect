"""Tests du sous-client document_line_types (synchrone et asynchrone)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from src.henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient,  # type: ignore[import]
)
from tests.conftest import DOCUMENT_LINE_TYPE_JSON, make_response


class TestSyncDocumentLineTypes:
    def test_list_retourne_types(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({"elements": [DOCUMENT_LINE_TYPE_JSON]})

        result = sync_client.document_line_types.list_document_line_types()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].label == "Article"
        assert result.elements[0].type == "Item"
        assert "/v1/documentlinetypes" in mock_http.request.call_args.args[1]


class TestAsyncDocumentLineTypes:
    async def test_list_retourne_types(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response({"elements": [DOCUMENT_LINE_TYPE_JSON]})

        result = await async_client.document_line_types.list_document_line_types()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].label == "Article"
