"""Modèles pour les clients dans l'API Henrri Connect."""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel, Link
from .base import CompanyIdentifierType
from .address_contacts import Contact, Address


class Customer(CamelModel):
    """"""
    id: int | None = None
    name: str
    type: str
    accounting_number: str | None = None
    company_identifier_type: CompanyIdentifierType | None = None
    siret: str | None = None
    trade_name: str | None = None
    trade_name_extension: str | None = None
    ict: str | None = None
    vat_number: str | None = None
    address: Address | None = None
    contacts: list[Contact] | None = None
    days_number_before_payment_reminder_level1: int | None = None
    days_number_before_payment_reminder_level2: int | None = None
    days_number_before_payment_reminder_level3: int | None = None
    days_number_before_payment_reminder_level4: int | None = None
    service_discount_percentage: float = 0.0
    product_discount_percentage: float = 0.0
    customer_type_alert_enabled: bool = False
    is_deleted: bool = False
    is_supplier: bool = False
    is_advisor: bool | None = None
    import_date: datetime | None = None
    comment: str | None = None
    website: str | None = None
    creation_date: datetime | None = None
    links: list[Link] | None = None
