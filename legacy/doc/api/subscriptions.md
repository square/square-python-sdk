# Subscriptions

```python
subscriptions_api = client.subscriptions
```

## Class Name

`SubscriptionsApi`

## Methods

* [Create Subscription](../../doc/api/subscriptions.md#create-subscription)
* [Bulk Swap Plan](../../doc/api/subscriptions.md#bulk-swap-plan)
* [Search Subscriptions](../../doc/api/subscriptions.md#search-subscriptions)
* [Retrieve Subscription](../../doc/api/subscriptions.md#retrieve-subscription)
* [Update Subscription](../../doc/api/subscriptions.md#update-subscription)
* [Delete Subscription Action](../../doc/api/subscriptions.md#delete-subscription-action)
* [Change Billing Anchor Date](../../doc/api/subscriptions.md#change-billing-anchor-date)
* [Cancel Subscription](../../doc/api/subscriptions.md#cancel-subscription)
* [List Subscription Events](../../doc/api/subscriptions.md#list-subscription-events)
* [Pause Subscription](../../doc/api/subscriptions.md#pause-subscription)
* [Resume Subscription](../../doc/api/subscriptions.md#resume-subscription)
* [Swap Plan](../../doc/api/subscriptions.md#swap-plan)


# Create Subscription

Enrolls a customer in a subscription.

If you provide a card on file in the request, Square charges the card for
the subscription. Otherwise, Square sends an invoice to the customer's email
address. The subscription starts immediately, unless the request includes
the optional `start_date`. Each individual subscription is associated with a particular location.

For more information, see [Create a subscription](https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions#create-a-subscription).

```python
def create_subscription(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Subscription Request`](../../doc/models/create-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Subscription Response`](../../doc/models/create-subscription-response.md).

## Example Usage

```python
body = {
    'location_id': 'S8GWD5R9QB376',
    'customer_id': 'CHFGVKYY8RSV93M5KCYTG4PN0G',
    'idempotency_key': '8193148c-9586-11e6-99f9-28cfe92138cf',
    'plan_variation_id': '6JHXF3B2CW3YKHDV4XEM674H',
    'start_date': '2023-06-20',
    'card_id': 'ccof:qy5x8hHGYsgLrp4Q4GB',
    'timezone': 'America/Los_Angeles',
    'source': {
        'name': 'My Application'
    },
    'phases': [
        {
            'ordinal': 0,
            'order_template_id': 'U2NaowWxzXwpsZU697x7ZHOAnCNZY'
        }
    ]
}

result = subscriptions_api.create_subscription(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Swap Plan

Schedules a plan variation change for all active subscriptions under a given plan
variation. For more information, see [Swap Subscription Plan Variations](https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations).

```python
def bulk_swap_plan(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Swap Plan Request`](../../doc/models/bulk-swap-plan-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Swap Plan Response`](../../doc/models/bulk-swap-plan-response.md).

## Example Usage

```python
body = {
    'new_plan_variation_id': 'FQ7CDXXWSLUJRPM3GFJSJGZ7',
    'old_plan_variation_id': '6JHXF3B2CW3YKHDV4XEM674H',
    'location_id': 'S8GWD5R9QB376'
}

result = subscriptions_api.bulk_swap_plan(body)

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

```python
def search_subscriptions(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Subscriptions Request`](../../doc/models/search-subscriptions-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Search Subscriptions Response`](../../doc/models/search-subscriptions-response.md).

## Example Usage

```python
body = {
    'query': {
        'filter': {
            'customer_ids': [
                'CHFGVKYY8RSV93M5KCYTG4PN0G'
            ],
            'location_ids': [
                'S8GWD5R9QB376'
            ],
            'source_names': [
                'My App'
            ]
        }
    }
}

result = subscriptions_api.search_subscriptions(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Subscription

Retrieves a specific subscription.

```python
def retrieve_subscription(self,
                         subscription_id,
                         include=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The ID of the subscription to retrieve. |
| `include` | `str` | Query, Optional | A query parameter to specify related information to be included in the response.<br><br>The supported query parameter values are:<br><br>- `actions`: to include scheduled actions on the targeted subscription. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Subscription Response`](../../doc/models/retrieve-subscription-response.md).

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

Updates a subscription by modifying or clearing `subscription` field values.
To clear a field, set its value to `null`.

```python
def update_subscription(self,
                       subscription_id,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The ID of the subscription to update. |
| `body` | [`Update Subscription Request`](../../doc/models/update-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Subscription Response`](../../doc/models/update-subscription-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

body = {
    'subscription': {
        'canceled_date': 'canceled_date6',
        'card_id': '{NEW CARD ID}'
    }
}

result = subscriptions_api.update_subscription(
    subscription_id,
    body
)

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
| `subscription_id` | `str` | Template, Required | The ID of the subscription the targeted action is to act upon. |
| `action_id` | `str` | Template, Required | The ID of the targeted action to be deleted. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Subscription Action Response`](../../doc/models/delete-subscription-action-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

action_id = 'action_id6'

result = subscriptions_api.delete_subscription_action(
    subscription_id,
    action_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Change Billing Anchor Date

Changes the [billing anchor date](https://developer.squareup.com/docs/subscriptions-api/subscription-billing#billing-dates)
for a subscription.

```python
def change_billing_anchor_date(self,
                              subscription_id,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The ID of the subscription to update the billing anchor date. |
| `body` | [`Change Billing Anchor Date Request`](../../doc/models/change-billing-anchor-date-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Change Billing Anchor Date Response`](../../doc/models/change-billing-anchor-date-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

body = {
    'monthly_billing_anchor_date': 1
}

result = subscriptions_api.change_billing_anchor_date(
    subscription_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Cancel Subscription

Schedules a `CANCEL` action to cancel an active subscription. This
sets the `canceled_date` field to the end of the active billing period. After this date,
the subscription status changes from ACTIVE to CANCELED.

```python
def cancel_subscription(self,
                       subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The ID of the subscription to cancel. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Cancel Subscription Response`](../../doc/models/cancel-subscription-response.md).

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

Lists all [events](https://developer.squareup.com/docs/subscriptions-api/actions-events) for a specific subscription.

```python
def list_subscription_events(self,
                            subscription_id,
                            cursor=None,
                            limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The ID of the subscription to retrieve the events for. |
| `cursor` | `str` | Query, Optional | When the total number of resulting subscription events exceeds the limit of a paged response,<br>specify the cursor returned from a preceding response here to fetch the next set of results.<br>If the cursor is unset, the response contains the last page of the results.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `limit` | `int` | Query, Optional | The upper limit on the number of subscription events to return<br>in a paged response. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Subscription Events Response`](../../doc/models/list-subscription-events-response.md).

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
| `subscription_id` | `str` | Template, Required | The ID of the subscription to pause. |
| `body` | [`Pause Subscription Request`](../../doc/models/pause-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Pause Subscription Response`](../../doc/models/pause-subscription-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

body = {}

result = subscriptions_api.pause_subscription(
    subscription_id,
    body
)

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
| `subscription_id` | `str` | Template, Required | The ID of the subscription to resume. |
| `body` | [`Resume Subscription Request`](../../doc/models/resume-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Resume Subscription Response`](../../doc/models/resume-subscription-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

body = {}

result = subscriptions_api.resume_subscription(
    subscription_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Swap Plan

Schedules a `SWAP_PLAN` action to swap a subscription plan variation in an existing subscription.
For more information, see [Swap Subscription Plan Variations](https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations).

```python
def swap_plan(self,
             subscription_id,
             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The ID of the subscription to swap the subscription plan for. |
| `body` | [`Swap Plan Request`](../../doc/models/swap-plan-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Swap Plan Response`](../../doc/models/swap-plan-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

body = {
    'new_plan_variation_id': 'FQ7CDXXWSLUJRPM3GFJSJGZ7',
    'phases': [
        {
            'ordinal': 0,
            'order_template_id': 'uhhnjH9osVv3shUADwaC0b3hNxQZY'
        }
    ]
}

result = subscriptions_api.swap_plan(
    subscription_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

