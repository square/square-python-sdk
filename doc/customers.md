# Customers

```python
customers_api = client.customers
```

## Class Name

`CustomersApi`

## Methods

* [List Customers](/doc/customers.md#list-customers)
* [Create Customer](/doc/customers.md#create-customer)
* [Search Customers](/doc/customers.md#search-customers)
* [Delete Customer](/doc/customers.md#delete-customer)
* [Retrieve Customer](/doc/customers.md#retrieve-customer)
* [Update Customer](/doc/customers.md#update-customer)
* [Create Customer Card](/doc/customers.md#create-customer-card)
* [Delete Customer Card](/doc/customers.md#delete-customer-card)

## List Customers

Lists a business's customers.

```python
def list_customers(self,
                  cursor=None,
                  sort_field=None,
                  sort_order=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |
| `sort_field` | [`str (Customer Sort Field)`](/doc/models/customer-sort-field.md) | Query, Optional | Indicates how Customers should be sorted. Default: `DEFAULT`. |
| `sort_order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Query, Optional | Indicates whether Customers should be sorted in ascending (`ASC`) or<br>descending (`DESC`) order. Default: `ASC`. |

### Response Type

[`List Customers Response`](/doc/models/list-customers-response.md)

### Example Usage

```python
result = customers_api.list_customers()

if result.is_success():
    print(result.data)
elif result.is_error():
    print(result.errors)
```

## Create Customer

Creates a new customer for a business, which can have associated cards on file.

You must provide __at least one__ of the following values in your request to this
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

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Customer Request`](/doc/models/create-customer-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Customer Response`](/doc/models/create-customer-response.md)

### Example Usage

```python
body = {}
body['given_name'] = 'Amelia'
body['family_name'] = 'Earhart'
body['email_address'] = 'Amelia.Earhart@example.com'
body['address'] = {}
body['address']['address_line_1'] = '500 Electric Ave'
body['address']['address_line_2'] = 'Suite 600'
body['address']['locality'] = 'New York'
body['address']['administrative_district_level_1'] = 'NY'
body['address']['postal_code'] = '10003'
body['address']['country'] = Country.US
body['phone_number'] = '1-212-555-4240'
body['reference_id'] = 'YOUR_REFERENCE_ID'
body['note'] = 'a customer'

result = customers_api.create_customer(body)

if result.is_success():
    print(result.data)
elif result.is_error():
    print(result.errors)
```

## Search Customers

Searches the customer profiles associated with a Square account.
Calling SearchCustomers without an explicit query parameter returns all
customer profiles ordered alphabetically based on `given_name` and
`family_name`.

```python
def search_customers(self,
                    body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Customers Request`](/doc/models/search-customers-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Customers Response`](/doc/models/search-customers-response.md)

### Example Usage

```python
body = {}
body['limit'] = 2
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['creation_source'] = {}
body['query']['filter']['creation_source']['values'] = [CustomerCreationSource.THIRD_PARTY]
body['query']['filter']['creation_source']['rule'] = CustomerInclusionExclusion.INCLUDE
body['query']['filter']['created_at'] = {}
body['query']['filter']['created_at']['start_at'] = '2018-01-01T00:00:00-00:00'
body['query']['filter']['created_at']['end_at'] = '2018-02-01T00:00:00-00:00'
body['query']['sort'] = {}
body['query']['sort']['field'] = CustomerSortField.CREATED_AT
body['query']['sort']['order'] = SortOrder.ASC

result = customers_api.search_customers(body)

if result.is_success():
    print(result.data)
elif result.is_error():
    print(result.errors)
```

## Delete Customer

Deletes a customer from a business, along with any linked cards on file. When two profiles
are merged into a single profile, that profile is assigned a new `customer_id`. You must use the
new `customer_id` to delete merged profiles.

```python
def delete_customer(self,
                   customer_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | The ID of the customer to delete. |

### Response Type

[`Delete Customer Response`](/doc/models/delete-customer-response.md)

### Example Usage

```python
customer_id = 'customer_id8'

result = customers_api.delete_customer(customer_id)

if result.is_success():
    print(result.data)
elif result.is_error():
    print(result.errors)
```

## Retrieve Customer

Returns details for a single customer.

```python
def retrieve_customer(self,
                     customer_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | The ID of the customer to retrieve. |

### Response Type

[`Retrieve Customer Response`](/doc/models/retrieve-customer-response.md)

### Example Usage

```python
customer_id = 'customer_id8'

result = customers_api.retrieve_customer(customer_id)

if result.is_success():
    print(result.data)
elif result.is_error():
    print(result.errors)
```

## Update Customer

Updates the details of an existing customer. When two profiles are merged
into a single profile, that profile is assigned a new `customer_id`. You must use
the new `customer_id` to update merged profiles.

You cannot edit a customer's cards on file with this endpoint. To make changes
to a card on file, you must delete the existing card on file with the
[DeleteCustomerCard](/doc/customers.md#deletecustomercard) endpoint, then
create a new one with the
[CreateCustomerCard](/doc/customers.md#createcustomercard) endpoint.

```python
def update_customer(self,
                   customer_id,
                   body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | The ID of the customer to update. |
| `body` | [`Update Customer Request`](/doc/models/update-customer-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Customer Response`](/doc/models/update-customer-response.md)

### Example Usage

```python
customer_id = 'customer_id8'
body = {}
body['email_address'] = 'New.Amelia.Earhart@example.com'
body['phone_number'] = ''
body['note'] = 'updated customer note'

result = customers_api.update_customer(customer_id, body)

if result.is_success():
    print(result.data)
elif result.is_error():
    print(result.errors)
```

## Create Customer Card

Adds a card on file to an existing customer.

As with charges, calls to `CreateCustomerCard` are idempotent. Multiple
calls with the same card nonce return the same card record that was created
with the provided nonce during the _first_ call.

Cards on file are automatically updated on a monthly basis to confirm they
are still valid and can be charged.

```python
def create_customer_card(self,
                        customer_id,
                        body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | The Square ID of the customer profile the card is linked to. |
| `body` | [`Create Customer Card Request`](/doc/models/create-customer-card-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Customer Card Response`](/doc/models/create-customer-card-response.md)

### Example Usage

```python
customer_id = 'customer_id8'
body = {}
body['card_nonce'] = 'YOUR_CARD_NONCE'
body['billing_address'] = {}
body['billing_address']['address_line_1'] = '500 Electric Ave'
body['billing_address']['address_line_2'] = 'Suite 600'
body['billing_address']['locality'] = 'New York'
body['billing_address']['administrative_district_level_1'] = 'NY'
body['billing_address']['postal_code'] = '10003'
body['billing_address']['country'] = Country.US
body['cardholder_name'] = 'Amelia Earhart'

result = customers_api.create_customer_card(customer_id, body)

if result.is_success():
    print(result.data)
elif result.is_error():
    print(result.errors)
```

## Delete Customer Card

Removes a card on file from a customer.

```python
def delete_customer_card(self,
                        customer_id,
                        card_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | The ID of the customer that the card on file belongs to. |
| `card_id` | `string` | Template, Required | The ID of the card on file to delete. |

### Response Type

[`Delete Customer Card Response`](/doc/models/delete-customer-card-response.md)

### Example Usage

```python
customer_id = 'customer_id8'
card_id = 'card_id4'

result = customers_api.delete_customer_card(customer_id, card_id)

if result.is_success():
    print(result.data)
elif result.is_error():
    print(result.errors)
```

