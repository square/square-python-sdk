# Transactions

```python
transactions_api = client.transactions
```

## Class Name

`TransactionsApi`

## Methods

* [List Refunds](/doc/transactions.md#list-refunds)
* [List Transactions](/doc/transactions.md#list-transactions)
* [Charge](/doc/transactions.md#charge)
* [Retrieve Transaction](/doc/transactions.md#retrieve-transaction)
* [Capture Transaction](/doc/transactions.md#capture-transaction)
* [Create Refund](/doc/transactions.md#create-refund)
* [Void Transaction](/doc/transactions.md#void-transaction)

## List Refunds

Lists refunds for one of a business's locations.

In addition to full or partial tender refunds processed through Square APIs,
refunds may result from itemized returns or exchanges through Square's
Point of Sale applications.

Refunds with a `status` of `PENDING` are not currently included in this
endpoint's response.

Max results per [page](#paginatingresults): 50

```python
def list_refunds(self,
                location_id,
                begin_time=None,
                end_time=None,
                sort_order=None,
                cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the location to list refunds for. |
| `begin_time` | `string` | Query, Optional | The beginning of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.<br><br>Default value: The current time minus one year. |
| `end_time` | `string` | Query, Optional | The end of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.<br><br>Default value: The current time. |
| `sort_order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Query, Optional | The order in which results are listed in the response (`ASC` for<br>oldest first, `DESC` for newest first).<br><br>Default value: `DESC` |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Paginating results](#paginatingresults) for more information. |

### Response Type

[`List Refunds Response`](/doc/models/list-refunds-response.md)

### Example Usage

```python
location_id = 'location_id4'
begin_time = 'begin_time2'
end_time = 'end_time2'
sort_order = 'DESC'
cursor = 'cursor6'

result = transactions_api.list_refunds(location_id, begin_time, end_time, sort_order, cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Transactions

Lists transactions for a particular location.

Transactions include payment information from sales and exchanges and refund
information from returns and exchanges.

Max results per [page](#paginatingresults): 50

```python
def list_transactions(self,
                     location_id,
                     begin_time=None,
                     end_time=None,
                     sort_order=None,
                     cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the location to list transactions for. |
| `begin_time` | `string` | Query, Optional | The beginning of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.<br><br>Default value: The current time minus one year. |
| `end_time` | `string` | Query, Optional | The end of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](#dateranges) for details on date inclusivity/exclusivity.<br><br>Default value: The current time. |
| `sort_order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Query, Optional | The order in which results are listed in the response (`ASC` for<br>oldest first, `DESC` for newest first).<br><br>Default value: `DESC` |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Paginating results](#paginatingresults) for more information. |

### Response Type

[`List Transactions Response`](/doc/models/list-transactions-response.md)

### Example Usage

```python
location_id = 'location_id4'
begin_time = 'begin_time2'
end_time = 'end_time2'
sort_order = 'DESC'
cursor = 'cursor6'

result = transactions_api.list_transactions(location_id, begin_time, end_time, sort_order, cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Charge

Charges a card represented by a card nonce or a customer's card on file.

Your request to this endpoint must include _either_:

- A value for the `card_nonce` parameter (to charge a card nonce generated
with the `SqPaymentForm`)
- Values for the `customer_card_id` and `customer_id` parameters (to charge
a customer's card on file)

In order for an eCommerce payment to potentially qualify for
[Square chargeback protection](https://squareup.com/help/article/5394), you
_must_ provide values for the following parameters in your request:

- `buyer_email_address`
- At least one of `billing_address` or `shipping_address`

When this response is returned, the amount of Square's processing fee might not yet be
calculated. To obtain the processing fee, wait about ten seconds and call
[RetrieveTransaction](#endpoint-retrievetransaction). See the `processing_fee_money`
field of each [Tender included](#type-tender) in the transaction.

```python
def charge(self,
          location_id,
          body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the location to associate the created transaction with. |
| `body` | [`Charge Request`](/doc/models/charge-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Charge Response`](/doc/models/charge-response.md)

### Example Usage

```python
location_id = 'location_id4'
body = {}
body['idempotency_key'] = '74ae1696-b1e3-4328-af6d-f1e04d947a13'
body['amount_money'] = {}
body['amount_money']['amount'] = 200
body['amount_money']['currency'] = 'USD'
body['card_nonce'] = 'card_nonce_from_square_123'
body['customer_card_id'] = 'customer_card_id6'
body['delay_capture'] = False
body['reference_id'] = 'some optional reference id'
body['note'] = 'some optional note'
body['billing_address'] = {}
body['billing_address']['address_line_1'] = '500 Electric Ave'
body['billing_address']['address_line_2'] = 'Suite 600'
body['billing_address']['address_line_3'] = 'address_line_38'
body['billing_address']['locality'] = 'New York'
body['billing_address']['sublocality'] = 'sublocality2'
body['billing_address']['administrative_district_level_1'] = 'NY'
body['billing_address']['postal_code'] = '10003'
body['billing_address']['country'] = 'US'
body['shipping_address'] = {}
body['shipping_address']['address_line_1'] = '123 Main St'
body['shipping_address']['address_line_2'] = 'address_line_24'
body['shipping_address']['address_line_3'] = 'address_line_30'
body['shipping_address']['locality'] = 'San Francisco'
body['shipping_address']['sublocality'] = 'sublocality4'
body['shipping_address']['administrative_district_level_1'] = 'CA'
body['shipping_address']['postal_code'] = '94114'
body['shipping_address']['country'] = 'US'
body['additional_recipients'] = []

body['additional_recipients'].append({})
body['additional_recipients'][0]['location_id'] = '057P5VYJ4A5X1'
body['additional_recipients'][0]['description'] = 'Application fees'
body['additional_recipients'][0]['amount_money'] = {}
body['additional_recipients'][0]['amount_money']['amount'] = 20
body['additional_recipients'][0]['amount_money']['currency'] = 'USD'
body['additional_recipients'][0]['receivable_id'] = 'receivable_id5'


result = transactions_api.charge(location_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Transaction

Retrieves details for a single transaction.

```python
def retrieve_transaction(self,
                        location_id,
                        transaction_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the transaction's associated location. |
| `transaction_id` | `string` | Template, Required | The ID of the transaction to retrieve. |

### Response Type

[`Retrieve Transaction Response`](/doc/models/retrieve-transaction-response.md)

### Example Usage

```python
location_id = 'location_id4'
transaction_id = 'transaction_id8'

result = transactions_api.retrieve_transaction(location_id, transaction_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Capture Transaction

Captures a transaction that was created with the [Charge](#endpoint-charge)
endpoint with a `delay_capture` value of `true`.


See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.

```python
def capture_transaction(self,
                       location_id,
                       transaction_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | - |
| `transaction_id` | `string` | Template, Required | - |

### Response Type

[`Capture Transaction Response`](/doc/models/capture-transaction-response.md)

### Example Usage

```python
location_id = 'location_id4'
transaction_id = 'transaction_id8'

result = transactions_api.capture_transaction(location_id, transaction_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Refund

Initiates a refund for a previously charged tender.

You must issue a refund within 120 days of the associated payment. See
[this article](https://squareup.com/help/us/en/article/5060) for more information
on refund behavior.

NOTE: Card-present transactions with Interac credit cards **cannot be
refunded using the Connect API**. Interac transactions must refunded
in-person (e.g., dipping the card using POS app).

```python
def create_refund(self,
                 location_id,
                 transaction_id,
                 body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the original transaction's associated location. |
| `transaction_id` | `string` | Template, Required | The ID of the original transaction that includes the tender to refund. |
| `body` | [`Create Refund Request`](/doc/models/create-refund-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Refund Response`](/doc/models/create-refund-response.md)

### Example Usage

```python
location_id = 'location_id4'
transaction_id = 'transaction_id8'
body = {}
body['idempotency_key'] = '86ae1696-b1e3-4328-af6d-f1e04d947ad2'
body['tender_id'] = 'MtZRYYdDrYNQbOvV7nbuBvMF'
body['reason'] = 'a reason'
body['amount_money'] = {}
body['amount_money']['amount'] = 100
body['amount_money']['currency'] = 'USD'

result = transactions_api.create_refund(location_id, transaction_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Void Transaction

Cancels a transaction that was created with the [Charge](#endpoint-charge)
endpoint with a `delay_capture` value of `true`.


See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.

```python
def void_transaction(self,
                    location_id,
                    transaction_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | - |
| `transaction_id` | `string` | Template, Required | - |

### Response Type

[`Void Transaction Response`](/doc/models/void-transaction-response.md)

### Example Usage

```python
location_id = 'location_id4'
transaction_id = 'transaction_id8'

result = transactions_api.void_transaction(location_id, transaction_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

