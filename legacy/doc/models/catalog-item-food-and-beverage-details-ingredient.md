
# Catalog Item Food and Beverage Details Ingredient

Describes the ingredient used in a `FOOD_AND_BEV` item.

## Structure

`Catalog Item Food and Beverage Details Ingredient`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | [`str (Catalog Item Food and Beverage Details Dietary Preference Type)`](../../doc/models/catalog-item-food-and-beverage-details-dietary-preference-type.md) | Optional | The type of dietary preference for the `FOOD_AND_BEV` type of items and integredients. |
| `standard_name` | [`str (Catalog Item Food and Beverage Details Ingredient Standard Ingredient)`](../../doc/models/catalog-item-food-and-beverage-details-ingredient-standard-ingredient.md) | Optional | Standard ingredients for food and beverage items that are recommended on item creation. |
| `custom_name` | `str` | Optional | The name of a custom user-defined ingredient. This should be null if it's a standard dietary preference. |

## Example (as JSON)

```json
{
  "type": "STANDARD",
  "standard_name": "GLUTEN",
  "custom_name": "custom_name6"
}
```

