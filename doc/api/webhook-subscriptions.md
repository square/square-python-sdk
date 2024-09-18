# Webhook Subscriptions

```python
webhook_subscriptions_api = client.webhook_subscriptions
```

## Class Name

`WebhookSubscriptionsApi`

## Methods

* [List Webhook Event Types](../../doc/api/webhook-subscriptions.md#list-webhook-event-types)
* [List Webhook Subscriptions](../../doc/api/webhook-subscriptions.md#list-webhook-subscriptions)
* [Create Webhook Subscription](../../doc/api/webhook-subscriptions.md#create-webhook-subscription)
* [Delete Webhook Subscription](../../doc/api/webhook-subscriptions.md#delete-webhook-subscription)
* [Retrieve Webhook Subscription](../../doc/api/webhook-subscriptions.md#retrieve-webhook-subscription)
* [Update Webhook Subscription](../../doc/api/webhook-subscriptions.md#update-webhook-subscription)
* [Update Webhook Subscription Signature Key](../../doc/api/webhook-subscriptions.md#update-webhook-subscription-signature-key)
* [Test Webhook Subscription](../../doc/api/webhook-subscriptions.md#test-webhook-subscription)


# List Webhook Event Types

Lists all webhook event types that can be subscribed to.

```python
def list_webhook_event_types(self,
                            api_version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_version` | `str` | Query, Optional | The API version for which to list event types. Setting this field overrides the default version used by the application. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Webhook Event Types Response`](../../doc/models/list-webhook-event-types-response.md).

## Example Usage

```python
result = webhook_subscriptions_api.list_webhook_event_types()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Webhook Subscriptions

Lists all webhook subscriptions owned by your application.

```python
def list_webhook_subscriptions(self,
                              cursor=None,
                              include_disabled=False,
                              sort_order=None,
                              limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `include_disabled` | `bool` | Query, Optional | Includes disabled [Subscription](entity:WebhookSubscription)s.<br>By default, all enabled [Subscription](entity:WebhookSubscription)s are returned.<br>**Default**: `False` |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Query, Optional | Sorts the returned list by when the [Subscription](entity:WebhookSubscription) was created with the specified order.<br>This field defaults to ASC. |
| `limit` | `int` | Query, Optional | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br>The default value of 100 is also the maximum allowed value.<br><br>Default: 100 |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Webhook Subscriptions Response`](../../doc/models/list-webhook-subscriptions-response.md).

## Example Usage

```python
include_disabled = False

result = webhook_subscriptions_api.list_webhook_subscriptions(
    include_disabled=include_disabled
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Webhook Subscription

Creates a webhook subscription.

```python
def create_webhook_subscription(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Webhook Subscription Request`](../../doc/models/create-webhook-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Webhook Subscription Response`](../../doc/models/create-webhook-subscription-response.md).

## Example Usage

```python
body = {
    'subscription': {
        'name': 'Example Webhook Subscription',
        'event_types': [
            'payment.created',
            'payment.updated'
        ],
        'notification_url': 'https://example-webhook-url.com',
        'api_version': '2021-12-15'
    },
    'idempotency_key': '63f84c6c-2200-4c99-846c-2670a1311fbf'
}

result = webhook_subscriptions_api.create_webhook_subscription(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Webhook Subscription

Deletes a webhook subscription.

```python
def delete_webhook_subscription(self,
                               subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to delete. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Webhook Subscription Response`](../../doc/models/delete-webhook-subscription-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

result = webhook_subscriptions_api.delete_webhook_subscription(subscription_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Webhook Subscription

Retrieves a webhook subscription identified by its ID.

```python
def retrieve_webhook_subscription(self,
                                 subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Webhook Subscription Response`](../../doc/models/retrieve-webhook-subscription-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

result = webhook_subscriptions_api.retrieve_webhook_subscription(subscription_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Webhook Subscription

Updates a webhook subscription.

```python
def update_webhook_subscription(self,
                               subscription_id,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update. |
| `body` | [`Update Webhook Subscription Request`](../../doc/models/update-webhook-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Webhook Subscription Response`](../../doc/models/update-webhook-subscription-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

body = {
    'subscription': {
        'name': 'Updated Example Webhook Subscription',
        'enabled': False
    }
}

result = webhook_subscriptions_api.update_webhook_subscription(
    subscription_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Webhook Subscription Signature Key

Updates a webhook subscription by replacing the existing signature key with a new one.

```python
def update_webhook_subscription_signature_key(self,
                                             subscription_id,
                                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update. |
| `body` | [`Update Webhook Subscription Signature Key Request`](../../doc/models/update-webhook-subscription-signature-key-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Webhook Subscription Signature Key Response`](../../doc/models/update-webhook-subscription-signature-key-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

body = {
    'idempotency_key': 'ed80ae6b-0654-473b-bbab-a39aee89a60d'
}

result = webhook_subscriptions_api.update_webhook_subscription_signature_key(
    subscription_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Test Webhook Subscription

Tests a webhook subscription by sending a test event to the notification URL.

```python
def test_webhook_subscription(self,
                             subscription_id,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to test. |
| `body` | [`Test Webhook Subscription Request`](../../doc/models/test-webhook-subscription-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Test Webhook Subscription Response`](../../doc/models/test-webhook-subscription-response.md).

## Example Usage

```python
subscription_id = 'subscription_id0'

body = {
    'event_type': 'payment.created'
}

result = webhook_subscriptions_api.test_webhook_subscription(
    subscription_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

