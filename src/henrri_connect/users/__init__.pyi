"""Stub de type pour le module de gestion des utilisateurs de Henrri Connect."""
from __future__ import annotations

from typing import Any

from ..models import Address, TokenResponse, User, UserAndCompany

class SyncUsersClient:  # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    def get(self, user_id: int) -> User: ...    # pylint: disable=C0116, W0613
    def get_address(self, user_id: int) -> Address: ... # pylint: disable=C0116, W0613
    def get_companies(self) -> list[UserAndCompany]: ...    # pylint: disable=C0116
    def authenticate(self) -> TokenResponse: ...    # pylint: disable=C0116
    def refresh_token(self, refresh_token: str) -> TokenResponse: ...   # pylint: disable=C0116, W0613

class AsyncUsersClient: # pylint: disable=C0115
    def __init__(self, client: Any) -> None: ...    # pylint: disable=W0613
    async def get(self, user_id: int) -> User: ...  # pylint: disable=C0116, W0613
    async def get_address(self, user_id: int) -> Address: ...   # pylint: disable=C0116, W0613
    async def get_companies(self) -> list[UserAndCompany]: ...  # pylint: disable=C0116
    async def authenticate(self) -> TokenResponse: ...  # pylint: disable=C0116
    async def refresh_token(self, refresh_token: str) -> TokenResponse: ... # pylint: disable=C0116, W0613
