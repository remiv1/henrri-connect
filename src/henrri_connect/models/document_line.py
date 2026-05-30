"""Modèles document pour l'API Henrri Connect."""

from __future__ import annotations

from .base import CamelModel, DocumentLineKind, Link
from .items import Item


class DocumentLineType(CamelModel):
    id: int | None = None
    label: str | None = None
    type: str = DocumentLineKind.NONE


class DocumentLine(CamelModel):
    id: int | None = None
    document_id: int | None = None
    reference: str | None = None
    description: str | None = None
    selling_price_without_tax: float | None = None
    purchasing_price_without_tax: float = 0.0
    vat_percent: float | None = None
    quantity: float = 0.0
    is_tax_included: bool = False
    total_without_tax: float | None = None
    total_with_tax: float | None = None
    are_elements_of_group_shown: bool = False
    line_number: int | None = None
    is_a_group: bool = False
    does_group_own_different_vat: bool = False
    is_member_of_a_group: bool = False
    is_adjustment_of_group: bool = False
    type_id: int
    type: DocumentLineType | None = None
    group_id: int | None = None
    item_id: int | None = None
    item: Item | None = None
    links: list[Link] | None = None


class DocumentLineMoveQueryParameters(CamelModel):
    to: int
