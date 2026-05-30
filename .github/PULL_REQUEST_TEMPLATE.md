# Pull Request Template

## Description

<!-- Décrivez les changements apportés par cette PR et leur motivation. -->

Fixes # <!-- numéro de l'issue associée, si applicable -->

## Type de changement

- [ ] Correction de bug (`fix`)
- [ ] Nouvelle fonctionnalité (`feat`)
- [ ] Refactoring sans changement de comportement (`refactor`)
- [ ] Mise à jour de la documentation (`docs`)
- [ ] Autre (préciser) :

## Changements effectués

- <!-- Ex. : Ajout de la méthode `list_by_date` dans `documents/synchro.py` et `documents/asynchro.py` -->
-
-

## Tests

- [ ] Les tests existants passent (`make test`)
- [ ] De nouveaux tests ont été ajoutés pour couvrir les changements
- [ ] Les cas limites ont été pris en compte

## Checklist

- [ ] Le code respecte les conventions du projet (type hints, docstrings Google style, commentaires en français)
- [ ] Le `CHANGELOG.md` a été mis à jour
- [ ] La version dans `pyproject.toml` a été incrémentée si nécessaire
- [ ] Les fichiers `.pyi` ont été mis à jour si l'interface publique a changé

## Contexte additionnel

<!-- Tout autre élément utile à la revue (captures d'écran, benchmark, etc.). -->
