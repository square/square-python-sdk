# Refunds

```python
refunds_api = client.refunds
```

## Class Name

`RefundsApi`

## Methods

* [List Payment Refunds](/doc/api/refunds.md#list-payment-refunds)
* [Refund Payment](/doc/api/refunds.md#refund-payment)
* [Get Payment Refund](/doc/api/refunds.md#get-payment-refund)


# List Payment Refunds

Retrieves a list of refunds for the account making the request.

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
| `begin_time` | `string` | Query, Optional | The timestamp for the beginning of the requested reporting period, in RFC 3339 format.<br><br>Default: The current time minus one year. |
| `end_time` | `string` | Query, Optional | The timestamp for the end of the requested reporting period, in RFC 3339 format.<br><br>Default: The current time. |
| `sort_order` | `string` | Query, Optional | The order in which results are listed:<br><br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default). |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |
| `location_id` | `string` | Query, Optional | Limit results to the location supplied. By default, results are returned<br>for all locations associated with the seller. |
| `status` | `string` | Query, Optional | If provided, only refunds with the given status are returned.<br>For a list of refund status values, see [PaymentRefund](#type-paymentrefund).<br><br>Default: If omitted, refunds are returned regardless of their status. |
| `source_type` | `string` | Query, Optional | If provided, only refunds with the given source type are returned.<br><br>- `CARD` - List refunds only for payments where `CARD` was specified as the payment<br>  source.<br><br>Default: If omitted, refunds are returned regardless of the source type. |
| `limit` | `int` | Query, Optional | The maximum number of results to be returned in a single page.<br><br>It is possible to receive fewer results than the specified limit on a given page.<br><br>If the supplied value is greater than 100, no more than 100 results are returned.<br><br>Default: 100 |

## Response Type

[`List Payment Refunds Response`](/doc/models/list-payment-refunds-response.md)

## Example Usage

```python
begin_time = 'begin_time2'
end_time = 'end_time2'
sort_order = 'sort_order0'
cursor = 'cursor6'
location_id = 'location_id4'
status = 'status8'
source_type = 'source_type0'
limit = 172

result = refunds_api.list_payment_refunds(begin_time, end_time, sort_order, cursor, location_id, status, source_type, limit)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Refund Payment

Refunds a payment. You can refund the entire payment amount or a
portion of it.

```python
def refund_payment(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Refund Payment Request`](/doc/models/refund-payment-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Refund Payment Response`](/doc/models/refund-payment-response.md)

## Example Usage

```python
body = {}
body['idempotency_key'] = 'a7e36d40-d24b-11e8-b568-0800200c9a66'
body['amount_money'] = {}
body['amount_money']['amount'] = 100
body['amount_money']['currency'] = 'USD'
body['app_fee_money'] = {}
body['app_fee_money']['amount'] = 114
body['app_fee_money']['currency'] = 'GEL'
body['payment_id'] = 'UNOE3kv2BZwqHlJ830RCt5YCuaB'
body['reason'] = 'reason8'

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
| `refund_id` | `string` | Template, Required | The unique ID for the desired `PaymentRefund`. |

## Response Type

[`Get Payment Refund Response`](/doc/models/get-payment-refund-response.md)

## Example Usage

```python
refund_id = 'refund_id4'

result = refunds_api.get_payment_refund(refund_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

