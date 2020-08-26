## Submit Evidence Response

Defines fields in a SubmitEvidence response.

### Structure

`SubmitEvidenceResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `dispute` | [`Dispute`](/doc/models/dispute.md) | Optional | Represents a dispute a cardholder initiated with their bank. |

### Example (as JSON)

```json
{
  "errors": [
    {
      "category": "AUTHENTICATION_ERROR",
      "code": "REQUEST_TIMEOUT",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "INVALID_REQUEST_ERROR",
      "code": "CONFLICT",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "RATE_LIMIT_ERROR",
      "code": "GONE",
      "detail": "detail3",
      "field": "field1"
    }
  ],
  "dispute": {
    "dispute_id": "dispute_id8",
    "amount_money": {
      "amount": 40,
      "currency": "BWP"
    },
    "reason": "CANCELLED",
    "state": "INQUIRY_PROCESSING",
    "due_at": "due_at4"
  }
}
```

