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
from henrri_connect import SyncHenrriClient

client = SyncHenrriClient("client_id", "client_secret")

result = client.document_types.list_document_types()
for dt in result.data:
    print(dt.id, dt.name)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import AsyncHenrriClient

async def main():
    client = AsyncHenrriClient("client_id", "client_secret")

    result = await client.document_types.list_document_types()
    for dt in result.data:
        print(dt.id, dt.name)

asyncio.run(main())
```

[↑ Retour en haut](#document_types--types-de-document)

[⇐ Retour à l'index](../README.md)
