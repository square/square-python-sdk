# Orders

```python
orders_api = client.orders
```

## Class Name

`OrdersApi`

## Methods

* [Create Order](../../doc/api/orders.md#create-order)
* [Batch Retrieve Orders](../../doc/api/orders.md#batch-retrieve-orders)
* [Calculate Order](../../doc/api/orders.md#calculate-order)
* [Clone Order](../../doc/api/orders.md#clone-order)
* [Search Orders](../../doc/api/orders.md#search-orders)
* [Retrieve Order](../../doc/api/orders.md#retrieve-order)
* [Update Order](../../doc/api/orders.md#update-order)
* [Pay Order](../../doc/api/orders.md#pay-order)


# Create Order

Creates a new [order](../../doc/models/order.md) that can include information about products for
purchase and settings to apply to the purchase.

To pay for a created order, see
[Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

You can modify open orders using the [UpdateOrder](../../doc/api/orders.md#update-order) endpoint.

```python
def create_order(self,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Order Request`](../../doc/models/create-order-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Order Response`](../../doc/models/create-order-response.md).

## Example Usage

```python
body = {
    'order': {
        'location_id': '057P5VYJ4A5X1',
        'reference_id': 'my-order-001',
        'line_items': [
            {
                'quantity': '1',
                'name': 'New York Strip Steak',
                'base_price_money': {
                    'amount': 1599,
                    'currency': 'USD'
                }
            },
            {
                'quantity': '2',
                'catalog_object_id': 'BEMYCSMIJL46OCDV4KYIKXIB',
                'modifiers': [
                    {
                        'catalog_object_id': 'CHQX7Y4KY6N5KINJKZCFURPZ'
                    }
                ],
                'applied_discounts': [
                    {
                        'discount_uid': 'one-dollar-off'
                    }
                ]
            }
        ],
        'taxes': [
            {
                'uid': 'state-sales-tax',
                'name': 'State Sales Tax',
                'percentage': '9',
                'scope': 'ORDER'
            }
        ],
        'discounts': [
            {
                'uid': 'labor-day-sale',
                'name': 'Labor Day Sale',
                'percentage': '5',
                'scope': 'ORDER'
            },
            {
                'uid': 'membership-discount',
                'catalog_object_id': 'DB7L55ZH2BGWI4H23ULIWOQ7',
                'scope': 'ORDER'
            },
            {
                'uid': 'one-dollar-off',
                'name': 'Sale - $1.00 off',
                'amount_money': {
                    'amount': 100,
                    'currency': 'USD'
                },
                'scope': 'LINE_ITEM'
            }
        ]
    },
    'idempotency_key': '8193148c-9586-11e6-99f9-28cfe92138cf'
}

result = orders_api.create_order(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Batch Retrieve Orders

Retrieves a set of [orders](../../doc/models/order.md) by their IDs.

If a given order ID does not exist, the ID is ignored instead of generating an error.

```python
def batch_retrieve_orders(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Retrieve Orders Request`](../../doc/models/batch-retrieve-orders-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Retrieve Orders Response`](../../doc/models/batch-retrieve-orders-response.md).

## Example Usage

```python
body = {
    'order_ids': [
        'CAISEM82RcpmcFBM0TfOyiHV3es',
        'CAISENgvlJ6jLWAzERDzjyHVybY'
    ],
    'location_id': '057P5VYJ4A5X1'
}

result = orders_api.batch_retrieve_orders(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Calculate Order

Enables applications to preview order pricing without creating an order.

```python
def calculate_order(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Calculate Order Request`](../../doc/models/calculate-order-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Calculate Order Response`](../../doc/models/calculate-order-response.md).

## Example Usage

```python
body = {
    'order': {
        'location_id': 'D7AVYMEAPJ3A3',
        'line_items': [
            {
                'quantity': '1',
                'name': 'Item 1',
                'base_price_money': {
                    'amount': 500,
                    'currency': 'USD'
                }
            },
            {
                'quantity': '2',
                'name': 'Item 2',
                'base_price_money': {
                    'amount': 300,
                    'currency': 'USD'
                }
            }
        ],
        'discounts': [
            {
                'name': '50% Off',
                'percentage': '50',
                'scope': 'ORDER'
            }
        ]
    }
}

result = orders_api.calculate_order(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Clone Order

Creates a new order, in the `DRAFT` state, by duplicating an existing order. The newly created order has
only the core fields (such as line items, taxes, and discounts) copied from the original order.

```python
def clone_order(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Clone Order Request`](../../doc/models/clone-order-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Clone Order Response`](../../doc/models/clone-order-response.md).

## Example Usage

```python
body = {
    'order_id': 'ZAISEM52YcpmcWAzERDOyiWS123',
    'version': 3,
    'idempotency_key': 'UNIQUE_STRING'
}

result = orders_api.clone_order(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Orders

Search all orders for one or more locations. Orders include all sales,
returns, and exchanges regardless of how or when they entered the Square
ecosystem (such as Point of Sale, Invoices, and Connect APIs).

`SearchOrders` requests need to specify which locations to search and define a
[SearchOrdersQuery](../../doc/models/search-orders-query.md) object that controls
how to sort or filter the results. Your `SearchOrdersQuery` can:

Set filter criteria.
Set the sort order.
Determine whether to return results as complete `Order` objects or as
[OrderEntry](../../doc/models/order-entry.md) objects.

Note that details for orders processed with Square Point of Sale while in
offline mode might not be transmitted to Square for up to 72 hours. Offline
orders have a `created_at` value that reflects the time the order was created,
not the time it was subsequently transmitted to Square.

```python
def search_orders(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Orders Request`](../../doc/models/search-orders-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Search Orders Response`](../../doc/models/search-orders-response.md).

## Example Usage

```python
body = {
    'location_ids': [
        '057P5VYJ4A5X1',
        '18YC4JDH91E1H'
    ],
    'query': {
        'filter': {
            'state_filter': {
                'states': [
                    'COMPLETED'
                ]
            },
            'date_time_filter': {
                'closed_at': {
                    'start_at': '2018-03-03T20:00:00+00:00',
                    'end_at': '2019-03-04T21:54:45+00:00'
                }
            }
        },
        'sort': {
            'sort_field': 'CLOSED_AT',
            'sort_order': 'DESC'
        }
    },
    'limit': 3,
    'return_entries': True
}

result = orders_api.search_orders(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Order

Retrieves an [Order](../../doc/models/order.md) by ID.

```python
def retrieve_order(self,
                  order_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | The ID of the order to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Order Response`](../../doc/models/retrieve-order-response.md).

## Example Usage

```python
order_id = 'order_id6'

result = orders_api.retrieve_order(order_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Order

Updates an open [order](../../doc/models/order.md) by adding, replacing, or deleting
fields. Orders with a `COMPLETED` or `CANCELED` state cannot be updated.

An `UpdateOrder` request requires the following:

- The `order_id` in the endpoint path, identifying the order to update.
- The latest `version` of the order to update.
- The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#sparse-order-objects)
  containing only the fields to update and the version to which the update is
  being applied.
- If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#identifying-fields-to-delete)
  identifying the fields to clear.

To pay for an order, see
[Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

```python
def update_order(self,
                order_id,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | The ID of the order to update. |
| `body` | [`Update Order Request`](../../doc/models/update-order-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Order Response`](../../doc/models/update-order-response.md).

## Example Usage

```python
order_id = 'order_id6'

body = {}

result = orders_api.update_order(
    order_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Pay Order

Pay for an [order](../../doc/models/order.md) using one or more approved [payments](../../doc/models/payment.md)
or settle an order with a total of `0`.

The total of the `payment_ids` listed in the request must be equal to the order
total. Orders with a total amount of `0` can be marked as paid by specifying an empty
array of `payment_ids` in the request.

To be used with `PayOrder`, a payment must:

- Reference the order by specifying the `order_id` when [creating the payment](../../doc/api/payments.md#create-payment).
  Any approved payments that reference the same `order_id` not specified in the
  `payment_ids` is canceled.
- Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture).
  Using a delayed capture payment with `PayOrder` completes the approved payment.

```python
def pay_order(self,
             order_id,
             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | The ID of the order being paid. |
| `body` | [`Pay Order Request`](../../doc/models/pay-order-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Pay Order Response`](../../doc/models/pay-order-response.md).

## Example Usage

```python
order_id = 'order_id6'

body = {
    'idempotency_key': 'c043a359-7ad9-4136-82a9-c3f1d66dcbff',
    'payment_ids': [
        'EnZdNAlWCmfh6Mt5FMNST1o7taB',
        '0LRiVlbXVwe8ozu4KbZxd12mvaB'
    ]
}

result = orders_api.pay_order(
    order_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

