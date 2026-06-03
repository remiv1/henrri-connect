# revenues — Statistiques de revenus

> [⇐ Retour à l'index](../README.md)

`client.revenues` — Consultation des statistiques de revenus annuelles et mensuelles.

---

## Méthodes

### `get_annual(year: int) -> RevenueStatistics`

Récupère les statistiques de revenus globales pour une année donnée.

### `get_monthly(year: int) -> list[MonthlyRevenueStatistics]`

Récupère les statistiques de revenus mois par mois pour une année donnée. Retourne une liste de 12 éléments.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import SyncHenrriClient

client = SyncHenrriClient("client_id", "client_secret")

# Statistiques annuelles
stats = client.revenues.get_annual(2025)
print(stats.total)

# Statistiques mensuelles
monthly = client.revenues.get_monthly(2025)
for month in monthly:
    print(month.month, month.total)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import AsyncHenrriClient

async def main():
    client = AsyncHenrriClient("client_id", "client_secret")

    stats = await client.revenues.get_annual(2025)
    print(stats.total)

    monthly = await client.revenues.get_monthly(2025)
    for month in monthly:
        print(month.month, month.total)

asyncio.run(main())
```

[↑ Retour en haut](#revenues--statistiques-de-revenus)

[⇐ Retour à l'index](../README.md)
