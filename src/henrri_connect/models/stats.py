"""
Modèles Pydantic représentant les entités de statistiques dans l'API Henrri.

Attributs:
- RevenueStatistics: Représente les statistiques de revenus dans l'API Henrri Connect.
- MonthlyRevenueStatistics: Représente les statistiques de revenus mensuels dans l'entreprise.
"""

from __future__ import annotations

from .base import CamelModel

class RevenueStatistics(CamelModel):
    """
    Représente les statistiques de revenus dans l'API Henrri Connect.

    Attributs:
    - year: Année des statistiques.
    - total_services_revenue: Revenu total des services.
    - total_products_revenue: Revenu total des produits.
    - total_products_margin: Marge totale sur les produits.
    - total_service_hours: Nombre total d'heures de service.
    """
    year: int = 0
    total_services_revenue: float = 0.0
    total_products_revenue: float = 0.0
    total_products_margin: float = 0.0
    total_service_hours: float = 0.0


class MonthlyRevenueStatistics(CamelModel):
    """
    Représente les statistiques de revenus mensuels dans l'API Henrri Connect.

    Attributs:
    - month: Mois des statistiques.
    - year: Année des statistiques.
    - total_services_revenue: Revenu total des services.
    - total_products_revenue: Revenu total des produits.
    - total_products_margin: Marge totale sur les produits.
    - total_service_hours: Nombre total d'heures de service.
    """
    month: int = 0
    year: int = 0
    total_services_revenue: float = 0.0
    total_products_revenue: float = 0.0
    total_products_margin: float = 0.0
    total_service_hours: float = 0.0
