## Catalog Item Option

A group of variations for a `CatalogItem`.

### Structure

`CatalogItemOption`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The item option's display name for the seller. Must be unique across<br>all item options. Searchable. |
| `display_name` | `string` | Optional | The item option's display name for the customer. Searchable. |
| `description` | `string` | Optional | The item option's human-readable description. Displayed in the Square<br>Point of Sale app for the seller and in the Online Store or on receipts for<br>the buyer. |
| `show_colors` | `bool` | Optional | If true, display colors for entries in `values` when present. |
| `values` | [`List of Catalog Object`]($m/CatalogObject) | Optional | A list of CatalogObjects containing the<br>`CatalogItemOptionValue`s for this item. |
| `item_count` | `long|int` | Optional | The number of `CatalogItem`s currently associated<br>with this item option. Present only if the `include_counts` was specified<br>in the request. Any count over 100 will be returned as `100`. |

### Example (as JSON)

```json
{
  "name": null,
  "display_name": null,
  "description": null,
  "show_colors": null,
  "values": null,
  "item_count": null
}
```

