# units — Unités de mesure

> [⇐ Retour à l'index](../README.md)

`client.units` — Gestion des unités de mesure utilisées dans les lignes de document (pièce, heure, kg, m², etc.).

---

## Méthodes

### `list_units() -> ListResponse[Unit]`

Retourne la liste complète des unités disponibles.

### `add(unit: Unit) -> Unit`

Crée une nouvelle unité personnalisée.

### `get(id: int) -> Unit`

Récupère une unité par son identifiant.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import SyncHenrriClient
from henrri_connect.models import Unit

client = SyncHenrriClient("client_id", "client_secret")

# Lister les unités disponibles
result = client.units.list_units()
for unit in result.data:
    print(unit.id, unit.name)

# Créer une unité personnalisée
new_unit = client.units.add(Unit(name="jour-homme", abbreviation="j/h"))

# Récupérer une unité
unit = client.units.get(new_unit.id)
print(unit.name)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import AsyncHenrriClient

async def main():
    client = AsyncHenrriClient("client_id", "client_secret")

    result = await client.units.list_units()
    for unit in result.data:
        print(unit.name)

asyncio.run(main())
```

[↑ Retour en haut](#units--unités-de-mesure)

[⇐ Retour à l'index](../README.md)
