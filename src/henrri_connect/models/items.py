"""
Modèles pour les articles et catégories d'articles dans l'API Henrri Connect.

Attributs:
- ItemCategoryRequest: Représente une requête de catégorie d'article.
- ItemCategoryType: Représente un type de catégorie d'article.
- ItemCategory: Représente une catégorie d'article.
- Item: Représente un article.
"""

from __future__ import annotations

from .base import CamelModel, Link, ItemCategoryContentKind, ItemCategoryKind, SortOrder


class ItemCategoryRequest(CamelModel):
    """
    Représente une requête de catégorie d'article dans l'API Henrri Connect.

    Attributes:
        page (int) : Index de la page de la requête (entre 1 et 2 147 483 647, defaut 1).
        limit (int) : Nombre d'articles par page (entre 1 et 100, défaut 50).
        search (str) : Chaine de recherche.
        sort_by (str) : Champ de tri.
        sort_order (str) : Ordre de tri (Ascending ou Descending).
        min_id (int) : Identifiant minimal de l'article (entre 1 et 2 147 483 647).
        from_date (str) : Date de début.
        to_date (str) : Date de fin.
    """
    page: int = 1
    limit: int = 50
    search: str
    sort_by: str | None = None
    sort_order: str | None = None
    min_id: int | None = None
    from_date: str | None = None
    to_date: str | None = None


class ItemCategoryType(CamelModel):
    """
    Représente un type de catégorie d'article dans l'API Henrri Connect.

    Attributs:
    - id: Identifiant unique du type de catégorie d'article.
    - label: Libellé du type de catégorie d'article.
    - item_category_content_kind: Type de contenu de la catégorie d'article.
    - item_category_kind: Type de catégorie d'article.
    """
    id: int | None = None
    label: str | None = None
    item_category_content_kind: str = ItemCategoryContentKind.SUPPLY
    item_category_kind: str = ItemCategoryKind.SERVICE


class ItemCategory(CamelModel):
    """
    Représente une catégorie d'article dans l'API Henrri Connect.

    Attributs:
    - id: Identifiant unique de la catégorie d'article.
    - type: Type de la catégorie d'article.
    - label: Libellé de la catégorie d'article.
    - margin_percent: Pourcentage de marge de la catégorie d'article.
    - hourly_rate: Tarif horaire de la catégorie d'article.
    - vat: Taux de TVA de la catégorie d'article.
    - is_added_to_revenue: Indique si les articles de la cat. sont ajoutés au chiffre d'affaires.
    - is_default: Indique si la catégorie d'article est la catégorie par défaut.
    - is_deleted: Indique si la catégorie d'article est supprimée.
    - item_category_kind: Type de la catégorie d'article (service, produit, ou fourniture).
    """
    id: int | None = None
    type: ItemCategoryType | None = None
    label: str | None = None
    margin_percent: float = 0.0
    hourly_rate: float = 0.0
    vat: float = 0.0
    is_added_to_revenue: bool = False
    is_default: bool = False
    is_deleted: bool = False
    item_category_kind: str = ItemCategoryKind.SERVICE


class Item(CamelModel):
    """
    Représente un article dans l'API Henrri Connect.

    Attributs:
    - id: Identifiant unique de l'article.
    - reference: Référence de l'article.
    - description: Description de l'article.
    - is_tax_included: Indique si la taxe est incluse dans le prix.
    - selling_price_without_tax: Prix de vente hors taxe de l'article.
    - selling_price_with_tax: Prix de vente TTC de l'article.
    - purchase_price: Prix d'achat de l'article.
    - vat_percent: Taux de TVA de l'article.
    - is_a_group: Indique si l'article est un groupe d'articles.
    - item_category: Catégorie de l'article (si applicable).
    - item_category_id: Identifiant de la catégorie de l'article (si applicable).
    - unit_id: Identifiant de l'unité de l'article (si applicable).
    - parent_item_id: Id d'article parent si l'article est un élément d'un grp
    d'articles (si applicable).
    - creation_date: Date de création de l'article.
    - links: Liste de liens associés à l'article (si applicable).
    """
    id: int | None = None
    reference: str | None = None
    description: str | None = None
    is_tax_included: bool = False
    selling_price_without_tax: float | None = None
    selling_price_with_tax: float | None = None
    purchase_price: float = 0.0
    vat_percent: float
    is_a_group: bool = False
    item_category: ItemCategory | None = None
    item_category_id: int | None = None
    unit_id: int | None = None
    parent_item_id: int | None = None
    creation_date: str
    links: list[Link] | None = None


class ItemsQuery(CamelModel):
    """
    Représente une requête de catégorie d'article dans l'API Henrri Connect.

    Attributs:
    - page (int) : Index de la page de la requête (entre 1 et 2 147 483 647, defaut 1).
    - limit (int) : Nombre d'articles par page (entre 1 et 100, défaut 50).
    - search (str) : Chaine de recherche.
    - sort_by (str) : Champ de tri.
    - sort_order (SortOrder) : Ordre de tri (Ascending ou Descending).
    - min_id (int) : Identifiant minimal de l'article (entre 1 et 2 147 483 647).
    - from_date (str) : Date de début.
    - to_date (str) : Date de fin.
    """
    page: int = 1
    limit: int = 50
    search: str | None = None
    sort_by: str | None = None
    sort_order: SortOrder | None = None
    min_id: int
    from_date: str
    to_date: str
