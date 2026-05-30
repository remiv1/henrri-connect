"""Modèles pour les unités dans l'API Henrri Connect."""

from __future__ import annotations

from .base import CamelModel, Link, UnitKind


class Unit(CamelModel):
    id: int | None = None
    name: str
    unit_kind: UnitKind | None = None
    links: list[Link] | None = None
