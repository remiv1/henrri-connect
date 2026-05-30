"""Sous-client pour les endpoints /v1/companies."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import Address, Company

if TYPE_CHECKING:
    from ..connect import (
        _AsyncHenrriClient,    # type: ignore[import]
    )

COMPANIES_ENDPOINT = "/v1/companies"

class AsyncCompaniesClient:
    """Accès asynchrone aux endpoints entreprises."""

    def __init__(self, client: _AsyncHenrriClient) -> None:
        self._c = client

    async def get(self, company_id: int) -> Company:
        """Récupère une entreprise par son identifiant."""
        resp = await self._c.request("GET", f"{COMPANIES_ENDPOINT}/{company_id}")
        return Company.model_validate(resp.json())

    async def get_address(self, company_id: int) -> Address:
        """Récupère l'adresse d'une entreprise."""
        resp = await self._c.request("GET", f"{COMPANIES_ENDPOINT}/{company_id}/address")
        return Address.model_validate(resp.json())
