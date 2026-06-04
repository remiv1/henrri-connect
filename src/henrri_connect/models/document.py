"""
Modèles Pydantic v2 pour les documents dans l'API Henrri Connect.

Attributs:
- DocumentType: Représente un type de document dans l'API Henrri Connect.
- DocumentLabelElement: Représente un élément d'étiquette de document dans l'API Henrri Connect.
- DocumentLabel: Représente une étiquette de document dans l'API Henrri Connect.
- DocumentLineType: Représente un type de ligne de document dans l'API Henrri Connect.
- DocumentLine: Représente une ligne de document dans l'API Henrri Connect.
- DocumentLineMoveQueryParameters: Représente les paramètres de requête pour déplacer une ligne
de document dans l'API Henrri Connect.
"""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel, Link, DocumentKind, DocumentState, SortOrder
from .document_line import DocumentLine
from .customer import Customer
from .address_contacts import Address

class DocumentType(CamelModel):
    """
    Représente un type de document dans l'API Henrri Connect.
    
    Attributs:
    - id: Identifiant unique du type de document.
    - label: Libellé du type de document.
    - short_label: Libellé court du type de document.
    - document_kind: Type de document.
    - is_accounting: Indique si le type de document est comptable.
    """
    id: int | None = None
    label: str | None = None
    short_label: str | None = None
    document_kind: str = DocumentKind.INVOICE
    is_accounting: bool = False
    is_managed: bool = False
    is_mandatory: bool = False
    is_visible: bool = False


class DocumentLabelElement(CamelModel):
    """
    Représente un élément d'étiquette de document dans l'API Henrri Connect.

    Attributs:
    - id: Identifiant unique de l'élément d'étiquette.
    - model_element_id: Id de l'élément de modèle auquel appartient l'élément d'étiquette.
    - label: Libellé de l'élément d'étiquette.
    - value: Valeur de l'élément d'étiquette.
    - element_type: Type de l'élément d'étiquette.
    - is_main_element: Indique si l'élément d'étiquette est l'élément principal de l'étiquette.
    - size: Taille de l'élément d'étiquette.
    - index: Index de l'élément d'étiquette dans l'étiquette.
    - links: Liste de liens associés à l'élément d'étiquette (si applicable).
    """
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
    """
    Représente une étiquette de document dans l'API Henrri Connect.
    
    Attributs:
    - id: Identifiant unique de l'étiquette de document.
    - model_id: Id du modèle auquel appartient l'étiquette de document.
    - document_id: Id du document auquel appartient l'étiquette de document.
    - label: Libellé de l'étiquette de document.
    - elements: Liste d'éléments d'étiquette de doc associés à l'étiquette de doc (si applicable).
    - links: Liste de liens associés à l'étiquette de document (si applicable).
    """
    id: int | None = None
    model_id: int | None = None
    document_id: int | None = None
    label: str | None = None
    elements: list[DocumentLabelElement] | None = None
    links: list[Link] | None = None


class Document(CamelModel):
    """
    Représente un document dans l'API Henrri Connect.
    
    Attributs:
    - id: Identifiant unique du document.
    - identity: Identité du document.
    - finalized: Indique si le document est finalisé.
    - type: Type du document.
    - document_type_id: Identifiant du type de document.
    - document_type: Type de document (si applicable).
    - title: Titre du document.
    - subtitle: Sous-titre du document (si applicable).
    - price_before_tax: Prix total avant taxe du document.
    - tax_amount: Montant total de la taxe du document.
    - price_after_tax: Prix total après taxe du document.
    - due_label: Libellé de l'échéance du document (si applicable).
    - last_modification_date: Date de dernière modification du document.
    - date: Date du document.
    - validated: Indique si le document est validé.
    - validation_date: Date de validation du document (si applicable).
    - validation_firstname: Prénom de la personne ayant validé le document (si applicable).
    - validation_lastname: Nom de la personne ayant validé le document (si applicable).
    - validation_email: E-mail de la personne ayant validé le document (si applicable).
    - validation_ip: IP de la personne ayant validé le document (si applicable).
    - lines: Liste de lignes de document associées au document (si applicable).
    - customer_id: Identifiant du client associé au document (si applicable).
    - customer: Client associé au document (si applicable).
    - customer_address: Adresse du client associée au document (si applicable).
    - user_can_validate: Indique si l'utilisateur peut valider le document.
    - footer_text: Texte de pied de page du document (si applicable).
    - bank_account_label: Libellé du compte bancaire associé au document (si applicable).
    - label_id: Identifiant de l'étiquette de document associée au document (si applicable).
    - links: Liste de liens associés au document (si applicable).
    """
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
    customer_id: int
    customer: Customer | None = None
    customer_address: Address | None = None
    user_can_validate: bool = False
    footer_text: str | None = None
    bank_account_label: str | None = None
    label_id: int | None = None
    links: list[Link] | None = None


class DocumentQuery(CamelModel):
    """
    Représente une requête de document dans l'API Henrri Connect.
    
    Attributs:
    - finalized (bool) : Indique si le document est finalisé.
    - document_types (list[DocumentKind]) :: Type du document.
    - state (Optional[DocumentState]) : Etat du document.
    - page (int) : Numéro de page (de 1 à 2 147 483 647, défaut 1).
    - limit (int) : Nombre de documents par page (de 1 à 100, défaut 50).
    - search (str) : Chaine de recherche.
    - sort_by (str) : Champ de tri.
    - sort_order (SortOrder) : Ordre de tri (Ascending ou Descending).
    - min_id (int) : Identifiant minimum.
    - from_date (str) : Date de debut.
    - to_date (str) : Date de fin.
    """
    finalized: bool = False
    document_types: list[DocumentKind] | None = None
    state: DocumentState | None = None
    page: int = 1
    limit: int = 50
    search: str | None = None
    sort_by: str | None = None
    sort_order: SortOrder | None = None
    min_id: int | None = None
    from_date: str | None = None
    to_date: str | None = None


class ValidateDocumentRequest(CamelModel):
    """
    Représente une requête de validation de document dans l'API Henrri Connect.
    
    Attributs:
    - email: Adresse e-mail de la personne validant le document.
    - first_name: Prénom de la personne validant le document.
    - last_name: Nom de la personne validant le document.
    - validation_date: Date de validation du document.
    - time_offset: Décalage horaire par rapport à UTC.
    - ip: Adresse IP de la personne validant le document.
    """
    email: str
    first_name: str
    last_name: str
    validation_date: str
    time_offset: int
    ip: str
