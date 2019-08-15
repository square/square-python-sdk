## Batch Retrieve Catalog Objects Request

### Structure

`BatchRetrieveCatalogObjectsRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object_ids` | `List of string` |  | The IDs of the [CatalogObject](./models/catalog-object.md)s to be retrieved. |
| `include_related_objects` | `bool` | Optional | If `true`, the response will include additional objects that are related to the<br>requested objects, as follows:<br><br>If the `objects` field of the response contains a [CatalogItem](./models/catalog-item.md), <br>its associated [CatalogCategory](./models/catalog-category.md), [CatalogTax](./models/catalog-tax.md)es,<br>[CatalogImage](./models/catalog-image.md)s and [CatalogModifierList](./models/catalog-modifier-list.md)s<br>will be returned in the `related_objects` field of the response. If the `objects`<br>field of the response contains a [CatalogItemVariation](./models/catalog-item-variation.md),<br>its parent [CatalogItem](./models/catalog-item.md) will be returned in the `related_objects` field of<br>the response. |

### Example (as JSON)

```json
{
  "object_ids": [
    "W62UWFY35CWMYGVWK6TWJDNI",
    "AA27W3M2GGTF3H6AVPNB77CK"
  ],
  "include_related_objects": true
}
```

