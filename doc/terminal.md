# Terminal

```python
terminal_api = client.terminal
```

## Class Name

`TerminalApi`

## Methods

* [Create Terminal Checkout](/doc/terminal.md#create-terminal-checkout)
* [Search Terminal Checkouts](/doc/terminal.md#search-terminal-checkouts)
* [Get Terminal Checkout](/doc/terminal.md#get-terminal-checkout)
* [Cancel Terminal Checkout](/doc/terminal.md#cancel-terminal-checkout)

## Create Terminal Checkout

Creates a new Terminal checkout request and sends it to the specified device to take a payment for the requested amount.

```python
def create_terminal_checkout(self,
                            body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Terminal Checkout Request`](/doc/models/create-terminal-checkout-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Terminal Checkout Response`](/doc/models/create-terminal-checkout-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = '28a0c3bc-7839-11ea-bc55-0242ac130003'
body['checkout'] = {}
body['checkout']['id'] = 'id8'
body['checkout']['amount_money'] = {}
body['checkout']['amount_money']['amount'] = 2610
body['checkout']['amount_money']['currency'] = 'USD'
body['checkout']['reference_id'] = 'id11572'
body['checkout']['note'] = 'A brief note'
body['checkout']['device_options'] = {}
body['checkout']['device_options']['device_id'] = 'dbb5d83a-7838-11ea-bc55-0242ac130003'
body['checkout']['device_options']['skip_receipt_screen'] = False
body['checkout']['device_options']['tip_settings'] = {}
body['checkout']['device_options']['tip_settings']['allow_tipping'] = False
body['checkout']['device_options']['tip_settings']['separate_tip_screen'] = False
body['checkout']['device_options']['tip_settings']['custom_tip_field'] = False
body['checkout']['deadline_duration'] = 'deadline_duration0'
body['checkout']['status'] = 'status0'

result = terminal_api.create_terminal_checkout(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Terminal Checkouts

Retrieves a filtered list of Terminal checkout requests created by the account making the request.

```python
def search_terminal_checkouts(self,
                             body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Terminal Checkouts Request`](/doc/models/search-terminal-checkouts-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Terminal Checkouts Response`](/doc/models/search-terminal-checkouts-response.md)

### Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['device_id'] = 'device_id8'
body['query']['filter']['created_at'] = {}
body['query']['filter']['created_at']['start_at'] = 'start_at2'
body['query']['filter']['created_at']['end_at'] = 'end_at0'
body['query']['filter']['status'] = 'COMPLETED'
body['query']['sort'] = {}
body['query']['sort']['sort_order'] = 'sort_order8'
body['cursor'] = 'cursor0'
body['limit'] = 2

result = terminal_api.search_terminal_checkouts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Terminal Checkout

Retrieves a Terminal checkout request by checkout_id.

```python
def get_terminal_checkout(self,
                         checkout_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_id` | `string` | Template, Required | Unique ID for the desired `TerminalCheckout` |

### Response Type

[`Get Terminal Checkout Response`](/doc/models/get-terminal-checkout-response.md)

### Example Usage

```python
checkout_id = 'checkout_id8'

result = terminal_api.get_terminal_checkout(checkout_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Cancel Terminal Checkout

Cancels a Terminal checkout request, if the status of the request permits it.

```python
def cancel_terminal_checkout(self,
                            checkout_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_id` | `string` | Template, Required | Unique ID for the desired `TerminalCheckout` |

### Response Type

[`Cancel Terminal Checkout Response`](/doc/models/cancel-terminal-checkout-response.md)

### Example Usage

```python
checkout_id = 'checkout_id8'

result = terminal_api.cancel_terminal_checkout(checkout_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

