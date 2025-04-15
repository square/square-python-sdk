# Booking Custom Attributes

```python
booking_custom_attributes_api = client.booking_custom_attributes
```

## Class Name

`BookingCustomAttributesApi`

## Methods

* [List Booking Custom Attribute Definitions](../../doc/api/booking-custom-attributes.md#list-booking-custom-attribute-definitions)
* [Create Booking Custom Attribute Definition](../../doc/api/booking-custom-attributes.md#create-booking-custom-attribute-definition)
* [Delete Booking Custom Attribute Definition](../../doc/api/booking-custom-attributes.md#delete-booking-custom-attribute-definition)
* [Retrieve Booking Custom Attribute Definition](../../doc/api/booking-custom-attributes.md#retrieve-booking-custom-attribute-definition)
* [Update Booking Custom Attribute Definition](../../doc/api/booking-custom-attributes.md#update-booking-custom-attribute-definition)
* [Bulk Delete Booking Custom Attributes](../../doc/api/booking-custom-attributes.md#bulk-delete-booking-custom-attributes)
* [Bulk Upsert Booking Custom Attributes](../../doc/api/booking-custom-attributes.md#bulk-upsert-booking-custom-attributes)
* [List Booking Custom Attributes](../../doc/api/booking-custom-attributes.md#list-booking-custom-attributes)
* [Delete Booking Custom Attribute](../../doc/api/booking-custom-attributes.md#delete-booking-custom-attribute)
* [Retrieve Booking Custom Attribute](../../doc/api/booking-custom-attributes.md#retrieve-booking-custom-attribute)
* [Upsert Booking Custom Attribute](../../doc/api/booking-custom-attributes.md#upsert-booking-custom-attribute)


# List Booking Custom Attribute Definitions

Get all bookings custom attribute definitions.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

```python
def list_booking_custom_attribute_definitions(self,
                                             limit=None,
                                             cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `cursor` | `str` | Query, Optional | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Booking Custom Attribute Definitions Response`](../../doc/models/list-booking-custom-attribute-definitions-response.md).

## Example Usage

```python
result = booking_custom_attributes_api.list_booking_custom_attribute_definitions()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Booking Custom Attribute Definition

Creates a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def create_booking_custom_attribute_definition(self,
                                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Booking Custom Attribute Definition Request`](../../doc/models/create-booking-custom-attribute-definition-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Booking Custom Attribute Definition Response`](../../doc/models/create-booking-custom-attribute-definition-response.md).

## Example Usage

```python
body = {
    'custom_attribute_definition': {}
}

result = booking_custom_attributes_api.create_booking_custom_attribute_definition(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Booking Custom Attribute Definition

Deletes a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def delete_booking_custom_attribute_definition(self,
                                              key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Template, Required | The key of the custom attribute definition to delete. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Booking Custom Attribute Definition Response`](../../doc/models/delete-booking-custom-attribute-definition-response.md).

## Example Usage

```python
key = 'key0'

result = booking_custom_attributes_api.delete_booking_custom_attribute_definition(key)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Booking Custom Attribute Definition

Retrieves a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

```python
def retrieve_booking_custom_attribute_definition(self,
                                                key,
                                                version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Template, Required | The key of the custom attribute definition to retrieve. If the requesting application<br>is not the definition owner, you must use the qualified key. |
| `version` | `int` | Query, Optional | The current version of the custom attribute definition, which is used for strongly consistent<br>reads to guarantee that you receive the most up-to-date data. When included in the request,<br>Square returns the specified version or a higher version if one exists. If the specified version<br>is higher than the current version, Square returns a `BAD_REQUEST` error. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Booking Custom Attribute Definition Response`](../../doc/models/retrieve-booking-custom-attribute-definition-response.md).

## Example Usage

```python
key = 'key0'

result = booking_custom_attributes_api.retrieve_booking_custom_attribute_definition(key)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Booking Custom Attribute Definition

Updates a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def update_booking_custom_attribute_definition(self,
                                              key,
                                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Template, Required | The key of the custom attribute definition to update. |
| `body` | [`Update Booking Custom Attribute Definition Request`](../../doc/models/update-booking-custom-attribute-definition-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Booking Custom Attribute Definition Response`](../../doc/models/update-booking-custom-attribute-definition-response.md).

## Example Usage

```python
key = 'key0'

body = {
    'custom_attribute_definition': {}
}

result = booking_custom_attributes_api.update_booking_custom_attribute_definition(
    key,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Delete Booking Custom Attributes

Bulk deletes bookings custom attributes.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def bulk_delete_booking_custom_attributes(self,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Delete Booking Custom Attributes Request`](../../doc/models/bulk-delete-booking-custom-attributes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Delete Booking Custom Attributes Response`](../../doc/models/bulk-delete-booking-custom-attributes-response.md).

## Example Usage

```python
body = {
    'values': {
        'key0': {
            'booking_id': 'booking_id4',
            'key': 'key0'
        },
        'key1': {
            'booking_id': 'booking_id4',
            'key': 'key0'
        }
    }
}

result = booking_custom_attributes_api.bulk_delete_booking_custom_attributes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Upsert Booking Custom Attributes

Bulk upserts bookings custom attributes.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def bulk_upsert_booking_custom_attributes(self,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Upsert Booking Custom Attributes Request`](../../doc/models/bulk-upsert-booking-custom-attributes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Upsert Booking Custom Attributes Response`](../../doc/models/bulk-upsert-booking-custom-attributes-response.md).

## Example Usage

```python
body = {
    'values': {
        'key0': {
            'booking_id': 'booking_id4',
            'custom_attribute': {}
        },
        'key1': {
            'booking_id': 'booking_id4',
            'custom_attribute': {}
        }
    }
}

result = booking_custom_attributes_api.bulk_upsert_booking_custom_attributes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Booking Custom Attributes

Lists a booking's custom attributes.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

```python
def list_booking_custom_attributes(self,
                                  booking_id,
                                  limit=None,
                                  cursor=None,
                                  with_definitions=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `str` | Template, Required | The ID of the target [booking](entity:Booking). |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `cursor` | `str` | Query, Optional | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request. For more<br>information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `with_definitions` | `bool` | Query, Optional | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: `False` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Booking Custom Attributes Response`](../../doc/models/list-booking-custom-attributes-response.md).

## Example Usage

```python
booking_id = 'booking_id4'

with_definitions = False

result = booking_custom_attributes_api.list_booking_custom_attributes(
    booking_id,
    with_definitions=with_definitions
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Booking Custom Attribute

Deletes a bookings custom attribute.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def delete_booking_custom_attribute(self,
                                   booking_id,
                                   key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `str` | Template, Required | The ID of the target [booking](entity:Booking). |
| `key` | `str` | Template, Required | The key of the custom attribute to delete. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Booking Custom Attribute Response`](../../doc/models/delete-booking-custom-attribute-response.md).

## Example Usage

```python
booking_id = 'booking_id4'

key = 'key0'

result = booking_custom_attributes_api.delete_booking_custom_attribute(
    booking_id,
    key
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Booking Custom Attribute

Retrieves a bookings custom attribute.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

```python
def retrieve_booking_custom_attribute(self,
                                     booking_id,
                                     key,
                                     with_definition=False,
                                     version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `str` | Template, Required | The ID of the target [booking](entity:Booking). |
| `key` | `str` | Template, Required | The key of the custom attribute to retrieve. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| `with_definition` | `bool` | Query, Optional | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of<br>the custom attribute. Set this parameter to `true` to get the name and description of the custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: `False` |
| `version` | `int` | Query, Optional | The current version of the custom attribute, which is used for strongly consistent reads to<br>guarantee that you receive the most up-to-date data. When included in the request, Square<br>returns the specified version or a higher version if one exists. If the specified version is<br>higher than the current version, Square returns a `BAD_REQUEST` error. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Booking Custom Attribute Response`](../../doc/models/retrieve-booking-custom-attribute-response.md).

## Example Usage

```python
booking_id = 'booking_id4'

key = 'key0'

with_definition = False

result = booking_custom_attributes_api.retrieve_booking_custom_attribute(
    booking_id,
    key,
    with_definition=with_definition
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upsert Booking Custom Attribute

Upserts a bookings custom attribute.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def upsert_booking_custom_attribute(self,
                                   booking_id,
                                   key,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `str` | Template, Required | The ID of the target [booking](entity:Booking). |
| `key` | `str` | Template, Required | The key of the custom attribute to create or update. This key must match the `key` of a<br>custom attribute definition in the Square seller account. If the requesting application is not<br>the definition owner, you must use the qualified key. |
| `body` | [`Upsert Booking Custom Attribute Request`](../../doc/models/upsert-booking-custom-attribute-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Upsert Booking Custom Attribute Response`](../../doc/models/upsert-booking-custom-attribute-response.md).

## Example Usage

```python
booking_id = 'booking_id4'

key = 'key0'

body = {
    'custom_attribute': {}
}

result = booking_custom_attributes_api.upsert_booking_custom_attribute(
    booking_id,
    key,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

