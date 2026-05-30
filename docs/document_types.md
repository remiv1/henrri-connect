# document_types — Types de document

> [⇐ Retour à l'index](../README.md)

`client.document_types` — Référentiel des types de documents disponibles dans Henrri (facture, devis, bon de livraison, avoir…).

---

## Méthodes

### `list_document_types() -> ListResponse[DocumentType]`

Retourne la liste complète des types de documents. Ce référentiel est généralement stable et peut être mis en cache côté application.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import HenrriClient

client = HenrriClient("client_id", "client_secret")

result = client.document_types.list_document_types()
for dt in result.data:
    print(dt.id, dt.name)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import HenrriClient

async def main():
    client = HenrriClient("client_id", "client_secret", async_mode=True)

    result = await client.document_types.list_document_types()
    for dt in result.data:
        print(dt.id, dt.name)

asyncio.run(main())
```
