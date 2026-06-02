from __future__ import annotations

from typing import Any
import httpx

from ..companies import SyncCompaniesClient
from ..customers import SyncCustomersClient
from ..document_line_types import SyncDocumentLineTypesClient
from ..document_lines import SyncDocumentLinesClient
from ..document_types import SyncDocumentTypesClient
from ..documents import SyncDocumentsClient
from ..item_categories import SyncItemCategoriesClient
from ..items import SyncItemsClient
from ..models import TokenResponse
from ..revenues import SyncRevenuesClient
from ..secures import SyncSecuresClient
from ..units import SyncUnitsClient
from ..users import SyncUsersClient


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
