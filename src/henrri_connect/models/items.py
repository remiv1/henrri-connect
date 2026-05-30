"""Modèles pour les articles et catégories d'articles dans l'API Henrri Connect."""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel, Link
from .base import ItemCategoryContentKind, ItemCategoryKind

class ItemCategoryType(CamelModel):
    id: int | None = None
    label: str | None = None
    item_category_content_kind: str = ItemCategoryContentKind.SUPPLY
    item_category_kind: str = ItemCategoryKind.SERVICE


class ItemCategory(CamelModel):
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
    creation_date: datetime | None = None
    links: list[Link] | None = None
