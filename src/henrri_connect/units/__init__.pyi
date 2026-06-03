"""Stub de type pour le module de gestion des unités de Henrri Connect."""
from __future__ import annotations

from typing import Any

from ..models import ListResponse, Unit

class SyncUnitsClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    def list_units(self) -> ListResponse[Unit]: ... # pylint: disable=C0116
    def add(self, unit: Unit) -> Unit: ...  # pylint: disable=W0613, C0116
    def get(self, unit_id: int) -> Unit: ... # pylint: disable=W0613, C0116

class AsyncUnitsClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    async def list_units(self) -> ListResponse[Unit]: ...   # pylint: disable=C0116
    async def add(self, unit: Unit) -> Unit: ...    # pylint: disable=W0613, C0116
    async def get(self, unit_id: int) -> Unit: ...   # pylint: disable=W0613, C0116
