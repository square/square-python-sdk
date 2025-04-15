
# Gift Card Activity Transfer Balance To

Represents details about a `TRANSFER_BALANCE_TO` [gift card activity type](../../doc/models/gift-card-activity-type.md).

## Structure

`Gift Card Activity Transfer Balance To`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_from_gift_card_id` | `str` | Required | The ID of the gift card from which the specified amount was transferred. |
| `amount_money` | [`Money`](../../doc/models/money.md) | Required | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |

## Example (as JSON)

```json
{
  "transfer_from_gift_card_id": "transfer_from_gift_card_id6",
  "amount_money": {
    "amount": 186,
    "currency": "AUD"
  }
}
```

