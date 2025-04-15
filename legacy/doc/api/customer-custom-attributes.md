# Customer Custom Attributes

```python
customer_custom_attributes_api = client.customer_custom_attributes
```

## Class Name

`CustomerCustomAttributesApi`

## Methods

* [List Customer Custom Attribute Definitions](../../doc/api/customer-custom-attributes.md#list-customer-custom-attribute-definitions)
* [Create Customer Custom Attribute Definition](../../doc/api/customer-custom-attributes.md#create-customer-custom-attribute-definition)
* [Delete Customer Custom Attribute Definition](../../doc/api/customer-custom-attributes.md#delete-customer-custom-attribute-definition)
* [Retrieve Customer Custom Attribute Definition](../../doc/api/customer-custom-attributes.md#retrieve-customer-custom-attribute-definition)
* [Update Customer Custom Attribute Definition](../../doc/api/customer-custom-attributes.md#update-customer-custom-attribute-definition)
* [Bulk Upsert Customer Custom Attributes](../../doc/api/customer-custom-attributes.md#bulk-upsert-customer-custom-attributes)
* [List Customer Custom Attributes](../../doc/api/customer-custom-attributes.md#list-customer-custom-attributes)
* [Delete Customer Custom Attribute](../../doc/api/customer-custom-attributes.md#delete-customer-custom-attribute)
* [Retrieve Customer Custom Attribute](../../doc/api/customer-custom-attributes.md#retrieve-customer-custom-attribute)
* [Upsert Customer Custom Attribute](../../doc/api/customer-custom-attributes.md#upsert-customer-custom-attribute)


# List Customer Custom Attribute Definitions

Lists the customer-related [custom attribute definitions](../../doc/models/custom-attribute-definition.md) that belong to a Square seller account.

When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that
seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

```python
def list_customer_custom_attribute_definitions(self,
                                              limit=None,
                                              cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `cursor` | `str` | Query, Optional | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Customer Custom Attribute Definitions Response`](../../doc/models/list-customer-custom-attribute-definitions-response.md).

## Example Usage

```python
result = customer_custom_attributes_api.list_customer_custom_attribute_definitions()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Customer Custom Attribute Definition

Creates a customer-related [custom attribute definition](../../doc/models/custom-attribute-definition.md) for a Square seller account.
Use this endpoint to define a custom attribute that can be associated with customer profiles.

A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
for a custom attribute. After the definition is created, you can call
[UpsertCustomerCustomAttribute](../../doc/api/customer-custom-attributes.md#upsert-customer-custom-attribute) or
[BulkUpsertCustomerCustomAttributes](../../doc/api/customer-custom-attributes.md#bulk-upsert-customer-custom-attributes)
to set the custom attribute for customer profiles in the seller's Customer Directory.

Sellers can view all custom attributes in exported customer data, including those set to
`VISIBILITY_HIDDEN`.

```python
def create_customer_custom_attribute_definition(self,
                                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Customer Custom Attribute Definition Request`](../../doc/models/create-customer-custom-attribute-definition-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Customer Custom Attribute Definition Response`](../../doc/models/create-customer-custom-attribute-definition-response.md).

## Example Usage

```python
body = {
    'custom_attribute_definition': {
        'key': 'favoritemovie',
        'name': 'Favorite Movie',
        'description': 'The favorite movie of the customer.',
        'visibility': 'VISIBILITY_HIDDEN'
    }
}

result = customer_custom_attributes_api.create_customer_custom_attribute_definition(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Customer Custom Attribute Definition

Deletes a customer-related [custom attribute definition](../../doc/models/custom-attribute-definition.md) from a Square seller account.

Deleting a custom attribute definition also deletes the corresponding custom attribute from
all customer profiles in the seller's Customer Directory.

Only the definition owner can delete a custom attribute definition.

```python
def delete_customer_custom_attribute_definition(self,
                                               key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Template, Required | The key of the custom attribute definition to delete. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Customer Custom Attribute Definition Response`](../../doc/models/delete-customer-custom-attribute-definition-response.md).

## Example Usage

```python
key = 'key0'

result = customer_custom_attributes_api.delete_customer_custom_attribute_definition(key)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Customer Custom Attribute Definition

Retrieves a customer-related [custom attribute definition](../../doc/models/custom-attribute-definition.md) from a Square seller account.

To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

```python
def retrieve_customer_custom_attribute_definition(self,
                                                 key,
                                                 version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Template, Required | The key of the custom attribute definition to retrieve. If the requesting application<br>is not the definition owner, you must use the qualified key. |
| `version` | `int` | Query, Optional | The current version of the custom attribute definition, which is used for strongly consistent<br>reads to guarantee that you receive the most up-to-date data. When included in the request,<br>Square returns the specified version or a higher version if one exists. If the specified version<br>is higher than the current version, Square returns a `BAD_REQUEST` error. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Customer Custom Attribute Definition Response`](../../doc/models/retrieve-customer-custom-attribute-definition-response.md).

## Example Usage

```python
key = 'key0'

result = customer_custom_attributes_api.retrieve_customer_custom_attribute_definition(key)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Customer Custom Attribute Definition

Updates a customer-related [custom attribute definition](../../doc/models/custom-attribute-definition.md) for a Square seller account.

Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
`schema` for a `Selection` data type.

Only the definition owner can update a custom attribute definition. Note that sellers can view
all custom attributes in exported customer data, including those set to `VISIBILITY_HIDDEN`.

```python
def update_customer_custom_attribute_definition(self,
                                               key,
                                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Template, Required | The key of the custom attribute definition to update. |
| `body` | [`Update Customer Custom Attribute Definition Request`](../../doc/models/update-customer-custom-attribute-definition-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Customer Custom Attribute Definition Response`](../../doc/models/update-customer-custom-attribute-definition-response.md).

## Example Usage

```python
key = 'key0'

body = {
    'custom_attribute_definition': {
        'description': 'Update the description as desired.',
        'visibility': 'VISIBILITY_READ_ONLY'
    }
}

result = customer_custom_attributes_api.update_customer_custom_attribute_definition(
    key,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Upsert Customer Custom Attributes

Creates or updates [custom attributes](../../doc/models/custom-attribute.md) for customer profiles as a bulk operation.

Use this endpoint to set the value of one or more custom attributes for one or more customer profiles.
A custom attribute is based on a custom attribute definition in a Square seller account, which is
created using the [CreateCustomerCustomAttributeDefinition](../../doc/api/customer-custom-attributes.md#create-customer-custom-attribute-definition) endpoint.

This `BulkUpsertCustomerCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides a customer ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

```python
def bulk_upsert_customer_custom_attributes(self,
                                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Upsert Customer Custom Attributes Request`](../../doc/models/bulk-upsert-customer-custom-attributes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Upsert Customer Custom Attributes Response`](../../doc/models/bulk-upsert-customer-custom-attributes-response.md).

## Example Usage

```python
body = {
    'values': {
        'key0': {
            'customer_id': 'customer_id8',
            'custom_attribute': {}
        },
        'key1': {
            'customer_id': 'customer_id8',
            'custom_attribute': {}
        }
    }
}

result = customer_custom_attributes_api.bulk_upsert_customer_custom_attributes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Customer Custom Attributes

Lists the [custom attributes](../../doc/models/custom-attribute.md) associated with a customer profile.

You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.

When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

```python
def list_customer_custom_attributes(self,
                                   customer_id,
                                   limit=None,
                                   cursor=None,
                                   with_definitions=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the target [customer profile](entity:Customer). |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `cursor` | `str` | Query, Optional | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request. For more<br>information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `with_definitions` | `bool` | Query, Optional | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: `False` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Customer Custom Attributes Response`](../../doc/models/list-customer-custom-attributes-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

with_definitions = False

result = customer_custom_attributes_api.list_customer_custom_attributes(
    customer_id,
    with_definitions=with_definitions
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Customer Custom Attribute

Deletes a [custom attribute](../../doc/models/custom-attribute.md) associated with a customer profile.

To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

```python
def delete_customer_custom_attribute(self,
                                    customer_id,
                                    key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the target [customer profile](entity:Customer). |
| `key` | `str` | Template, Required | The key of the custom attribute to delete. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Customer Custom Attribute Response`](../../doc/models/delete-customer-custom-attribute-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

key = 'key0'

result = customer_custom_attributes_api.delete_customer_custom_attribute(
    customer_id,
    key
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Customer Custom Attribute

Retrieves a [custom attribute](../../doc/models/custom-attribute.md) associated with a customer profile.

You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.

To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

```python
def retrieve_customer_custom_attribute(self,
                                      customer_id,
                                      key,
                                      with_definition=False,
                                      version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the target [customer profile](entity:Customer). |
| `key` | `str` | Template, Required | The key of the custom attribute to retrieve. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| `with_definition` | `bool` | Query, Optional | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of<br>the custom attribute. Set this parameter to `true` to get the name and description of the custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: `False` |
| `version` | `int` | Query, Optional | The current version of the custom attribute, which is used for strongly consistent reads to<br>guarantee that you receive the most up-to-date data. When included in the request, Square<br>returns the specified version or a higher version if one exists. If the specified version is<br>higher than the current version, Square returns a `BAD_REQUEST` error. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Customer Custom Attribute Response`](../../doc/models/retrieve-customer-custom-attribute-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

key = 'key0'

with_definition = False

result = customer_custom_attributes_api.retrieve_customer_custom_attribute(
    customer_id,
    key,
    with_definition=with_definition
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upsert Customer Custom Attribute

Creates or updates a [custom attribute](../../doc/models/custom-attribute.md) for a customer profile.

Use this endpoint to set the value of a custom attribute for a specified customer profile.
A custom attribute is based on a custom attribute definition in a Square seller account, which
is created using the [CreateCustomerCustomAttributeDefinition](../../doc/api/customer-custom-attributes.md#create-customer-custom-attribute-definition) endpoint.

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

```python
def upsert_customer_custom_attribute(self,
                                    customer_id,
                                    key,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Template, Required | The ID of the target [customer profile](entity:Customer). |
| `key` | `str` | Template, Required | The key of the custom attribute to create or update. This key must match the `key` of a<br>custom attribute definition in the Square seller account. If the requesting application is not<br>the definition owner, you must use the qualified key. |
| `body` | [`Upsert Customer Custom Attribute Request`](../../doc/models/upsert-customer-custom-attribute-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Upsert Customer Custom Attribute Response`](../../doc/models/upsert-customer-custom-attribute-response.md).

## Example Usage

```python
customer_id = 'customer_id8'

key = 'key0'

body = {
    'custom_attribute': {}
}

result = customer_custom_attributes_api.upsert_customer_custom_attribute(
    customer_id,
    key,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

