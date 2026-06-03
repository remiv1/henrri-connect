# secures — Endpoint de santé

> [⇐ Retour à l'index](../README.md)

`client.secures` — Vérifie que la connexion authentifiée à l'API fonctionne correctement.

---

## Méthodes

### `hello_world() -> str`

Appelle l'endpoint `GET /v1/secures/hello-world` et retourne le texte de la réponse.  
Utile pour valider les identifiants et tester la connectivité.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import SyncHenrriClient

client = SyncHenrriClient("client_id", "client_secret")
print(client.secures.hello_world())  # "Hello World"
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import AsyncHenrriClient

async def main():
    client = AsyncHenrriClient("client_id", "client_secret")
    print(await client.secures.hello_world())

asyncio.run(main())
```

[↑ Retour en haut](#secures--endpoint-de-santé)

[⇐ Retour à l'index](../README.md)
