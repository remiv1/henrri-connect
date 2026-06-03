"""Modèles de base pour les réponses de l'API Henrri Connect."""

from typing import Generic, TypeVar
from .models import (
    CamelModel,
    Link,
    MetaListResponse,
    MetaPagedListResponse,
)

T = TypeVar("T")

class Cell(CamelModel):
    """Représente une cellule de total dans une réponse paginée."""
    name: str | None = None
    value: str | None = None
    type: str | None = None
    is_amount: bool = False
    show_alert: bool = False
    links: list[Link] | None = None


class ElementDisplay(CamelModel):
    """Représente les informations d'affichage pour un élément dans une réponse paginée."""
    id: int | None = None
    title: str | None = None
    index: int = 0
    width: int = 0


class PagedListResponse(CamelModel, Generic[T]):
    """Réponse paginée générique."""

    elements: list[T] | None = None
    totals: list[Cell] | None = None
    display: list[ElementDisplay] | None = None
    meta: MetaPagedListResponse | None = None


class ListResponse(CamelModel, Generic[T]):
    """Réponse liste générique."""

    elements: list[T] | None = None
    meta: MetaListResponse | None = None
