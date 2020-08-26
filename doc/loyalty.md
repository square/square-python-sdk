# Loyalty

```python
loyalty_api = client.loyalty
```

## Class Name

`LoyaltyApi`

## Methods

* [Create Loyalty Account](/doc/loyalty.md#create-loyalty-account)
* [Search Loyalty Accounts](/doc/loyalty.md#search-loyalty-accounts)
* [Retrieve Loyalty Account](/doc/loyalty.md#retrieve-loyalty-account)
* [Accumulate Loyalty Points](/doc/loyalty.md#accumulate-loyalty-points)
* [Adjust Loyalty Points](/doc/loyalty.md#adjust-loyalty-points)
* [Search Loyalty Events](/doc/loyalty.md#search-loyalty-events)
* [List Loyalty Programs](/doc/loyalty.md#list-loyalty-programs)
* [Calculate Loyalty Points](/doc/loyalty.md#calculate-loyalty-points)
* [Create Loyalty Reward](/doc/loyalty.md#create-loyalty-reward)
* [Search Loyalty Rewards](/doc/loyalty.md#search-loyalty-rewards)
* [Delete Loyalty Reward](/doc/loyalty.md#delete-loyalty-reward)
* [Retrieve Loyalty Reward](/doc/loyalty.md#retrieve-loyalty-reward)
* [Redeem Loyalty Reward](/doc/loyalty.md#redeem-loyalty-reward)

## Create Loyalty Account

Creates a loyalty account. For more information, see 
[Create a loyalty account](https://developer.squareup.com/docs/docs/loyalty-api/overview/#loyalty-overview-create-account).

```python
def create_loyalty_account(self,
                          body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Loyalty Account Request`](/doc/models/create-loyalty-account-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Loyalty Account Response`](/doc/models/create-loyalty-account-response.md)

### Example Usage

```python
body = {}
body['loyalty_account'] = {}
body['loyalty_account']['id'] = 'id2'
body['loyalty_account']['mappings'] = []

body['loyalty_account']['mappings'].append({})
body['loyalty_account']['mappings'][0]['id'] = 'id0'
body['loyalty_account']['mappings'][0]['type'] = 'PHONE'
body['loyalty_account']['mappings'][0]['value'] = '+14155551234'
body['loyalty_account']['mappings'][0]['created_at'] = 'created_at8'

body['loyalty_account']['program_id'] = 'd619f755-2d17-41f3-990d-c04ecedd64dd'
body['loyalty_account']['balance'] = 14
body['loyalty_account']['lifetime_points'] = 38
body['loyalty_account']['customer_id'] = 'customer_id0'
body['loyalty_account']['enrolled_at'] = 'enrolled_at2'
body['idempotency_key'] = 'ec78c477-b1c3-4899-a209-a4e71337c996'

result = loyalty_api.create_loyalty_account(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Loyalty Accounts

Searches for loyalty accounts. 
In the current implementation, you can search for a loyalty account using the phone number associated with the account. 
If no phone number is provided, all loyalty accounts are returned.

```python
def search_loyalty_accounts(self,
                           body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Loyalty Accounts Request`](/doc/models/search-loyalty-accounts-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Loyalty Accounts Response`](/doc/models/search-loyalty-accounts-response.md)

### Example Usage

```python
body = {}
body['query'] = {}
body['query']['mappings'] = []

body['query']['mappings'].append({})
body['query']['mappings'][0]['id'] = 'id4'
body['query']['mappings'][0]['type'] = 'PHONE'
body['query']['mappings'][0]['value'] = '+14155551234'
body['query']['mappings'][0]['created_at'] = 'created_at8'

body['limit'] = 10
body['cursor'] = 'cursor0'

result = loyalty_api.search_loyalty_accounts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Loyalty Account

Retrieves a loyalty account.

```python
def retrieve_loyalty_account(self,
                            account_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | The ID of the [loyalty account](#type-LoyaltyAccount) to retrieve. |

### Response Type

[`Retrieve Loyalty Account Response`](/doc/models/retrieve-loyalty-account-response.md)

### Example Usage

```python
account_id = 'account_id2'

result = loyalty_api.retrieve_loyalty_account(account_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Accumulate Loyalty Points

Adds points to a loyalty account.

- If you are using the Orders API to manage orders, you only provide the `order_id`. 
The endpoint reads the order to compute points to add to the buyer's account.
- If you are not using the Orders API to manage orders, 
you first perform a client-side computation to compute the points.  
For spend-based and visit-based programs, you can call 
`CalculateLoyaltyPoints` to compute the points. For more information, 
see [Loyalty Program Overview](https://developer.squareup.com/docs/docs/loyalty/overview). 
You then provide the points in a request to this endpoint. 

For more information, see [Accumulate points](https://developer.squareup.com/docs/docs/loyalty-api/overview/#accumulate-points).

```python
def accumulate_loyalty_points(self,
                             account_id,
                             body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | The [loyalty account](#type-LoyaltyAccount) ID to which to add the points. |
| `body` | [`Accumulate Loyalty Points Request`](/doc/models/accumulate-loyalty-points-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Accumulate Loyalty Points Response`](/doc/models/accumulate-loyalty-points-response.md)

### Example Usage

```python
account_id = 'account_id2'
body = {}
body['accumulate_points'] = {}
body['accumulate_points']['loyalty_program_id'] = 'loyalty_program_id8'
body['accumulate_points']['points'] = 90
body['accumulate_points']['order_id'] = 'RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY'
body['idempotency_key'] = '58b90739-c3e8-4b11-85f7-e636d48d72cb'
body['location_id'] = 'P034NEENMD09F'

result = loyalty_api.accumulate_loyalty_points(account_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Adjust Loyalty Points

Adds points to or subtracts points from a buyer's account. 

Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call 
[AccumulateLoyaltyPoints](https://developer.squareup.com/docs/reference/square/loyalty-api/accumulate-loyalty-points) 
to add points when a buyer pays for the purchase.

```python
def adjust_loyalty_points(self,
                         account_id,
                         body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | The ID of the [loyalty account](#type-LoyaltyAccount) in which to adjust the points. |
| `body` | [`Adjust Loyalty Points Request`](/doc/models/adjust-loyalty-points-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Adjust Loyalty Points Response`](/doc/models/adjust-loyalty-points-response.md)

### Example Usage

```python
account_id = 'account_id2'
body = {}
body['idempotency_key'] = 'idempotency_key2'
body['adjust_points'] = {}
body['adjust_points']['loyalty_program_id'] = 'loyalty_program_id4'
body['adjust_points']['points'] = 112
body['adjust_points']['reason'] = 'reason0'

result = loyalty_api.adjust_loyalty_points(account_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Loyalty Events

Searches for loyalty events.

A Square loyalty program maintains a ledger of events that occur during the lifetime of a 
buyer's loyalty account. Each change in the point balance 
(for example, points earned, points redeemed, and points expired) is 
recorded in the ledger. Using this endpoint, you can search the ledger for events. 
For more information, see 
[Loyalty events](https://developer.squareup.com/docs/docs/loyalty-api/overview/#loyalty-events).

```python
def search_loyalty_events(self,
                         body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Loyalty Events Request`](/doc/models/search-loyalty-events-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Loyalty Events Response`](/doc/models/search-loyalty-events-response.md)

### Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['loyalty_account_filter'] = {}
body['query']['filter']['loyalty_account_filter']['loyalty_account_id'] = 'loyalty_account_id6'
body['query']['filter']['type_filter'] = {}
body['query']['filter']['type_filter']['types'] = ['DELETE_REWARD', 'ADJUST_POINTS', 'EXPIRE_POINTS']
body['query']['filter']['date_time_filter'] = {}
body['query']['filter']['date_time_filter']['created_at'] = {}
body['query']['filter']['date_time_filter']['created_at']['start_at'] = 'start_at8'
body['query']['filter']['date_time_filter']['created_at']['end_at'] = 'end_at4'
body['query']['filter']['location_filter'] = {}
body['query']['filter']['location_filter']['location_ids'] = ['location_ids2', 'location_ids3', 'location_ids4']
body['query']['filter']['order_filter'] = {}
body['query']['filter']['order_filter']['order_id'] = 'PyATxhYLfsMqpVkcKJITPydgEYfZY'
body['limit'] = 30
body['cursor'] = 'cursor0'

result = loyalty_api.search_loyalty_events(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Loyalty Programs

Returns a list of loyalty programs in the seller's account.
Currently, a seller can only have one loyalty program. For more information, see 
[Loyalty Overview](https://developer.squareup.com/docs/docs/loyalty/overview).
.

```python
def list_loyalty_programs(self)
```

### Response Type

[`List Loyalty Programs Response`](/doc/models/list-loyalty-programs-response.md)

### Example Usage

```python
result = loyalty_api.list_loyalty_programs()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Calculate Loyalty Points

Calculates the points a purchase earns.

- If you are using the Orders API to manage orders, you provide `order_id` in the request. The 
endpoint calculates the points by reading the order.
- If you are not using the Orders API to manage orders, you provide the purchase amount in 
the request for the endpoint to calculate the points.

An application might call this endpoint to show the points that a buyer can earn with the 
specific purchase.

```python
def calculate_loyalty_points(self,
                            program_id,
                            body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `program_id` | `string` | Template, Required | The [loyalty program](#type-LoyaltyProgram) ID, which defines the rules for accruing points. |
| `body` | [`Calculate Loyalty Points Request`](/doc/models/calculate-loyalty-points-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Calculate Loyalty Points Response`](/doc/models/calculate-loyalty-points-response.md)

### Example Usage

```python
program_id = 'program_id0'
body = {}
body['order_id'] = 'RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY'
body['transaction_amount_money'] = {}
body['transaction_amount_money']['amount'] = 72
body['transaction_amount_money']['currency'] = 'UZS'

result = loyalty_api.calculate_loyalty_points(program_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Loyalty Reward

Creates a loyalty reward. In the process, the endpoint does following:

- Uses the `reward_tier_id` in the request to determine the number of points 
to lock for this reward. 
- If the request includes `order_id`, it adds the reward and related discount to the order. 

After a reward is created, the points are locked and 
not available for the buyer to redeem another reward. 
For more information, see 
[Loyalty rewards](https://developer.squareup.com/docs/docs/loyalty-api/overview/#loyalty-overview-loyalty-rewards).

```python
def create_loyalty_reward(self,
                         body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Loyalty Reward Request`](/doc/models/create-loyalty-reward-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Loyalty Reward Response`](/doc/models/create-loyalty-reward-response.md)

### Example Usage

```python
body = {}
body['reward'] = {}
body['reward']['id'] = 'id4'
body['reward']['status'] = 'REDEEMED'
body['reward']['loyalty_account_id'] = '5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd'
body['reward']['reward_tier_id'] = 'e1b39225-9da5-43d1-a5db-782cdd8ad94f'
body['reward']['points'] = 230
body['reward']['order_id'] = 'RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY'
body['reward']['created_at'] = 'created_at2'
body['idempotency_key'] = '18c2e5ea-a620-4b1f-ad60-7b167285e451'

result = loyalty_api.create_loyalty_reward(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Loyalty Rewards

Searches for loyalty rewards in a loyalty account. 

In the current implementation, the endpoint supports search by the reward `status`.

If you know a reward ID, use the 
[RetrieveLoyaltyReward](https://developer.squareup.com/docs/reference/square/loyalty-api/retrieve-loyalty-reward) endpoint.

For more information about loyalty rewards, see 
[Loyalty Rewards](https://developer.squareup.com/docs/docs/loyalty-api/overview/#loyalty-rewards).

```python
def search_loyalty_rewards(self,
                          body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Loyalty Rewards Request`](/doc/models/search-loyalty-rewards-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Loyalty Rewards Response`](/doc/models/search-loyalty-rewards-response.md)

### Example Usage

```python
body = {}
body['query'] = {}
body['query']['loyalty_account_id'] = '5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd'
body['query']['status'] = 'REDEEMED'
body['limit'] = 10
body['cursor'] = 'cursor0'

result = loyalty_api.search_loyalty_rewards(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Delete Loyalty Reward

Deletes a loyalty reward by doing the following:

- Returns the loyalty points back to the loyalty account.
- If an order ID was specified when the reward was created 
(see [CreateLoyaltyReward](https://developer.squareup.com/docs/reference/square/loyalty-api/create-loyalty-reward)), 
it updates the order by removing the reward and related 
discounts.

You cannot delete a reward that has reached the terminal state (REDEEMED). 
For more information, see 
[Loyalty rewards](https://developer.squareup.com/docs/docs/loyalty-api/overview/#loyalty-overview-loyalty-rewards).

```python
def delete_loyalty_reward(self,
                         reward_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reward_id` | `string` | Template, Required | The ID of the [loyalty reward](#type-LoyaltyReward) to delete. |

### Response Type

[`Delete Loyalty Reward Response`](/doc/models/delete-loyalty-reward-response.md)

### Example Usage

```python
reward_id = 'reward_id4'

result = loyalty_api.delete_loyalty_reward(reward_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Loyalty Reward

Retrieves a loyalty reward.

```python
def retrieve_loyalty_reward(self,
                           reward_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reward_id` | `string` | Template, Required | The ID of the [loyalty reward](#type-LoyaltyReward) to retrieve. |

### Response Type

[`Retrieve Loyalty Reward Response`](/doc/models/retrieve-loyalty-reward-response.md)

### Example Usage

```python
reward_id = 'reward_id4'

result = loyalty_api.retrieve_loyalty_reward(reward_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Redeem Loyalty Reward

Redeems a loyalty reward.

The endpoint sets the reward to the terminal state (`REDEEMED`). 

If you are using your own order processing system (not using the 
Orders API), you call this endpoint after the buyer paid for the 
purchase.

After the reward reaches the terminal state, it cannot be deleted. 
In other words, points used for the reward cannot be returned 
to the account.

For more information, see 
[Loyalty rewards](https://developer.squareup.com/docs/docs/loyalty-api/overview/#loyalty-overview-loyalty-rewards).

```python
def redeem_loyalty_reward(self,
                         reward_id,
                         body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reward_id` | `string` | Template, Required | The ID of the [loyalty reward](#type-LoyaltyReward) to redeem. |
| `body` | [`Redeem Loyalty Reward Request`](/doc/models/redeem-loyalty-reward-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Redeem Loyalty Reward Response`](/doc/models/redeem-loyalty-reward-response.md)

### Example Usage

```python
reward_id = 'reward_id4'
body = {}
body['idempotency_key'] = '98adc7f7-6963-473b-b29c-f3c9cdd7d994'
body['location_id'] = 'P034NEENMD09F'

result = loyalty_api.redeem_loyalty_reward(reward_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

