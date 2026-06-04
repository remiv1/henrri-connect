"""Modèles Pydantic v2 pour l'API Henrri."""

from __future__ import annotations

from .address_contacts import Address, Contact
from .authentication import AuthenticateRequest, RefreshTokenRequest, TokenResponse
from .base import CompanyIdentifierType, Link, UnitKind
from .base.responses import ListResponse, PagedListResponse
from .company import Company
from .customer import Customer, CustomerRequest, CustomerType
from .document import (
    Document,
    DocumentType,
    DocumentLabelElement,
    DocumentLabel,
    DocumentQuery,
    ValidateDocumentRequest,
)
from .document_line import (
    DocumentLine,
    DocumentLineListQueryParameters,
    DocumentLineType,
    DocumentLineMoveQueryParameters,
)
from .items import Item, ItemCategory, ItemCategoryType, ItemCategoryRequest, ItemsQuery
from .payments import PaymentMilestone, TaxDetail, TaxDetailArray
from .pdf import PdfUrlResponse
from .stats import MonthlyRevenueStatistics, RevenueStatistics
from .units import Unit
from .users import User, UserAndCompany

__all__ = [
    "Address",
    "AuthenticateRequest",
    "Company",
    "CompanyIdentifierType",
    "Contact",
    "Customer",
    "CustomerType",
    "CustomerRequest",
    "Document",
    "DocumentLabel",
    "DocumentLabelElement",
    "DocumentLine",
    "DocumentLineListQueryParameters",
    "DocumentLineMoveQueryParameters",
    "DocumentLineType",
    "DocumentQuery",
    "DocumentType",
    "Item",
    "ItemCategory",
    "ItemCategoryRequest",
    "ItemCategoryType",
    "ItemsQuery",
    "Link",
    "ListResponse",
    "MonthlyRevenueStatistics",
    "PagedListResponse",
    "PaymentMilestone",
    "PdfUrlResponse",
    "RefreshTokenRequest",
    "RevenueStatistics",
    "TaxDetail",
    "TaxDetailArray",
    "TokenResponse",
    "Unit",
    "UnitKind",
    "User",
    "UserAndCompany",
    "ValidateDocumentRequest",
]
