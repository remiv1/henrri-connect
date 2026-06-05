"""
Module contenant les énumérations utilisées dans les modèles de données.

Attributs
- CustomerType: Type de client pour les clients dans l'API Henrri Connect.
- SortOrder: Ordre de tri pour les listes d'articles et de catégories d'articles.
- DocumentKind: Type de document pour les documents commerciaux.
- DocumentState: État d'un document commercial.
- DocumentLineKind: Type de ligne pour les lignes de document commercial.
- UnitKind: Type d'unité pour les unités de mesure.
- CompanyIdentifierType: Type d'identifiant pour les entreprises.
- ItemCategoryKind: Type de catégorie d'articles.
- ItemCategoryContentKind: Type de contenu pour les catégories d'articles.
"""
from __future__ import annotations

from enum import Enum

class CustomerType(str, Enum):
    """
    Type de client pour les clients dans l'API Henrri Connect.

    Attributs
    - INDIVIDUAL: Client individuel.
    - COMPANY: Client entreprise.
    """
    INDIVIDUAL = "Individual"
    COMPANY = "Company"

class SortOrder(str, Enum):
    """
    Ordre de tri pour les listes d'articles et de catégories d'articles.

    Attributs
    - ASCENDING: Tri ascendant.
    - DESCENDING: Tri descendant.
    """
    ASCENDING = "Ascending"
    DESCENDING = "Descending"

class DocumentKind(str, Enum):
    """
    Type de document pour les documents commerciaux.

    Attributs
    - INVOICE: Facture.
    - CREDIT_NOTE: Avoir.
    - DELIVERY_NOTE: Bon de livraison.
    - QUOTATION: Devis.
    - WORK_ORDER: Bon de commande.
    - PROGRESS_INVOICE: Facture de progression.
    - ORDER: Commande.
    - AMENDMENT: Avenant.
    - MISCELLANEOUS: Divers.
    - SUMMARY: Sommaire.
    - DEPOSIT_INVOICE: Facture de caution.
    - DEPOSIT_RECEIPT: Recueil de caution.
    """
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
    """
    État d'un document commercial.

    Attributs
    - FINALIZED: Finalisé.
    - PENDING: En attente.
    """
    FINALIZED = "Finalized"
    PENDING = "Pending"

class DocumentLineKind(str, Enum):
    """
    Type de ligne pour les lignes de document commercial.

    Attributs
    - NONE: Aucun.
    - ITEM: Article.
    - TOTAL: Total.
    - SUBTOTAL: Sous-total.
    - TEXT: Texte.
    - GROUP: Groupe d'articles.
    - ADJUSTMENT: Ajustement de groupe d'articles.
    - LINE_BREAK: Saut de ligne.
    - HORIZONTAL_TRAIT: Trait horizontal.
    """
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
    """
    Type d'unité pour les unités de mesure.

    Attributs
    - HOURLY: Horaire.
    - METER: Mètre.
    - CENTIMETER: Centimètre.
    - SQUARE_CENTIMETER: Centimètre carré.
    - CUBIC_CENTIMETER: Centimètre cube.
    - DECIMETER: Décimètre.
    - SQUARE_METER: Mètre carré.
    - CUBIC_METER: Mètre cube.
    - MILLIMETER: Millimètre.
    - SQUARE_MILLIMETER: Millimètre carré.
    - CUBIC_MILLIMETER: Millimètre cube.
    - KILOGRAM: Kilogramme.
    - GRAM: Gramme.
    - METRIC_TON: Tonne métrique.
    - SPECIFIC: Spécifique.
    - FLAT_RATE: Forfait.
    - LINEAR_METER: Mètre linéaire.
    - UNIT: Unité.
    - CUSTOM: Personnalisé.
    """
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
    """
    Type d'identifiant pour les entreprises.

    Attributs
    - SIRET: SIRET.
    - BCE: BCE.
    - UNKNOWN: Inconnu.
    """
    SIRET = "Siret"
    BCE = "Bce"
    UNKNOWN = "Unknown"

class ItemCategoryKind(str, Enum):
    """
    Type de catégorie d'articles.

    Attributs
    - SERVICE: Service.
    - PRODUCT: Produit.
    - MIXED: Mixte.
    """
    SERVICE = "Service"
    PRODUCT = "Product"
    MIXED = "Mixed"

class ItemCategoryContentKind(str, Enum):
    """
    Type de contenu pour les catégories d'articles.

    Attributs
    - SUPPLY: Approvisionnement.
    - FLAT_SERVICE: Service forfaitaire.
    - HOURLY_SERVICE: Service horaire.
    - MIXED: Mixte.
    - SUBCONTRACTING: Sous-traitance.
    - MACHINE_TIME: Temps machine.
    - SPECIAL_SALE: Vente spéciale.
    - USED_VEHICLE: Véhicule d'occasion.
    """
    SUPPLY = "Supply"
    FLAT_SERVICE = "FlatService"
    HOURLY_SERVICE = "HourlyService"
    MIXED = "Mixed"
    SUBCONTRACTING = "Subcontracting"
    MACHINE_TIME = "MachineTime"
    SPECIAL_SALE = "SpecialSale"
    USED_VEHICLE = "UsedVehicle"
