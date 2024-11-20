
# List Cards Response

Defines the fields that are included in the response body of
a request to the [ListCards](../../doc/api/cards.md#list-cards) endpoint.

Note: if there are errors processing the request, the card field will not be
present.

## Structure

`List Cards Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `cards` | [`List Card`](../../doc/models/card.md) | Optional | The requested list of `Card`s. |
| `cursor` | `str` | Optional | The pagination cursor to be used in a subsequent request. If empty,<br>this is the final response.<br><br>See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information. |

## Example (as JSON)

```json
{
  "cards": [
    {
      "billing_address": {
        "address_line_1": "500 Electric Ave",
        "address_line_2": "Suite 600",
        "administrative_district_level_1": "NY",
        "country": "US",
        "locality": "New York",
        "postal_code": "10003"
      },
      "bin": "411111",
      "card_brand": "VISA",
      "card_type": "CREDIT",
      "cardholder_name": "Amelia Earhart",
      "customer_id": "VDKXEEKPJN48QDG3BGGFAK05P8",
      "enabled": true,
      "exp_month": 11,
      "exp_year": 2022,
      "fingerprint": "ex-p-cs80EK9Flz7LsCMv-szbptQ_ssAGrhemzSTsPFgt9nzyE6t7okiLIQc-qw_quqKX4Q",
      "id": "ccof:uIbfJXhXETSP197M3GB",
      "last_4": "1111",
      "merchant_id": "6SSW7HV8K2ST5",
      "prepaid_type": "NOT_PREPAID",
      "reference_id": "user-id-1",
      "version": 1
    }
  ],
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ],
  "cursor": "cursor6"
}
```

