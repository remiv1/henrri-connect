"""Stub pour le module companies."""
from __future__ import annotations

from typing import Any
from ..models import Address, Company

class SyncCompaniesClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    def get(self, company_id: int) -> Company: ...  # pylint: disable=C0116, W0613
    def get_address(self, company_id: int) -> Address: ...  # pylint: disable=C0116, W0613

class AsyncCompaniesClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    async def get(self, company_id: int) -> Company: ...  # pylint: disable=C0116, W0613
    async def get_address(self, company_id: int) -> Address: ...  # pylint: disable=C0116, W0613
