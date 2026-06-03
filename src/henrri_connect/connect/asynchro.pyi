"""Fichier Stub pour le module connect.asynchro."""
from __future__ import annotations

from typing import Any
import httpx

from ..companies import AsyncCompaniesClient
from ..customers import AsyncCustomersClient
from ..document_line_types import AsyncDocumentLineTypesClient
from ..document_lines import AsyncDocumentLinesClient
from ..document_types import AsyncDocumentTypesClient
from ..documents import AsyncDocumentsClient
from ..item_categories import AsyncItemCategoriesClient
from ..items import AsyncItemsClient
from ..models import TokenResponse
from ..revenues import AsyncRevenuesClient
from ..secures import AsyncSecuresClient
from ..units import AsyncUnitsClient
from ..users import AsyncUsersClient


class AsyncHenrriClient:  # pylint: disable=C0115
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
        client_id: str, # pylint: disable=W0613
        client_secret: str, # pylint: disable=W0613
        *,
        base_url: str = ..., # pylint: disable=W0613
    ) -> None: ...
    async def authenticate(self) -> TokenResponse: ...  # pylint: disable=C0116
    async def request(self, method: str, endpoint: str, **kwargs: Any) -> httpx.Response: ... # pylint: disable=W0613, C0116
    async def close(self) -> None: ...  # pylint: disable=C0116
    async def __aenter__(self) -> AsyncHenrriClient: ...
    async def __aexit__(self, *args: Any) -> None: ...
    async def _init_subclients(self) -> None: ...
    async def _do_refresh(self) -> None: ...
