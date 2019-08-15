## Batch Delete Catalog Objects Request

### Structure

`BatchDeleteCatalogObjectsRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object_ids` | `List of string` | Optional | The IDs of the [CatalogObject](./models/catalog-object.md)s to be deleted. When an object is deleted, other objects<br>in the graph that depend on that object will be deleted as well (for example, deleting a<br>[CatalogItem](./models/catalog-item.md) will delete its [CatalogItemVariation](./models/catalog-item-variation.md)s). |

### Example (as JSON)

```json
{
  "object_ids": [
    "W62UWFY35CWMYGVWK6TWJDNI",
    "AA27W3M2GGTF3H6AVPNB77CK"
  ]
}
```

