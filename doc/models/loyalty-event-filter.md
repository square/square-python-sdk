## Loyalty Event Filter

The filtering criteria. If the request specifies multiple filters, 
the endpoint uses a logical AND to evaluate them.

### Structure

`LoyaltyEventFilter`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loyalty_account_filter` | [`Loyalty Event Loyalty Account Filter`](/doc/models/loyalty-event-loyalty-account-filter.md) | Optional | Filter events by loyalty account. |
| `type_filter` | [`Loyalty Event Type Filter`](/doc/models/loyalty-event-type-filter.md) | Optional | Filter events by event type. |
| `date_time_filter` | [`Loyalty Event Date Time Filter`](/doc/models/loyalty-event-date-time-filter.md) | Optional | Filter events by date time range. |
| `location_filter` | [`Loyalty Event Location Filter`](/doc/models/loyalty-event-location-filter.md) | Optional | Filter events by location. |
| `order_filter` | [`Loyalty Event Order Filter`](/doc/models/loyalty-event-order-filter.md) | Optional | Filter events by the order associated with the event. |

### Example (as JSON)

```json
{
  "loyalty_account_filter": {
    "loyalty_account_id": "loyalty_account_id8"
  },
  "type_filter": {
    "types": [
      "REDEEM_REWARD",
      "DELETE_REWARD",
      "ADJUST_POINTS"
    ]
  },
  "date_time_filter": {
    "created_at": {
      "start_at": "start_at0",
      "end_at": "end_at2"
    }
  },
  "location_filter": {
    "location_ids": [
      "location_ids0",
      "location_ids1",
      "location_ids2"
    ]
  },
  "order_filter": {
    "order_id": "order_id2"
  }
}
```

