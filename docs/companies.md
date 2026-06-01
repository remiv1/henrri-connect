# companies — Entreprises

> [⇐ Retour à l'index](../README.md)

`client.companies` — Lecture des données d'une entreprise et de son adresse.

---

## Méthodes

### `get(company_id: int) -> Company`

Récupère une entreprise par son identifiant.

### `get_address(company_id: int) -> Address`

Récupère l'adresse d'une entreprise.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import HenrriClient

client = HenrriClient("client_id", "client_secret")

company = client.companies.get(1)
print(company.name)

address = client.companies.get_address(1)
print(address.city)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import HenrriClient

async def main():
    client = HenrriClient("client_id", "client_secret", async_mode=True)

    company = await client.companies.get(1)
    print(company.name)

asyncio.run(main())
```

[↑ Retour en haut](#companies--entreprises)

[⇐ Retour à l'index](../README.md)
