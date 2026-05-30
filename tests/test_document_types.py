"""Tests du sous-client document_types (synchrone et asynchrone)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from src.henrri_connect.connect import (
    _AsyncHenrriClient, _SyncHenrriClient, # type: ignore[import]
)
from tests.conftest import DOCUMENT_TYPE_JSON, make_response


class TestSyncDocumentTypes:
    def test_list_retourne_types(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({"elements": [DOCUMENT_TYPE_JSON]})

        result = sync_client.document_types.list_document_types()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].label == "Facture"
        assert result.elements[0].document_kind == "Invoice"
        assert "/v1/documenttypes" in mock_http.request.call_args.args[1]


class TestAsyncDocumentTypes:
    async def test_list_retourne_types(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response({"elements": [DOCUMENT_TYPE_JSON]})

        result = await async_client.document_types.list_document_types()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].label == "Facture"
