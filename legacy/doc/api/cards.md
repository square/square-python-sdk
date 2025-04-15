# Cards

```python
cards_api = client.cards
```

## Class Name

`CardsApi`

## Methods

* [List Cards](../../doc/api/cards.md#list-cards)
* [Create Card](../../doc/api/cards.md#create-card)
* [Retrieve Card](../../doc/api/cards.md#retrieve-card)
* [Disable Card](../../doc/api/cards.md#disable-card)


# List Cards

Retrieves a list of cards owned by the account making the request.
A max of 25 cards will be returned.

```python
def list_cards(self,
              cursor=None,
              customer_id=None,
              include_disabled=False,
              reference_id=None,
              sort_order=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information. |
| `customer_id` | `str` | Query, Optional | Limit results to cards associated with the customer supplied.<br>By default, all cards owned by the merchant are returned. |
| `include_disabled` | `bool` | Query, Optional | Includes disabled cards.<br>By default, all enabled cards owned by the merchant are returned.<br>**Default**: `False` |
| `reference_id` | `str` | Query, Optional | Limit results to cards associated with the reference_id supplied. |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Query, Optional | Sorts the returned list by when the card was created with the specified order.<br>This field defaults to ASC. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Cards Response`](../../doc/models/list-cards-response.md).

## Example Usage

```python
include_disabled = False

result = cards_api.list_cards(
    include_disabled=include_disabled
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Card

Adds a card on file to an existing merchant.

```python
def create_card(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Card Request`](../../doc/models/create-card-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Card Response`](../../doc/models/create-card-response.md).

## Example Usage

```python
body = {
    'idempotency_key': '4935a656-a929-4792-b97c-8848be85c27c',
    'source_id': 'cnon:uIbfJXhXETSP197M3GB',
    'card': {
        'cardholder_name': 'Amelia Earhart',
        'billing_address': {
            'address_line_1': '500 Electric Ave',
            'address_line_2': 'Suite 600',
            'locality': 'New York',
            'administrative_district_level_1': 'NY',
            'postal_code': '10003',
            'country': 'US'
        },
        'customer_id': 'VDKXEEKPJN48QDG3BGGFAK05P8',
        'reference_id': 'user-id-1'
    }
}

result = cards_api.create_card(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Card

Retrieves details for a specific Card.

```python
def retrieve_card(self,
                 card_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `str` | Template, Required | Unique ID for the desired Card. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Card Response`](../../doc/models/retrieve-card-response.md).

## Example Usage

```python
card_id = 'card_id4'

result = cards_api.retrieve_card(card_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Disable Card

Disables the card, preventing any further updates or charges.
Disabling an already disabled card is allowed but has no effect.

```python
def disable_card(self,
                card_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_id` | `str` | Template, Required | Unique ID for the desired Card. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Disable Card Response`](../../doc/models/disable-card-response.md).

## Example Usage

```python
card_id = 'card_id4'

result = cards_api.disable_card(card_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

