
# List Cash Drawer Shift Events Response

## Structure

`List Cash Drawer Shift Events Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Optional | Opaque cursor for fetching the next page. Cursor is not present in<br>the last page of results. |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `cash_drawer_shift_events` | [`List Cash Drawer Shift Event`](../../doc/models/cash-drawer-shift-event.md) | Optional | All of the events (payments, refunds, etc.) for a cash drawer during<br>the shift. |

## Example (as JSON)

```json
{
  "cash_drawer_shift_events": [
    {
      "created_at": "2019-11-22T00:43:02.000Z",
      "description": "",
      "event_money": {
        "amount": 100,
        "currency": "USD"
      },
      "event_type": "CASH_TENDER_PAYMENT",
      "id": "9F07DB01-D85A-4B77-88C3-D5C64CEB5155",
      "team_member_id": ""
    },
    {
      "created_at": "2019-11-22T00:43:12.000Z",
      "description": "",
      "event_money": {
        "amount": 250,
        "currency": "USD"
      },
      "event_type": "CASH_TENDER_PAYMENT",
      "id": "B2854CEA-A781-49B3-8F31-C64558231F48",
      "team_member_id": ""
    },
    {
      "created_at": "2019-11-22T00:43:23.000Z",
      "description": "",
      "event_money": {
        "amount": 250,
        "currency": "USD"
      },
      "event_type": "CASH_TENDER_CANCELLED_PAYMENT",
      "id": "B5FB7F72-95CD-44A3-974D-26C41064D042",
      "team_member_id": ""
    },
    {
      "created_at": "2019-11-22T00:43:46.000Z",
      "description": "",
      "event_money": {
        "amount": 100,
        "currency": "USD"
      },
      "event_type": "CASH_TENDER_REFUND",
      "id": "0B425480-8504-40B4-A867-37B23543931B",
      "team_member_id": ""
    },
    {
      "created_at": "2019-11-22T00:44:18.000Z",
      "description": "Transfer from another drawer",
      "event_money": {
        "amount": 10000,
        "currency": "USD"
      },
      "event_type": "PAID_IN",
      "id": "8C66E60E-FDCF-4EEF-A98D-3B14B7ED5CBE",
      "team_member_id": ""
    },
    {
      "created_at": "2019-11-22T00:44:29.000Z",
      "description": "Transfer out to another drawer",
      "event_money": {
        "amount": 10000,
        "currency": "USD"
      },
      "event_type": "PAID_OUT",
      "id": "D5ACA7FE-C64D-4ADA-8BC8-82118A2DAE4F",
      "team_member_id": ""
    }
  ],
  "cursor": "cursor8",
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

