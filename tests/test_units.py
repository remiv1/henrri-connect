"""Tests du sous-client units (synchrone et asynchrone)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from src.henrri_connect.connect import (
    _AsyncHenrriClient, _SyncHenrriClient, # type: ignore[import]
)
from src.henrri_connect.models import Unit
from tests.conftest import UNIT_JSON, make_response


class TestSyncUnits:
    def test_list_retourne_unites(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({"elements": [UNIT_JSON]})

        result = sync_client.units.list_units()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].name == "Heure"
        assert "/v1/units" in mock_http.request.call_args.args[1]

    def test_add_cree_unite(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response({**UNIT_JSON, "id": 10})
        unit = Unit(name="Jour", unit_kind="Specific")  # type: ignore[call-arg]

        result = sync_client.units.add(unit)

        assert result.id == 10
        assert mock_http.request.call_args.args[0] == "POST"

    def test_get_retourne_unite(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(UNIT_JSON)

        result = sync_client.units.get(3)

        assert result.id == 3
        assert result.name == "Heure"
        assert "/v1/units/3" in mock_http.request.call_args.args[1]


class TestAsyncUnits:
    async def test_list_retourne_unites(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response({"elements": [UNIT_JSON]})

        result = await async_client.units.list_units()

        assert result.elements is not None
        assert len(result.elements) == 1
        assert result.elements[0].name == "Heure"

    async def test_get_retourne_unite(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response(UNIT_JSON)

        result = await async_client.units.get(3)

        assert result.id == 3
