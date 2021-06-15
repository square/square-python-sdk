
# Create Gift Card Request

A request to create a gift card.

## Structure

`Create Gift Card Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `string` | Required | A unique string that identifies the `CreateGiftCard` request.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128` |
| `location_id` | `string` | Required | The location ID where the gift card that will be created should be registered.<br>**Constraints**: *Minimum Length*: `1` |
| `gift_card` | [`Gift Card`](/doc/models/gift-card.md) | Required | Represents a Square gift card. |

## Example (as JSON)

```json
{
  "gift_card": {
    "type": "DIGITAL"
  },
  "idempotency_key": "NC9Tm69EjbjtConu",
  "location_id": "81FN9BNFZTKS4"
}
```

