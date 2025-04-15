
# V1 List Orders Request

## Structure

`V1 List Orders Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |
| `limit` | `int` | Optional | The maximum number of payments to return in a single response. This value cannot exceed 200. |
| `batch_token` | `str` | Optional | A pagination cursor to retrieve the next set of results for your<br>original query to the endpoint. |

## Example (as JSON)

```json
{
  "order": "DESC",
  "limit": 24,
  "batch_token": "batch_token4"
}
```

