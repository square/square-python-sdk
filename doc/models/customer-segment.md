
# Customer Segment

Represents a group of customer profiles that match one or more predefined filter criteria.

Segments (also known as Smart Groups) are defined and created within the Customer Directory in the
Square Seller Dashboard or Point of Sale.

## Structure

`Customer Segment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | A unique Square-generated ID for the segment.<br>**Constraints**: *Maximum Length*: `255` |
| `name` | `str` | Required | The name of the segment. |
| `created_at` | `str` | Optional | The timestamp when the segment was created, in RFC 3339 format. |
| `updated_at` | `str` | Optional | The timestamp when the segment was last updated, in RFC 3339 format. |

## Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "created_at": "created_at8",
  "updated_at": "updated_at6"
}
```

