# Subscriptions

```python
subscriptions_api = client.subscriptions
```

## Class Name

`SubscriptionsApi`

## Methods

* [Create Subscription](/doc/subscriptions.md#create-subscription)
* [Search Subscriptions](/doc/subscriptions.md#search-subscriptions)
* [Retrieve Subscription](/doc/subscriptions.md#retrieve-subscription)
* [Update Subscription](/doc/subscriptions.md#update-subscription)
* [Cancel Subscription](/doc/subscriptions.md#cancel-subscription)
* [List Subscription Events](/doc/subscriptions.md#list-subscription-events)

## Create Subscription

Creates a subscription for a customer to a subscription plan.

If you provide a card on file in the request, Square charges the card for 
the subscription. Otherwise, Square bills an invoice to the customer's email 
address. The subscription starts immediately, unless the request includes 
the optional `start_date`. Each individual subscription is associated with a particular location.

Subscriptions Guide: [https://developer.squareup.com/docs/subscriptions-api/overview#create-subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#create-subscriptions)

```python
def create_subscription(self,
                       body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Subscription Request`](/doc/models/create-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Subscription Response`](/doc/models/create-subscription-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = '8193148c-9586-11e6-99f9-28cfe92138cf'
body['location_id'] = 'S8GWD5R9QB376'
body['plan_id'] = '6JHXF3B2CW3YKHDV4XEM674H'
body['customer_id'] = 'CHFGVKYY8RSV93M5KCYTG4PN0G'
body['start_date'] = '2020-08-01'
body['canceled_date'] = 'canceled_date0'
body['tax_percentage'] = '5'
body['price_override_money'] = {}
body['price_override_money']['amount'] = 100
body['price_override_money']['currency'] = 'USD'
body['card_id'] = 'ccof:qy5x8hHGYsgLrp4Q4GB'
body['timezone'] = 'America/Los_Angeles'

result = subscriptions_api.create_subscription(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Subscriptions

Searches for subscriptions. 
Results are ordered chronologically by subscription creation date. If
the request specifies more than one location ID, 
the endpoint orders the result 
by location ID, and then by creation date within each location. If no locations are given
in the query, all locations are searched.

You can also optionally specify `customer_ids` to search by customer. 
If left unset, all customers 
associated with the specified locations are returned. 
If the request specifies customer IDs, the endpoint orders results 
first by location, within location by customer ID, and within 
customer by subscription creation date.

For more information, see 
[Retrieve subscriptions](https://developer.squareup.com/docs/docs/subscriptions-api/overview#retrieve-subscriptions).

Subscriptions Guide: [https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions)

```python
def search_subscriptions(self,
                        body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Subscriptions Request`](/doc/models/search-subscriptions-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Subscriptions Response`](/doc/models/search-subscriptions-response.md)

### Example Usage

```python
body = {}
body['cursor'] = 'cursor0'
body['limit'] = 164
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['customer_ids'] = ['CHFGVKYY8RSV93M5KCYTG4PN0G']
body['query']['filter']['location_ids'] = ['S8GWD5R9QB376']

result = subscriptions_api.search_subscriptions(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Subscription

Retrieves a subscription.

Subscriptions Guide: [https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions)

```python
def retrieve_subscription(self,
                         subscription_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to retrieve. |

### Response Type

[`Retrieve Subscription Response`](/doc/models/retrieve-subscription-response.md)

### Example Usage

```python
subscription_id = 'subscription_id0'

result = subscriptions_api.retrieve_subscription(subscription_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Subscription

Updates a subscription. You can set, modify, and clear the 
`subscription` field values.

Subscriptions Guide: [https://developer.squareup.com/docs/subscriptions-api/overview#update-subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#update-subscriptions)

```python
def update_subscription(self,
                       subscription_id,
                       body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID for the subscription to update. |
| `body` | [`Update Subscription Request`](/doc/models/update-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Subscription Response`](/doc/models/update-subscription-response.md)

### Example Usage

```python
subscription_id = 'subscription_id0'
body = {}
body['subscription'] = {}
body['subscription']['id'] = 'id8'
body['subscription']['location_id'] = 'location_id2'
body['subscription']['plan_id'] = 'plan_id0'
body['subscription']['customer_id'] = 'customer_id6'
body['subscription']['start_date'] = 'start_date2'
body['subscription']['tax_percentage'] = 'null'
body['subscription']['price_override_money'] = {}
body['subscription']['price_override_money']['amount'] = 2000
body['subscription']['price_override_money']['currency'] = 'USD'
body['subscription']['version'] = 1594155459464

result = subscriptions_api.update_subscription(subscription_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Cancel Subscription

Sets the `canceled_date` field to the end of the active billing period.
After this date, the status changes from ACTIVE to CANCELED.

Subscriptions Guide: [https://developer.squareup.com/docs/subscriptions-api/overview#cancel-subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#cancel-subscriptions)

```python
def cancel_subscription(self,
                       subscription_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to cancel. |

### Response Type

[`Cancel Subscription Response`](/doc/models/cancel-subscription-response.md)

### Example Usage

```python
subscription_id = 'subscription_id0'

result = subscriptions_api.cancel_subscription(subscription_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Subscription Events

Lists all events for a specific subscription.
In the current implementation, only `START_SUBSCRIPTION` and `STOP_SUBSCRIPTION` (when the subscription was canceled) events are returned.

Subscriptions Guide: [https://developer.squareup.com/docs/subscriptions-api/overview#subscription-events](https://developer.squareup.com/docs/subscriptions-api/overview#subscription-events)

```python
def list_subscription_events(self,
                            subscription_id,
                            cursor=None,
                            limit=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to retrieve the events for. |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination). |
| `limit` | `int` | Query, Optional | The upper limit on the number of subscription events to return <br>in the response. <br><br>Default: `200` |

### Response Type

[`List Subscription Events Response`](/doc/models/list-subscription-events-response.md)

### Example Usage

```python
subscription_id = 'subscription_id0'
cursor = 'cursor6'
limit = 172

result = subscriptions_api.list_subscription_events(subscription_id, cursor, limit)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

