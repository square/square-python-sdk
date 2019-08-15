## Update Item Modifier Lists Request

### Structure

`UpdateItemModifierListsRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_ids` | `List of string` |  | The [CatalogItem](./models/catalog-item.md)s whose [CatalogModifierList](./models/catalog-modifier-list.md)s are being updated. |
| `modifier_lists_to_enable` | `List of string` | Optional | The set of [CatalogModifierList](./models/catalog-modifier-list.md)s (referenced by ID) to enable for the [CatalogItem](./models/catalog-item.md). |
| `modifier_lists_to_disable` | `List of string` | Optional | The set of [CatalogModifierList](./models/catalog-modifier-list.md)s (referenced by ID) to disable for the [CatalogItem](./models/catalog-item.md). |

### Example (as JSON)

```json
{
  "item_ids": [
    "H42BRLUJ5KTZTTMPVSLFAACQ",
    "2JXOBJIHCWBQ4NZ3RIXQGJA6"
  ],
  "modifier_lists_to_enable": [
    "H42BRLUJ5KTZTTMPVSLFAACQ",
    "2JXOBJIHCWBQ4NZ3RIXQGJA6"
  ],
  "modifier_lists_to_disable": [
    "7WRC16CJZDVLSNDQ35PP6YAD"
  ]
}
```

