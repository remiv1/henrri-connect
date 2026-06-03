"""
Modèles pour les utilisateurs dans l'API Henrri Connect.
"""

from __future__ import annotations

from datetime import datetime

from .base import CamelModel, Link
from .company import Company
from .address_contacts import Address


class User(CamelModel):
    """
    Représente un utilisateur dans l'API Henrri Connect.
    
    Attributs:
    - id: Identifiant de l'utilisateur.
    - email: Adresse email de l'utilisateur.
    - first_name: Prénom de l'utilisateur.
    - last_name: Nom de famille de l'utilisateur.
    - url_image: URL de l'image de profil de l'utilisateur.
    - first_connexion_date: Date de la première connexion de l'utilisateur.
    - last_connexion_date: Date de la dernière connexion de l'utilisateur.
    - connexion_count: Nombre de connexions de l'utilisateur.
    - created_from: Source de création de l'utilisateur.
    - phone_number: Numéro de téléphone de l'utilisateur.
    - creation_date: Date de création de l'utilisateur.
    - is_enabled: Indique si l'utilisateur est activé.
    - two_factor_enabled: Indique si l'authentification à deux facteurs est activée pour
    l'utilisateur.
    - address: Adresse de l'utilisateur (si applicable).
    - links: Liste de liens associés à l'utilisateur (si applicable).
    """
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
    """
    Représente un utilisateur et son entreprise dans l'API Henrri Connect.

    Attributs:
     - user: Utilisateur de l'API Henrri Connect.
     - company: Entreprise associée à l'utilisateur dans l'API Henrri Connect.
    """
    user: User
    company: Company
