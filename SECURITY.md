# Politique de Sécurité

Merci de contribuer à la sécurité de **henrri-connect**.
Nous prenons la sécurité très au sérieux et apprécions toute démarche responsable visant à signaler une vulnérabilité.

---

## 🔐 Signalement d’une vulnérabilité

Si vous découvrez une faille de sécurité, merci de **ne pas ouvrir d’issue publique**.

Veuillez signaler la vulnérabilité de manière responsable à l’adresse suivante :

**<rverschuur@audit-io.fr>**

Merci d’inclure dans votre message :

- une description claire de la vulnérabilité
- les étapes pour la reproduire
- l’impact potentiel
- toute preuve de concept utile
- votre environnement (OS, version Python, etc.)

Nous nous engageons à répondre dans un délai raisonnable.

---

## 🕒 Délais de réponse

Nous nous efforçons de :

- **accuser réception** du signalement sous 72 heures
- **analyser** la vulnérabilité sous 7 jours
- **proposer un correctif** ou un plan d’action sous 14 jours
- **publier un correctif** dès qu’il est prêt et testé

Ces délais peuvent varier selon la gravité et la complexité de la vulnérabilité.

---

## 🤝 Divulgation responsable

Nous demandons aux chercheurs en sécurité de :

- ne pas exploiter la vulnérabilité au-delà de ce qui est nécessaire pour la démonstration
- ne pas accéder, modifier ou supprimer des données
- ne pas perturber les services ou les utilisateurs
- nous laisser le temps de corriger le problème avant toute divulgation publique

Une divulgation responsable permet de protéger l’ensemble de la communauté.

---

## 🧪 Ce qui est considéré comme une vulnérabilité

Nous considérons comme vulnérabilité :

- exécution de code non autorisée
- injection (commande, code, CSV, etc.)
- contournement de validation ou de typage
- corruption de données
- escalade de privilèges
- fuite d’informations sensibles
- comportement non déterministe pouvant mener à une corruption de données ONIX

---

## ❌ Ce qui n’est pas considéré comme une vulnérabilité

- erreurs de parsing dues à des fichiers ONIX mal formés
- absence de prise en charge d’un format ONIX spécifique
- problèmes liés à des dépendances obsolètes (sauf si exploitables)
- erreurs de configuration dans l’environnement utilisateur
- comportements attendus documentés dans la spécification ONIX

---

## 🔄 Processus de publication des correctifs

Lorsqu’une vulnérabilité est confirmée :

1. Un correctif est développé dans une branche privée.
2. Le correctif est testé et validé.
3. Une nouvelle version est publiée sur PyPI.
4. Une note de version (release note) décrit la correction.
5. La vulnérabilité peut être divulguée publiquement une fois corrigée.

---

## 🙏 Remerciements

Merci à toutes les personnes qui contribuent à la sécurité de **henrri-connect**.
Votre aide renforce la fiabilité et la souveraineté de l’écosystème Henrri.
