"""Stub de type pour le module de sécurités de Henrri Connect."""
from __future__ import annotations

from typing import Any

class SyncSecuresClient:    # pylint: disable=C0115, R0903
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    def hello_world(self) -> str: ...   # pylint: disable=C0116

class AsyncSecuresClient:   # pylint: disable=C0115, R0903
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    async def hello_world(self) -> str: ... # pylint: disable=C0116
