
# Quick Pay

Describes an ad hoc item and price to generate a quick pay checkout link.
For more information,
see [Quick Pay Checkout](https://developer.squareup.com/docs/checkout-api/quick-pay-checkout).

## Structure

`Quick Pay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The ad hoc item name. In the resulting `Order`, this name appears as the line item name.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `price_money` | [`Money`](../../doc/models/money.md) | Required | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `location_id` | `str` | Required | The ID of the business location the checkout is associated with. |

## Example (as JSON)

```json
{
  "name": "name8",
  "price_money": {
    "amount": 202,
    "currency": "GTQ"
  },
  "location_id": "location_id2"
}
```

