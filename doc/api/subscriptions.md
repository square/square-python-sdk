# Subscriptions

```python
subscriptions_api = client.subscriptions
```

## Class Name

`SubscriptionsApi`

## Methods

* [Create Subscription](../../doc/api/subscriptions.md#create-subscription)
* [Search Subscriptions](../../doc/api/subscriptions.md#search-subscriptions)
* [Retrieve Subscription](../../doc/api/subscriptions.md#retrieve-subscription)
* [Update Subscription](../../doc/api/subscriptions.md#update-subscription)
* [Delete Subscription Action](../../doc/api/subscriptions.md#delete-subscription-action)
* [Cancel Subscription](../../doc/api/subscriptions.md#cancel-subscription)
* [List Subscription Events](../../doc/api/subscriptions.md#list-subscription-events)
* [Pause Subscription](../../doc/api/subscriptions.md#pause-subscription)
* [Resume Subscription](../../doc/api/subscriptions.md#resume-subscription)
* [Swap Plan](../../doc/api/subscriptions.md#swap-plan)


# Create Subscription

Creates a subscription to a subscription plan by a customer.

If you provide a card on file in the request, Square charges the card for
the subscription. Otherwise, Square bills an invoice to the customer's email
address. The subscription starts immediately, unless the request includes
the optional `start_date`. Each individual subscription is associated with a particular location.

```python
def create_subscription(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Subscription Request`](../../doc/models/create-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Subscription Response`](../../doc/models/create-subscription-response.md)

## Example Usage

```python
body = {}
body['idempotency_key'] = '8193148c-9586-11e6-99f9-28cfe92138cf'
body['location_id'] = 'S8GWD5R9QB376'
body['plan_id'] = '6JHXF3B2CW3YKHDV4XEM674H'
body['customer_id'] = 'CHFGVKYY8RSV93M5KCYTG4PN0G'
body['start_date'] = '2021-10-20'
body['tax_percentage'] = '5'
body['price_override_money'] = {}
body['price_override_money']['amount'] = 100
body['price_override_money']['currency'] = 'USD'
body['card_id'] = 'ccof:qy5x8hHGYsgLrp4Q4GB'
body['timezone'] = 'America/Los_Angeles'
body['source'] = {}
body['source']['name'] = 'My App'

result = subscriptions_api.create_subscription(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Subscriptions

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
[Retrieve subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions).

```python
def search_subscriptions(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Subscriptions Request`](../../doc/models/search-subscriptions-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Search Subscriptions Response`](../../doc/models/search-subscriptions-response.md)

## Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['customer_ids'] = ['CHFGVKYY8RSV93M5KCYTG4PN0G']
body['query']['filter']['location_ids'] = ['S8GWD5R9QB376']
body['query']['filter']['source_names'] = ['My App']

result = subscriptions_api.search_subscriptions(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Subscription

Retrieves a subscription.

```python
def retrieve_subscription(self,
                         subscription_id,
                         include=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to retrieve. |
| `include` | `string` | Query, Optional | A query parameter to specify related information to be included in the response.<br><br>The supported query parameter values are:<br><br>- `actions`: to include scheduled actions on the targeted subscription. |

## Response Type

[`Retrieve Subscription Response`](../../doc/models/retrieve-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = subscriptions_api.retrieve_subscription(subscription_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Subscription

Updates a subscription. You can set, modify, and clear the
`subscription` field values.

```python
def update_subscription(self,
                       subscription_id,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to update. |
| `body` | [`Update Subscription Request`](../../doc/models/update-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Update Subscription Response`](../../doc/models/update-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'
body = {}
body['subscription'] = {}
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


# Delete Subscription Action

Deletes a scheduled action for a subscription.

```python
def delete_subscription_action(self,
                              subscription_id,
                              action_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription the targeted action is to act upon. |
| `action_id` | `string` | Template, Required | The ID of the targeted action to be deleted. |

## Response Type

[`Delete Subscription Action Response`](../../doc/models/delete-subscription-action-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'
action_id = 'action_id6'

result = subscriptions_api.delete_subscription_action(subscription_id, action_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Cancel Subscription

Schedules a `CANCEL` action to cancel an active subscription
by setting the `canceled_date` field to the end of the active billing period
and changing the subscription status from ACTIVE to CANCELED after this date.

```python
def cancel_subscription(self,
                       subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to cancel. |

## Response Type

[`Cancel Subscription Response`](../../doc/models/cancel-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = subscriptions_api.cancel_subscription(subscription_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Subscription Events

Lists all events for a specific subscription.

```python
def list_subscription_events(self,
                            subscription_id,
                            cursor=None,
                            limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to retrieve the events for. |
| `cursor` | `string` | Query, Optional | When the total number of resulting subscription events exceeds the limit of a paged response,<br>specify the cursor returned from a preceding response here to fetch the next set of results.<br>If the cursor is unset, the response contains the last page of the results.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |
| `limit` | `int` | Query, Optional | The upper limit on the number of subscription events to return<br>in a paged response. |

## Response Type

[`List Subscription Events Response`](../../doc/models/list-subscription-events-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = subscriptions_api.list_subscription_events(subscription_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Pause Subscription

Schedules a `PAUSE` action to pause an active subscription.

```python
def pause_subscription(self,
                      subscription_id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to pause. |
| `body` | [`Pause Subscription Request`](../../doc/models/pause-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Pause Subscription Response`](../../doc/models/pause-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'
body = {}

result = subscriptions_api.pause_subscription(subscription_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Resume Subscription

Schedules a `RESUME` action to resume a paused or a deactivated subscription.

```python
def resume_subscription(self,
                       subscription_id,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to resume. |
| `body` | [`Resume Subscription Request`](../../doc/models/resume-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Resume Subscription Response`](../../doc/models/resume-subscription-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'
body = {}

result = subscriptions_api.resume_subscription(subscription_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Swap Plan

Schedules a `SWAP_PLAN` action to swap a subscription plan in an existing subscription.

```python
def swap_plan(self,
             subscription_id,
             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `string` | Template, Required | The ID of the subscription to swap the subscription plan for. |
| `body` | [`Swap Plan Request`](../../doc/models/swap-plan-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Swap Plan Response`](../../doc/models/swap-plan-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'
body = {}
body['new_plan_id'] = 'new_plan_id2'

result = subscriptions_api.swap_plan(subscription_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

