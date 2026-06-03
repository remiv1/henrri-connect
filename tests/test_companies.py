"""Tests du sous-client companies (synchrone et asynchrone)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from src.henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient,  # type: ignore[import]
)
from tests.conftest import COMPANY_JSON, make_response


class TestSyncCompanies:
    def test_get_retourne_company(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(COMPANY_JSON)

        company = sync_client.companies.get(42)

        assert company.id == 42
        assert company.name == "Ma Société"
        args = mock_http.request.call_args
        assert args.args[0] == "GET"
        assert "/v1/companies/42" in args.args[1]

    def test_get_address(
        self, sync_client: SyncHenrriClient, mock_http: MagicMock
    ) -> None:
        mock_http.request.return_value = make_response(
            {"id": 1, "city": "Paris", "isPostCodeShared": False}
        )

        address = sync_client.companies.get_address(42)

        assert address.city == "Paris"
        args = mock_http.request.call_args
        assert "/v1/companies/42/address" in args.args[1]


class TestAsyncCompanies:
    async def test_get_retourne_company(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response(COMPANY_JSON)

        company = await async_client.companies.get(42)

        assert company.id == 42
        assert company.name == "Ma Société"

    async def test_get_address(
        self, async_client: AsyncHenrriClient, mock_async_http: AsyncMock
    ) -> None:
        mock_async_http.request.return_value = make_response(
            {"id": 1, "city": "Lyon", "isPostCodeShared": False}
        )

        address = await async_client.companies.get_address(42)

        assert address.city == "Lyon"
