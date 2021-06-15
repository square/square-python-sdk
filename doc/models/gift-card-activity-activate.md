
# Gift Card Activity Activate

Describes a gift card activity of the ACTIVATE type.

## Structure

`Gift Card Activity Activate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_money` | [`Money`](/doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `order_id` | `string` | Optional | The ID of the order associated with the activity.<br>This is required if your application uses the Square Orders API. |
| `line_item_uid` | `string` | Optional | The `line_item_uid` of the gift card line item in an order.<br>This is required if your application uses the Square Orders API. |
| `reference_id` | `string` | Optional | If your application does not use the Square Orders API, you can optionally use this field<br>to associate the gift card activity with a client-side entity. |
| `buyer_payment_instrument_ids` | `List of string` | Optional | Required if your application does not use the Square Orders API.<br>This is a list of client-provided payment instrument IDs.<br>Square uses this information to perform compliance checks.<br>If you use the Square Orders API, Square has the necessary instrument IDs to perform necessary<br>compliance checks. |

## Example (as JSON)

```json
{
  "amount_money": {
    "amount": 186,
    "currency": "NGN"
  },
  "order_id": "order_id6",
  "line_item_uid": "line_item_uid0",
  "reference_id": "reference_id2",
  "buyer_payment_instrument_ids": [
    "buyer_payment_instrument_ids6"
  ]
}
```

