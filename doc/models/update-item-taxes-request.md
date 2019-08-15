## Update Item Taxes Request

### Structure

`UpdateItemTaxesRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_ids` | `List of string` |  | The [CatalogItem](./models/catalog-item.md)s whose enabled/disabled [CatalogTax](./models/catalog-tax.md)es are being updated. |
| `taxes_to_enable` | `List of string` | Optional | The set of [CatalogTax](./models/catalog-tax.md)es (referenced by ID) to enable for the [CatalogItem](./models/catalog-item.md). |
| `taxes_to_disable` | `List of string` | Optional | The set of [CatalogTax](./models/catalog-tax.md)es (referenced by ID) to disable for the [CatalogItem](./models/catalog-item.md). |

### Example (as JSON)

```json
{
  "item_ids": [
    "H42BRLUJ5KTZTTMPVSLFAACQ",
    "2JXOBJIHCWBQ4NZ3RIXQGJA6"
  ],
  "taxes_to_enable": [
    "4WRCNHCJZDVLSNDQ35PP6YAD"
  ],
  "taxes_to_disable": [
    "AQCEGCEBBQONINDOHRGZISEX"
  ]
}
```

