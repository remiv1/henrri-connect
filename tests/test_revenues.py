"""Tests du sous-client revenues (synchrone et asynchrone)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from src.henrri_connect.connect import (
    _AsyncHenrriClient, _SyncHenrriClient, # type: ignore[import]
)
from tests.conftest import MONTHLY_REVENUE_JSON, REVENUE_JSON, make_response


class TestSyncRevenues:
    def test_get_annual(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(REVENUE_JSON)

        result = sync_client.revenues.get_annual(2025)

        assert result.year == 2025
        assert result.total_services_revenue == float(50000)
        assert "/v1/revenues/2025" in mock_http.request.call_args.args[1]

    def test_get_monthly(
        self, sync_client: _SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response([MONTHLY_REVENUE_JSON])

        result = sync_client.revenues.get_monthly(2025)

        assert len(result) == 1
        assert result[0].month == 1
        assert result[0].total_services_revenue == float(4000)
        assert "/v1/revenues/2025/months" in mock_http.request.call_args.args[1]


class TestAsyncRevenues:
    async def test_get_annual(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response(REVENUE_JSON)

        result = await async_client.revenues.get_annual(2025)

        assert result.year == 2025
        assert result.total_products_revenue == float(10000)

    async def test_get_monthly(
        self, async_client: _AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response([MONTHLY_REVENUE_JSON])

        result = await async_client.revenues.get_monthly(2025)

        assert len(result) == 1
        assert result[0].month == 1
