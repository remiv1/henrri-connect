"""Modèles pour les utilisateurs dans l'API Henrri Connect."""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel, Link
from .company import Company
from .address_contacts import Address


class User(CamelModel):
    id: int | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    url_image: str | None = None
    first_connexion_date: datetime | None = None
    last_connexion_date: datetime | None = None
    connexion_count: str | None = None
    created_from: str | None = None
    phone_number: str | None = None
    creation_date: datetime | None = None
    is_enabled: bool = False
    two_factor_enabled: bool = False
    address: Address | None = None
    links: list[Link] | None = None


class UserAndCompany(CamelModel):
    user: User
    company: Company
