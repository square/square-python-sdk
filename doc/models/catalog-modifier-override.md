## Catalog Modifier Override

### Structure

`CatalogModifierOverride`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `modifier_id` | `string` |  | The ID of the [CatalogModifier](./models/catalog-modifier.md) whose default behavior is being overridden. |
| `on_by_default` | `bool` | Optional | If `true`, this [CatalogModifier](./models/catalog-modifier.md) should be selected by default for this [CatalogItem](./models/catalog-item.md). |

### Example (as JSON)

```json
{
  "modifier_id": "modifier_id2",
  "on_by_default": null
}
```

