"""Façade principale du package henrri_connect."""
from .connect import AsyncHenrriClient, SyncHenrriClient

__all__ = [
    "AsyncHenrriClient",
    "SyncHenrriClient",
]
