# document_line_types — Types de ligne de document

> [⇐ Retour à l'index](../README.md)

``client.document_line_types`` — Référentiel des types de lignes pouvant apparaître dans un document (article, texte libre, sous-total, saut de page…).

---

## Méthodes

### ``list_document_line_types() -> ListResponse[DocumentLineType]``

Retourne la liste complète des types de lignes de document. Ce référentiel est stable et peut être mis en cache côté application.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import SyncHenrriClient

client = SyncHenrriClient("client_id", "client_secret")

result = client.document_line_types.list_document_line_types()
for lt in result.data:
    print(lt.id, lt.name)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import AsyncHenrriClient

async def main():
    client = AsyncHenrriClient("client_id", "client_secret")

    result = await client.document_line_types.list_document_line_types()
    for lt in result.data:
        print(lt.id, lt.name)

asyncio.run(main())
```

[↑ Retour en haut](#document_line_types--types-de-ligne-de-document)

[⇐ Retour à l'index](../README.md)
