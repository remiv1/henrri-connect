from __future__ import annotations

from typing import overload, Literal

from .synchro import _SyncHenrriClient
from .asynchro import _AsyncHenrriClient


class HenrriClient:
    @overload
    def __new__(
        cls,
        client_id: str,
        client_secret: str,
        *,
        base_url: str = ...,
        async_mode: Literal[False] = False,
    ) -> _SyncHenrriClient: ...
    @overload
    def __new__(
        cls,
        client_id: str,
        client_secret: str,
        *,
        base_url: str = ...,
        async_mode: Literal[True],
    ) -> _AsyncHenrriClient: ...
    def __new__(
        cls,
        client_id: str,
        client_secret: str,
        *,
        base_url: str = ...,
        async_mode: bool = False,
    ) -> _SyncHenrriClient | _AsyncHenrriClient: ...


SyncHenrriClient = _SyncHenrriClient
AsyncHenrriClient = _AsyncHenrriClient

__all__ = ["HenrriClient", "_SyncHenrriClient", "_AsyncHenrriClient"]