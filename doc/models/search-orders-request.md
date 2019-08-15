## Search Orders Request

The request does not have any required fields. When given no query criteria,
SearchOrders will return all results for all of the merchant’s locations. When fetching additional
pages using a `cursor`, the `query` must be equal to the `query` used to fetch the first page of
results.

### Structure

`SearchOrdersRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_ids` | `List of string` | Optional | The location IDs for the orders to query. The caller must have access to<br>all provided locations. Leave unset to search all locations that the caller has access to. |
| `cursor` | `string` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |
| `query` | [`Search Orders Query`](/doc/models/search-orders-query.md) | Optional | Contains query criteria for the search. |
| `limit` | `int` | Optional | Number of results to be returned in a single page. SearchOrders may<br>use a smaller limit than specified depending on server load. If the response<br>includes a `cursor` field, you can use it to retrieve the next set of results.<br>Default: `500` |
| `return_entries` | `bool` | Optional | If set to `true`, SearchOrders will return [`OrderEntry`](#type-orderentry)<br>objects instead of `Order` objects. `OrderEntry` objects are lightweight<br>descriptions of orders that include `order_id`s.<br><br>Default: `false`. |

### Example (as JSON)

```json
{
  "return_entries": true,
  "limit": 3,
  "location_ids": [
    "057P5VYJ4A5X1",
    "18YC4JDH91E1H"
  ],
  "query": {
    "filter": {
      "date_time_filter": {
        "closed_at": {
          "start_at": "2018-03-03T20:00:00+00:00",
          "end_at": "2019-03-04T21:54:45+00:00"
        }
      },
      "state_filter": {
        "states": [
          "COMPLETED"
        ]
      }
    },
    "sort": {
      "sort_field": "CLOSED_AT",
      "sort_order": "DESC"
    }
  }
}
```

