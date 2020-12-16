
# Create Dispute Evidence Text Response

Defines the fields in a `CreateDisputeEvidenceText` response.

## Structure

`Create Dispute Evidence Text Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `evidence` | [`Dispute Evidence`](/doc/models/dispute-evidence.md) | Optional | - |

## Example (as JSON)

```json
{
  "evidence": {
    "dispute_id": "bVTprrwk0gygTLZ96VX1oB",
    "evidence_id": "TOomLInj6iWmP3N8qfCXrB",
    "evidence_text": "1Z8888888888888888",
    "uploaded_at": "2018-10-18T16:01:10.000Z"
  }
}
```

