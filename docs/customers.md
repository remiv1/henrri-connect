# customers — Clients

> [⇐ Retour à l'index](../README.md)

`client.customers` — CRUD complet sur les clients, avec gestion des adresses et des contacts.

---

## Méthodes

### Liste et recherche

#### `list_customers(*, page=1, limit=50, search=None, sort_by=None, sort_order=None, min_id=None, from_date=None, to_date=None) -> PagedListResponse[Customer]`

Liste les clients avec pagination et filtres optionnels.

| Paramètre | Type | Description |
| --- | --- | --- |
| `page` | `int` | Numéro de page (défaut : 1) |
| `limit` | `int` | Nombre de résultats par page (défaut : 50) |
| `search` | `str \| None` | Recherche textuelle |
| `sort_by` | `str \| None` | Champ de tri |
| `sort_order` | `str \| None` | `"asc"` ou `"desc"` |
| `min_id` | `int \| None` | Filtre sur l'identifiant minimum |
| `from_date` | `str \| None` | Date de début (format ISO 8601) |
| `to_date` | `str \| None` | Date de fin (format ISO 8601) |

#### `get_best_sales(*, page=1, limit=50, search=None, sort_by=None, sort_order=None) -> PagedListResponse[Customer]`

Récupère les meilleurs clients (par chiffre d'affaires).

### CRUD

#### `add(customer: Customer) -> Customer`

Crée un nouveau client.

#### `get(customer_id: int) -> Customer`

Récupère un client par son identifiant.

#### `modify(customer_id: int, customer: Customer) -> Customer`

Met à jour un client existant.

#### `delete(customer_id: int) -> None`

Supprime un client.

### Adresse

#### `get_address(customer_id: int) -> Address`

Récupère l'adresse d'un client.

### Contacts

#### `list_contacts(customer_id: int) -> list[Contact]`

Liste les contacts d'un client.

#### `add_contact(customer_id: int, contact: Contact) -> Contact`

Ajoute un contact à un client.

#### `get_contact(customer_id: int, contact_id: int) -> Contact`

Récupère un contact spécifique.

#### `modify_contact(customer_id: int, contact_id: int, contact: Contact) -> Contact`

Met à jour un contact.

#### `delete_contact(customer_id: int, contact_id: int) -> None`

Supprime un contact.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import SyncHenrriClient
from henrri_connect.models import Customer, Contact

client = SyncHenrriClient("client_id", "client_secret")

# Lister les clients avec recherche
result = client.customers.list_customers(search="Dupont", limit=10)
for customer in result.data:
    print(customer.id, customer.name)

# Créer un client
nouveau = client.customers.add(Customer(name="Société Example", email="contact@example.fr"))
print(nouveau.id)

# Modifier un client
client.customers.modify(nouveau.id, Customer(name="Société Example SARL"))

# Ajouter un contact
contact = client.customers.add_contact(nouveau.id, Contact(first_name="Alice", last_name="Martin"))

# Supprimer
client.customers.delete(nouveau.id)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import AsyncHenrriClient

async def main():
    client = AsyncHenrriClient("client_id", "client_secret")

    result = await client.customers.list_customers(limit=5)
    for customer in result.data:
        print(customer.name)

asyncio.run(main())
```

[↑ Retour en haut](#customers--clients)

[⇐ Retour à l'index](../README.md)
