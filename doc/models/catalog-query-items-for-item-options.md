## Catalog Query Items for Item Options

### Structure

`CatalogQueryItemsForItemOptions`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_option_ids` | `List of string` | Optional | A set of [CatalogItemOption](#type-catalogitemoption) IDs to be used to find associated<br>[CatalogItem](#type-catalogitem)s. All Items that contain all of the given Item Options (in any order)<br>will be returned. |

### Example (as JSON)

```json
{
  "item_option_ids": null
}
```

