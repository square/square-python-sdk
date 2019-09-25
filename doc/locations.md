# Locations

```python
locations_api = client.locations
```

## Class Name

`LocationsApi`

## Methods

* [List Locations](/doc/locations.md#list-locations)
* [Retrieve Location](/doc/locations.md#retrieve-location)
* [Update Location](/doc/locations.md#update-location)

## List Locations

Provides the details for all of a business's locations.

Most other Connect API endpoints have a required `location_id` path parameter.
The `id` field of the [`Location`](#type-location) objects returned by this
endpoint correspond to that `location_id` parameter.

```python
def list_locations(self)
```

### Response Type

[`List Locations Response`](/doc/models/list-locations-response.md)

### Example Usage

```python
result = locations_api.list_locations()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Location

Retrieves details of a location.

```python
def retrieve_location(self,
                     location_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the location to retrieve. |

### Response Type

[`Retrieve Location Response`](/doc/models/retrieve-location-response.md)

### Example Usage

```python
location_id = 'location_id4'

result = locations_api.retrieve_location(location_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Location

Updates the `Location` specified by the given ID.

```python
def update_location(self,
                   location_id,
                   body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the location to update. |
| `body` | [`Update Location Request`](/doc/models/update-location-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Location Response`](/doc/models/update-location-response.md)

### Example Usage

```python
location_id = 'location_id4'
body = {}

result = locations_api.update_location(location_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

