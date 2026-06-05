"""Tests de la fonction raise_for_status."""
from __future__ import annotations

from unittest.mock import MagicMock
from typing import cast

import json
import httpx
import pytest

from henrri_connect.utils import raise_for_status
from henrri_connect.exc import (
    HenrriValidationError,
    HenrriAuthError,
    HenrriForbiddenError,
    HenrriNotFoundError,
    HenrriServerError,
    HenrriHTTPError,
)


def _make_resp(status: int, data: dict | None = None, text: str = "") -> httpx.Response:
    m = MagicMock(spec=httpx.Response)
    m.status_code = status
    m.is_success = status < 400
    if data is None:
        m.json.side_effect = json.JSONDecodeError("msg", "doc", 0)
    else:
        m.json.return_value = data
    m.text = text
    return cast(httpx.Response, m)


@pytest.mark.parametrize(
    "status,exc",
    [
        (400, HenrriValidationError),
        (401, HenrriAuthError),
        (403, HenrriForbiddenError),
        (404, HenrriNotFoundError),
        (500, HenrriServerError),
        (418, HenrriHTTPError),
    ],
)
def test_raise_for_status_raises_correct_exception(status, exc):
    """Leve une exception appropriée selon le code HTTP de la réponse."""
    resp = _make_resp(status, {"detail": "boom"}, text="boom")
    with pytest.raises(exc):
        raise_for_status(resp)


def test_raise_for_status_handles_invalid_json():
    """Si le corps de la réponse n'est pas du JSON valide, le texte brut est utilisé."""
    resp = _make_resp(500, None, text="plain error")
    with pytest.raises(HenrriServerError):
        raise_for_status(resp)
