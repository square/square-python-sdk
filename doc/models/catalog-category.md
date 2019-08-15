## Catalog Category

A category to which an [CatalogItem](./models/catalog-item.md) belongs in the Catalog object model.

### Structure

`CatalogCategory`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The category's name. Searchable. This field has max length of 255 Unicode code points. |

### Example (as JSON)

```json
{
  "object": {
    "type": "CATEGORY",
    "id": "#Beverages",
    "present_at_all_locations": true,
    "category_data": {
      "name": "Beverages"
    }
  }
}
```

