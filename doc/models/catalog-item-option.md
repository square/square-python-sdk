
# Catalog Item Option

A group of variations for a `CatalogItem`.

## Structure

`Catalog Item Option`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The item option's display name for the seller. Must be unique across<br>all item options. This is a searchable attribute for use in applicable query filters. |
| `display_name` | `string` | Optional | The item option's display name for the customer. This is a searchable attribute for use in applicable query filters. |
| `description` | `string` | Optional | The item option's human-readable description. Displayed in the Square<br>Point of Sale app for the seller and in the Online Store or on receipts for<br>the buyer. This is a searchable attribute for use in applicable query filters. |
| `show_colors` | `bool` | Optional | If true, display colors for entries in `values` when present. |
| `values` | [`List of Catalog Object`](../../doc/models/catalog-object.md) | Optional | A list of CatalogObjects containing the<br>`CatalogItemOptionValue`s for this item. |

## Example (as JSON)

```json
{
  "name": null,
  "display_name": null,
  "description": null,
  "show_colors": null,
  "values": null
}
```

