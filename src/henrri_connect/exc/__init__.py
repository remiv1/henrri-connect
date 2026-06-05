"""
Module d'exceptions personnalisées pour la bibliothèque henrri-connect.

Exceptions:
- HenrriError: Erreur de base pour la bibliothèque henrri-connect.
- HenrriHTTPError: Erreur HTTP retournée par l'API Henrri.
- HenrriAuthError: Erreur d'authentification (HTTP 401).
- HenrriForbiddenError: Accès interdit (HTTP 403).
- HenrriNotFoundError: Ressource introuvable (HTTP 404).
- HenrriValidationError: Erreur de validation des données (HTTP 400 ou 422).
- HenrriServerError: Erreur interne du serveur (HTTP 5xx)."""
from __future__ import annotations


class HenrriError(Exception):
    """
    Erreur de base pour la bibliothèque henrri-connect.

    Ces exceptions sont utilisées pour indiquer des erreurs dans la bibliothèque henrri-connect.
    """


class HenrriHTTPError(HenrriError):
    """
    Erreur HTTP retournée par l'API Henrri.

    Ces exceptions sont utilisées pour indiquer des erreurs HTTP retournées par l'API Henrri.

    Arguments
    - status_code: Code de statut HTTP.
    - message: Message d'erreur.
    """

    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        super().__init__(f"HTTP {status_code} : {message}")


class HenrriAuthError(HenrriHTTPError):
    """
    Erreur d'authentification (HTTP 401).

    Ces exceptions sont utilisées pour indiquer des erreurs d'authentification (HTTP 401).

    Arguments
    - status_code: Code de statut HTTP.
    - message: Message d'erreur.
    """


class HenrriForbiddenError(HenrriHTTPError):
    """
    Accès interdit (HTTP 403).

    Ces exceptions sont utilisées pour indiquer des accès interdits (HTTP 403).

    Arguments
    - status_code: Code de statut HTTP.
    - message: Message d'erreur.
    """


class HenrriNotFoundError(HenrriHTTPError):
    """
    Ressource introuvable (HTTP 404).

    Ces exceptions sont utilisées pour indiquer des ressources introuvables (HTTP 404).

    Arguments
    - status_code: Code de statut HTTP.
    - message: Message d'erreur.
    """


class HenrriValidationError(HenrriHTTPError):
    """
    Erreur de validation des données (HTTP 400 ou 422).

    Ces exceptions sont utilisées pour indiquer des erreurs de validation des données
    (HTTP 400 ou 422).

    Arguments
    - status_code: Code de statut HTTP.
    - message: Message d'erreur.
    """


class HenrriServerError(HenrriHTTPError):
    """
    Erreur interne du serveur (HTTP 5xx).

    Ces exceptions sont utilisées pour indiquer des erreurs internes du serveur (HTTP 5xx).

    Arguments
    - status_code: Code de statut HTTP.
    - message: Message d'erreur.
    """
