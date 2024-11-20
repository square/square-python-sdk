
# List Customer Segments Response

Defines the fields that are included in the response body for requests to the `ListCustomerSegments` endpoint.

Either `errors` or `segments` is present in a given response (never both).

## Structure

`List Customer Segments Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `segments` | [`List Customer Segment`](../../doc/models/customer-segment.md) | Optional | The list of customer segments belonging to the associated Square account. |
| `cursor` | `str` | Optional | A pagination cursor to be used in subsequent calls to `ListCustomerSegments`<br>to retrieve the next set of query results. The cursor is only present if the request succeeded and<br>additional results are available.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Example (as JSON)

```json
{
  "segments": [
    {
      "created_at": "2020-01-09T19:33:24.469Z",
      "id": "GMNXRZVEXNQDF.CHURN_RISK",
      "name": "Lapsed",
      "updated_at": "2020-04-13T21:47:04Z"
    },
    {
      "created_at": "2020-01-09T19:33:24.486Z",
      "id": "GMNXRZVEXNQDF.LOYAL",
      "name": "Regulars",
      "updated_at": "2020-04-13T21:47:04Z"
    },
    {
      "created_at": "2020-01-09T19:33:21.813Z",
      "id": "GMNXRZVEXNQDF.REACHABLE",
      "name": "Reachable",
      "updated_at": "2020-04-13T21:47:04Z"
    },
    {
      "created_at": "2020-01-09T19:33:25Z",
      "id": "gv2:KF92J19VXN5FK30GX2E8HSGQ20",
      "name": "Instant Profile",
      "updated_at": "2020-04-13T23:01:03Z"
    }
  ],
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ],
  "cursor": "cursor2"
}
```

