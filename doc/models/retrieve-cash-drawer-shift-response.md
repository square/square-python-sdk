## Retrieve Cash Drawer Shift Response

### Structure

`RetrieveCashDrawerShiftResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cash_drawer_shift` | [`Cash Drawer Shift`](/doc/models/cash-drawer-shift.md) | Optional | This model gives the details of a cash drawer shift.<br>The cash_payment_money, cash_refund_money, cash_paid_in_money,<br>and cash_paid_out_money fields are all computed by summing their respective<br>event types. |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |

### Example (as JSON)

```json
{
  "cash_drawer_shift": {
    "id": "id6",
    "state": "CLOSED",
    "opened_at": "opened_at4",
    "ended_at": "ended_at8",
    "closed_at": "closed_at8"
  },
  "errors": [
    {
      "category": "AUTHENTICATION_ERROR",
      "code": "REQUEST_TIMEOUT",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "INVALID_REQUEST_ERROR",
      "code": "CONFLICT",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "RATE_LIMIT_ERROR",
      "code": "GONE",
      "detail": "detail3",
      "field": "field1"
    }
  ]
}
```

