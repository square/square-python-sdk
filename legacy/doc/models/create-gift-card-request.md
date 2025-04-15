
# Create Gift Card Request

Represents a [CreateGiftCard](../../doc/api/gift-cards.md#create-gift-card) request.

## Structure

`Create Gift Card Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Required | A unique identifier for this request, used to ensure idempotency. For more information,<br>see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `location_id` | `str` | Required | The ID of the [location](entity:Location) where the gift card should be registered for<br>reporting purposes. Gift cards can be redeemed at any of the seller's locations.<br>**Constraints**: *Minimum Length*: `1` |
| `gift_card` | [`Gift Card`](../../doc/models/gift-card.md) | Required | Represents a Square gift card. |

## Example (as JSON)

```json
{
  "gift_card": {
    "type": "DIGITAL",
    "id": "id0",
    "gan_source": "SQUARE",
    "state": "ACTIVE",
    "balance_money": {
      "amount": 146,
      "currency": "BBD"
    },
    "gan": "gan6"
  },
  "idempotency_key": "NC9Tm69EjbjtConu",
  "location_id": "81FN9BNFZTKS4"
}
```

