# Customers

```python
customers_api = client.customers
```

## Class Name

`CustomersApi`

## Methods

* [List Customers](../../doc/api/customers.md#list-customers)
* [Create Customer](../../doc/api/customers.md#create-customer)
* [Bulk Create Customers](../../doc/api/customers.md#bulk-create-customers)
* [Bulk Delete Customers](../../doc/api/customers.md#bulk-delete-customers)
* [Bulk Retrieve Customers](../../doc/api/customers.md#bulk-retrieve-customers)
* [Bulk Update Customers](../../doc/api/customers.md#bulk-update-customers)
* [Search Customers](../../doc/api/customers.md#search-customers)
* [Delete Customer](../../doc/api/customers.md#delete-customer)
* [Retrieve Customer](../../doc/api/customers.md#retrieve-customer)
* [Update Customer](../../doc/api/customers.md#update-customer)
* [Create Customer Card](../../doc/api/customers.md#create-customer-card)
* [Delete Customer Card](../../doc/api/customers.md#delete-customer-card)
* [Remove Group From Customer](../../doc/api/customers.md#remove-group-from-customer)
* [Add Group to Customer](../../doc/api/customers.md#add-group-to-customer)


# List Customers

Lists customer profiles associated with a Square account.

Under normal operating conditions, newly created or updated customer profiles become available
for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated
profiles can take closer to one minute or longer, especially during network incidents and outages.

```python
def list_customers(self,
                  cursor=None,
                  limit=None,
                  sort_field=None,
                  sort_order=None,
                  count=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for your original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.<br>If the specified limit is less than 1 or greater than 100, Square returns a `400 VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default value is 100.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `sort_field` | [`str (Customer Sort Field)`](../../doc/models/customer-sort-field.md) | Query, Optional | Indicates how customers should be sorted.<br><br>The default value is `DEFAULT`. |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Query, Optional | Indicates whether customers should be sorted in ascending (`ASC`) or<br>descending (`DESC`) order.<br><br>The default value is `ASC`. |
| `count` | `bool` | Query, Optional | Indicates whether to return the total count of customers in the `count` field of the response.<br><br>The default value is `false`.<br>**Default**: `False` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Customers Response`](../../doc/models/list-customers-response.md).

## Example Usage

```python
count = False

result = customers_api.list_customers(
    count=count
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Customer

Creates a new customer for a business.

You must provide at least one of the following values in your request to this
endpoint:

- `given_name`
- `family_name`
- `company_name`
- `email_address`
- `phone_number`

```python
def create_customer(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Customer Request`](../../doc/models/create-customer-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Customer Response`](../../doc/models/create-customer-response.md).

## Example Usage

```python
body = {
    'given_name': 'Amelia',
    'family_name': 'Earhart',
    'email_address': 'Amelia.Earhart@example.com',
    'address': {
        'address_line_1': '500 Electric Ave',
        'address_line_2': 'Suite 600',
        'locality': 'New York',
        'administrative_district_level_1': 'NY',
        'postal_code': '10003',
        'country': 'US'
    },
    'phone_number': '+1-212-555-4240',
    'reference_id': 'YOUR_REFERENCE_ID',
    'note': 'a customer'
}

result = customers_api.create_customer(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Create Customers

Creates multiple [customer profiles](../../doc/models/customer.md) for a business.

This endpoint takes a map of individual create requests and returns a map of responses.

You must provide at least one of the following values in each create request:

- `given_name`
- `family_name`
- `company_name`
- `email_address`
- `phone_number`

```python
def bulk_create_customers(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Create Customers Request`](../../doc/models/bulk-create-customers-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Create Customers Response`](../../doc/models/bulk-create-customers-response.md).

## Example Usage

```python
body = {
    'customers': {
        '8bb76c4f-e35d-4c5b-90de-1194cd9179f0': {
            'given_name': 'Amelia',
            'family_name': 'Earhart',
            'email_address': 'Amelia.Earhart@example.com',
            'address': {
                'address_line_1': '500 Electric Ave',
                'address_line_2': 'Suite 600',
                'locality': 'New York',
                'administrative_district_level_1': 'NY',
                'postal_code': '10003',
                'country': 'US'
            },
            'phone_number': '+1-212-555-4240',
            'reference_id': 'YOUR_REFERENCE_ID',
            'note': 'a customer'
        },
        'd1689f23-b25d-4932-b2f0-aed00f5e2029': {
            'given_name': 'Marie',
            'family_name': 'Curie',
            'email_address': 'Marie.Curie@example.com',
            'address': {
                'address_line_1': '500 Electric Ave',
                'address_line_2': 'Suite 601',
                'locality': 'New York',
                'administrative_district_level_1': 'NY',
                'postal_code': '10003',
                'country': 'US'
            },
            'phone_number': '+1-212-444-4240',
            'reference_id': 'YOUR_REFERENCE_ID',
            'note': 'another customer'
        }
    }
}

result = customers_api.bulk_create_customers(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Delete Customers

Deletes multiple customer profiles.

The endpoint takes a list of customer IDs and returns a map of responses.

```python
def bulk_delete_customers(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Delete Customers Request`](../../doc/models/bulk-delete-customers-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Delete Customers Response`](../../doc/models/bulk-delete-customers-response.md).

## Example Usage

```python
body = {
    'customer_ids': [
        '8DDA5NZVBZFGAX0V3HPF81HHE0',
        'N18CPRVXR5214XPBBA6BZQWF3C',
        '2GYD7WNXF7BJZW1PMGNXZ3Y8M8'
    ]
}

result = customers_api.bulk_delete_customers(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Retrieve Customers

Retrieves multiple customer profiles.

This endpoint takes a list of customer IDs and returns a map of responses.

```python
def bulk_retrieve_customers(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Retrieve Customers Request`](../../doc/models/bulk-retrieve-customers-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Retrieve Customers Response`](../../doc/models/bulk-retrieve-customers-response.md).

## Example Usage

```python
body = {
    'customer_ids': [
        '8DDA5NZVBZFGAX0V3HPF81HHE0',
        'N18CPRVXR5214XPBBA6BZQWF3C',
        '2GYD7WNXF7BJZW1PMGNXZ3Y8M8'
    ]
}

result = customers_api.bulk_retrieve_customers(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Update Customers

Updates multiple customer profiles.

This endpoint takes a map of individual update requests and returns a map of responses.

You cannot use this endpoint to change cards on file. To make changes, use the [Cards API](../../doc/api/cards.md) or [Gift Cards API](../../doc/api/gift-cards.md).

```python
def bulk_update_customers(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Update Customers Request`](../../doc/models/bulk-update-customers-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Update Customers Response`](../../doc/models/bulk-update-customers-response.md).

## Example Usage

```python
body = {
    'customers': {
        '8DDA5NZVBZFGAX0V3HPF81HHE0': {
            'email_address': 'New.Amelia.Earhart@example.com',
            'phone_number': 'phone_number2',
            'note': 'updated customer note',
            'version': 2
        },
        'N18CPRVXR5214XPBBA6BZQWF3C': {
            'given_name': 'Marie',
            'family_name': 'Curie',
            'version': 0
        }
    }
}

result = customers_api.bulk_update_customers(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Customers

Searches the customer profiles associated with a Square account using one or more supported query filters.

Calling `SearchCustomers` without any explicit query filter returns all
customer profiles ordered alphabetically based on `given_name` and
`family_name`.

Under normal operating conditions, newly created or updated customer profiles become available
for the search operation in well under 30 seconds. Occasionally, propagation of the new or updated
profiles can take closer to one minute or longer, especially during network incidents and outages.

```python
def search_customers(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Customers Request`](../../doc/models/search-customers-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Search Customers Response`](../../doc/models/search-customers-response.md).

## Example Usage

```python
body = {
    'limit': 2,
    'query': {
        'filter': {
            'creation_source': {
                'values': [
                    'THIRD_PARTY'
                ],
                'rule': 'INCLUDE'
            },
            'created_at': {
                'start_at': '2018-01-01T00:00:00-00:00',
                'end_at': '2018-02-01T00:00:00-00:00'
            },
            'email_address': {
                'fuzzy': 'example.com'
            },
            'group_ids': {
                'all': [
                    '545AXB44B4XXWMVQ4W8SBT3HHF'
                ]
            }
        },
        'sort': {
            'field': 'CREATED_AT',
            'order': 'ASC'
        }
    }
}

result = customers_api.search_customers(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Customer

Deletes a customer profile from a business. This operation also unlinks any associated cards on file.

To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

```python
def delete_customer(self,
                   customer_id,
                   version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the customer to delete. |
| `version` | `long\|int` | Query, Optional | The current version of the customer profile.<br><br>As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Customer Response`](../../doc/models/delete-customer-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

result = customers_api.delete_customer(customer_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Customer

Returns details for a single customer.

```python
def retrieve_customer(self,
                     customer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the customer to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Customer Response`](../../doc/models/retrieve-customer-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

result = customers_api.retrieve_customer(customer_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Customer

Updates a customer profile. This endpoint supports sparse updates, so only new or changed fields are required in the request.
To add or update a field, specify the new value. To remove a field, specify `null`.

To update a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

You cannot use this endpoint to change cards on file. To make changes, use the [Cards API](../../doc/api/cards.md) or [Gift Cards API](../../doc/api/gift-cards.md).

```python
def update_customer(self,
                   customer_id,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the customer to update. |
| `body` | [`Update Customer Request`](../../doc/models/update-customer-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Customer Response`](../../doc/models/update-customer-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

body = {
    'email_address': 'New.Amelia.Earhart@example.com',
    'phone_number': 'phone_number2',
    'note': 'updated customer note',
    'version': 2
}

result = customers_api.update_customer(
    customer_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Customer Card

**This endpoint is deprecated.**

Adds a card on file to an existing customer.

As with charges, calls to `CreateCustomerCard` are idempotent. Multiple
calls with the same card nonce return the same card record that was created
with the provided nonce during the _first_ call.

```python
def create_customer_card(self,
                        customer_id,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The Square ID of the customer profile the card is linked to. |
| `body` | [`Create Customer Card Request`](../../doc/models/create-customer-card-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Customer Card Response`](../../doc/models/create-customer-card-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

body = {
    'card_nonce': 'YOUR_CARD_NONCE',
    'billing_address': {
        'address_line_1': '500 Electric Ave',
        'address_line_2': 'Suite 600',
        'locality': 'New York',
        'administrative_district_level_1': 'NY',
        'postal_code': '10003',
        'country': 'US'
    },
    'cardholder_name': 'Amelia Earhart'
}

result = customers_api.create_customer_card(
    customer_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Customer Card

**This endpoint is deprecated.**

Removes a card on file from a customer.

```python
def delete_customer_card(self,
                        customer_id,
                        card_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the customer that the card on file belongs to. |
| `card_id` | `str` | Template, Required | The ID of the card on file to delete. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Customer Card Response`](../../doc/models/delete-customer-card-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

card_id = 'card_id4'

result = customers_api.delete_customer_card(
    customer_id,
    card_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Remove Group From Customer

Removes a group membership from a customer.

The customer is identified by the `customer_id` value
and the customer group is identified by the `group_id` value.

```python
def remove_group_from_customer(self,
                              customer_id,
                              group_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the customer to remove from the group. |
| `group_id` | `str` | Template, Required | The ID of the customer group to remove the customer from. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Remove Group From Customer Response`](../../doc/models/remove-group-from-customer-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

group_id = 'group_id0'

result = customers_api.remove_group_from_customer(
    customer_id,
    group_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Add Group to Customer

Adds a group membership to a customer.

The customer is identified by the `customer_id` value
and the customer group is identified by the `group_id` value.

```python
def add_group_to_customer(self,
                         customer_id,
                         group_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the customer to add to a group. |
| `group_id` | `str` | Template, Required | The ID of the customer group to add the customer to. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Add Group to Customer Response`](../../doc/models/add-group-to-customer-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

group_id = 'group_id0'

result = customers_api.add_group_to_customer(
    customer_id,
    group_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

