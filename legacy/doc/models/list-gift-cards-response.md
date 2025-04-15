
# List Gift Cards Response

A response that contains a list of `GiftCard` objects. If the request resulted in errors,
the response contains a set of `Error` objects.

## Structure

`List Gift Cards Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `gift_cards` | [`List Gift Card`](../../doc/models/gift-card.md) | Optional | The requested gift cards or an empty object if none are found. |
| `cursor` | `str` | Optional | When a response is truncated, it includes a cursor that you can use in a<br>subsequent request to retrieve the next set of gift cards. If a cursor is not present, this is<br>the final response.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |

## Example (as JSON)

```json
{
  "cursor": "JbFmyvUpaNKsfC1hoLSA4WlqkgkZXTWeKuStajR5BkP7OE0ETAbeWSi6U6u7sH",
  "gift_cards": [
    {
      "balance_money": {
        "amount": 3900,
        "currency": "USD"
      },
      "created_at": "2021-06-09T22:26:54.000Z",
      "gan": "7783320008524605",
      "gan_source": "SQUARE",
      "id": "gftc:00113070ba5745f0b2377c1b9570cb03",
      "state": "ACTIVE",
      "type": "DIGITAL"
    },
    {
      "balance_money": {
        "amount": 2000,
        "currency": "USD"
      },
      "created_at": "2021-05-20T22:26:54.000Z",
      "gan": "7783320002692465",
      "gan_source": "SQUARE",
      "id": "gftc:00128a12725b41e58e0de1d20497a9dd",
      "state": "ACTIVE",
      "type": "DIGITAL"
    }
  ],
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ]
}
```

