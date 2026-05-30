"""Modèles pour les entreprises dans l'API Henrri Connect."""

from __future__ import annotations

from .base import CamelModel, Link
from .address_contacts import Address

class Company(CamelModel):
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
