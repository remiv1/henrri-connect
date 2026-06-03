"""Modèles Pydantic v2 pour l'API Henrri."""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel, Link

class PaymentMilestone(CamelModel):
    """Représente une étape de paiement dans l'API Henrri Connect."""
    id: int | None = None
    amount: float | None = None
    percentage: float | None = None
    due_date: datetime
    is_paid: bool = False
    document_id: int
    payment_id: int | None = None
    links: list[Link] | None = None


class TaxDetail(CamelModel):
    """Représente les détails de taxe dans l'API Henrri Connect."""
    rate: float = 0.0
    price_before_tax: float = 0.0
    tax_amount: float = 0.0
    price_after_tax: float = 0.0


class TaxDetailArray(CamelModel):
    """Représente un tableau de détails de taxe dans l'API Henrri Connect."""
    tax_detail_array: list[TaxDetail] | None = None
    document_id: str | None = None
    links: list[Link] | None = None
