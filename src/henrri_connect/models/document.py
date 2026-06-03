"""Modèles Pydantic v2 pour l'API Henrri."""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel, Link, DocumentKind
from .document_line import DocumentLine
from .customer import Customer
from .address_contacts import Address

class DocumentType(CamelModel):
    """Représente un type de document dans l'API Henrri Connect."""
    id: int | None = None
    label: str | None = None
    short_label: str | None = None
    document_kind: str = DocumentKind.INVOICE
    is_accounting: bool = False
    is_managed: bool = False
    is_mandatory: bool = False
    is_visible: bool = False


class DocumentLabelElement(CamelModel):
    """Représente un élément d'étiquette de document dans l'API Henrri Connect."""
    id: int | None = None
    model_element_id: int | None = None
    label: str | None = None
    value: str | None = None
    element_type: str | None = None
    is_main_element: bool = False
    size: int | None = None
    index: int | None = None
    links: list[Link] | None = None


class DocumentLabel(CamelModel):
    """Représente une étiquette de document dans l'API Henrri Connect."""
    id: int | None = None
    model_id: int | None = None
    document_id: int | None = None
    label: str | None = None
    elements: list[DocumentLabelElement] | None = None
    links: list[Link] | None = None


class Document(CamelModel):
    """Représente un document dans l'API Henrri Connect."""
    id: int | None = None
    identity: str | None = None
    finalized: bool = False
    type: str | None = None
    document_type_id: int
    document_type: DocumentType | None = None
    title: str | None = None
    subtitle: str | None = None
    price_before_tax: float = 0.0
    tax_amount: float = 0.0
    price_after_tax: float = 0.0
    due_label: str | None = None
    last_modification_date: datetime | None = None
    date: datetime | None = None
    validated: bool = False
    validation_date: datetime | None = None
    validation_firstname: str | None = None
    validation_lastname: str | None = None
    validation_email: str | None = None
    validation_ip: str | None = None
    lines: list[DocumentLine] | None = None
    customer_id: int | None = None
    customer: Customer | None = None
    customer_address: Address | None = None
    user_can_validate: bool = False
    footer_text: str | None = None
    bank_account_label: str | None = None
    label_id: int | None = None
    links: list[Link] | None = None


class ValidateDocumentRequest(CamelModel):
    """Représente une requête de validation de document dans l'API Henrri Connect."""
    email: str
    first_name: str
    last_name: str
    validation_date: str
    time_offset: int
    ip: str
