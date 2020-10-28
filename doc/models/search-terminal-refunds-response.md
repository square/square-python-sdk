
# Search Terminal Refunds Response

## Structure

`Search Terminal Refunds Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `refunds` | [`List of Terminal Refund`](/doc/models/terminal-refund.md) | Optional | The requested search result of `TerminalRefund`s. |
| `cursor` | `string` | Optional | The pagination cursor to be used in a subsequent request. If empty,<br>this is the final response.<br><br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |

## Example (as JSON)

```json
{
  "errors": [
    {
      "category": "AUTHENTICATION_ERROR",
      "code": "MAP_KEY_LENGTH_TOO_SHORT",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "INVALID_REQUEST_ERROR",
      "code": "MAP_KEY_LENGTH_TOO_LONG",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "RATE_LIMIT_ERROR",
      "code": "CARD_EXPIRED",
      "detail": "detail3",
      "field": "field1"
    }
  ],
  "refunds": [
    {
      "id": "id4",
      "refund_id": "refund_id8",
      "payment_id": "payment_id4",
      "order_id": "order_id8",
      "amount_money": {
        "amount": 186,
        "currency": "YER"
      },
      "reason": "reason0",
      "device_id": "device_id0"
    },
    {
      "id": "id5",
      "refund_id": "refund_id9",
      "payment_id": "payment_id5",
      "order_id": "order_id9",
      "amount_money": {
        "amount": 187,
        "currency": "ZAR"
      },
      "reason": "reason9",
      "device_id": "device_id1"
    },
    {
      "id": "id6",
      "refund_id": "refund_id0",
      "payment_id": "payment_id6",
      "order_id": "order_id0",
      "amount_money": {
        "amount": 188,
        "currency": "ZMK"
      },
      "reason": "reason8",
      "device_id": "device_id2"
    }
  ],
  "cursor": "cursor6"
}
```

