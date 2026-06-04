"""Stub d'exportation des modèles de données pour l'API Henrri Connect."""
from __future__ import annotations

from datetime import datetime
from typing import Generic, TypeVar
from pydantic import BaseModel

from .base import (
    CompanyIdentifierType,
    CustomerType,
    DocumentKind,
    DocumentState,
    UnitKind,
    SortOrder,
)


T = TypeVar("T")

# ── Types internes aux champs des modèles ─────────────────────────────────────

class Link(BaseModel):  # pylint: disable=C0115
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

class PagedListResponse(BaseModel, Generic[T]): # pylint: disable=C0115
    elements: list[T] | None
    totals: list[_Cell] | None
    display: list[_ElementDisplay] | None
    meta: _MetaPagedListResponse | None

class ListResponse(BaseModel, Generic[T]):  # pylint: disable=C0115
    elements: list[T] | None
    meta: _MetaListResponse | None

# ── Authentification ──────────────────────────────────────────────────────────

class AuthenticateRequest(BaseModel):   # pylint: disable=C0115
    client_id: str
    client_secret: str

class TokenResponse(BaseModel): # pylint: disable=C0115
    access_token: str | None
    identity_token: str | None
    scope: str | None
    token_type: str | None
    refresh_token: str | None
    expires_in: int
    is_error: bool
    error: str | None
    error_description: str | None

class RefreshTokenRequest(BaseModel):   # pylint: disable=C0115
    refresh_token: str
    client_id: str | None
    client_secret: str | None
    check_point: str | None

# ── Adresse et contacts ───────────────────────────────────────────────────────

class Address(BaseModel):   # pylint: disable=C0115
    id: int | None
    address: str | None
    city: str | None
    post_code: str | None
    country: str | None
    is_post_code_shared: bool
    links: list[Link] | None

class Contact(BaseModel):   # pylint: disable=C0115
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

class Company(BaseModel):   # pylint: disable=C0115
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

class User(BaseModel):  # pylint: disable=C0115
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

class UserAndCompany(BaseModel):    # pylint: disable=C0115
    user: User
    company: Company

# ── Client ────────────────────────────────────────────────────────────────────

class CustomerRequest(BaseModel):  # pylint: disable=C0115
    page: int = ...
    limit: int = ...
    search: str
    sort_by: str | None = ...
    sort_order: SortOrder | None = ...
    min_id: int | None = ...
    from_date: str
    to_date: str

class Customer(BaseModel):  # pylint: disable=C0115
    id: int | None = ...
    name: str
    type: CustomerType = CustomerType.INDIVIDUAL
    accounting_number: str | None = ...
    company_identifier_type: CompanyIdentifierType | None = ...
    siret: str | None = ...
    trade_name: str | None = ...
    trade_name_extension: str | None = ...
    ict: str | None = ...
    vat_number: str | None = ...
    address: Address | None = ...
    contacts: list[Contact] | None = ...
    days_number_before_payment_reminder_level1: int | None = ...
    days_number_before_payment_reminder_level2: int | None = ...
    days_number_before_payment_reminder_level3: int | None = ...
    days_number_before_payment_reminder_level4: int | None = ...
    service_discount_percentage: float = ...
    product_discount_percentage: float = ...
    customer_type_alert_enabled: bool = ...
    is_deleted: bool = ...
    is_supplier: bool = ...
    is_advisor: bool | None = ...
    import_date: datetime | None = ...
    comment: str | None = ...
    website: str | None = ...
    creation_date: datetime | None = ...
    links: list[Link] | None = ...

# ── Catégories d'articles ─────────────────────────────────────────────────────

class ItemCategoryType(BaseModel):  # pylint: disable=C0115
    id: int | None
    label: str | None
    item_category_content_kind: str
    item_category_kind: str

class ItemCategoryRequest(BaseModel):  # pylint: disable=C0115
    page: int = 1
    limit: int = 50
    search: str
    sort_by: str | None = ...
    sort_order: SortOrder | None = ...
    min_id: int | None = ...
    from_date: str | None = ...
    to_date: str | None = ...

class ItemCategory(BaseModel):  # pylint: disable=C0115
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

class Unit(BaseModel):  # pylint: disable=C0115
    id: int | None
    name: str
    unit_kind: UnitKind | None
    links: list[Link] | None

# ── Articles ──────────────────────────────────────────────────────────────────

class Item(BaseModel):  # pylint: disable=C0115
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

class ItemsQuery(BaseModel):  # pylint: disable=C0115
    page: int = 1
    limit: int = 50
    search: str | None = ...
    sort_by: str | None = ...
    sort_order: SortOrder | None = ...
    min_id: int
    from_date: str
    to_date: str

# ── Types de lignes de document ───────────────────────────────────────────────

class DocumentLineType(BaseModel):  # pylint: disable=C0115
    id: int | None
    label: str | None
    type: str

# ── Lignes de document ────────────────────────────────────────────────────────

class DocumentLine(BaseModel):  # pylint: disable=C0115
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

class DocumentLineMoveQueryParameters(BaseModel):   # pylint: disable=C0115
    to: int

class DocumentLineListQueryParameters(BaseModel):   # pylint: disable=C0115
    page: int | None = 1
    limit: int | None = 50
    search: str | None = None
    sort_by: str | None = ...
    sort_order: SortOrder | None = ...
    min_id: int
    from_date: str
    to_date: str

# ── Types de documents ────────────────────────────────────────────────────────

class DocumentType(BaseModel):  # pylint: disable=C0115
    id: int | None
    label: str | None
    short_label: str | None
    document_kind: str
    is_accounting: bool
    is_managed: bool
    is_mandatory: bool
    is_visible: bool

# ── Labels de document ────────────────────────────────────────────────────────

class DocumentLabelElement(BaseModel):  # pylint: disable=C0115
    id: int | None
    model_element_id: int | None
    label: str | None
    value: str | None
    element_type: str | None
    is_main_element: bool
    size: int | None
    index: int | None
    links: list[Link] | None

class DocumentLabel(BaseModel): # pylint: disable=C0115
    id: int | None
    model_id: int | None
    document_id: int | None
    label: str | None
    elements: list[DocumentLabelElement] | None
    links: list[Link] | None

# ── Documents ─────────────────────────────────────────────────────────────────

class Document(BaseModel):  # pylint: disable=C0115
    id: int | None = ...
    identity: str | None = ...
    finalized: bool
    type: str | None = ...
    document_type_id: int
    document_type: DocumentType | None = ...
    title: str | None = ...
    subtitle: str | None = ...
    price_before_tax: float
    tax_amount: float
    price_after_tax: float
    due_label: str | None = ...
    last_modification_date: datetime | None = ...
    date: datetime | None = ...
    validated: bool
    validation_date: datetime | None = ...
    validation_firstname: str | None = ...
    validation_lastname: str | None = ...
    validation_email: str | None = ...
    validation_ip: str | None = ...
    lines: list[DocumentLine] | None = ...
    customer_id: int
    customer: Customer | None = ...
    customer_address: Address | None = ...
    user_can_validate: bool
    footer_text: str | None = ...
    bank_account_label: str | None = ...
    label_id: int | None = ...
    links: list[Link] | None = ...

class DocumentQuery(BaseModel):  # pylint: disable=C0115
    finalized: bool = ...
    document_types: list[DocumentKind] | None = ...
    state: DocumentState | None = ...
    page: int = 1
    limit: int = 50
    search: str | None = ...
    sort_by: str | None = ...
    sort_order: SortOrder | None = ...
    min_id: int | None = ...
    from_date: str | None = ...
    to_date: str | None = ...

class ValidateDocumentRequest(BaseModel):  # pylint: disable=C0115
    email: str
    first_name: str
    last_name: str
    validation_date: str
    time_offset: int
    ip: str

# ── Jalons de paiement ────────────────────────────────────────────────────────

class PaymentMilestone(BaseModel):  # pylint: disable=C0115
    id: int | None
    amount: float | None
    percentage: float | None
    due_date: datetime
    is_paid: bool
    document_id: int
    payment_id: int | None
    links: list[Link] | None

# ── Détails de taxe ───────────────────────────────────────────────────────────

class TaxDetail(BaseModel): # pylint: disable=C0115
    rate: float
    price_before_tax: float
    tax_amount: float
    price_after_tax: float

class TaxDetailArray(BaseModel):    # pylint: disable=C0115
    tax_detail_array: list[TaxDetail] | None
    document_id: str | None
    links: list[Link] | None

# ── PDF ───────────────────────────────────────────────────────────────────────

class PdfUrlResponse(BaseModel):    # pylint: disable=C0115
    download_url: str | None
    expires_at: datetime | None
    file_name: str | None

# ── Statistiques de revenus ───────────────────────────────────────────────────

class RevenueStatistics(BaseModel): # pylint: disable=C0115
    year: int
    total_services_revenue: float
    total_products_revenue: float
    total_products_margin: float
    total_service_hours: float

class MonthlyRevenueStatistics(BaseModel):  # pylint: disable=C0115
    month: int
    year: int
    total_services_revenue: float
    total_products_revenue: float
    total_products_margin: float
    total_service_hours: float
