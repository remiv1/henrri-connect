"""
Sous-client pour les endpoints /v1/units.

Classes:
- ``henrri_connect.units.synchro.SyncUnitsClient`` : Accès synchrone aux endpoints unités.

Notes:
- Utiliser de préférence l'objet ``henrri_connect.SyncHenrriClient`` pour acceder aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import ListResponse, Unit

if TYPE_CHECKING:
    from ..connect import (
        SyncHenrriClient,
    )

UNITS_ENDPOINT = "/v1/units"

class SyncUnitsClient:
    """
    Accès synchrone aux unités.

    Arguments
    - client (SyncHenrriClient) : Client synchrone pour acceder aux endpoints.

    Methods
    - list_units() : Liste toutes les unités disponibles.
    - add(unit: Unit) : Crée une nouvelle unité.
    - get(unit_id: int) : Récupère une unité par son identifiant.
    """

    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def list_units(self) -> ListResponse[Unit]:
        """
        Liste toutes les unités disponibles.

        Arguments
        - ``None``

        Returns
        - ``ListResponse[Unit]`` : Liste de unités.
        """
        resp = self._c.request("GET", UNITS_ENDPOINT)
        return ListResponse[Unit].model_validate(resp.json())

    def add(self, unit: Unit) -> Unit:
        """
        Crée une nouvelle unité.

        Arguments
        - ``unit: Unit`` : Unité à crée.

        Returns
        - ``Unit`` : Unité crée.
        """
        resp = self._c.request(
            "POST",
            UNITS_ENDPOINT,
            json=unit.model_dump(by_alias=True, exclude_unset=True, exclude_none=True),
        )
        return Unit.model_validate(resp.json())

    def get(self, unit_id: int) -> Unit:
        """
        Récupère une unité par son identifiant.

        Arguments
        - ``unit_id`` (int) : Identifiant de l'unité.

        Returns
        - ``Unit`` : Unité.
        """
        resp = self._c.request("GET", f"{UNITS_ENDPOINT}/{unit_id}")
        return Unit.model_validate(resp.json())
