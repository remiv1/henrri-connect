"""Modèles Pydantic v2 pour l'API Henrri."""

from __future__ import annotations

from .base import CamelModel

class RevenueStatistics(CamelModel):
    year: int = 0
    total_services_revenue: float = 0.0
    total_products_revenue: float = 0.0
    total_products_margin: float = 0.0
    total_service_hours: float = 0.0


class MonthlyRevenueStatistics(CamelModel):
    month: int = 0
    year: int = 0
    total_services_revenue: float = 0.0
    total_products_revenue: float = 0.0
    total_products_margin: float = 0.0
    total_service_hours: float = 0.0