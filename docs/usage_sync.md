# Guide d'utilisation — Mode synchrone

> [⇐ Retour à l'index](../README.md)

Ce guide montre un flux d'utilisation complet en mode synchrone : recherche d'un client, création d'un client, création d'un produit, création d'un devis puis transformation en facture.

## Prérequis

- Python 3.11+ et un environnement virtuel activé
- Installer le paquet (local ou PyPI) :

```bash
pip install -e .    # depuis la racine du projet pour le développement
# ou
pip install henrri-connect
```

- Variables d'environnement : HENRRI_API_KEY, HENRRI_SECRET_KEY (ou utilisez un fichier .env.henrri chargé par python-dotenv).

## Authentification

Le client s'authentifie automatiquement à la première requête et gère le rafraîchissement du token. Il n'est pas nécessaire d'appeler authenticate() explicitement.

## Création du client

```python
from henrri_connect import HenrriClient
import os

client = HenrriClient(os.environ['HENRRI_API_KEY'], os.environ['HENRRI_SECRET_KEY'], async_mode=False)
```

### 1. Recherche d'un client

```python
# Liste paginée (PagedListResponse) ; récupérer la liste via .elements
page = client.customers.list_customers(search="ACME", limit=10)
customers = page.elements or []
for c in customers:
    print(c.id, c.name)
```

### 2. Création d'un client

```python
from henrri_connect.models import Customer, Contact, Address

customer = Customer(
    name="ACME Company",
    type="professional",
    address=Address(address="1 Rue Exemple", city="Paris", post_code="75001"),
    contacts=[Contact(first_name="Jean", last_name="Dupont", email="jean@acme.example", is_primary=True)],
)
created_customer = client.customers.add(customer)
print('Customer id:', created_customer.id)
```

### 3. Création d'un produit (item)

```python
from henrri_connect.models import Item

item = Item(
    reference="SKU-001",
    description="Chaise design",
    selling_price_without_tax=100.0,
    vat_percent=20.0,
)
created_item = client.items.add(item)
print('Item id:', created_item.id)
```

### 4. Création d'un devis puis transformation en facture

- Récupérer le document_type pour un devis et un type_id pour les lignes :

```python
doc_types = client.document_types.list_document_types()
quote_type = next((d for d in (doc_types.elements or []) if d.label and ("devis" in d.label.lower() or "quote" in d.label.lower())), None)
line_types = client.document_line_types.list_document_line_types()
line_type_id = (line_types.elements or [])[0].id
```

- Construire la ligne et le document :

```python
from henrri_connect.models import Document, DocumentLine

line = DocumentLine(
    type_id=line_type_id,
    item_id=created_item.id,
    description=created_item.description,
    quantity=2,
    selling_price_without_tax=created_item.selling_price_without_tax,
    vat_percent=created_item.vat_percent,
)

doc = Document(
    document_type_id=quote_type.id,
    customer_id=created_customer.id,
    title="Devis ACME - 001",
    lines=[line],
)

created_doc = client.documents.add(doc)
print('Devis id:', created_doc.id)
```

- Transformer en facture et finaliser :

```python
invoice = client.documents.transform_to_invoice(created_doc.id)
print('Invoice id:', invoice.id)

# (optionnel) finaliser
finalized = client.documents.finalize(invoice.id)
```

Gestion des erreurs

Les erreurs HTTP sont converties en exceptions typées (HenrriHTTPError, HenrriAuthError, HenrriValidationError, ...). Exemple :

```python
from henrri_connect.exc import HenrriHTTPError

try:
    client.customers.add(customer)
except HenrriHTTPError as e:
    print('Erreur API :', e)
```

## Ressources

- Spécification OpenAPI : docs/v1.json
- Référence code : src/henrri_connect

[↑ Retour en haut](#guide-dutilisation--mode-synchrone)

[⇐ Retour à l'index](../README.md)
