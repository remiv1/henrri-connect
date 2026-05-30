# items — Articles

> [⇐ Retour à l'index](../README.md)

`client.items` — CRUD complet sur le catalogue d'articles / produits, avec statistiques d'utilisation.

---

## Méthodes

### Liste et recherche

#### `list_items(*, page=1, limit=50, search=None, sort_by=None, sort_order=None, item_category_id=None, min_id=None) -> PagedListResponse[Item]`

Liste les articles avec pagination et filtres.

| Paramètre | Type | Description |
| --- | --- | --- |
| `page` | `int` | Numéro de page (défaut : 1) |
| `limit` | `int` | Résultats par page (défaut : 50) |
| `search` | `str \| None` | Recherche textuelle |
| `sort_by` | `str \| None` | Champ de tri |
| `sort_order` | `str \| None` | `"asc"` ou `"desc"` |
| `item_category_id` | `int \| None` | Filtre par catégorie |
| `min_id` | `int \| None` | Identifiant minimum |

#### `get_most_used(*, page=1, limit=50, search=None) -> PagedListResponse[Item]`

Récupère les articles les plus fréquemment utilisés dans les documents.

#### `get_best_sales(*, page=1, limit=50, search=None) -> PagedListResponse[Item]`

Récupère les articles générant le plus de chiffre d'affaires.

#### `list_with_selected_fields(*, page=1, limit=50, fields=None) -> PagedListResponse[Item]`

Liste les articles avec sélection de champs (optimise la charge réseau).

### CRUD

#### `add(item: Item) -> Item`

Crée un nouvel article.

#### `get(id: int) -> Item`

Récupère un article par son identifiant.

#### `modify(id: int, item: Item) -> Item`

Met à jour un article existant.

#### `delete(id: int) -> None`

Supprime un article.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import HenrriClient
from henrri_connect.models import Item

client = HenrriClient("client_id", "client_secret")

# Lister les articles d'une catégorie
result = client.items.list_items(item_category_id=3, limit=20)
for item in result.data:
    print(item.id, item.name, item.price)

# Articles les plus vendus
top = client.items.get_best_sales(limit=5)

# Créer un article
new_item = client.items.add(Item(name="Prestation conseil", price=150.0, unit_id=1))

# Modifier
client.items.modify(new_item.id, Item(price=165.0))

# Supprimer
client.items.delete(new_item.id)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import HenrriClient

async def main():
    client = HenrriClient("client_id", "client_secret", async_mode=True)

    result = await client.items.list_items(limit=10)
    for item in result.data:
        print(item.name)

asyncio.run(main())
```
