
# Invoice Filter

Describes query filters to apply.

## Structure

`Invoice Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_ids` | `List[str]` | Required | Limits the search to the specified locations. A location is required.<br>In the current implementation, only one location can be specified. |
| `customer_ids` | `List[str]` | Optional | Limits the search to the specified customers, within the specified locations.<br>Specifying a customer is optional. In the current implementation,<br>a maximum of one customer can be specified. |

## Example (as JSON)

```json
{
  "location_ids": [
    "location_ids0",
    "location_ids1",
    "location_ids2"
  ],
  "customer_ids": [
    "customer_ids3",
    "customer_ids2"
  ]
}
```

