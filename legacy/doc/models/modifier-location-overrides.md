
# Modifier Location Overrides

Location-specific overrides for specified properties of a `CatalogModifier` object.

## Structure

`Modifier Location Overrides`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | The ID of the `Location` object representing the location. This can include a deactivated location. |
| `price_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `sold_out` | `bool` | Optional | Indicates whether the modifier is sold out at the specified location or not. As an example, for cheese (modifier) burger (item), when the modifier is sold out, it is the cheese, but not the burger, that is sold out.<br>The seller can manually set this sold out status. Attempts by an application to set this attribute are ignored. |

## Example (as JSON)

```json
{
  "location_id": "location_id2",
  "price_money": {
    "amount": 202,
    "currency": "GTQ"
  },
  "sold_out": false
}
```

