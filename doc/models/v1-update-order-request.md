## V1 Update Order Request

V1UpdateOrderRequest

### Structure

`V1UpdateOrderRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`str (V1 Update Order Request Action)`]($m/V1UpdateOrderRequestAction) |  | - |
| `shipped_tracking_number` | `string` | Optional | The tracking number of the shipment associated with the order. Only valid if action is COMPLETE. |
| `completed_note` | `string` | Optional | A merchant-specified note about the completion of the order. Only valid if action is COMPLETE. |
| `refunded_note` | `string` | Optional | A merchant-specified note about the refunding of the order. Only valid if action is REFUND. |
| `canceled_note` | `string` | Optional | A merchant-specified note about the canceling of the order. Only valid if action is CANCEL. |

### Example (as JSON)

```json
{
  "action": "COMPLETE",
  "shipped_tracking_number": null,
  "completed_note": null,
  "refunded_note": null,
  "canceled_note": null
}
```

