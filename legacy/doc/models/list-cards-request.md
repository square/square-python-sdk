
# List Cards Request

Retrieves details for a specific Card. Accessible via
HTTP requests at GET https://connect.squareup.com/v2/cards

## Structure

`List Cards Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.<br>**Constraints**: *Maximum Length*: `256` |
| `customer_id` | `str` | Optional | Limit results to cards associated with the customer supplied.<br>By default, all cards owned by the merchant are returned. |
| `include_disabled` | `bool` | Optional | Includes disabled cards.<br>By default, all enabled cards owned by the merchant are returned. |
| `reference_id` | `str` | Optional | Limit results to cards associated with the reference_id supplied. |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |

## Example (as JSON)

```json
{
  "cursor": "cursor6",
  "customer_id": "customer_id8",
  "include_disabled": false,
  "reference_id": "reference_id8",
  "sort_order": "DESC"
}
```

