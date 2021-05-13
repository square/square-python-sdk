# Payments

```python
payments_api = client.payments
```

## Class Name

`PaymentsApi`

## Methods

* [List Payments](/doc/api/payments.md#list-payments)
* [Create Payment](/doc/api/payments.md#create-payment)
* [Cancel Payment by Idempotency Key](/doc/api/payments.md#cancel-payment-by-idempotency-key)
* [Get Payment](/doc/api/payments.md#get-payment)
* [Update Payment](/doc/api/payments.md#update-payment)
* [Cancel Payment](/doc/api/payments.md#cancel-payment)
* [Complete Payment](/doc/api/payments.md#complete-payment)


# List Payments

Retrieves a list of payments taken by the account making the request.

Results are eventually consistent, and new payments or changes to payments might take several
seconds to appear.

The maximum results per page is 100.

```python
def list_payments(self,
                 begin_time=None,
                 end_time=None,
                 sort_order=None,
                 cursor=None,
                 location_id=None,
                 total=None,
                 last_4=None,
                 card_brand=None,
                 limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `begin_time` | `string` | Query, Optional | The timestamp for the beginning of the reporting period, in RFC 3339 format.<br>Inclusive. Default: The current time minus one year. |
| `end_time` | `string` | Query, Optional | The timestamp for the end of the reporting period, in RFC 3339 format.<br><br>Default: The current time. |
| `sort_order` | `string` | Query, Optional | The order in which results are listed:<br><br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default). |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |
| `location_id` | `string` | Query, Optional | Limit results to the location supplied. By default, results are returned<br>for the default (main) location associated with the seller. |
| `total` | `long\|int` | Query, Optional | The exact amount in the `total_money` for a payment. |
| `last_4` | `string` | Query, Optional | The last four digits of a payment card. |
| `card_brand` | `string` | Query, Optional | The brand of the payment card (for example, VISA). |
| `limit` | `int` | Query, Optional | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br><br>The default value of 100 is also the maximum allowed value. If the provided value is<br>greater than 100, it is ignored and the default value is used instead.<br><br>Default: `100` |

## Response Type

[`List Payments Response`](/doc/models/list-payments-response.md)

## Example Usage

```python
begin_time = 'begin_time2'
end_time = 'end_time2'
sort_order = 'sort_order0'
cursor = 'cursor6'
location_id = 'location_id4'
total = 10
last_4 = 'last_42'
card_brand = 'card_brand6'
limit = 172

result = payments_api.list_payments(begin_time, end_time, sort_order, cursor, location_id, total, last_4, card_brand, limit)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Payment

Creates a payment using the provided source. You can use this endpoint
to charge a card (credit/debit card or  
Square gift card) or record a payment that the seller received outside of Square
(cash payment from a buyer or a payment that an external entity
processed on behalf of the seller).

The endpoint creates a
`Payment` object and returns it in the response.

```python
def create_payment(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Payment Request`](/doc/models/create-payment-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Payment Response`](/doc/models/create-payment-response.md)

## Example Usage

```python
body = {}
body['source_id'] = 'ccof:uIbfJXhXETSP197M3GB'
body['idempotency_key'] = '4935a656-a929-4792-b97c-8848be85c27c'
body['amount_money'] = {}
body['amount_money']['amount'] = 200
body['amount_money']['currency'] = 'USD'
body['tip_money'] = {}
body['tip_money']['amount'] = 198
body['tip_money']['currency'] = 'CHF'
body['app_fee_money'] = {}
body['app_fee_money']['amount'] = 10
body['app_fee_money']['currency'] = 'USD'
body['delay_duration'] = 'delay_duration6'
body['autocomplete'] = True
body['order_id'] = 'order_id0'
body['customer_id'] = 'VDKXEEKPJN48QDG3BGGFAK05P8'
body['location_id'] = 'XK3DBG77NJBFX'
body['reference_id'] = '123456'
body['note'] = 'Brief description'

result = payments_api.create_payment(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Cancel Payment by Idempotency Key

Cancels (voids) a payment identified by the idempotency key that is specified in the
request.

Use this method when the status of a `CreatePayment` request is unknown (for example, after you send a
`CreatePayment` request, a network error occurs and you do not get a response). In this case, you can
direct Square to cancel the payment using this endpoint. In the request, you provide the same
idempotency key that you provided in your `CreatePayment` request that you want to cancel. After
canceling the payment, you can submit your `CreatePayment` request again.

Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint
returns successfully.

```python
def cancel_payment_by_idempotency_key(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Cancel Payment by Idempotency Key Request`](/doc/models/cancel-payment-by-idempotency-key-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Cancel Payment by Idempotency Key Response`](/doc/models/cancel-payment-by-idempotency-key-response.md)

## Example Usage

```python
body = {}
body['idempotency_key'] = 'a7e36d40-d24b-11e8-b568-0800200c9a66'

result = payments_api.cancel_payment_by_idempotency_key(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Payment

Retrieves details for a specific payment.

```python
def get_payment(self,
               payment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `string` | Template, Required | A unique ID for the desired payment. |

## Response Type

[`Get Payment Response`](/doc/models/get-payment-response.md)

## Example Usage

```python
payment_id = 'payment_id0'

result = payments_api.get_payment(payment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Payment

Updates a payment with the APPROVED status.
You can update the `amount_money` and `tip_money` using this endpoint.

```python
def update_payment(self,
                  payment_id,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `string` | Template, Required | The ID of the payment to update. |
| `body` | [`Update Payment Request`](/doc/models/update-payment-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Update Payment Response`](/doc/models/update-payment-response.md)

## Example Usage

```python
payment_id = 'payment_id0'
body = {}
body['payment'] = {}
body['payment']['id'] = 'id2'
body['payment']['created_at'] = 'created_at0'
body['payment']['updated_at'] = 'updated_at8'
body['payment']['amount_money'] = {}
body['payment']['amount_money']['amount'] = 1000
body['payment']['amount_money']['currency'] = 'USD'
body['payment']['tip_money'] = {}
body['payment']['tip_money']['amount'] = 300
body['payment']['tip_money']['currency'] = 'USD'
body['payment']['version_token'] = 'Z3okDzm2VRv5m5nE3WGx381ItTNhvjkB4VapByyz54h6o'
body['idempotency_key'] = '3d3c3b22-9572-4fc6-1111-e4d2f41b4122'

result = payments_api.update_payment(payment_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Cancel Payment

Cancels (voids) a payment. You can use this endpoint to cancel a payment with
the APPROVED `status`.

```python
def cancel_payment(self,
                  payment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `string` | Template, Required | The ID of the payment to cancel. |

## Response Type

[`Cancel Payment Response`](/doc/models/cancel-payment-response.md)

## Example Usage

```python
payment_id = 'payment_id0'

result = payments_api.cancel_payment(payment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Complete Payment

Completes (captures) a payment.
By default, payments are set to complete immediately after they are created.

You can use this endpoint to complete a payment with the APPROVED `status`.

```python
def complete_payment(self,
                    payment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `string` | Template, Required | The unique ID identifying the payment to be completed. |

## Response Type

[`Complete Payment Response`](/doc/models/complete-payment-response.md)

## Example Usage

```python
payment_id = 'payment_id0'

result = payments_api.complete_payment(payment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

