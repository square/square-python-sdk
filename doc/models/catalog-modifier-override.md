## Catalog Modifier Override

### Structure

`CatalogModifierOverride`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `modifier_id` | `string` |  | The ID of the [CatalogModifier](#type-catalogmodifier) whose default behavior is being overridden. |
| `on_by_default` | `bool` | Optional | If `true`, this [CatalogModifier](#type-catalogmodifier) should be selected by default for this [CatalogItem](#type-catalogitem). |

### Example (as JSON)

```json
{
  "modifier_id": "modifier_id2",
  "on_by_default": null
}
```

