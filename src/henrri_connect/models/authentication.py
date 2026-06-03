"""Modèles pour l'authentification avec l'API Henrri Connect."""

from __future__ import annotations

from .base import CamelModel

class AuthenticateRequest(CamelModel):
    """Représente une requête d'authentification pour obtenir un token d'accès."""
    client_id: str
    client_secret: str


class TokenResponse(CamelModel):
    """Représente la réponse d'une authentification réussie ou d'un rafraîchissement de token."""
    access_token: str | None = None
    identity_token: str | None = None
    scope: str | None = None
    token_type: str | None = None
    refresh_token: str | None = None
    expires_in: int = 0
    is_error: bool = False
    error: str | None = None
    error_description: str | None = None


class RefreshTokenRequest(CamelModel):
    """Représente une requête de rafraîchissement du token d'accès."""
    refresh_token: str
    client_id: str | None = None
    client_secret: str | None = None
    check_point: str | None = None
