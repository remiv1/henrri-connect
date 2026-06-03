"""
Sous-client pour les endpoints /v1/companies.

Constantes:
-----------
- `COMPANIES_ENDPOINT`: URL de base des endpoints entreprises (/v1/companies).

Classes:
--------
- `henrri_connect.companies.synchro.SyncCompaniesClient`:
    Accès synchrone aux endpoints entreprises.

Notes:
-----
- Utiliser de préférence l'objet `henrri_connect.connect.SyncHenrriClient` pour acceder
aux endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..models import Address, Company

if TYPE_CHECKING:
    from ..connect import (
        SyncHenrriClient,
    )

class SyncCompaniesClient:
    """
    Accès synchrone aux endpoints entreprises.

    Arguments:
    - `client`(SyncHenrriClient): Client HTTP.
    
    Methodes:
    - get(self, company_id: int): Récupère une entreprise par son identifiant.
    - get_address(self, company_id: int): Récupère l'adresse d'une entreprise.
    """
    def __init__(self, client: SyncHenrriClient) -> None:
        self._c = client

    def get(self, company_id: int) -> Company:
        """
        Récupère une entreprise par son identifiant.
        
        Arguments:
        - `company_id`: Identifiant de l'entreprise.
        
        Retourne:
        - `henrri_connect.models.Company`: Entreprise.
        """
        resp = self._c.request("GET", f"/v1/companies/{company_id}")
        return Company.model_validate(resp.json())

    def get_address(self, company_id: int) -> Address:
        """
        Récupère l'adresse d'une entreprise.
        
        Arguments:
        - `company_id`: Identifiant de l'entreprise.
        
        Retourne:
        - `henrri_connect.models.Address`: Adresse de l'entreprise.
        """
        resp = self._c.request("GET", f"/v1/companies/{company_id}/address")
        return Address.model_validate(resp.json())
