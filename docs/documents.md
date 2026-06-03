# documents — Documents

> [⇐ Retour à l'index](../README.md)

`client.documents` — Gestion complète des documents commerciaux (factures, devis, bons de livraison, avoirs…).

---

## Méthodes

### Liste et recherche

#### `list_documents(*, page=1, limit=50, search=None, sort_by=None, sort_order=None, document_type_id=None, customer_id=None, state=None, from_date=None, to_date=None, min_id=None) -> PagedListResponse[Document]`

Liste les documents avec pagination et filtres.

| Paramètre | Type | Description |
| --- | --- | --- |
| `page` | `int` | Numéro de page (défaut : 1) |
| `limit` | `int` | Résultats par page (défaut : 50) |
| `search` | `str \| None` | Recherche textuelle |
| `sort_by` | `str \| None` | Champ de tri |
| `sort_order` | `str \| None` | `"asc"` ou `"desc"` |
| `document_type_id` | `int \| None` | Filtre par type de document |
| `customer_id` | `int \| None` | Filtre par client |
| `state` | `str \| None` | Filtre par état (`"draft"`, `"validated"`, etc.) |
| `from_date` | `str \| None` | Date de début (ISO 8601) |
| `to_date` | `str \| None` | Date de fin (ISO 8601) |
| `min_id` | `int \| None` | Identifiant minimum |

#### `list_with_selected_fields(*, page=1, limit=50, fields=None, **kwargs) -> PagedListResponse[Document]`

Liste les documents avec sélection de champs (optimise la charge réseau).

### CRUD

#### `add(document: Document) -> Document`

Crée un nouveau document.

#### `get(id: int) -> Document`

Récupère un document par son identifiant.

#### `get_with_all(id: int) -> Document`

Récupère un document avec toutes ses relations incluses (lignes, client, etc.).

#### `get_all_included(id: int) -> Document`

Récupère un document avec toutes ses données incluses.

#### `get_display(id: int) -> Document`

Récupère les données d'affichage d'un document.

#### `modify(id: int, document: Document) -> Document`

Met à jour un document existant.

#### `delete(id: int) -> None`

Supprime un document.

### Taxes et paiements

#### `get_tax_details(id: int) -> TaxDetailArray`

Récupère le détail des taxes appliquées au document.

#### `get_payment_milestones(document_id: int) -> ListResponse[PaymentMilestone]`

Récupère les jalons de paiement d'un document.

### Cycle de vie

#### `validate(id: int, request: ValidateDocumentRequest) -> Document`

Valide électroniquement un document.

#### `finalize(id: int) -> Document`

Finalise un document (passage en état définitif).

#### `transform_to_invoice(id: int) -> Document`

Transforme un document (devis, bon de livraison…) en facture.

#### `get_next_quote_batch() -> object`

Récupère le prochain numéro de lot pour un devis.

### PDF

#### `get_pdf_url(id: int) -> PdfUrlResponse`

Génère une URL de téléchargement temporaire pour le PDF du document.

#### `get_pdf_bytes(id: int) -> bytes`

Télécharge le PDF du document et retourne les octets bruts.

#### `get_pdf_file(id: int, guid: str) -> bytes`

Télécharge un PDF identifié par son GUID.

---

## Exemples

### **Synchrone**

```python
from henrri_connect import SyncHenrriClient
from henrri_connect.models import Document

client = SyncHenrriClient("client_id", "client_secret")

# Lister les factures d'un client
result = client.documents.list_documents(customer_id=42, document_type_id=1)
for doc in result.data:
    print(doc.id, doc.number)

# Créer un document
doc = client.documents.add(Document(customer_id=42, document_type_id=1))

# Récupérer avec toutes les relations
full_doc = client.documents.get_with_all(doc.id)

# Télécharger le PDF
pdf_bytes = client.documents.get_pdf_bytes(doc.id)
with open("facture.pdf", "wb") as f:
    f.write(pdf_bytes)

# Valider
from henrri_connect.models import ValidateDocumentRequest
client.documents.validate(doc.id, ValidateDocumentRequest())

# Transformer un devis en facture
invoice = client.documents.transform_to_invoice(doc.id)
```

### **Asynchrone**

```python
import asyncio
from henrri_connect import AsyncHenrriClient

async def main():
    client = AsyncHenrriClient("client_id", "client_secret")

    result = await client.documents.list_documents(limit=10)
    for doc in result.data:
        print(doc.id)

asyncio.run(main())
```

[↑ Retour en haut](#documents--documents)

[⇐ Retour à l'index](../README.md)
