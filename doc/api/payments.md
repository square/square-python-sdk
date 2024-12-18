# Payments

```python
payments_api = client.payments
```

## Class Name

`PaymentsApi`

## Methods

* [List Payments](../../doc/api/payments.md#list-payments)
* [Create Payment](../../doc/api/payments.md#create-payment)
* [Cancel Payment by Idempotency Key](../../doc/api/payments.md#cancel-payment-by-idempotency-key)
* [Get Payment](../../doc/api/payments.md#get-payment)
* [Update Payment](../../doc/api/payments.md#update-payment)
* [Cancel Payment](../../doc/api/payments.md#cancel-payment)
* [Complete Payment](../../doc/api/payments.md#complete-payment)


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
                 limit=None,
                 is_offline_payment=False,
                 offline_begin_time=None,
                 offline_end_time=None,
                 updated_at_begin_time=None,
                 updated_at_end_time=None,
                 sort_field=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `begin_time` | `str` | Query, Optional | Indicates the start of the time range to retrieve payments for, in RFC 3339 format.  <br>The range is determined using the `created_at` field for each Payment.<br>Inclusive. Default: The current time minus one year. |
| `end_time` | `str` | Query, Optional | Indicates the end of the time range to retrieve payments for, in RFC 3339 format.  The<br>range is determined using the `created_at` field for each Payment.<br><br>Default: The current time. |
| `sort_order` | `str` | Query, Optional | The order in which results are listed by `ListPaymentsRequest.sort_field`:<br><br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default). |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `location_id` | `str` | Query, Optional | Limit results to the location supplied. By default, results are returned<br>for the default (main) location associated with the seller. |
| `total` | `long\|int` | Query, Optional | The exact amount in the `total_money` for a payment. |
| `last_4` | `str` | Query, Optional | The last four digits of a payment card. |
| `card_brand` | `str` | Query, Optional | The brand of the payment card (for example, VISA). |
| `limit` | `int` | Query, Optional | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br><br>The default value of 100 is also the maximum allowed value. If the provided value is<br>greater than 100, it is ignored and the default value is used instead.<br><br>Default: `100` |
| `is_offline_payment` | `bool` | Query, Optional | Whether the payment was taken offline or not.<br>**Default**: `False` |
| `offline_begin_time` | `str` | Query, Optional | Indicates the start of the time range for which to retrieve offline payments, in RFC 3339<br>format for timestamps. The range is determined using the<br>`offline_payment_details.client_created_at` field for each Payment. If set, payments without a<br>value set in `offline_payment_details.client_created_at` will not be returned.<br><br>Default: The current time. |
| `offline_end_time` | `str` | Query, Optional | Indicates the end of the time range for which to retrieve offline payments, in RFC 3339<br>format for timestamps. The range is determined using the<br>`offline_payment_details.client_created_at` field for each Payment. If set, payments without a<br>value set in `offline_payment_details.client_created_at` will not be returned.<br><br>Default: The current time. |
| `updated_at_begin_time` | `str` | Query, Optional | Indicates the start of the time range to retrieve payments for, in RFC 3339 format.  The<br>range is determined using the `updated_at` field for each Payment. |
| `updated_at_end_time` | `str` | Query, Optional | Indicates the end of the time range to retrieve payments for, in RFC 3339 format.  The<br>range is determined using the `updated_at` field for each Payment. |
| `sort_field` | [`str (Payment Sort Field)`](../../doc/models/payment-sort-field.md) | Query, Optional | The field used to sort results by. The default is `CREATED_AT`. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Payments Response`](../../doc/models/list-payments-response.md).

## Example Usage

```python
is_offline_payment = False

result = payments_api.list_payments(
    is_offline_payment=is_offline_payment
)

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
| `body` | [`Create Payment Request`](../../doc/models/create-payment-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Payment Response`](../../doc/models/create-payment-response.md).

## Example Usage

```python
body = {
    'source_id': 'ccof:GaJGNaZa8x4OgDJn4GB',
    'idempotency_key': '7b0f3ec5-086a-4871-8f13-3c81b3875218',
    'amount_money': {
        'amount': 1000,
        'currency': 'USD'
    },
    'app_fee_money': {
        'amount': 10,
        'currency': 'USD'
    },
    'autocomplete': True,
    'customer_id': 'W92WH6P11H4Z77CTET0RNTGFW8',
    'location_id': 'L88917AVBK2S5',
    'reference_id': '123456',
    'note': 'Brief description'
}

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
| `body` | [`Cancel Payment by Idempotency Key Request`](../../doc/models/cancel-payment-by-idempotency-key-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Cancel Payment by Idempotency Key Response`](../../doc/models/cancel-payment-by-idempotency-key-response.md).

## Example Usage

```python
body = {
    'idempotency_key': 'a7e36d40-d24b-11e8-b568-0800200c9a66'
}

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
| `payment_id` | `str` | Template, Required | A unique ID for the desired payment. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Get Payment Response`](../../doc/models/get-payment-response.md).

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
| `payment_id` | `str` | Template, Required | The ID of the payment to update. |
| `body` | [`Update Payment Request`](../../doc/models/update-payment-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Payment Response`](../../doc/models/update-payment-response.md).

## Example Usage

```python
payment_id = 'payment_id0'

body = {
    'idempotency_key': '956f8b13-e4ec-45d6-85e8-d1d95ef0c5de',
    'payment': {
        'amount_money': {
            'amount': 1000,
            'currency': 'USD'
        },
        'tip_money': {
            'amount': 100,
            'currency': 'USD'
        },
        'version_token': 'ODhwVQ35xwlzRuoZEwKXucfu7583sPTzK48c5zoGd0g6o'
    }
}

result = payments_api.update_payment(
    payment_id,
    body
)

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
| `payment_id` | `str` | Template, Required | The ID of the payment to cancel. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Cancel Payment Response`](../../doc/models/cancel-payment-response.md).

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
                    payment_id,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `str` | Template, Required | The unique ID identifying the payment to be completed. |
| `body` | [`Complete Payment Request`](../../doc/models/complete-payment-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Complete Payment Response`](../../doc/models/complete-payment-response.md).

## Example Usage

```python
payment_id = 'payment_id0'

body = {}

result = payments_api.complete_payment(
    payment_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

