
# Dispute Evidence

## Structure

`Dispute Evidence`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `evidence_id` | `str` | Optional | The Square-generated ID of the evidence.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `id` | `str` | Optional | The Square-generated ID of the evidence.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `dispute_id` | `str` | Optional | The ID of the dispute the evidence is associated with.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `evidence_file` | [`Dispute Evidence File`](../../doc/models/dispute-evidence-file.md) | Optional | A file to be uploaded as dispute evidence. |
| `evidence_text` | `str` | Optional | Raw text<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `500` |
| `uploaded_at` | `str` | Optional | The time when the evidence was uploaded, in RFC 3339 format.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `evidence_type` | [`str (Dispute Evidence Type)`](../../doc/models/dispute-evidence-type.md) | Optional | The type of the dispute evidence. |

## Example (as JSON)

```json
{
  "evidence_id": "evidence_id0",
  "id": "id2",
  "dispute_id": "dispute_id4",
  "evidence_file": {
    "filename": "filename8",
    "filetype": "filetype8"
  },
  "evidence_text": "evidence_text6"
}
```

