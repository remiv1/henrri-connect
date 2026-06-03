"""
Modèles pour l'authentification avec l'API Henrri Connect.

Attributs:
- AuthenticateRequest: Représente une requête d'authentification pour obtenir un token d'accès.
- TokenResponse: Représente la réponse d'une authentification réussie ou d'un rafraîchissement
de token.
- RefreshTokenRequest: Représente une requête de rafraîchissement du token d'accès.
"""

from __future__ import annotations

from .base import CamelModel

class AuthenticateRequest(CamelModel):
    """
    Représente une requête d'authentification pour obtenir un token d'accès.
    
    Attributs:
    - client_id: Identifiant du client.
    - client_secret: Secret du client.
    """
    client_id: str
    client_secret: str


class TokenResponse(CamelModel):
    """
    Représente la réponse d'une authentification réussie ou d'un rafraîchissement de token.

    Attributs:
    - access_token: Token d'accès.
    - identity_token: Token d'identité.
    - scope: Portée du token.
    - token_type: Type du token.
    - refresh_token: Token de rafraîchissement.
    - expires_in: Durée de validité du token en secondes.
    - is_error: Indique si la réponse contient une erreur.
    - error: Code de l'erreur (si applicable).
    - error_description: Description de l'erreur (si applicable).
    """
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
    """
    Représente une requête de rafraîchissement du token d'accès.

    Attributs:
    - refresh_token: Token de rafraîchissement.
    - client_id: Identifiant du client.
    - client_secret: Secret du client.
    - check_point: Point de contrôle (si applicable).
    """
    refresh_token: str
    client_id: str | None = None
    client_secret: str | None = None
    check_point: str | None = None
