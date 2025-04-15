
# List Payment Refunds Request

Describes a request to list refunds using
[ListPaymentRefunds](../../doc/api/refunds.md#list-payment-refunds).

The maximum results per page is 100.

## Structure

`List Payment Refunds Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `begin_time` | `str` | Optional | Indicates the start of the time range to retrieve each `PaymentRefund` for, in RFC 3339<br>format.  The range is determined using the `created_at` field for each `PaymentRefund`.<br><br>Default: The current time minus one year. |
| `end_time` | `str` | Optional | Indicates the end of the time range to retrieve each `PaymentRefund` for, in RFC 3339<br>format.  The range is determined using the `created_at` field for each `PaymentRefund`.<br><br>Default: The current time. |
| `sort_order` | `str` | Optional | The order in which results are listed by `PaymentRefund.created_at`:<br><br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default). |
| `cursor` | `str` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `location_id` | `str` | Optional | Limit results to the location supplied. By default, results are returned<br>for all locations associated with the seller. |
| `status` | `str` | Optional | If provided, only refunds with the given status are returned.<br>For a list of refund status values, see [PaymentRefund](entity:PaymentRefund).<br><br>Default: If omitted, refunds are returned regardless of their status. |
| `source_type` | `str` | Optional | If provided, only returns refunds whose payments have the indicated source type.<br>Current values include `CARD`, `BANK_ACCOUNT`, `WALLET`, `CASH`, and `EXTERNAL`.<br>For information about these payment source types, see<br>[Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).<br><br>Default: If omitted, refunds are returned regardless of the source type. |
| `limit` | `int` | Optional | The maximum number of results to be returned in a single page.<br><br>It is possible to receive fewer results than the specified limit on a given page.<br><br>If the supplied value is greater than 100, no more than 100 results are returned.<br><br>Default: 100 |

## Example (as JSON)

```json
{
  "begin_time": "begin_time8",
  "end_time": "end_time2",
  "sort_order": "sort_order0",
  "cursor": "cursor4",
  "location_id": "location_id4"
}
```

