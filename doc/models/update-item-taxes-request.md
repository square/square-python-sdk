## Update Item Taxes Request

### Structure

`UpdateItemTaxesRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_ids` | `List of string` |  | The [CatalogItem](#type-catalogitem)s whose enabled/disabled [CatalogTax](#type-catalogtax)es are being updated. |
| `taxes_to_enable` | `List of string` | Optional | The set of [CatalogTax](#type-catalogtax)es (referenced by ID) to enable for the [CatalogItem](#type-catalogitem). |
| `taxes_to_disable` | `List of string` | Optional | The set of [CatalogTax](#type-catalogtax)es (referenced by ID) to disable for the [CatalogItem](#type-catalogitem). |

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

