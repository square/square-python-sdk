# Orders

```python
orders_api = client.orders
```

## Class Name

`OrdersApi`

## Methods

* [Create Order](/doc/orders.md#create-order)
* [Batch Retrieve Orders](/doc/orders.md#batch-retrieve-orders)
* [Update Order](/doc/orders.md#update-order)
* [Calculate Order](/doc/orders.md#calculate-order)
* [Search Orders](/doc/orders.md#search-orders)
* [Pay Order](/doc/orders.md#pay-order)

## Create Order

Creates a new [Order](#type-order) which can include information on products for
purchase and settings to apply to the purchase.

To pay for a created order, please refer to the [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders)
guide.

You can modify open orders using the [UpdateOrder](#endpoint-orders-updateorder) endpoint.

To learn more about the Orders API, see the
[Orders API Overview](https://developer.squareup.com/docs/orders-api/what-it-does).

```python
def create_order(self,
                location_id,
                body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the business location to associate the order with. |
| `body` | [`Create Order Request`](/doc/models/create-order-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Order Response`](/doc/models/create-order-response.md)

### Example Usage

```python
location_id = 'location_id4'
body = {}

result = orders_api.create_order(location_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Batch Retrieve Orders

Retrieves a set of [Order](#type-order)s by their IDs.

If a given Order ID does not exist, the ID is ignored instead of generating an error.

```python
def batch_retrieve_orders(self,
                         location_id,
                         body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the orders' associated location. |
| `body` | [`Batch Retrieve Orders Request`](/doc/models/batch-retrieve-orders-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Retrieve Orders Response`](/doc/models/batch-retrieve-orders-response.md)

### Example Usage

```python
location_id = 'location_id4'
body = {}
body['order_ids'] = ['CAISEM82RcpmcFBM0TfOyiHV3es', 'CAISENgvlJ6jLWAzERDzjyHVybY']

result = orders_api.batch_retrieve_orders(location_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Order

Updates an open [Order](#type-order) by adding, replacing, or deleting
fields. Orders with a `COMPLETED` or `CANCELED` state cannot be updated.

An UpdateOrder request requires the following:

- The `order_id` in the endpoint path, identifying the order to update.
- The latest `version` of the order to update.
- The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders#sparse-order-objects)
containing only the fields to update and the version the update is
being applied to.
- If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation)
identifying fields to clear.

To pay for an order, please refer to the [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders) guide.

To learn more about the Orders API, see the
[Orders API Overview](https://developer.squareup.com/docs/orders-api/what-it-does).

```python
def update_order(self,
                location_id,
                order_id,
                body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the order's associated location. |
| `order_id` | `string` | Template, Required | The ID of the order to update. |
| `body` | [`Update Order Request`](/doc/models/update-order-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Order Response`](/doc/models/update-order-response.md)

### Example Usage

```python
location_id = 'location_id4'
order_id = 'order_id6'
body = {}

result = orders_api.update_order(location_id, order_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Calculate Order

Calculates an [Order](#type-order).

```python
def calculate_order(self,
                   body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Calculate Order Request`](/doc/models/calculate-order-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Calculate Order Response`](/doc/models/calculate-order-response.md)

### Example Usage

```python
body = {}
body['order'] = {}
body['order']['location_id'] = 'D7AVYMEAPJ3A3'
body['order']['line_items'] = []

body['order']['line_items'].append({})
body['order']['line_items'][0]['name'] = 'Item 1'
body['order']['line_items'][0]['quantity'] = '1'
body['order']['line_items'][0]['base_price_money'] = {}
body['order']['line_items'][0]['base_price_money']['amount'] = 500
body['order']['line_items'][0]['base_price_money']['currency'] = 'USD'

body['order']['line_items'].append({})
body['order']['line_items'][1]['name'] = 'Item 2'
body['order']['line_items'][1]['quantity'] = '2'
body['order']['line_items'][1]['base_price_money'] = {}
body['order']['line_items'][1]['base_price_money']['amount'] = 300
body['order']['line_items'][1]['base_price_money']['currency'] = 'USD'

body['order']['discounts'] = []

body['order']['discounts'].append({})
body['order']['discounts'][0]['name'] = '50% Off'
body['order']['discounts'][0]['percentage'] = '50'
body['order']['discounts'][0]['scope'] = 'ORDER'


result = orders_api.calculate_order(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Orders

Search all orders for one or more locations. Orders include all sales,
returns, and exchanges regardless of how or when they entered the Square
Ecosystem (e.g. Point of Sale, Invoices, Connect APIs, etc).

SearchOrders requests need to specify which locations to search and define a
[`SearchOrdersQuery`](#type-searchordersquery) object which controls
how to sort or filter the results. Your SearchOrdersQuery can:

  Set filter criteria.
  Set sort order.
  Determine whether to return results as complete Order objects, or as
[OrderEntry](#type-orderentry) objects.

Note that details for orders processed with Square Point of Sale while in
offline mode may not be transmitted to Square for up to 72 hours. Offline
orders have a `created_at` value that reflects the time the order was created,
not the time it was subsequently transmitted to Square.

```python
def search_orders(self,
                 body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Orders Request`](/doc/models/search-orders-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Orders Response`](/doc/models/search-orders-response.md)

### Example Usage

```python
body = {}
body['location_ids'] = ['057P5VYJ4A5X1', '18YC4JDH91E1H']
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['state_filter'] = {}
body['query']['filter']['state_filter']['states'] = ['COMPLETED']
body['query']['filter']['date_time_filter'] = {}
body['query']['filter']['date_time_filter']['closed_at'] = {}
body['query']['filter']['date_time_filter']['closed_at']['start_at'] = '2018-03-03T20:00:00+00:00'
body['query']['filter']['date_time_filter']['closed_at']['end_at'] = '2019-03-04T21:54:45+00:00'
body['query']['sort'] = {}
body['query']['sort']['sort_field'] = 'CLOSED_AT'
body['query']['sort']['sort_order'] = 'DESC'
body['limit'] = 3
body['return_entries'] = True

result = orders_api.search_orders(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Pay Order

Pay for an [order](#type-order) using one or more approved [payments](#type-payment),
or settle an order with a total of `0`.

The total of the `payment_ids` listed in the request must be equal to the order
total. Orders with a total amount of `0` can be marked as paid by specifying an empty
array of `payment_ids` in the request.

To be used with PayOrder, a payment must:

- Reference the order by specifying the `order_id` when [creating the payment](#endpoint-payments-createpayment).
Any approved payments that reference the same `order_id` not specified in the
`payment_ids` will be canceled.
- Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments#delayed-capture).
Using a delayed capture payment with PayOrder will complete the approved payment.

Learn how to [pay for orders with a single payment using the Payments API](https://developer.squareup.com/docs/orders-api/pay-for-orders).

```python
def pay_order(self,
             order_id,
             body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Template, Required | The ID of the order being paid. |
| `body` | [`Pay Order Request`](/doc/models/pay-order-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Pay Order Response`](/doc/models/pay-order-response.md)

### Example Usage

```python
order_id = 'order_id6'
body = {}
body['idempotency_key'] = 'c043a359-7ad9-4136-82a9-c3f1d66dcbff'
body['payment_ids'] = ['EnZdNAlWCmfh6Mt5FMNST1o7taB', '0LRiVlbXVwe8ozu4KbZxd12mvaB']

result = orders_api.pay_order(order_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

