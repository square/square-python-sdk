## Retrieve Catalog Object Request

### Structure

`RetrieveCatalogObjectRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_related_objects` | `bool` | Optional | If `true`, the response will include additional objects that are related to the<br>requested object, as follows:<br><br>If the `object` field of the response contains a [CatalogItem](./models/catalog-item.md),<br>its associated [CatalogCategory](./models/catalog-category.md), [CatalogTax](./models/catalog-tax.md)es,<br>[CatalogImage](./models/catalog-image.md)s and [CatalogModifierList](./models/catalog-modifier-list.md)s<br>will be returned in the `related_objects` field of the response. If the `object`<br>field of the response contains a [CatalogItemVariation](./models/catalog-item-variation.md),<br>its parent [CatalogItem](./models/catalog-item.md) will be returned in the `related_objects` field of <br>the response.<br><br>Default value: `false` |

### Example (as JSON)

```json
{
  "include_related_objects": null
}
```

