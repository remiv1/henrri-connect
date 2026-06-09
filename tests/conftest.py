"""Fixtures partagées pour l'ensemble des tests henrri-connect."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest

from henrri_connect.connect import (
    AsyncHenrriClient, SyncHenrriClient, # type: ignore[import]
    )


def make_response(
    data: dict[str, Any] | list[Any],
    status_code: int = 200,
    content: bytes | None = None,
    text: str = "",
) -> MagicMock:
    """Construit une réponse httpx mockée."""
    mock = MagicMock(spec=httpx.Response)
    mock.status_code = status_code
    mock.is_success = status_code < 400
    mock.json.return_value = data
    mock.content = content or b""
    mock.text = text
    return mock


def _build_sync_client(mock_http: MagicMock) -> SyncHenrriClient:   # pylint: disable=W0621
    """Crée un client synchrone avec HTTP mocké (sans __init__)."""
    client: SyncHenrriClient = SyncHenrriClient.__new__(SyncHenrriClient)
    client._client_id = "test_id"   # pylint: disable=W0212
    client._client_secret = "test_secret"   # pylint: disable=W0212
    client._base_url = "https://api-sandbox.henrri.io"  # pylint: disable=W0212
    client._access_token = "fake_access_token"  # pylint: disable=W0212
    client._refresh_token_str = "fake_refresh_token"    # pylint: disable=W0212
    client._http = mock_http    # pylint: disable=W0212
    client._init_subclients()   # pylint: disable=W0212
    return client


def _build_async_client(mock_http: AsyncMock) -> AsyncHenrriClient: # pylint: disable=W0621
    """Crée un client asynchrone avec HTTP mocké (sans __init__)."""
    client: AsyncHenrriClient = AsyncHenrriClient.__new__(AsyncHenrriClient)
    client._client_id = "test_id"   # pylint: disable=W0212
    client._client_secret = "test_secret"   # pylint: disable=W0212
    client._base_url = "https://api-sandbox.henrri.io"  # pylint: disable=W0212
    client._access_token = "fake_access_token"  # pylint: disable=W0212
    client._refresh_token_str = "fake_refresh_token"    # pylint: disable=W0212
    client._http = mock_http    # pylint: disable=W0212
    client._init_subclients()   # type: ignore[union-attr]  # pylint: disable=W0212
    return client   # pylint: disable=W0212


@pytest.fixture
def mock_http() -> MagicMock:
    """Mock httpx.Client."""
    return MagicMock(spec=httpx.Client)


@pytest.fixture
def mock_async_http() -> AsyncMock:
    """Mock httpx.AsyncClient."""
    return AsyncMock(spec=httpx.AsyncClient)


@pytest.fixture
def sync_client(mock_http: MagicMock) -> SyncHenrriClient: # pylint: disable=W0621
    """Client synchrone prêt à l'emploi avec HTTP mocké."""
    return _build_sync_client(mock_http)


@pytest.fixture
async def async_client(mock_async_http: AsyncMock) -> AsyncHenrriClient: # pylint: disable=W0621
    """Client asynchrone prêt à l'emploi avec HTTP mocké."""
    return _build_async_client(mock_async_http)


# ── Helpers de données de test ────────────────────────────────────────────────

CUSTOMER_JSON: dict[str, Any] = {
    "id": 1,
    "name": "Acme Corp",
    "type": "professional",
    "accountingNumber": "411000",
    "isDeleted": False,
    "isSupplier": False,
    "serviceDiscountPercentage": 0.0,
    "productDiscountPercentage": 0.0,
    "customerTypeAlertEnabled": False,
}

COMPANY_JSON: dict[str, Any] = {
    "id": 42,
    "name": "Ma Société",
    "isSelfEmployed": False,
}

USER_JSON: dict[str, Any] = {
    "id": 7,
    "email": "user@example.com",
    "firstName": "Jean",
    "lastName": "Dupont",
    "isEnabled": True,
    "twoFactorEnabled": False,
}

DOCUMENT_JSON: dict[str, Any] = {
    "id": 100,
    "documentTypeId": 1,
    "customerId": 1,
    "finalized": False,
    "priceBeforeTax": 100.0,
    "taxAmount": 20.0,
    "priceAfterTax": 120.0,
    "validated": False,
    "userCanValidate": False,
}

DOCUMENT_LINE_JSON: dict[str, Any] = {
    "id": 10,
    "documentId": 100,
    "typeId": 2,
    "quantity": 1.0,
    "purchasingPriceWithoutTax": 0.0,
    "isATaxIncluded": False,
    "areElementsOfGroupShown": False,
    "isAGroup": False,
    "doesGroupOwnDifferentVat": False,
    "isMemberOfAGroup": False,
    "isAdjustmentOfGroup": False,
}

UNIT_JSON: dict[str, Any] = {
    "id": 3,
    "name": "Heure",
    "unitKind": "Hourly",
}

ITEM_JSON: dict[str, Any] = {
    "id": 5,
    "description": "Prestation de conseil",
    "vatPercent": 20.0,
    "creationDate": "2025-01-01T00:00:00",
    "isATaxIncluded": False,
    "purchasePrice": 0.0,
    "isAGroup": False,
}

ITEM_CATEGORY_JSON: dict[str, Any] = {
    "id": 2,
    "label": "Services",
    "marginPercent": 0.0,
    "hourlyRate": 0.0,
    "vat": 20.0,
    "isAddedToRevenue": True,
    "isDefault": False,
    "isDeleted": False,
    "itemCategoryKind": "Service",
}

DOCUMENT_TYPE_JSON: dict[str, Any] = {
    "id": 1,
    "label": "Facture",
    "shortLabel": "FA",
    "documentKind": "Invoice",
    "isAccounting": True,
    "isManaged": True,
    "isMandatory": False,
    "isVisible": True,
}

DOCUMENT_LINE_TYPE_JSON: dict[str, Any] = {
    "id": 1,
    "label": "Article",
    "type": "Item",
}

TOKEN_JSON: dict[str, Any] = {
    "accessToken": "new_access_token",
    "refreshToken": "new_refresh_token",
    "expiresIn": 3600,
    "isError": False,
}

REVENUE_JSON: dict[str, Any] = {
    "year": 2025,
    "totalServicesRevenue": 50000.0,
    "totalProductsRevenue": 10000.0,
    "totalProductsMargin": 3000.0,
    "totalServiceHours": 500.0,
}

MONTHLY_REVENUE_JSON: dict[str, Any] = {
    "month": 1,
    "year": 2025,
    "totalServicesRevenue": 4000.0,
    "totalProductsRevenue": 800.0,
    "totalProductsMargin": 250.0,
    "totalServiceHours": 40.0,
}

PAGED_META: dict[str, Any] = {
    "page": 1,
    "limit": 50,
    "totalCount": 1,
    "totalPages": 1,
    "hasNext": False,
}
