
# Dispute Evidence

## Structure

`Dispute Evidence`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `evidence_id` | `string` | Optional | The Square-generated ID of the evidence.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `id` | `string` | Optional | The Square-generated ID of the evidence.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `dispute_id` | `string` | Optional | The ID of the dispute the evidence is associated with.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `evidence_file` | [`Dispute Evidence File`](/doc/models/dispute-evidence-file.md) | Optional | A file to be uploaded as dispute evidence. |
| `evidence_text` | `string` | Optional | Raw text<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `500` |
| `uploaded_at` | `string` | Optional | The time when the next action is due, in RFC 3339 format.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `evidence_type` | [`str (Dispute Evidence Type)`](/doc/models/dispute-evidence-type.md) | Optional | The type of the dispute evidence. |

## Example (as JSON)

```json
{
  "evidence_id": "evidence_id2",
  "id": "id0",
  "dispute_id": "dispute_id2",
  "evidence_file": {
    "filename": "filename8",
    "filetype": "filetype8"
  },
  "evidence_text": "evidence_text6"
}
```

