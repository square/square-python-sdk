
# Loyalty Program Terminology

Represents the naming used for loyalty points.

## Structure

`Loyalty Program Terminology`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `one` | `str` | Required | A singular unit for a point (for example, 1 point is called 1 star).<br>**Constraints**: *Minimum Length*: `1` |
| `other` | `str` | Required | A plural unit for point (for example, 10 points is called 10 stars).<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "one": "one4",
  "other": "other0"
}
```

