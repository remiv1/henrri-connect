"""Module utilitaire pour les clients Henrri Connect."""
from __future__ import annotations
import json
import httpx
from henrri_connect.exc import (
    HenrriAuthError,
    HenrriForbiddenError,
    HenrriHTTPError,
    HenrriNotFoundError,
    HenrriServerError,
    HenrriValidationError,
)

def raise_for_status(resp: httpx.Response) -> None:
    """
    Lève une exception appropriée selon le code HTTP de la réponse.
     - 400 : HenrriValidationError
     - 401 : HenrriAuthError
     - 403 : HenrriForbiddenError
     - 404 : HenrriNotFoundError
     - 5xx : HenrriServerError
     - Autres : HenrriHTTPError
    Tente d'extraire un message d'erreur détaillé depuis la réponse JSON,
    ou utilise le texte brut de la réponse si le JSON est invalide.
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
        raise HenrriValidationError(sc, str(msg))
    if sc == 401:
        raise HenrriAuthError(sc, str(msg))
    if sc == 403:
        raise HenrriForbiddenError(sc, str(msg))
    if sc == 404:
        raise HenrriNotFoundError(sc, str(msg))
    if sc >= 500:
        raise HenrriServerError(sc, str(msg))
    raise HenrriHTTPError(sc, str(msg))
