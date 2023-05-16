
# Destination Details

Details about a refund's destination.

## Structure

`Destination Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_details` | [`Destination Details Card Refund Details`](../../doc/models/destination-details-card-refund-details.md) | Optional | - |

## Example (as JSON)

```json
{
  "card_details": {
    "card": {
      "id": "id6",
      "card_brand": "JCB",
      "last_4": "last_48",
      "exp_month": 4,
      "exp_year": 36
    },
    "entry_method": "entry_method8"
  }
}
```

