"""
Modèles Pydantic représentant les entités de PDF dans l'API Henrri.

Attributs:
- PdfUrlResponse: Représente la réponse de l'API Henrri Connect pour une URL de PDF.
"""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel

class PdfUrlResponse(CamelModel):
    """
    Représente la réponse de l'API Henrri Connect pour une URL de PDF.
    
    Attributs:
    - download_url: URL de téléchargement du PDF.
    - expires_at: Date d'expiration de l'URL de téléchargement du PDF.
    - file_name: Nom du fichier PDF (si applicable).
    """
    download_url: str | None = None
    expires_at: datetime | None = None
    file_name: str | None = None
