
# Dispute Evidence Created Webhook Data

## Structure

`Dispute Evidence Created Webhook Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | `string` | Optional | Name of the affected dispute's type. |
| `id` | `string` | Optional | ID of the affected dispute. |
| `object` | [`Dispute Evidence Created Webhook Object`](/doc/models/dispute-evidence-created-webhook-object.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "type0",
  "id": "id0",
  "object": {
    "object": {
      "dispute_id": "dispute_id2",
      "id": "id0",
      "amount_money": {
        "amount": 186,
        "currency": "NGN"
      },
      "reason": "NOT_AS_DESCRIBED",
      "state": "PROCESSING"
    }
  }
}
```

