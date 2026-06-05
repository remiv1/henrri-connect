"""
Modèles de base Pydantic v2 pour l'API Henrri.

Attributs:
- CamelModel: Modèle de base avec conversion automatique camelCase ↔ snake_case.
- Link: Représente un lien hypertexte.
- MetaPagedListResponse: Représente les métadonnées d'une réponse de liste paginée.
- MetaListResponse: Représente les métadonnées d'une réponse de liste.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class CamelModel(BaseModel):
    """
    Modèle de base avec conversion automatique camelCase ↔ snake_case.

    Attributs
    - model_config: Configuration du modèle pour activer la conversion automatique des
    noms de champs.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel,
    )

class Link(CamelModel):
    """
    Représente un lien hypertexte.

    Attributs
    - href: URL du lien.
    - rel: Relation du lien.
    - method: Méthode HTTP du lien.
    - label: Libellé du lien.
    """
    href: str | None = None
    rel: str | None = None
    method: str | None = None
    label: str | None = None


class MetaPagedListResponse(CamelModel):
    """
    Représente les métadonnées d'une réponse de liste paginée.

    Attributs
    - page: Numéro de la page.
    - limit: Nombre d'éléments par page.
    - total_count: Nombre total d'éléments.
    - total_pages: Nombre total de pages.
    - has_next: Indique si une page suivante existe.
    """
    page: int = 0
    limit: int = 0
    total_count: int = 0
    total_pages: int = 0
    has_next: bool = False


class MetaListResponse(CamelModel):
    """
    Représente les métadonnées d'une réponse de liste.

    Attributs
    - total_count: Nombre total d'éléments.
    """
    total_count: int = 0
