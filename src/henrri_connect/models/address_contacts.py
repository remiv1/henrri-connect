"""Modèles pour les adresses et contacts dans l'API Henrri Connect."""
from __future__ import annotations

from .base import CamelModel, Link

class Address(CamelModel):
    """Représente une adresse d'entreprise."""
    id: int | None = None
    address: str | None = None
    city: str | None = None
    post_code: str | None = None
    country: str | None = None
    is_post_code_shared: bool = False
    links: list[Link] | None = None


class Contact(CamelModel):
    """Représente un contact d'entreprise."""
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
