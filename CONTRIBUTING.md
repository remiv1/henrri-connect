# Guide de Contribution

Merci de votre intérêt pour **henrri-connect** !
Ce projet vise à fournir une bibliothèque souveraine, fiable et ouverte pour le traitement des opération de facturation avec [Henrri](https://www.henrri.com).
Les contributions sont les bienvenues : corrections, améliorations, documentation, tests, nouvelles fonctionnalités…

Ce document explique comment contribuer efficacement.

---

## 🧱 Principes Généraux

- Soyez respectueux et bienveillant (voir le Code de Conduite).
- Préférez des contributions **simples, lisibles et testées**.
- Privilégiez la cohérence : style, structure, typage, documentation.
- Une petite PR bien ciblée vaut mieux qu’une grosse PR difficile à relire.

---

## 🛠 Prérequis

Avant de contribuer, assurez-vous d’avoir :

- Python 3.11 ou plus
- `pip` ou `uv` ou `poetry`
- `git`

Clonez le dépôt :

```bash
git clone https://github.com/remiv1/henrri-connect.git
cd henrri-connect

Installez les dépendances :

```bash
pip install -e .
pip install -r requirements-dev.txt
```

## 🧪 Lancer les tests

Les tests se trouvent dans le dossier `tests/`.

Pour les exécuter :

```bash
pytest
# ou avec le fichier Make
make test
```

Merci de vérifier que tous les tests passent avant de soumettre une PR.

## 🧩 Style de Code

Nous utilisons :

- PEP8 pour le style général
- type hints obligatoires
- dataclasses ou pydantic pour les modèles Henrri
- pytest pour les tests

Merci de respecter ces conventions.

## 🧬 Structure du Projet

```txt
henrri_connect/
    models/         # Dataclasses ou Pydantic pour les modèles Henrri
    utils/          # Alignement, validation, exceptions
    tests/          # Tests unitaires
```

## 📝 Proposer une Contribution

### 1. Ouvrir une issue

Avant de commencer une fonctionnalité importante, merci d’ouvrir une issue pour :

- décrire le problème
- proposer une solution
- éviter les doublons
- valider l’approche

### 2. Créer une branche

```bash
git checkout -b feature/ma-fonctionnalite
```

### 3. Faire des commits clairs

Format recommandé :

```txt
feat: ajout de la fonctionnalité X
fix: correction du décalage des colonnes
docs: amélioration du README
test: ajout de tests pour le bloc 2
```

### 4. Soumettre une Pull Request

Merci de :

- décrire clairement ce que fait la PR
- lier l’issue correspondante
- vérifier que les tests passent
- ajouter des tests si nécessaire

Les mainteneurs feront une revue dans les meilleurs délais.

## 🤝 Comment aider sans coder ?

Vous pouvez aussi contribuer en :

- signalant des bugs
- améliorant la documentation
- proposant des exemples d’usage
- testant la bibliothèque sur différents environnements
- partageant le projet

## 📬 Contact

Pour toute question, suggestion ou retour :

- <rverschuur@audit-io.fr>

Merci de contribuer à construire un outil souverain et utile pour Henrri !
