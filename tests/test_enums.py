"""Tests des énumérations du module models.base.enums."""

from __future__ import annotations

import pytest   # type: ignore[import] # pylint: disable=W0611

from henrri_connect.models.base.enums import CompanyIdentifierType


class TestCompanyIdentifierType:
    """Tests du comportement de l'enum CompanyIdentifierType."""

    def test_valeur_exacte(self) -> None:
        """Vérifie la résolution des valeurs canoniques de l'enum."""
        assert CompanyIdentifierType("Unknown") is CompanyIdentifierType.UNKNOWN
        assert CompanyIdentifierType("Siret") is CompanyIdentifierType.SIRET
        assert CompanyIdentifierType("Bce") is CompanyIdentifierType.BCE

    @pytest.mark.parametrize("valeur_api", ["unknown", "UNKNOWN", "UnKnOwN"])
    def test_insensible_a_la_casse(self, valeur_api: str) -> None:
        """L'API Henrri peut renvoyer 'unknown' en minuscule (bug observé en sandbox)."""
        assert CompanyIdentifierType(valeur_api) is CompanyIdentifierType.UNKNOWN

    def test_valeur_invalide_leve_value_error(self) -> None:
        """Une valeur inconnue doit lever une ValueError standard."""
        with pytest.raises(ValueError):
            CompanyIdentifierType("ValeurInexistante")