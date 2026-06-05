"""
Modèles pour les adresses et contacts dans l'API Henrri Connect.

Attributs:
- Address: Représente une adresse d'entreprise.
- Contact: Représente un contact d'entreprise.
"""
from __future__ import annotations

from .base import CamelModel, Link

class Address(CamelModel):
    """
    Représente une adresse d'entreprise.

    Attributs:
    - id: Identifiant unique de l'adresse.
    - address: Adresse de l'entreprise.
    - city: Ville de l'entreprise.
    - post_code: Code postal de l'entreprise.
    - country: Pays de l'entreprise.
    - is_post_code_shared: Indique si le code postal est partagé avec d'autres adresses.
    - links: Liste de liens associés à l'adresse (si applicable).
    """
    id: int | None = None
    address: str | None = None
    city: str | None = None
    post_code: str | None = None
    country: str | None = None
    is_post_code_shared: bool = False
    links: list[Link] | None = None


class Contact(CamelModel):
    """
    Représente un contact d'entreprise.

    Attributs:
    - id: Identifiant unique du contact.
    - title: Titre du contact.
    - first_name: Prénom du contact.
    - last_name: Nom de famille du contact.
    - email: Adresse e-mail du contact.
    - phone: Numéro de téléphone du contact.
    - mobile: Numéro de téléphone mobile du contact.
    - role: Rôle du contact dans l'entreprise.
    - is_primary: Indique si le contact est le contact principal de l'entreprise.
    - show_on_document: Indique si le contact doit être affiché sur les documents.
    - links: Liste de liens associés au contact (si applicable).
    """
    id: int | None = None
    title: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    mobile: str | None = None
    role: str | None = None
    is_primary: bool = False
    show_on_document: bool = False
    links: list[Link] | None = None
