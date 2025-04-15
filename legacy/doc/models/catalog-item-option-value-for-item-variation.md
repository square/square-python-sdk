
# Catalog Item Option Value for Item Variation

A `CatalogItemOptionValue` links an item variation to an item option as
an item option value. For example, a t-shirt item may offer a color option and
a size option. An item option value would represent each variation of t-shirt:
For example, "Color:Red, Size:Small" or "Color:Blue, Size:Medium".

## Structure

`Catalog Item Option Value for Item Variation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_option_id` | `str` | Optional | The unique id of an item option. |
| `item_option_value_id` | `str` | Optional | The unique id of the selected value for the item option. |

## Example (as JSON)

```json
{
  "item_option_id": "item_option_id0",
  "item_option_value_id": "item_option_value_id2"
}
```

