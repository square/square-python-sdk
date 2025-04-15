
# Deprecated Create Dispute Evidence File Request

Defines the parameters for a `DeprecatedCreateDisputeEvidenceFile` request.

## Structure

`Deprecated Create Dispute Evidence File Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Required | The Unique ID. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `45` |
| `evidence_type` | [`str (Dispute Evidence Type)`](../../doc/models/dispute-evidence-type.md) | Optional | The type of the dispute evidence. |
| `content_type` | `str` | Optional | The MIME type of the uploaded file.<br>The type can be image/heic, image/heif, image/jpeg, application/pdf, image/png, or image/tiff.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |

## Example (as JSON)

```json
{
  "idempotency_key": "idempotency_key4",
  "evidence_type": "ONLINE_OR_APP_ACCESS_LOG",
  "content_type": "content_type2"
}
```

