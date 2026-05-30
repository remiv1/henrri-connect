from __future__ import annotations

from typing import Any

import httpx

from ..models import TokenResponse
from ..companies import AsyncCompaniesClient, SyncCompaniesClient
from ..customers import AsyncCustomersClient, SyncCustomersClient
from ..document_line_types import (
    AsyncDocumentLineTypesClient,
    SyncDocumentLineTypesClient,
)
from ..document_lines import AsyncDocumentLinesClient, SyncDocumentLinesClient
from ..document_types import AsyncDocumentTypesClient, SyncDocumentTypesClient
from ..documents import AsyncDocumentsClient, SyncDocumentsClient
from ..item_categories import AsyncItemCategoriesClient, SyncItemCategoriesClient
from ..items import AsyncItemsClient, SyncItemsClient
from ..revenues import AsyncRevenuesClient, SyncRevenuesClient
from ..secures import AsyncSecuresClient, SyncSecuresClient
from ..units import AsyncUnitsClient, SyncUnitsClient
from ..users import AsyncUsersClient, SyncUsersClient

class _SyncHenrriClient:
    _client_id: str
    _client_secret: str
    _base_url: str
    _access_token: str | None
    _refresh_token_str: str | None
    _http: httpx.Client
    users: SyncUsersClient
    companies: SyncCompaniesClient
    customers: SyncCustomersClient
    documents: SyncDocumentsClient
    document_lines: SyncDocumentLinesClient
    document_line_types: SyncDocumentLineTypesClient
    document_types: SyncDocumentTypesClient
    items: SyncItemsClient
    item_categories: SyncItemCategoriesClient
    units: SyncUnitsClient
    revenues: SyncRevenuesClient
    secures: SyncSecuresClient

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        *,
        base_url: str = ...,
    ) -> None: ...
    def authenticate(self) -> TokenResponse: ...
    def request(self, method: str, endpoint: str, **kwargs: Any) -> httpx.Response: ...
    def close(self) -> None: ...
    def __enter__(self) -> _SyncHenrriClient: ...
    def __exit__(self, *args: Any) -> None: ...
    def _init_subclients(self) -> None: ...
    def _do_refresh(self) -> None: ...

class _AsyncHenrriClient:
    _client_id: str
    _client_secret: str
    _base_url: str
    _access_token: str | None
    _refresh_token_str: str | None
    _http: httpx.AsyncClient
    users: AsyncUsersClient
    companies: AsyncCompaniesClient
    customers: AsyncCustomersClient
    documents: AsyncDocumentsClient
    document_lines: AsyncDocumentLinesClient
    document_line_types: AsyncDocumentLineTypesClient
    document_types: AsyncDocumentTypesClient
    items: AsyncItemsClient
    item_categories: AsyncItemCategoriesClient
    units: AsyncUnitsClient
    revenues: AsyncRevenuesClient
    secures: AsyncSecuresClient

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        *,
        base_url: str = ...,
    ) -> None: ...
    async def authenticate(self) -> TokenResponse: ...
    async def request(self, method: str, endpoint: str, **kwargs: Any) -> httpx.Response: ...
    async def close(self) -> None: ...
    async def __aenter__(self) -> _AsyncHenrriClient: ...
    async def __aexit__(self, *args: Any) -> None: ...
    async def _init_subclients(self) -> None: ...
    async def _do_refresh(self) -> None: ...

class HenrriClient:
    def __new__(
        cls,
        client_id: str,
        client_secret: str,
        *,
        base_url: str = ...,
        async_mode: bool = False,
    ) -> _SyncHenrriClient | _AsyncHenrriClient: ...
