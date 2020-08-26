# Payments

```python
payments_api = client.payments
```

## Class Name

`PaymentsApi`

## Methods

* [List Payments](/doc/payments.md#list-payments)
* [Create Payment](/doc/payments.md#create-payment)
* [Cancel Payment by Idempotency Key](/doc/payments.md#cancel-payment-by-idempotency-key)
* [Get Payment](/doc/payments.md#get-payment)
* [Cancel Payment](/doc/payments.md#cancel-payment)
* [Complete Payment](/doc/payments.md#complete-payment)

## List Payments

Retrieves a list of payments taken by the account making the request.

Max results per page: 100

```python
def list_payments(self,
                 begin_time=None,
                 end_time=None,
                 sort_order=None,
                 cursor=None,
                 location_id=None,
                 total=None,
                 last_4=None,
                 card_brand=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `begin_time` | `string` | Query, Optional | Timestamp for the beginning of the reporting period, in RFC 3339 format.<br>Inclusive. Default: The current time minus one year. |
| `end_time` | `string` | Query, Optional | Timestamp for the end of the requested reporting period, in RFC 3339 format.<br><br>Default: The current time. |
| `sort_order` | `string` | Query, Optional | The order in which results are listed.<br>- `ASC` - oldest to newest<br>- `DESC` - newest to oldest (default). |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |
| `location_id` | `string` | Query, Optional | Limit results to the location supplied. By default, results are returned<br>for all locations associated with the merchant. |
| `total` | `long|int` | Query, Optional | The exact amount in the total_money for a `Payment`. |
| `last_4` | `string` | Query, Optional | The last 4 digits of `Payment` card. |
| `card_brand` | `string` | Query, Optional | The brand of `Payment` card. For example, `VISA` |

### Response Type

[`List Payments Response`](/doc/models/list-payments-response.md)

### Example Usage

```python
begin_time = 'begin_time2'
end_time = 'end_time2'
sort_order = 'sort_order0'
cursor = 'cursor6'
location_id = 'location_id4'
total = 10
last_4 = 'last_42'
card_brand = 'card_brand6'

result = payments_api.list_payments(begin_time, end_time, sort_order, cursor, location_id, total, last_4, card_brand)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Payment

Charges a payment source, for example, a card 
represented by customer's card on file or a card nonce. In addition 
to the payment source, the request must also include the 
amount to accept for the payment.

There are several optional parameters that you can include in the request. 
For example, tip money, whether to autocomplete the payment, or a reference ID
to correlate this payment with another system. 
For more information about these 
payment options, see [Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).

The `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission is required
to enable application fees.

```python
def create_payment(self,
                  body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Payment Request`](/doc/models/create-payment-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Payment Response`](/doc/models/create-payment-response.md)

### Example Usage

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

## Cancel Payment by Idempotency Key

Cancels (voids) a payment identified by the idempotency key that is specified in the
request.

Use this method when status of a CreatePayment request is unknown. For example, after you send a
CreatePayment request a network error occurs and you don't get a response. In this case, you can
direct Square to cancel the payment using this endpoint. In the request, you provide the same
idempotency key that you provided in your CreatePayment request you want  to cancel. After
cancelling the payment, you can submit your CreatePayment request again.

Note that if no payment with the specified idempotency key is found, no action is taken, the end
point returns successfully.

```python
def cancel_payment_by_idempotency_key(self,
                                     body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Cancel Payment by Idempotency Key Request`](/doc/models/cancel-payment-by-idempotency-key-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Cancel Payment by Idempotency Key Response`](/doc/models/cancel-payment-by-idempotency-key-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = 'a7e36d40-d24b-11e8-b568-0800200c9a66'

result = payments_api.cancel_payment_by_idempotency_key(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Payment

Retrieves details for a specific Payment.

```python
def get_payment(self,
               payment_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `string` | Template, Required | Unique ID for the desired `Payment`. |

### Response Type

[`Get Payment Response`](/doc/models/get-payment-response.md)

### Example Usage

```python
payment_id = 'payment_id0'

result = payments_api.get_payment(payment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Cancel Payment

Cancels (voids) a payment. If you set `autocomplete` to false when creating a payment, 
you can cancel the payment using this endpoint. For more information, see 
[Delayed Payments](https://developer.squareup.com/docs/payments-api/take-payments#delayed-payments).

```python
def cancel_payment(self,
                  payment_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `string` | Template, Required | `payment_id` identifying the payment to be canceled. |

### Response Type

[`Cancel Payment Response`](/doc/models/cancel-payment-response.md)

### Example Usage

```python
payment_id = 'payment_id0'

result = payments_api.cancel_payment(payment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Complete Payment

Completes (captures) a payment.

By default, payments are set to complete immediately after they are created. 
If you set autocomplete to false when creating a payment, you can complete (capture) 
the payment using this endpoint. For more information, see
[Delayed Payments](https://developer.squareup.com/docs/payments-api/take-payments#delayed-payments).

```python
def complete_payment(self,
                    payment_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `string` | Template, Required | Unique ID identifying the payment to be completed. |

### Response Type

[`Complete Payment Response`](/doc/models/complete-payment-response.md)

### Example Usage

```python
payment_id = 'payment_id0'

result = payments_api.complete_payment(payment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

