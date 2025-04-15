
# Loyalty Event Type Filter

Filter events by event type.

## Structure

`Loyalty Event Type Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `types` | [`str (List Loyalty Event Type)`](../../doc/models/loyalty-event-type.md) | Required | The loyalty event types used to filter the result.<br>If multiple values are specified, the endpoint uses a<br>logical OR to combine them.<br>See [LoyaltyEventType](#type-loyaltyeventtype) for possible values |

## Example (as JSON)

```json
{
  "types": [
    "EXPIRE_POINTS",
    "OTHER",
    "ACCUMULATE_PROMOTION_POINTS"
  ]
}
```

