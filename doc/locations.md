# Locations

```python
locations_api = client.locations
```

## Class Name

`LocationsApi`

## Methods

* [List Locations](/doc/locations.md#list-locations)
* [Create Location](/doc/locations.md#create-location)
* [Retrieve Location](/doc/locations.md#retrieve-location)
* [Update Location](/doc/locations.md#update-location)

## List Locations

Provides information of all locations of a business.

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

## Create Location

Creates a location.
For more information about locations, see [Locations API Overview](https://developer.squareup.com/docs/locations-api).

```python
def create_location(self,
                   body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Location Request`](/doc/models/create-location-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Location Response`](/doc/models/create-location-response.md)

### Example Usage

```python
body = {}
body['location'] = {}
body['location']['id'] = 'id0'
body['location']['name'] = 'New location name'
body['location']['address'] = {}
body['location']['address']['address_line_1'] = '1234 Peachtree St. NE'
body['location']['address']['address_line_2'] = 'address_line_26'
body['location']['address']['address_line_3'] = 'address_line_32'
body['location']['address']['locality'] = 'Atlanta'
body['location']['address']['sublocality'] = 'sublocality6'
body['location']['address']['administrative_district_level_1'] = 'GA'
body['location']['address']['postal_code'] = '30309'
body['location']['timezone'] = 'timezone0'
body['location']['capabilities'] = ['CREDIT_CARD_PROCESSING', 'CREDIT_CARD_PROCESSING', 'CREDIT_CARD_PROCESSING']
body['location']['description'] = 'My new location.'
body['location']['facebook_url'] = 'null'

result = locations_api.create_location(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Location

Retrieves details of a location. You can specify "main" 
as the location ID to retrieve details of the 
main location. For more information, 
see [Locations API Overview](https://developer.squareup.com/docs/docs/locations-api).

```python
def retrieve_location(self,
                     location_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Template, Required | The ID of the location to retrieve. If you specify the string "main",<br>then the endpoint returns the main location. |

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

Updates a location.

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
body['location'] = {}
body['location']['id'] = 'id0'
body['location']['name'] = 'Updated nickname'
body['location']['address'] = {}
body['location']['address']['address_line_1'] = '1234 Peachtree St. NE'
body['location']['address']['address_line_2'] = 'address_line_26'
body['location']['address']['address_line_3'] = 'address_line_32'
body['location']['address']['locality'] = 'Atlanta'
body['location']['address']['sublocality'] = 'sublocality6'
body['location']['address']['administrative_district_level_1'] = 'GA'
body['location']['address']['postal_code'] = '30309'
body['location']['timezone'] = 'timezone0'
body['location']['capabilities'] = ['CREDIT_CARD_PROCESSING', 'CREDIT_CARD_PROCESSING', 'CREDIT_CARD_PROCESSING']
body['location']['business_hours'] = {}
body['location']['business_hours']['periods'] = []

body['location']['business_hours']['periods'].append({})
body['location']['business_hours']['periods'][0]['day_of_week'] = 'MON'
body['location']['business_hours']['periods'][0]['start_local_time'] = '09:00'
body['location']['business_hours']['periods'][0]['end_local_time'] = '17:00'

body['location']['description'] = 'Updated description'
body['location']['twitter_username'] = 'twitter'
body['location']['instagram_username'] = 'instagram'
body['location']['facebook_url'] = 'null'

result = locations_api.update_location(location_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

