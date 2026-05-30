from __future__ import annotations


class HenrriError(Exception):
    """Erreur de base pour la bibliothèque henrri-connect."""


class HenrriHTTPError(HenrriError):
    """Erreur HTTP retournée par l'API Henrri."""

    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        super().__init__(f"HTTP {status_code} : {message}")


class HenrriAuthError(HenrriHTTPError):
    """Erreur d'authentification (HTTP 401)."""


class HenrriForbiddenError(HenrriHTTPError):
    """Accès interdit (HTTP 403)."""


class HenrriNotFoundError(HenrriHTTPError):
    """Ressource introuvable (HTTP 404)."""


class HenrriValidationError(HenrriHTTPError):
    """Erreur de validation des données (HTTP 400 ou 422)."""


class HenrriServerError(HenrriHTTPError):
    """Erreur interne du serveur (HTTP 5xx)."""
