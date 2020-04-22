## Customer Segment

Represents a group of customer profiles that match one or more predefined filter criteria. 

Segments (also known as Smart Groups) are defined and created within Customer Directory in the Square Dashboard or Point of Sale.

### Structure

`CustomerSegment`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Unique Square-generated ID for the segment. |
| `name` | `string` |  | Name of the segment. |
| `created_at` | `string` | Optional | The timestamp when the segment was created, in RFC 3339 format. |
| `updated_at` | `string` | Optional | The timestamp when the segment was last updated, in RFC 3339 format. |

### Example (as JSON)

```json
{
  "id": null,
  "name": "name0",
  "created_at": null,
  "updated_at": null
}
```

