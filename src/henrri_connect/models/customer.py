"""
Modèles pour les clients dans l'API Henrri Connect.

Attributs:
- Customer: Représente un client dans l'API Henrri Connect.
"""

from __future__ import annotations

from .base import CamelModel, Link, CompanyIdentifierType, CustomerType, SortOrder
from .address_contacts import Contact, Address


class CustomerRequest(CamelModel):
    """
    Modèle pour les requêtes de recherches clients dans l'API Henrri Connect.

    Attributs:
    - page: Numéro de page (par défaut 1).
    - limit: Nombre de clients par page (par défaut 50).
    - search: Chaîne de recherche (obligatoire).
    - sort_by: Champ de tri.
    - sort_order: Ordre de tri (Ascending ou Descending).
    - min_id: Identifiant minimal de client (entre 1 et 2 147 483 647).
    - from_date: Date de début.
    - to_date: Date de fin.
    """
    page: int = 1
    limit: int = 50
    search: str
    sort_by: str | None = None
    sort_order: SortOrder | None = None
    min_id: int | None = None
    from_date: str
    to_date: str


class Customer(CamelModel):
    """
    Modèle pour les clients dans l'API Henrri Connect.

    Attributs:
    - id: Identifiant unique du client.
    - name: Nom du client.
    - type: Type de client (individuel ou entreprise).
    - accounting_number: Numéro comptable du client.
    - company_identifier_type: Type d'identifiant de l'entreprise (SIRET, BCE, ou inconnu).
    - siret: Numéro SIRET de l'entreprise (si applicable).
    - trade_name: Nom commercial de l'entreprise (si applicable).
    - trade_name_extension: Extension du nom commercial de l'entreprise (si applicable).
    - ict: Identifiant de contact de l'entreprise (si applicable).
    - vat_number: Numéro de TVA du client (si applicable).
    - address: Adresse du client (si applicable).
    - contacts: Liste de contacts associés au client (si applicable).
    - days_number_before_payment_reminder_level1: Nb jours avant le premier rappel de paiement.
    - days_number_before_payment_reminder_level2: Nb jours avant le deuxième rappel de paiement.
    - days_number_before_payment_reminder_level3: Nb jours avant le troisième rappel de paiement.
    - days_number_before_payment_reminder_level4: Nb jours avant le quatrième rappel de paiement.
    - service_discount_percentage: Pourcentage de remise pour les services.
    - product_discount_percentage: Pourcentage de remise pour les produits.
    - customer_type_alert_enabled: Indique si les alertes de type de client sont activées.
    - is_deleted: Indique si le client est supprimé.
    - is_supplier: Indique si le client est également un fournisseur.
    - is_advisor: Indique si le client est également un conseiller.
    - import_date: Date d'importation du client.
    - comment: Commentaire sur le client.
    - website: Site web du client (si applicable).
    - creation_date: Date de création du client.
    - links: Liste de liens associés au client (si applicable).
    """
    id: int | None = None
    name: str
    type: CustomerType = CustomerType.INDIVIDUAL
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
    import_date: str | None = None
    comment: str | None = None
    website: str | None = None
    creation_date: str | None = None
    links: list[Link] | None = None
