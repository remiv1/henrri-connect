# users — Utilisateurs

> [⇐ Retour à l'index](../README.md)

`client.users` — Accès aux données utilisateurs et aux entreprises associées.

> **Note :** L'authentification est gérée automatiquement par `HenrriClient`. Les méthodes `authenticate()` et `refresh_token()` du sous-client sont exposées pour les cas d'usage avancés.

---

## Méthodes

### `get(id: int) -> User`

Récupère un utilisateur par son identifiant.

### `get_address(id: int) -> Address`

Récupère l'adresse d'un utilisateur.

### `get_companies() -> list[UserAndCompany]`

Récupère les entreprises associées à l'utilisateur courant.

### `authenticate() -> TokenResponse`

Authentifie via les identifiants du client. Retourne `access_token` et `refresh_token`.

### `refresh_token(refresh_token: str) -> TokenResponse`

Rafraîchit le token d'accès à partir d'un refresh token.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import HenrriClient

client = HenrriClient("client_id", "client_secret")

user = client.users.get(1)
print(user.email)

companies = client.users.get_companies()
for uc in companies:
    print(uc.company.name)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import HenrriClient

async def main():
    client = HenrriClient("client_id", "client_secret", async_mode=True)

    user = await client.users.get(1)
    print(user.email)

asyncio.run(main())
```

[↑ Retour en haut](#users--utilisateurs)

[⇐ Retour à l'index](../README.md)
