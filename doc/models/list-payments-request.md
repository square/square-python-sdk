
# List Payments Request

Retrieves a list of payments taken by the account making the request.

The maximum results per page is 100.

## Structure

`List Payments Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `begin_time` | `string` | Optional | The timestamp for the beginning of the reporting period, in RFC 3339 format.<br>Inclusive. Default: The current time minus one year. |
| `end_time` | `string` | Optional | The timestamp for the end of the reporting period, in RFC 3339 format.<br><br>Default: The current time. |
| `sort_order` | `string` | Optional | The order in which results are listed:<br><br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default). |
| `cursor` | `string` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |
| `location_id` | `string` | Optional | Limit results to the location supplied. By default, results are returned<br>for the default (main) location associated with the seller. |
| `total` | `long|int` | Optional | The exact amount in the `total_money` for a payment. |
| `last_4` | `string` | Optional | The last four digits of a payment card. |
| `card_brand` | `string` | Optional | The brand of the payment card (for example, VISA). |
| `limit` | `int` | Optional | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br><br>The default value of 100 is also the maximum allowed value. If the provided value is<br>greater than 100, it is ignored and the default value is used instead.<br><br>Default: `100` |

## Example (as JSON)

```json
{}
```

