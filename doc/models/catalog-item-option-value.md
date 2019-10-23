## Catalog Item Option Value

An enumerated value that can link a
[CatalogItemVariation(#type-catalogitemvariation) to an item option as one of
its item option values.

### Structure

`CatalogItemOptionValue`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_option_id` | `string` | Optional | Unique ID of the associated item option. |
| `name` | `string` | Optional | Name of this item option value. Searchable. |
| `description` | `string` | Optional | The option value's human-readable description. |
| `color` | `string` | Optional | The HTML-supported hex color for the item option<br>(e.g., "#ff8d4e85"). Only displayed if `show_colors` is enabled on the<br>parent `ItemOption`. When left unset, `color` defaults to white ("#ffffff")<br>when `show_colors` is enabled on the parent `ItemOption`. |
| `ordinal` | `int` | Optional | Determines where this option value appears in a list of option values. |
| `item_variation_count` | `long|int` | Optional | The number of [CatalogItemVariation(#type-catalogitemvariation)s that<br>currently make use of this Item Option value. Present only if `retrieve_counts`<br>was specified on the request used to retrieve the parent Item Option of this<br>value.<br><br>Maximum: 100 counts. |

### Example (as JSON)

```json
{
  "item_option_id": null,
  "name": null,
  "description": null,
  "color": null,
  "ordinal": null,
  "item_variation_count": null
}
```

