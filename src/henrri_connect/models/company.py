"""
Modèles pour les entreprises dans l'API Henrri Connect.

Attributs:
- Company: Représente une entreprise dans l'API Henrri Connect.
"""

from __future__ import annotations

from .base import CamelModel, Link
from .address_contacts import Address

class Company(CamelModel):
    """
    Représente une entreprise dans l'API Henrri Connect.

    Attributs:
    - id: Identifiant unique de l'entreprise.
    - name: Nom de l'entreprise.
    - logo_url: URL du logo de l'entreprise.
    - is_self_employed: Indique si l'entreprise est un travailleur indépendant.
    - siret: Numéro SIRET de l'entreprise (si applicable).
    - email: Adresse e-mail de l'entreprise (si applicable).
    - web_site: Site web de l'entreprise (si applicable).
    - ape_code: Code APE de l'entreprise (si applicable).
    - ape_label: Libellé du code APE de l'entreprise (si applicable).
    - global_id: Identifiant global de l'entreprise (si applicable).
    - address: Adresse de l'entreprise (si applicable).
    - links: Liste de liens associés à l'entreprise (si applicable).
    """
    id: int | None = None
    name: str | None = None
    logo_url: str | None = None
    is_self_employed: bool = False
    siret: str | None = None
    email: str | None = None
    web_site: str | None = None
    ape_code: str | None = None
    ape_label: str | None = None
    global_id: int | None = None
    address: Address | None = None
    links: list[Link] | None = None
