
# Dispute Evidence File

A file to be uploaded as dispute evidence.

## Structure

`Dispute Evidence File`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filename` | `str` | Optional | The file name including the file extension. For example: "receipt.tiff".<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `filetype` | `str` | Optional | Dispute evidence files must be application/pdf, image/heic, image/heif, image/jpeg, image/png, or image/tiff formats.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |

## Example (as JSON)

```json
{
  "filename": "filename0",
  "filetype": "filetype0"
}
```

