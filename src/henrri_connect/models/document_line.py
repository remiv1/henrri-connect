"""
Modèles document pour l'API Henrri Connect.

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

from .base import CamelModel, DocumentLineKind, Link, SortOrder
from .items import Item


class DocumentLineType(CamelModel):
    """
    Représente un type de ligne de document dans l'API Henrri Connect.

    Attributs:
    - id: Identifiant unique du type de ligne de document.
    - label: Libellé du type de ligne de document.
    - type: Type de ligne de document.
    """
    id: int | None = None
    label: str | None = None
    type: str = DocumentLineKind.NONE


class DocumentLine(CamelModel):
    """
    Représente une ligne de document dans l'API Henrri Connect.

    ``type_id`` peut être récupéré par un GET sur ``/documentlinetypes`` ou avec
    ``henrry_connect.<client>.document_line_types.list_document_line_types``

    Attributs:
    - id: Identifiant unique de la ligne de document.
    - document_id: Identifiant du document auquel appartient la ligne.
    - reference: Référence de la ligne de document.
    - description: Description de la ligne de document.
    - selling_price_without_tax: Prix de vente sans taxe de la ligne de document.
    - purchasing_price_without_tax: Prix d'achat sans taxe de la ligne de document.
    - vat_percent: Pourcentage de TVA appliqué à la ligne de document.
    - quantity: Quantité de l'article dans la ligne de document.
    - is_tax_included: Indique si les prix incluent la taxe.
    - total_without_tax: Total sans taxe pour la ligne de document.
    - total_with_tax: Total avec taxe pour la ligne de document.
    - are_elements_of_group_shown: Indique si les éléments du groupe sont affichés.
    - line_number: Numéro de la ligne dans le document.
    - is_a_group: Indique si la ligne est un groupe d'articles.
    - does_group_own_different_vat: Indique si le groupe a une TVA différente pour ses éléments.
    - is_member_of_a_group: Indique si la ligne est membre d'un groupe d'articles.
    - is_adjustment_of_group: Indique si la ligne est un ajustement d'un groupe d'articles.
    - type_id: Identifiant du type de ligne de document.
    - type: Type de ligne de document (si applicable).
    - group_id: Identifiant du groupe d'articles auquel appartient la ligne (si applicable).
    - item_id: Identifiant de l'article associé à la ligne (si applicable).
    - item: Article associé à la ligne (si applicable).
    - links: Liste de liens associés à la ligne de document (si applicable).
    """
    id: int | None = None
    document_id: int | None = None
    reference: str | None = None
    description: str | None = None
    selling_price_without_tax: float | None = None
    purchasing_price_without_tax: float = 0.0
    vat_percent: float | None = None
    quantity: float = 0.0
    is_tax_included: bool = False
    total_without_tax: float | None = None
    total_with_tax: float | None = None
    are_elements_of_group_shown: bool = False
    line_number: int | None = None
    is_a_group: bool = False
    does_group_own_different_vat: bool = False
    is_member_of_a_group: bool = False
    is_adjustment_of_group: bool = False
    type_id: int
    type: DocumentLineType | None = None
    group_id: int | None = None
    item_id: int | None = None
    item: Item | None = None
    links: list[Link] | None = None

class DecorativeDocumentLine(DocumentLine):
    """
    Représente une ligne de document decoratif dans l'API Henrri Connect.

    Attributs:
    - type_id: Identifiant du type de ligne de document.
    """
    type_id: int = 0
    document_id: int| None = None
    reference: str | None = None
    description: str | None = None
    selling_price_without_tax: float | None = None
    purchasing_price_without_tax: float = 0.0
    vat_percent: float | None = None
    quantity: float = 1.0
    is_tax_included: bool = False
    total_without_tax: float | None = None
    total_with_tax: float | None = None
    are_elements_of_group_shown: bool = False
    line_number: int | None = None
    is_a_group: bool = False
    does_group_own_different_vat: bool = False
    is_member_of_a_group: bool = False
    is_adjustment_of_group: bool = False
    type_id: int
    type: DocumentLineType | None = None
    group_id: int | None = None
    item_id: int | None = None
    item: Item | None = None
    links: list[Link] | None = None

    def horizontal_line(self) -> "DocumentLine":
        """
        Créer une ligne horizontale dans le document.

        Returns:
            DocumentLine: La ligne horizontale crée.
        """
        self.type_id = 13
        return self

    def empty_line(self) -> "DocumentLine":
        """
        Créer une ligne vide dans le document.

        Returns:
            DocumentLine: La ligne vide crée.
        """
        self.type_id = 11
        return self

    def subtotal_line(self) -> "DocumentLine":
        """
        Créer une ligne de sous-total dans le document.

        Returns:
            DocumentLine: La ligne de sous-total crée.
        """
        self.type_id = 5
        return self

    def total_line(self) -> "DocumentLine":
        """
        Créer une ligne de total dans le document.

        Returns:
            DocumentLine: La ligne de total crée.
        """
        self.type_id = 4
        return self

    def textual_line(self, text: str) -> "DocumentLine":
        """
        Créer une ligne de texte dans le document.

        Returns:
            DocumentLine: La ligne de texte crée.
        """
        self.type_id = 12
        self.description = text
        return self

class DocumentLineMoveQueryParameters(CamelModel):
    """
    Représente les paramètres de requête pour déplacer une ligne de document dans
    l'API Henrri Connect.

    Attributs:
    - to: Identifiant de la ligne de document vers laquelle déplacer la ligne.
    """
    to: int


class DocumentLineListQueryParameters(CamelModel):
    """
    Représente les paramètres de requête pour obtenir une liste de lignes de document
    dans l'API Henrri Connect.

    Attributs:
    - document_id: Identifiant du document auquel appartient la ligne.
    """
    page: int = 1
    limit: int = 50
    search: str | None = None
    sort_by: str | None = None
    sort_order: SortOrder | None = None
    minId: int
    from_date: str
    to_date: str
