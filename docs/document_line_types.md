# document_line_types — Types de ligne de document

> [⇐ Retour à l'index](../README.md)

`client.document_line_types` — Référentiel des types de lignes pouvant apparaître dans un document (article, texte libre, sous-total, saut de page…).

---

## Méthodes

### `list_document_line_types() -> ListResponse[DocumentLineType]`

Retourne la liste complète des types de lignes de document. Ce référentiel est stable et peut être mis en cache côté application.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import HenrriClient

client = HenrriClient("client_id", "client_secret")

result = client.document_line_types.list_document_line_types()
for lt in result.data:
    print(lt.id, lt.name)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import HenrriClient

async def main():
    client = HenrriClient("client_id", "client_secret", async_mode=True)

    result = await client.document_line_types.list_document_line_types()
    for lt in result.data:
        print(lt.id, lt.name)

asyncio.run(main())
```
