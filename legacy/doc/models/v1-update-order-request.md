
# V1 Update Order Request

V1UpdateOrderRequest

## Structure

`V1 Update Order Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`str (V1 Update Order Request Action)`](../../doc/models/v1-update-order-request-action.md) | Required | - |
| `shipped_tracking_number` | `str` | Optional | The tracking number of the shipment associated with the order. Only valid if action is COMPLETE. |
| `completed_note` | `str` | Optional | A merchant-specified note about the completion of the order. Only valid if action is COMPLETE. |
| `refunded_note` | `str` | Optional | A merchant-specified note about the refunding of the order. Only valid if action is REFUND. |
| `canceled_note` | `str` | Optional | A merchant-specified note about the canceling of the order. Only valid if action is CANCEL. |

## Example (as JSON)

```json
{
  "action": "COMPLETE",
  "shipped_tracking_number": "shipped_tracking_number4",
  "completed_note": "completed_note4",
  "refunded_note": "refunded_note8",
  "canceled_note": "canceled_note6"
}
```

