# Transactions

```python
transactions_api = client.transactions
```

## Class Name

`TransactionsApi`

## Methods

* [List Transactions](../../doc/api/transactions.md#list-transactions)
* [Retrieve Transaction](../../doc/api/transactions.md#retrieve-transaction)
* [Capture Transaction](../../doc/api/transactions.md#capture-transaction)
* [Void Transaction](../../doc/api/transactions.md#void-transaction)


# List Transactions

**This endpoint is deprecated.**

Lists transactions for a particular location.

Transactions include payment information from sales and exchanges and refund
information from returns and exchanges.

Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

```python
def list_transactions(self,
                     location_id,
                     begin_time=None,
                     end_time=None,
                     sort_order=None,
                     cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Template, Required | The ID of the location to list transactions for. |
| `begin_time` | `str` | Query, Optional | The beginning of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.<br><br>Default value: The current time minus one year. |
| `end_time` | `str` | Query, Optional | The end of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.<br><br>Default value: The current time. |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Query, Optional | The order in which results are listed in the response (`ASC` for<br>oldest first, `DESC` for newest first).<br><br>Default value: `DESC` |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Transactions Response`](../../doc/models/list-transactions-response.md).

## Example Usage

```python
location_id = 'location_id4'

result = transactions_api.list_transactions(location_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Transaction

**This endpoint is deprecated.**

Retrieves details for a single transaction.

```python
def retrieve_transaction(self,
                        location_id,
                        transaction_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Template, Required | The ID of the transaction's associated location. |
| `transaction_id` | `str` | Template, Required | The ID of the transaction to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Transaction Response`](../../doc/models/retrieve-transaction-response.md).

## Example Usage

```python
location_id = 'location_id4'

transaction_id = 'transaction_id8'

result = transactions_api.retrieve_transaction(
    location_id,
    transaction_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Capture Transaction

**This endpoint is deprecated.**

Captures a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
endpoint with a `delay_capture` value of `true`.

See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.

```python
def capture_transaction(self,
                       location_id,
                       transaction_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Template, Required | - |
| `transaction_id` | `str` | Template, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Capture Transaction Response`](../../doc/models/capture-transaction-response.md).

## Example Usage

```python
location_id = 'location_id4'

transaction_id = 'transaction_id8'

result = transactions_api.capture_transaction(
    location_id,
    transaction_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Void Transaction

**This endpoint is deprecated.**

Cancels a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
endpoint with a `delay_capture` value of `true`.

See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.

```python
def void_transaction(self,
                    location_id,
                    transaction_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Template, Required | - |
| `transaction_id` | `str` | Template, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Void Transaction Response`](../../doc/models/void-transaction-response.md).

## Example Usage

```python
location_id = 'location_id4'

transaction_id = 'transaction_id8'

result = transactions_api.void_transaction(
    location_id,
    transaction_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

