from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")

# ── Enums exportés ────────────────────────────────────────────────────────────

class CompanyIdentifierType(str, Enum):
    SIRET: str
    BCE: str
    UNKNOWN: str

class UnitKind(str, Enum):
    HOURLY: str
    METER: str
    CENTIMETER: str
    SQUARE_CENTIMETER: str
    CUBIC_CENTIMETER: str
    DECIMETER: str
    SQUARE_METER: str
    CUBIC_METER: str
    MILLIMETER: str
    SQUARE_MILLIMETER: str
    CUBIC_MILLIMETER: str
    KILOGRAM: str
    GRAM: str
    METRIC_TON: str
    SPECIFIC: str
    FLAT_RATE: str
    LINEAR_METER: str
    UNIT: str
    CUSTOM: str

# ── Types internes aux champs des modèles ─────────────────────────────────────

class Link(BaseModel):
    href: str | None
    rel: str | None
    method: str | None
    label: str | None

class _MetaPagedListResponse(BaseModel):
    page: int
    limit: int
    total_count: int
    total_pages: int
    has_next: bool

class _MetaListResponse(BaseModel):
    total_count: int

class _Cell(BaseModel):
    name: str | None
    value: str | None
    type: str | None
    is_amount: bool
    show_alert: bool
    links: list[Link] | None

class _ElementDisplay(BaseModel):
    id: int | None
    title: str | None
    index: int
    width: int

# ── Réponses génériques ───────────────────────────────────────────────────────

class PagedListResponse(BaseModel, Generic[T]):
    elements: list[T] | None
    totals: list[_Cell] | None
    display: list[_ElementDisplay] | None
    meta: _MetaPagedListResponse | None

class ListResponse(BaseModel, Generic[T]):
    elements: list[T] | None
    meta: _MetaListResponse | None

# ── Authentification ──────────────────────────────────────────────────────────

class AuthenticateRequest(BaseModel):
    client_id: str
    client_secret: str

class TokenResponse(BaseModel):
    access_token: str | None
    identity_token: str | None
    scope: str | None
    token_type: str | None
    refresh_token: str | None
    expires_in: int
    is_error: bool
    error: str | None
    error_description: str | None

class RefreshTokenRequest(BaseModel):
    refresh_token: str
    client_id: str | None
    client_secret: str | None
    check_point: str | None

# ── Adresse et contacts ───────────────────────────────────────────────────────

class Address(BaseModel):
    id: int | None
    address: str | None
    city: str | None
    post_code: str | None
    country: str | None
    is_post_code_shared: bool
    links: list[Link] | None

class Contact(BaseModel):
    id: int | None
    title: str | None
    first_name: str | None
    last_name: str | None
    email: str | None
    phone: str | None
    mobile: str | None
    role: str | None
    is_primary: bool
    show_on_document: bool
    links: list[Link] | None

# ── Entreprise ────────────────────────────────────────────────────────────────

class Company(BaseModel):
    id: int | None
    name: str | None
    logo_url: str | None
    is_self_employed: bool
    siret: str | None
    email: str | None
    web_site: str | None
    ape_code: str | None
    ape_label: str | None
    global_id: int | None
    address: Address | None
    links: list[Link] | None

# ── Utilisateur ───────────────────────────────────────────────────────────────

class User(BaseModel):
    id: int | None
    email: str | None
    first_name: str | None
    last_name: str | None
    url_image: str | None
    first_connexion_date: datetime | None
    last_connexion_date: datetime | None
    connexion_count: str | None
    created_from: str | None
    phone_number: str | None
    creation_date: datetime | None
    is_enabled: bool
    two_factor_enabled: bool
    address: Address | None
    links: list[Link] | None

class UserAndCompany(BaseModel):
    user: User
    company: Company

# ── Client ────────────────────────────────────────────────────────────────────

class Customer(BaseModel):
    id: int | None
    name: str
    type: str
    accounting_number: str | None
    company_identifier_type: CompanyIdentifierType | None
    siret: str | None
    trade_name: str | None
    trade_name_extension: str | None
    ict: str | None
    vat_number: str | None
    address: Address | None
    contacts: list[Contact] | None
    days_number_before_payment_reminder_level1: int | None
    days_number_before_payment_reminder_level2: int | None
    days_number_before_payment_reminder_level3: int | None
    days_number_before_payment_reminder_level4: int | None
    service_discount_percentage: float
    product_discount_percentage: float
    customer_type_alert_enabled: bool
    is_deleted: bool
    is_supplier: bool
    is_advisor: bool | None
    import_date: datetime | None
    comment: str | None
    website: str | None
    creation_date: datetime | None
    links: list[Link] | None

# ── Catégories d'articles ─────────────────────────────────────────────────────

class ItemCategoryType(BaseModel):
    id: int | None
    label: str | None
    item_category_content_kind: str
    item_category_kind: str

class ItemCategory(BaseModel):
    id: int | None
    type: ItemCategoryType | None
    label: str | None
    margin_percent: float
    hourly_rate: float
    vat: float
    is_added_to_revenue: bool
    is_default: bool
    is_deleted: bool
    item_category_kind: str

# ── Unités ────────────────────────────────────────────────────────────────────

class Unit(BaseModel):
    id: int | None
    name: str
    unit_kind: UnitKind | None
    links: list[Link] | None

# ── Articles ──────────────────────────────────────────────────────────────────

class Item(BaseModel):
    id: int | None
    reference: str | None
    description: str | None
    is_tax_included: bool
    selling_price_without_tax: float | None
    selling_price_with_tax: float | None
    purchase_price: float
    vat_percent: float
    is_a_group: bool
    item_category: ItemCategory | None
    item_category_id: int | None
    unit_id: int | None
    parent_item_id: int | None
    creation_date: datetime | None
    links: list[Link] | None

# ── Types de lignes de document ───────────────────────────────────────────────

class DocumentLineType(BaseModel):
    id: int | None
    label: str | None
    type: str

# ── Lignes de document ────────────────────────────────────────────────────────

class DocumentLine(BaseModel):
    id: int | None
    document_id: int | None
    reference: str | None
    description: str | None
    selling_price_without_tax: float | None
    purchasing_price_without_tax: float
    vat_percent: float | None
    quantity: float
    is_tax_included: bool
    total_without_tax: float | None
    total_with_tax: float | None
    are_elements_of_group_shown: bool
    line_number: int | None
    is_a_group: bool
    does_group_own_different_vat: bool
    is_member_of_a_group: bool
    is_adjustment_of_group: bool
    type_id: int
    type: DocumentLineType | None
    group_id: int | None
    item_id: int | None
    item: Item | None
    links: list[Link] | None

class DocumentLineMoveQueryParameters(BaseModel):
    to: int

# ── Types de documents ────────────────────────────────────────────────────────

class DocumentType(BaseModel):
    id: int | None
    label: str | None
    short_label: str | None
    document_kind: str
    is_accounting: bool
    is_managed: bool
    is_mandatory: bool
    is_visible: bool

# ── Labels de document ────────────────────────────────────────────────────────

class DocumentLabelElement(BaseModel):
    id: int | None
    model_element_id: int | None
    label: str | None
    value: str | None
    element_type: str | None
    is_main_element: bool
    size: int | None
    index: int | None
    links: list[Link] | None

class DocumentLabel(BaseModel):
    id: int | None
    model_id: int | None
    document_id: int | None
    label: str | None
    elements: list[DocumentLabelElement] | None
    links: list[Link] | None

# ── Documents ─────────────────────────────────────────────────────────────────

class Document(BaseModel):
    id: int | None
    identity: str | None
    finalized: bool
    type: str | None
    document_type_id: int
    document_type: DocumentType | None
    title: str | None
    subtitle: str | None
    price_before_tax: float
    tax_amount: float
    price_after_tax: float
    due_label: str | None
    last_modification_date: datetime | None
    date: datetime | None
    validated: bool
    validation_date: datetime | None
    validation_firstname: str | None
    validation_lastname: str | None
    validation_email: str | None
    validation_ip: str | None
    lines: list[DocumentLine] | None
    customer_id: int | None
    customer: Customer | None
    customer_address: Address | None
    user_can_validate: bool
    footer_text: str | None
    bank_account_label: str | None
    label_id: int | None
    links: list[Link] | None

class ValidateDocumentRequest(BaseModel):
    email: str
    first_name: str
    last_name: str
    validation_date: str
    time_offset: int
    ip: str

# ── Jalons de paiement ────────────────────────────────────────────────────────

class PaymentMilestone(BaseModel):
    id: int | None
    amount: float | None
    percentage: float | None
    due_date: datetime
    is_paid: bool
    document_id: int
    payment_id: int | None
    links: list[Link] | None

# ── Détails de taxe ───────────────────────────────────────────────────────────

class TaxDetail(BaseModel):
    rate: float
    price_before_tax: float
    tax_amount: float
    price_after_tax: float

class TaxDetailArray(BaseModel):
    tax_detail_array: list[TaxDetail] | None
    document_id: str | None
    links: list[Link] | None

# ── PDF ───────────────────────────────────────────────────────────────────────

class PdfUrlResponse(BaseModel):
    download_url: str | None
    expires_at: datetime | None
    file_name: str | None

# ── Statistiques de revenus ───────────────────────────────────────────────────

class RevenueStatistics(BaseModel):
    year: int
    total_services_revenue: float
    total_products_revenue: float
    total_products_margin: float
    total_service_hours: float

class MonthlyRevenueStatistics(BaseModel):
    month: int
    year: int
    total_services_revenue: float
    total_products_revenue: float
    total_products_margin: float
    total_service_hours: float
