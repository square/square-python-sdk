# Refunds

```python
refunds_api = client.refunds
```

## Class Name

`RefundsApi`

## Methods

* [List Payment Refunds](../../doc/api/refunds.md#list-payment-refunds)
* [Refund Payment](../../doc/api/refunds.md#refund-payment)
* [Get Payment Refund](../../doc/api/refunds.md#get-payment-refund)


# List Payment Refunds

Retrieves a list of refunds for the account making the request.

Results are eventually consistent, and new refunds or changes to refunds might take several
seconds to appear.

The maximum results per page is 100.

```python
def list_payment_refunds(self,
                        begin_time=None,
                        end_time=None,
                        sort_order=None,
                        cursor=None,
                        location_id=None,
                        status=None,
                        source_type=None,
                        limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `begin_time` | `str` | Query, Optional | Indicates the start of the time range to retrieve each `PaymentRefund` for, in RFC 3339<br>format.  The range is determined using the `created_at` field for each `PaymentRefund`.<br><br>Default: The current time minus one year. |
| `end_time` | `str` | Query, Optional | Indicates the end of the time range to retrieve each `PaymentRefund` for, in RFC 3339<br>format.  The range is determined using the `created_at` field for each `PaymentRefund`.<br><br>Default: The current time. |
| `sort_order` | `str` | Query, Optional | The order in which results are listed by `PaymentRefund.created_at`:<br><br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default). |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `location_id` | `str` | Query, Optional | Limit results to the location supplied. By default, results are returned<br>for all locations associated with the seller. |
| `status` | `str` | Query, Optional | If provided, only refunds with the given status are returned.<br>For a list of refund status values, see [PaymentRefund](entity:PaymentRefund).<br><br>Default: If omitted, refunds are returned regardless of their status. |
| `source_type` | `str` | Query, Optional | If provided, only returns refunds whose payments have the indicated source type.<br>Current values include `CARD`, `BANK_ACCOUNT`, `WALLET`, `CASH`, and `EXTERNAL`.<br>For information about these payment source types, see<br>[Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).<br><br>Default: If omitted, refunds are returned regardless of the source type. |
| `limit` | `int` | Query, Optional | The maximum number of results to be returned in a single page.<br><br>It is possible to receive fewer results than the specified limit on a given page.<br><br>If the supplied value is greater than 100, no more than 100 results are returned.<br><br>Default: 100 |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Payment Refunds Response`](../../doc/models/list-payment-refunds-response.md).

## Example Usage

```python
result = refunds_api.list_payment_refunds()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Refund Payment

Refunds a payment. You can refund the entire payment amount or a
portion of it. You can use this endpoint to refund a card payment or record a
refund of a cash or external payment. For more information, see
[Refund Payment](https://developer.squareup.com/docs/payments-api/refund-payments).

```python
def refund_payment(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Refund Payment Request`](../../doc/models/refund-payment-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Refund Payment Response`](../../doc/models/refund-payment-response.md).

## Example Usage

```python
body = {
    'idempotency_key': '9b7f2dcf-49da-4411-b23e-a2d6af21333a',
    'amount_money': {
        'amount': 1000,
        'currency': 'USD'
    },
    'app_fee_money': {
        'amount': 10,
        'currency': 'USD'
    },
    'payment_id': 'R2B3Z8WMVt3EAmzYWLZvz7Y69EbZY',
    'reason': 'Example'
}

result = refunds_api.refund_payment(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Payment Refund

Retrieves a specific refund using the `refund_id`.

```python
def get_payment_refund(self,
                      refund_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `refund_id` | `str` | Template, Required | The unique ID for the desired `PaymentRefund`. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Get Payment Refund Response`](../../doc/models/get-payment-refund-response.md).

## Example Usage

```python
refund_id = 'refund_id4'

result = refunds_api.get_payment_refund(refund_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

