"""Modèles Pydantic v2 pour l'API Henrri."""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel

class PdfUrlResponse(CamelModel):
    """Représente la réponse de l'API Henrri Connect pour une URL de PDF."""
    download_url: str | None = None
    expires_at: datetime | None = None
    file_name: str | None = None
