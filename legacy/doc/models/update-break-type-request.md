
# Update Break Type Request

A request to update a `BreakType`.

## Structure

`Update Break Type Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `break_type` | [`Break Type`](../../doc/models/break-type.md) | Required | A defined break template that sets an expectation for possible `Break`<br>instances on a `Shift`. |

## Example (as JSON)

```json
{
  "break_type": {
    "break_name": "Lunch",
    "expected_duration": "PT50M",
    "is_paid": true,
    "location_id": "26M7H24AZ9N6R",
    "version": 1,
    "id": "id8",
    "created_at": "created_at6",
    "updated_at": "updated_at4"
  }
}
```

