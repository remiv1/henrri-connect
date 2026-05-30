# document_lines — Lignes de document

> [⇐ Retour à l'index](../README.md)

`client.document_lines` — Gestion des lignes au sein d'un document (articles, descriptions, sous-totaux…).

---

## Méthodes

### `list_document_lines(document_id: int) -> ListResponse[DocumentLine]`

Liste toutes les lignes d'un document.

### `add(document_id: int, line: DocumentLine) -> DocumentLine`

Ajoute une ligne au document.

### `get(document_id: int, line_id: int) -> DocumentLine`

Récupère une ligne par son identifiant.

### `modify(document_id: int, line_id: int, line: DocumentLine) -> DocumentLine`

Met à jour une ligne existante.

### `delete(document_id: int, line_id: int) -> None`

Supprime une ligne.

### `move(document_id: int, line_id: int, to: int) -> None`

Déplace une ligne à la position indiquée (1-indexé).

---

## Exemples

### **Synchrone**

```python
from henrri_connect import HenrriClient
from henrri_connect.models import DocumentLine

client = HenrriClient("client_id", "client_secret")

document_id = 123

# Lister les lignes
result = client.document_lines.list_document_lines(document_id)
for line in result.data:
    print(line.id, line.description)

# Ajouter une ligne
line = client.document_lines.add(
    document_id,
    DocumentLine(item_id=10, quantity=2, unit_price=50.0),
)

# Déplacer la ligne en première position
client.document_lines.move(document_id, line.id, to=1)

# Modifier
client.document_lines.modify(document_id, line.id, DocumentLine(quantity=3))

# Supprimer
client.document_lines.delete(document_id, line.id)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import HenrriClient

async def main():
    client = HenrriClient("client_id", "client_secret", async_mode=True)

    result = await client.document_lines.list_document_lines(123)
    for line in result.data:
        print(line.id)

asyncio.run(main())
```
