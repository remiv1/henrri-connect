"""
Modèles pour les unités dans l'API Henrri Connect.

Attributs:
- Unit: Représente une unité dans l'API Henrri Connect.
"""

from __future__ import annotations

from .base import CamelModel, Link, UnitKind


class Unit(CamelModel):
    """
    Représente une unité dans l'API Henrri Connect.

    Attributs:
    - id: Identifiant de l'unité.
    - name: Nom de l'unité.
    - unit_kind: Type de l'unité.
    - links: Liens associés à l'unité.
    """
    id: int | None = None
    name: str
    unit_kind: UnitKind | None = None
    links: list[Link] | None = None
