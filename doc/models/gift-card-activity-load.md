
# Gift Card Activity Load

Present only when `GiftCardActivityType` is LOAD.

## Structure

`Gift Card Activity Load`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `order_id` | `string` | Optional | The `order_id` of the order associated with the activity.<br>It is populated along with `line_item_uid` and is required if using the Square Orders API. |
| `line_item_uid` | `string` | Optional | The `line_item_uid` of the gift card’s line item in the order associated with the activity.<br>It is populated along with `order_id` and is required if using the Square Orders API. |
| `reference_id` | `string` | Optional | A client-specified ID to associate an entity, in another system, with this gift card<br>activity. This can be used to track the order or payment related information when the Square Orders<br>API is not being used. |
| `buyer_payment_instrument_ids` | `List of string` | Optional | If you are not using the Orders API, this field is required because it is used to identify a buyer<br>to perform compliance checks. |

## Example (as JSON)

```json
{
  "amount_money": null,
  "order_id": null,
  "line_item_uid": null,
  "reference_id": null,
  "buyer_payment_instrument_ids": null
}
```

