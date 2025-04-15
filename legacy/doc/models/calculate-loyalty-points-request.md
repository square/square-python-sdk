
# Calculate Loyalty Points Request

Represents a [CalculateLoyaltyPoints](../../doc/api/loyalty.md#calculate-loyalty-points) request.

## Structure

`Calculate Loyalty Points Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Optional | The [order](entity:Order) ID for which to calculate the points.<br>Specify this field if your application uses the Orders API to process orders.<br>Otherwise, specify the `transaction_amount_money`. |
| `transaction_amount_money` | [`Money`](../../doc/models/money.md) | Optional | Represents an amount of money. `Money` fields can be signed or unsigned.<br>Fields that do not explicitly define whether they are signed or unsigned are<br>considered unsigned and can only hold positive amounts. For signed fields, the<br>sign of the value indicates the purpose of the money transfer. See<br>[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts)<br>for more information. |
| `loyalty_account_id` | `str` | Optional | The ID of the target [loyalty account](entity:LoyaltyAccount). Optionally specify this field<br>if your application uses the Orders API to process orders.<br><br>If specified, the `promotion_points` field in the response shows the number of points the buyer would<br>earn from the purchase. In this case, Square uses the account ID to determine whether the promotion's<br>`trigger_limit` (the maximum number of times that a buyer can trigger the promotion) has been reached.<br>If not specified, the `promotion_points` field shows the number of points the purchase qualifies<br>for regardless of the trigger limit.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |

## Example (as JSON)

```json
{
  "loyalty_account_id": "79b807d2-d786-46a9-933b-918028d7a8c5",
  "order_id": "RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY",
  "transaction_amount_money": {
    "amount": 64,
    "currency": "ANG"
  }
}
```

