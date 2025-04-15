
# List Payout Entries Response

The response to retrieve payout records entries.

## Structure

`List Payout Entries Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payout_entries` | [`List Payout Entry`](../../doc/models/payout-entry.md) | Optional | The requested list of payout entries, ordered with the given or default sort order. |
| `cursor` | `str` | Optional | The pagination cursor to be used in a subsequent request. If empty, this is the final response.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Information about errors encountered during the request. |

## Example (as JSON)

```json
{
  "cursor": "TbfI80z98Xc2LdApCyZ2NvCYLpkPurYLR16GRIttpMJ55mrSIMzHgtkcRQdT0mOnTtfHO",
  "payout_entries": [
    {
      "effective_at": "2021-12-14T23:31:49Z",
      "fee_amount_money": {
        "amount": -2,
        "currency_code": "USD",
        "currency": "CHF"
      },
      "gross_amount_money": {
        "amount": -50,
        "currency_code": "USD",
        "currency": "MNT"
      },
      "id": "poe_ZQWcw41d0SGJS6IWd4cSi8mKHk",
      "net_amount_money": {
        "amount": -48,
        "currency_code": "USD",
        "currency": "XPT"
      },
      "payout_id": "po_4d28e6c4-7dd5-4de4-8ec9-a059277646a6",
      "type": "REFUND",
      "type_refund_details": {
        "payment_id": "HVdG62HeMlti8YYf94oxrN",
        "refund_id": "HVdG62HeMlti8YYf94oxrN_dR8Nztxg7umf94oxrN12Ji5r2KW14FAY"
      }
    },
    {
      "effective_at": "2021-12-14T23:31:49Z",
      "fee_amount_money": {
        "amount": 19,
        "currency_code": "USD",
        "currency": "CHF"
      },
      "gross_amount_money": {
        "amount": 100,
        "currency_code": "USD",
        "currency": "MNT"
      },
      "id": "poe_EibbY9Ob1d0SGJS6IWd4cSiSi6wkaPk",
      "net_amount_money": {
        "amount": 81,
        "currency_code": "USD",
        "currency": "XPT"
      },
      "payout_id": "po_4d28e6c4-7dd5-4de4-8ec9-a059277646a6",
      "type": "CHARGE",
      "type_charge_details": {
        "payment_id": "HVdG62H5K3291d0SGJS6IWd4cSi8YY"
      }
    }
  ],
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ]
}
```

