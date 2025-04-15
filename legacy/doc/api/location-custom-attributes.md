# Location Custom Attributes

```python
location_custom_attributes_api = client.location_custom_attributes
```

## Class Name

`LocationCustomAttributesApi`

## Methods

* [List Location Custom Attribute Definitions](../../doc/api/location-custom-attributes.md#list-location-custom-attribute-definitions)
* [Create Location Custom Attribute Definition](../../doc/api/location-custom-attributes.md#create-location-custom-attribute-definition)
* [Delete Location Custom Attribute Definition](../../doc/api/location-custom-attributes.md#delete-location-custom-attribute-definition)
* [Retrieve Location Custom Attribute Definition](../../doc/api/location-custom-attributes.md#retrieve-location-custom-attribute-definition)
* [Update Location Custom Attribute Definition](../../doc/api/location-custom-attributes.md#update-location-custom-attribute-definition)
* [Bulk Delete Location Custom Attributes](../../doc/api/location-custom-attributes.md#bulk-delete-location-custom-attributes)
* [Bulk Upsert Location Custom Attributes](../../doc/api/location-custom-attributes.md#bulk-upsert-location-custom-attributes)
* [List Location Custom Attributes](../../doc/api/location-custom-attributes.md#list-location-custom-attributes)
* [Delete Location Custom Attribute](../../doc/api/location-custom-attributes.md#delete-location-custom-attribute)
* [Retrieve Location Custom Attribute](../../doc/api/location-custom-attributes.md#retrieve-location-custom-attribute)
* [Upsert Location Custom Attribute](../../doc/api/location-custom-attributes.md#upsert-location-custom-attribute)


# List Location Custom Attribute Definitions

Lists the location-related [custom attribute definitions](../../doc/models/custom-attribute-definition.md) that belong to a Square seller account.
When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

```python
def list_location_custom_attribute_definitions(self,
                                              visibility_filter=None,
                                              limit=None,
                                              cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `visibility_filter` | [`str (Visibility Filter)`](../../doc/models/visibility-filter.md) | Query, Optional | Filters the `CustomAttributeDefinition` results by their `visibility` values. |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `cursor` | `str` | Query, Optional | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Location Custom Attribute Definitions Response`](../../doc/models/list-location-custom-attribute-definitions-response.md).

## Example Usage

```python
result = location_custom_attributes_api.list_location_custom_attribute_definitions()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Location Custom Attribute Definition

Creates a location-related [custom attribute definition](../../doc/models/custom-attribute-definition.md) for a Square seller account.
Use this endpoint to define a custom attribute that can be associated with locations.
A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
for a custom attribute. After the definition is created, you can call
[UpsertLocationCustomAttribute](../../doc/api/location-custom-attributes.md#upsert-location-custom-attribute) or
[BulkUpsertLocationCustomAttributes](../../doc/api/location-custom-attributes.md#bulk-upsert-location-custom-attributes)
to set the custom attribute for locations.

```python
def create_location_custom_attribute_definition(self,
                                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Location Custom Attribute Definition Request`](../../doc/models/create-location-custom-attribute-definition-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Location Custom Attribute Definition Response`](../../doc/models/create-location-custom-attribute-definition-response.md).

## Example Usage

```python
body = {
    'custom_attribute_definition': {
        'key': 'bestseller',
        'name': 'Bestseller',
        'description': 'Bestselling item at location',
        'visibility': 'VISIBILITY_READ_WRITE_VALUES'
    }
}

result = location_custom_attributes_api.create_location_custom_attribute_definition(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Location Custom Attribute Definition

Deletes a location-related [custom attribute definition](../../doc/models/custom-attribute-definition.md) from a Square seller account.
Deleting a custom attribute definition also deletes the corresponding custom attribute from
all locations.
Only the definition owner can delete a custom attribute definition.

```python
def delete_location_custom_attribute_definition(self,
                                               key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Template, Required | The key of the custom attribute definition to delete. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Location Custom Attribute Definition Response`](../../doc/models/delete-location-custom-attribute-definition-response.md).

## Example Usage

```python
key = 'key0'

result = location_custom_attributes_api.delete_location_custom_attribute_definition(key)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Location Custom Attribute Definition

Retrieves a location-related [custom attribute definition](../../doc/models/custom-attribute-definition.md) from a Square seller account.
To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

```python
def retrieve_location_custom_attribute_definition(self,
                                                 key,
                                                 version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Template, Required | The key of the custom attribute definition to retrieve. If the requesting application<br>is not the definition owner, you must use the qualified key. |
| `version` | `int` | Query, Optional | The current version of the custom attribute definition, which is used for strongly consistent<br>reads to guarantee that you receive the most up-to-date data. When included in the request,<br>Square returns the specified version or a higher version if one exists. If the specified version<br>is higher than the current version, Square returns a `BAD_REQUEST` error. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Location Custom Attribute Definition Response`](../../doc/models/retrieve-location-custom-attribute-definition-response.md).

## Example Usage

```python
key = 'key0'

result = location_custom_attributes_api.retrieve_location_custom_attribute_definition(key)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Location Custom Attribute Definition

Updates a location-related [custom attribute definition](../../doc/models/custom-attribute-definition.md) for a Square seller account.
Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
`schema` for a `Selection` data type.
Only the definition owner can update a custom attribute definition.

```python
def update_location_custom_attribute_definition(self,
                                               key,
                                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Template, Required | The key of the custom attribute definition to update. |
| `body` | [`Update Location Custom Attribute Definition Request`](../../doc/models/update-location-custom-attribute-definition-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Location Custom Attribute Definition Response`](../../doc/models/update-location-custom-attribute-definition-response.md).

## Example Usage

```python
key = 'key0'

body = {
    'custom_attribute_definition': {
        'description': 'Update the description as desired.',
        'visibility': 'VISIBILITY_READ_ONLY'
    }
}

result = location_custom_attributes_api.update_location_custom_attribute_definition(
    key,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Delete Location Custom Attributes

Deletes [custom attributes](../../doc/models/custom-attribute.md) for locations as a bulk operation.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.

```python
def bulk_delete_location_custom_attributes(self,
                                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Delete Location Custom Attributes Request`](../../doc/models/bulk-delete-location-custom-attributes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Delete Location Custom Attributes Response`](../../doc/models/bulk-delete-location-custom-attributes-response.md).

## Example Usage

```python
body = {
    'values': {
        'id1': {},
        'id2': {},
        'id3': {}
    }
}

result = location_custom_attributes_api.bulk_delete_location_custom_attributes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Upsert Location Custom Attributes

Creates or updates [custom attributes](../../doc/models/custom-attribute.md) for locations as a bulk operation.
Use this endpoint to set the value of one or more custom attributes for one or more locations.
A custom attribute is based on a custom attribute definition in a Square seller account, which is
created using the [CreateLocationCustomAttributeDefinition](../../doc/api/location-custom-attributes.md#create-location-custom-attribute-definition) endpoint.
This `BulkUpsertLocationCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides a location ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.

```python
def bulk_upsert_location_custom_attributes(self,
                                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Upsert Location Custom Attributes Request`](../../doc/models/bulk-upsert-location-custom-attributes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Upsert Location Custom Attributes Response`](../../doc/models/bulk-upsert-location-custom-attributes-response.md).

## Example Usage

```python
body = {
    'values': {
        'key0': {
            'location_id': 'location_id4',
            'custom_attribute': {}
        },
        'key1': {
            'location_id': 'location_id4',
            'custom_attribute': {}
        }
    }
}

result = location_custom_attributes_api.bulk_upsert_location_custom_attributes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Location Custom Attributes

Lists the [custom attributes](../../doc/models/custom-attribute.md) associated with a location.
You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.
When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

```python
def list_location_custom_attributes(self,
                                   location_id,
                                   visibility_filter=None,
                                   limit=None,
                                   cursor=None,
                                   with_definitions=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Template, Required | The ID of the target [location](entity:Location). |
| `visibility_filter` | [`str (Visibility Filter)`](../../doc/models/visibility-filter.md) | Query, Optional | Filters the `CustomAttributeDefinition` results by their `visibility` values. |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `cursor` | `str` | Query, Optional | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request. For more<br>information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `with_definitions` | `bool` | Query, Optional | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: `False` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Location Custom Attributes Response`](../../doc/models/list-location-custom-attributes-response.md).

## Example Usage

```python
location_id = 'location_id4'

with_definitions = False

result = location_custom_attributes_api.list_location_custom_attributes(
    location_id,
    with_definitions=with_definitions
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Location Custom Attribute

Deletes a [custom attribute](../../doc/models/custom-attribute.md) associated with a location.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.

```python
def delete_location_custom_attribute(self,
                                    location_id,
                                    key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Template, Required | The ID of the target [location](entity:Location). |
| `key` | `str` | Template, Required | The key of the custom attribute to delete. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Location Custom Attribute Response`](../../doc/models/delete-location-custom-attribute-response.md).

## Example Usage

```python
location_id = 'location_id4'

key = 'key0'

result = location_custom_attributes_api.delete_location_custom_attribute(
    location_id,
    key
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Location Custom Attribute

Retrieves a [custom attribute](../../doc/models/custom-attribute.md) associated with a location.
You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.
To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

```python
def retrieve_location_custom_attribute(self,
                                      location_id,
                                      key,
                                      with_definition=False,
                                      version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Template, Required | The ID of the target [location](entity:Location). |
| `key` | `str` | Template, Required | The key of the custom attribute to retrieve. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| `with_definition` | `bool` | Query, Optional | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of<br>the custom attribute. Set this parameter to `true` to get the name and description of the custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: `False` |
| `version` | `int` | Query, Optional | The current version of the custom attribute, which is used for strongly consistent reads to<br>guarantee that you receive the most up-to-date data. When included in the request, Square<br>returns the specified version or a higher version if one exists. If the specified version is<br>higher than the current version, Square returns a `BAD_REQUEST` error. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Location Custom Attribute Response`](../../doc/models/retrieve-location-custom-attribute-response.md).

## Example Usage

```python
location_id = 'location_id4'

key = 'key0'

with_definition = False

result = location_custom_attributes_api.retrieve_location_custom_attribute(
    location_id,
    key,
    with_definition=with_definition
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upsert Location Custom Attribute

Creates or updates a [custom attribute](../../doc/models/custom-attribute.md) for a location.
Use this endpoint to set the value of a custom attribute for a specified location.
A custom attribute is based on a custom attribute definition in a Square seller account, which
is created using the [CreateLocationCustomAttributeDefinition](../../doc/api/location-custom-attributes.md#create-location-custom-attribute-definition) endpoint.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.

```python
def upsert_location_custom_attribute(self,
                                    location_id,
                                    key,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Template, Required | The ID of the target [location](entity:Location). |
| `key` | `str` | Template, Required | The key of the custom attribute to create or update. This key must match the `key` of a<br>custom attribute definition in the Square seller account. If the requesting application is not<br>the definition owner, you must use the qualified key. |
| `body` | [`Upsert Location Custom Attribute Request`](../../doc/models/upsert-location-custom-attribute-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Upsert Location Custom Attribute Response`](../../doc/models/upsert-location-custom-attribute-response.md).

## Example Usage

```python
location_id = 'location_id4'

key = 'key0'

body = {
    'custom_attribute': {}
}

result = location_custom_attributes_api.upsert_location_custom_attribute(
    location_id,
    key,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

