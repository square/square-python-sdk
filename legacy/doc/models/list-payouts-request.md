
# List Payouts Request

A request to retrieve payout records.

## Structure

`List Payouts Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Optional | The ID of the location for which to list the payouts.<br>By default, payouts are returned for the default (main) location associated with the seller.<br>**Constraints**: *Maximum Length*: `255` |
| `status` | [`str (Payout Status)`](../../doc/models/payout-status.md) | Optional | Payout status types |
| `begin_time` | `str` | Optional | The timestamp for the beginning of the payout creation time, in RFC 3339 format.<br>Inclusive. Default: The current time minus one year. |
| `end_time` | `str` | Optional | The timestamp for the end of the payout creation time, in RFC 3339 format.<br>Default: The current time. |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |
| `cursor` | `str` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>If request parameters change between requests, subsequent results may contain duplicates or missing records. |
| `limit` | `int` | Optional | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br>The default value of 100 is also the maximum allowed value. If the provided value is<br>greater than 100, it is ignored and the default value is used instead.<br>Default: `100` |

## Example (as JSON)

```json
{
  "location_id": "location_id4",
  "status": "SENT",
  "begin_time": "begin_time2",
  "end_time": "end_time2",
  "sort_order": "DESC"
}
```

