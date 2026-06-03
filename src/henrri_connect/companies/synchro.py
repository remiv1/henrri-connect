"""Sous-client pour les endpoints /v1/companies."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import Address, Company

if TYPE_CHECKING:
    from ..connect import (
        SyncHenrriClient,
    )

class SyncCompaniesClient:
    """Accès synchrone aux endpoints entreprises."""

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def get(self, company_id: int) -> Company:
        """Récupère une entreprise par son identifiant."""
        resp = self._c.request("GET", f"/v1/companies/{company_id}")
        return Company.model_validate(resp.json())

    def get_address(self, company_id: int) -> Address:
        """Récupère l'adresse d'une entreprise."""
        resp = self._c.request("GET", f"/v1/companies/{company_id}/address")
        return Address.model_validate(resp.json())
