# item_categories — Catégories d'articles

> [⇐ Retour à l'index](../README.md)

``client.item_categories`` — Référentiel des catégories permettant d'organiser le catalogue d'articles.

---

## Méthodes

### `list_item_categories(*, page=1, limit=50, search=None, sort_by=None, sort_order=None) -> PagedListResponse[ItemCategory]`

Liste les catégories d'articles avec pagination.

| Paramètre | Type | Description |
| --- | --- | --- |
| ``page`` | ``int`` | Numéro de page (défaut : 1) |
| ``limit`` | ``int`` | Résultats par page (défaut : 50) |
| ``search`` | ``str \| None`` | Recherche textuelle |
| ``sort_by`` | ``str \| None`` | Champ de tri |
| ``sort_order`` | ``str \| None`` | ``"asc"`` ou ``"desc"`` |

---

## Exemples

### **Synchrone**

```python
from henrri_connect import SyncHenrriClient

client = SyncHenrriClient("client_id", "client_secret")

result = client.item_categories.list_item_categories()
for category in result.data:
    print(category.id, category.name)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import AsyncHenrriClient

async def main():
    client = AsyncHenrriClient("client_id", "client_secret")

    result = await client.item_categories.list_item_categories()
    for category in result.data:
        print(category.id, category.name)

asyncio.run(main())
```

[↑ Retour en haut](#item_categories--catégories-darticles)

[⇐ Retour à l'index](../README.md)
