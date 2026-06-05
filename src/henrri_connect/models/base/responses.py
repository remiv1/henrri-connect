"""
Modèles de base pour les réponses de l'API Henrri Connect.

Attributs:
- Cell: Représente une cellule de total dans une réponse paginée.
- ElementDisplay: Représente les informations d'affichage pour un élément dans une réponse paginée.
- PagedListResponse: Réponse paginée générique.
- ListResponse: Réponse liste générique.
"""

from typing import Generic, TypeVar
from .models import (
    CamelModel,
    Link,
    MetaListResponse,
    MetaPagedListResponse,
)

T = TypeVar("T")

class Cell(CamelModel):
    """
    Représente une cellule de total dans une réponse paginée.

    Attributs
    - name: Nom de la cellule.
    - value: Valeur de la cellule.
    - type: Type de la cellule.
    - is_amount: Indique si la cellule représente un montant.
    - show_alert: Indique si une alerte doit être affichée pour cette cellule.
    - links: Liste de liens associés à la cellule (si applicable).
    """
    name: str | None = None
    value: str | None = None
    type: str | None = None
    is_amount: bool = False
    show_alert: bool = False
    links: list[Link] | None = None


class ElementDisplay(CamelModel):
    """
    Représente les informations d'affichage pour un élément dans une réponse paginée.

    Attributs
    - id: Identifiant de l'élément.
    - title: Titre de l'élément.
    - index: Index de l'élément.
    - width: Largeur de l'élément.
    """
    id: int | None = None
    title: str | None = None
    index: int = 0
    width: int = 0


class PagedListResponse(CamelModel, Generic[T]):
    """
    Réponse paginée générique.

    Attributs
    - elements: Liste d'éléments de la page.
    - totals: Liste de cellules de total pour la page (si applicable).
    - display: Liste d'informations d'affichage pour les éléments de la page (si applicable).
    - meta: Métadonnées de la réponse paginée (si applicable).
    """

    elements: list[T] | None = None
    totals: list[Cell] | None = None
    display: list[ElementDisplay] | None = None
    meta: MetaPagedListResponse | None = None


class ListResponse(CamelModel, Generic[T]) :
    """
    Réponse liste générique.

    Attributs
    - elements: Liste d'éléments.
    - meta: Métadonnées de la réponse liste (si applicable).
    """

    elements: list[T] | None = None
    meta: MetaListResponse | None = None
