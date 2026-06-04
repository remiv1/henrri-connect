"""Module utilitaire pour les clients Henrri Connect."""
from __future__ import annotations

import logging
import json
from typing import Any
import httpx
from .exc import (
    HenrriAuthError,
    HenrriForbiddenError,
    HenrriHTTPError,
    HenrriNotFoundError,
    HenrriServerError,
    HenrriValidationError,
)

logger = logging.getLogger(__name__)

def raise_for_status(resp: httpx.Response) -> None:
    """Lève une exception appropriée selon le code HTTP de la réponse.

    Correspondance des codes HTTP :

    - 400 : ``HenrriValidationError``
    - 401 : ``HenrriAuthError``
    - 403 : ``HenrriForbiddenError``
    - 404 : ``HenrriNotFoundError``
    - 5xx : ``HenrriServerError``
    - Autres : ``HenrriHTTPError``

    Tente d'extraire un message d'erreur détaillé depuis la réponse JSON,
    ou utilise le texte brut de la réponse si le JSON est invalide.

    Args:
        resp: La réponse HTTP httpx à analyser.

    Raises:
        HenrriValidationError: Si le code HTTP est 400.
        HenrriAuthError: Si le code HTTP est 401.
        HenrriForbiddenError: Si le code HTTP est 403.
        HenrriNotFoundError: Si le code HTTP est 404.
        HenrriServerError: Si le code HTTP est >= 500.
        HenrriHTTPError: Pour tout autre code d'erreur.
    """
    if resp.is_success:
        return
    try:
        detail = resp.json()
        msg: str = (
            detail.get("detail")
            or detail.get("title")
            or detail.get("message")
            or resp.text
        )
    except json.JSONDecodeError:
        msg = resp.text or f"Erreur HTTP {resp.status_code}"

    sc = resp.status_code
    if sc == 400:
        logger.error("Validation error: %s", msg)
        raise HenrriValidationError(sc, str(msg))
    if sc == 401:
        logger.error("Authentication error: %s", msg)
        raise HenrriAuthError(sc, str(msg))
    if sc == 403:
        logger.error("Forbidden error: %s", msg)
        raise HenrriForbiddenError(sc, str(msg))
    if sc == 404:
        logger.error("Not found error: %s", msg)
        raise HenrriNotFoundError(sc, str(msg))
    if sc >= 500:
        logger.error("Server error: %s", msg)
        raise HenrriServerError(sc, str(msg))
    logger.error("HTTP error: %s", msg)
    raise HenrriHTTPError(sc, str(msg))

def clean(params: dict[str, Any]) -> dict[str, Any]:
    """
    Supprime les valeurs None d'un dictionnaire

    Args:
        params (dict[str, Any]): Dictionnaire contenant des valeurs None

    Returns:
        dict[str, Any]: Dictionnaire sans valeurs None
    """
    return {k: v for k, v in params.items() if v is not None}
