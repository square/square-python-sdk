## Update Item Modifier Lists Request

### Structure

`UpdateItemModifierListsRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_ids` | `List of string` |  | The [CatalogItem](#type-catalogitem)s whose [CatalogModifierList](#type-catalogmodifierlist)s are being updated. |
| `modifier_lists_to_enable` | `List of string` | Optional | The set of [CatalogModifierList](#type-catalogmodifierlist)s (referenced by ID) to enable for the [CatalogItem](#type-catalogitem). |
| `modifier_lists_to_disable` | `List of string` | Optional | The set of [CatalogModifierList](#type-catalogmodifierlist)s (referenced by ID) to disable for the [CatalogItem](#type-catalogitem). |

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

