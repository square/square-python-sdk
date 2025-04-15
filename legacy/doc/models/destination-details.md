
# Destination Details

Details about a refund's destination.

## Structure

`Destination Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_details` | [`Destination Details Card Refund Details`](../../doc/models/destination-details-card-refund-details.md) | Optional | - |
| `cash_details` | [`Destination Details Cash Refund Details`](../../doc/models/destination-details-cash-refund-details.md) | Optional | Stores details about a cash refund. Contains only non-confidential information. |
| `external_details` | [`Destination Details External Refund Details`](../../doc/models/destination-details-external-refund-details.md) | Optional | Stores details about an external refund. Contains only non-confidential information. |

## Example (as JSON)

```json
{
  "card_details": {
    "card": {
      "id": "id6",
      "card_brand": "OTHER_BRAND",
      "last_4": "last_48",
      "exp_month": 228,
      "exp_year": 68
    },
    "entry_method": "entry_method8",
    "auth_result_code": "auth_result_code0"
  },
  "cash_details": {
    "seller_supplied_money": {
      "amount": 36,
      "currency": "MKD"
    },
    "change_back_money": {
      "amount": 78,
      "currency": "XBD"
    }
  },
  "external_details": {
    "type": "type6",
    "source": "source0",
    "source_id": "source_id8"
  }
}
```

