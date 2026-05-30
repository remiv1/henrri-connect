"""Modèles Pydantic v2 pour l'API Henrri."""

from __future__ import annotations

from .address_contacts import Address, Contact
from .authentication import AuthenticateRequest, RefreshTokenRequest, TokenResponse
from .base import CompanyIdentifierType, Link, UnitKind
from .base.responses import ListResponse, PagedListResponse
from .company import Company
from .customer import Customer
from .document import (
    Document, DocumentType, DocumentLabelElement, DocumentLabel, ValidateDocumentRequest
)
from .document_line import DocumentLine, DocumentLineType, DocumentLineMoveQueryParameters
from .items import Item, ItemCategory, ItemCategoryType
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
    "Document",
    "DocumentLabel",
    "DocumentLabelElement",
    "DocumentLine",
    "DocumentLineMoveQueryParameters",
    "DocumentLineType",
    "DocumentType",
    "Item",
    "ItemCategory",
    "ItemCategoryType",
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
