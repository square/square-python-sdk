
# Create Dispute Evidence Text Request

Defines the parameters for a `CreateDisputeEvidenceText` request.

## Structure

`Create Dispute Evidence Text Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `string` |  | The Unique ID. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency). |
| `evidence_type` | [`str (Dispute Evidence Type)`](/doc/models/dispute-evidence-type.md) | Optional | The type of the dispute evidence. |
| `evidence_text` | `string` |  | The evidence string. |

## Example (as JSON)

```json
{
  "evidence_text": "1Z8888888888888888",
  "evidence_type": "TRACKING_NUMBER",
  "idempotency_key": "ed3ee3933d946f1514d505d173c82648"
}
```

