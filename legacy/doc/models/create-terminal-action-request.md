
# Create Terminal Action Request

## Structure

`Create Terminal Action Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Required | A unique string that identifies this `CreateAction` request. Keys can be any valid string<br>but must be unique for every `CreateAction` request.<br><br>See [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more<br>information.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64` |
| `action` | [`Terminal Action`](../../doc/models/terminal-action.md) | Required | Represents an action processed by the Square Terminal. |

## Example (as JSON)

```json
{
  "action": {
    "deadline_duration": "PT5M",
    "device_id": "{{DEVICE_ID}}",
    "save_card_options": {
      "customer_id": "{{CUSTOMER_ID}}",
      "reference_id": "user-id-1"
    },
    "type": "SAVE_CARD",
    "id": "id2",
    "status": "status4",
    "cancel_reason": "TIMED_OUT"
  },
  "idempotency_key": "thahn-70e75c10-47f7-4ab6-88cc-aaa4076d065e"
}
```

