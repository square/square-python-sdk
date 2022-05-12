
# Cancel Booking Request

## Structure

`Cancel Booking Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `string` | Optional | A unique key to make this request an idempotent operation.<br>**Constraints**: *Maximum Length*: `255` |
| `booking_version` | `int` | Optional | The revision number for the booking used for optimistic concurrency. |

## Example (as JSON)

```json
{
  "idempotency_key": null,
  "booking_version": null
}
```

