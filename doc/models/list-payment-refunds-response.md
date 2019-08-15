## List Payment Refunds Response

Defines the fields that are included in the response body of
a request to the [ListPaymentRefunds](/doc/refunds.md#listpaymentrefunds) endpoint.

One of `errors` or `refunds` is present in a given response (never both).

### Structure

`ListPaymentRefundsResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `refunds` | [`List of Payment Refund`](/doc/models/payment-refund.md) | Optional | The list of requested refunds. |
| `cursor` | `string` | Optional | The pagination cursor to be used in a subsequent request. If empty,<br>this is the final response.<br><br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |

### Example (as JSON)

```json
{
  "errors": null,
  "refunds": null,
  "cursor": null
}
```

