from __future__ import annotations

from enum import Enum

# ── Enums ─────────────────────────────────────────────────────────────────────

class SortOrder(str, Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"

class DocumentKind(str, Enum):
    INVOICE = "Invoice"
    CREDIT_NOTE = "CreditNote"
    DELIVERY_NOTE = "DeliveryNote"
    QUOTATION = "Quotation"
    WORK_ORDER = "WorkOrder"
    PROGRESS_INVOICE = "ProgressInvoice"
    ORDER = "Order"
    AMENDMENT = "Amendment"
    MISCELLANEOUS = "Miscellaneous"
    SUMMARY = "Summary"
    DEPOSIT_INVOICE = "DepositInvoice"
    DEPOSIT_RECEIPT = "DepositReceipt"

class DocumentState(str, Enum):
    FINALIZED = "Finalized"
    PENDING = "Pending"

class DocumentLineKind(str, Enum):
    NONE = "None"
    ITEM = "Item"
    TOTAL = "Total"
    SUBTOTAL = "Subtotal"
    TEXT = "Text"
    GROUP = "Group"
    ADJUSTMENT = "Adjustment"
    LINE_BREAK = "LineBreak"
    HORIZONTAL_TRAIT = "HorizontalTrait"

class UnitKind(str, Enum):
    HOURLY = "Hourly"
    METER = "Meter"
    CENTIMETER = "Centimeter"
    SQUARE_CENTIMETER = "SquareCentimeter"
    CUBIC_CENTIMETER = "CubicCentimeter"
    DECIMETER = "Decimeter"
    SQUARE_METER = "SquareMeter"
    CUBIC_METER = "CubicMeter"
    MILLIMETER = "Millimeter"
    SQUARE_MILLIMETER = "SquareMillimeter"
    CUBIC_MILLIMETER = "CubicMillimeter"
    KILOGRAM = "Kilogram"
    GRAM = "Gram"
    METRIC_TON = "MetricTon"
    SPECIFIC = "Specific"
    FLAT_RATE = "FlatRate"
    LINEAR_METER = "LinearMeter"
    UNIT = "Unit"
    CUSTOM = "Custom"

class CompanyIdentifierType(str, Enum):
    SIRET = "Siret"
    BCE = "Bce"
    UNKNOWN = "Unknown"

class ItemCategoryKind(str, Enum):
    SERVICE = "Service"
    PRODUCT = "Product"
    MIXED = "Mixed"

class ItemCategoryContentKind(str, Enum):
    SUPPLY = "Supply"
    FLAT_SERVICE = "FlatService"
    HOURLY_SERVICE = "HourlyService"
    MIXED = "Mixed"
    SUBCONTRACTING = "Subcontracting"
    MACHINE_TIME = "MachineTime"
    SPECIAL_SALE = "SpecialSale"
    USED_VEHICLE = "UsedVehicle"
