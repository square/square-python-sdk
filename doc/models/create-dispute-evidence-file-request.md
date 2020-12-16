
# Create Dispute Evidence File Request

Defines the parameters for a `CreateDisputeEvidenceFile` request.

## Structure

`Create Dispute Evidence File Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `string` |  | The Unique ID. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency). |
| `evidence_type` | [`str (Dispute Evidence Type)`](/doc/models/dispute-evidence-type.md) | Optional | The type of the dispute evidence. |
| `content_type` | `string` | Optional | The MIME type of the uploaded file.<br>The type can be image/heic, image/heif, image/jpeg, application/pdf, image/png, or image/tiff. |

## Example (as JSON)

```json
{
  "idempotency_key": "idempotency_key6",
  "evidence_type": "RECEIPT",
  "content_type": "content_type6"
}
```

