"""Modèles de services pour Henrri."""

from typing import Optional, Any
from os import getenv
from dataclasses import dataclass
from henrri_connect import SyncHenrriClient

class HenrriService:
    """Service de base pour les échanges avec Henrri."""

    client: SyncHenrriClient

    def __init__(self):
        key = HenrriConfig().api_key
        secret = HenrriConfig().api_secret
        url = HenrriConfig().api_url
        if url:
            client = SyncHenrriClient(
                    key,
                    secret,
                    base_url=url,
                )
        else:
            client = SyncHenrriClient(
                    key,
                    secret,
                )
        self.client = client



@dataclass
class HenrriConfig:
    """Configuration pour les échanges avec Henrri."""
    api_key: str = getenv("HENRRI_API_KEY", "")
    api_url: Optional[str] = getenv("HENRRI_API_URL", None)
    api_secret: str = getenv("HENRRI_API_SECRET", "")



class HenrriProductsService(HenrriService):
    """Service de gestion des produits pour Henrri."""

    def get_products(self) -> list[dict[str, Any]]:
        """Récupère la liste des produits depuis Henrri."""

        response = self.client.items.list_items()
        return [item.model_dump() for item in response.elements or []]
