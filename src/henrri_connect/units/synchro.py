"""Sous-client pour les endpoints /v1/units."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import ListResponse, Unit

if TYPE_CHECKING:
    from ..connect import (
        SyncHenrriClient,
    )

UNITS_ENDPOINT = "/v1/units"

class SyncUnitsClient:
    """Accès synchrone aux unités."""

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def list_units(self) -> ListResponse[Unit]:
        """Liste toutes les unités disponibles."""
        resp = self._c.request("GET", UNITS_ENDPOINT)
        return ListResponse[Unit].model_validate(resp.json())

    def add(self, unit: Unit) -> Unit:
        """Crée une nouvelle unité."""
        resp = self._c.request(
            "POST",
            UNITS_ENDPOINT,
            json=unit.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Unit.model_validate(resp.json())

    def get(self, unit_id: int) -> Unit:
        """Récupère une unité par son identifiant."""
        resp = self._c.request("GET", f"{UNITS_ENDPOINT}/{unit_id}")
        return Unit.model_validate(resp.json())
