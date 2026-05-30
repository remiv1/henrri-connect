"""Modèles de base Pydantic v2 pour l'API Henrri."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class CamelModel(BaseModel):
    """Modèle de base avec conversion automatique camelCase ↔ snake_case."""

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel,
    )

class Link(CamelModel):
    href: str | None = None
    rel: str | None = None
    method: str | None = None
    label: str | None = None


class MetaPagedListResponse(CamelModel):
    page: int = 0
    limit: int = 0
    total_count: int = 0
    total_pages: int = 0
    has_next: bool = False


class MetaListResponse(CamelModel):
    total_count: int = 0
