"""
Modèles Pydantic représentant les entités de paiement dans l'API Henrri.

Attributs:
- PaymentMilestone: Représente une étape de paiement dans l'API Henrri Connect.
- TaxDetail: Représente les détails de taxe dans l'API Henrri Connect.
- TaxDetailArray: Représente un tableau de détails de taxe dans l'API Henrri Connect.
"""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel, Link

class PaymentMilestone(CamelModel):
    """
    Représente une étape de paiement dans l'API Henrri Connect.
    
    Attributs:
    - id: Identifiant unique de l'étape de paiement.
    - amount: Montant de l'étape de paiement.
    - percentage: Pourcentage de l'étape de paiement.
    - due_date: Date d'échéance de l'étape de paiement.
    - is_paid: Indique si l'étape de paiement est payée.
    - document_id: Identifiant du document associé à l'étape de paiement.
    - payment_id: Identifiant du paiement associé à l'étape de paiement (si applicable).
    - links: Liste de liens associés à l'étape de paiement (si applicable).
    """
    id: int | None = None
    amount: float | None = None
    percentage: float | None = None
    due_date: datetime
    is_paid: bool = False
    document_id: int
    payment_id: int | None = None
    links: list[Link] | None = None


class TaxDetail(CamelModel):
    """
    Représente les détails de taxe dans l'API Henrri Connect.
    
    Attributs:
    - rate: Taux de taxe.
    - price_before_tax: Prix total avant taxe.
    - tax_amount: Montant total de la taxe.
    - price_after_tax: Prix total après taxe.
    """
    rate: float = 0.0
    price_before_tax: float = 0.0
    tax_amount: float = 0.0
    price_after_tax: float = 0.0


class TaxDetailArray(CamelModel):
    """
    Représente un tableau de détails de taxe dans l'API Henrri Connect.

    Attributs:
    - tax_detail_array: Liste des détails de taxe.
    - document_id: Identifiant du document associé aux détails de taxe.
    - links: Liste de liens associés au tableau de détails de taxe (si applicable).
    """
    tax_detail_array: list[TaxDetail] | None = None
    document_id: str | None = None
    links: list[Link] | None = None
