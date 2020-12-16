# Bookings

```python
bookings_api = client.bookings
```

## Class Name

`BookingsApi`

## Methods

* [Create Booking](/doc/api/bookings.md#create-booking)
* [Search Availability](/doc/api/bookings.md#search-availability)
* [Retrieve Business Booking Profile](/doc/api/bookings.md#retrieve-business-booking-profile)
* [List Team Member Booking Profiles](/doc/api/bookings.md#list-team-member-booking-profiles)
* [Retrieve Team Member Booking Profile](/doc/api/bookings.md#retrieve-team-member-booking-profile)
* [Retrieve Booking](/doc/api/bookings.md#retrieve-booking)
* [Update Booking](/doc/api/bookings.md#update-booking)
* [Cancel Booking](/doc/api/bookings.md#cancel-booking)


# Create Booking

Creates a booking.

```python
def create_booking(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Booking Request`](/doc/models/create-booking-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Create Booking Response`](/doc/models/create-booking-response.md)

## Example Usage

```python
body = {}
body['idempotency_key'] = 'idempotency_key2'
body['booking'] = {}
body['booking']['id'] = 'id8'
body['booking']['version'] = 148
body['booking']['status'] = 'ACCEPTED'
body['booking']['created_at'] = 'created_at6'
body['booking']['updated_at'] = 'updated_at4'

result = bookings_api.create_booking(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Availability

Searches for availabilities for booking.

```python
def search_availability(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Availability Request`](/doc/models/search-availability-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Search Availability Response`](/doc/models/search-availability-response.md)

## Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['start_at_range'] = {}
body['query']['filter']['start_at_range']['start_at'] = 'start_at8'
body['query']['filter']['start_at_range']['end_at'] = 'end_at4'
body['query']['filter']['location_id'] = 'location_id6'
body['query']['filter']['segment_filters'] = []

body['query']['filter']['segment_filters'].append({})
body['query']['filter']['segment_filters'][0]['service_variation_id'] = 'service_variation_id8'
body['query']['filter']['segment_filters'][0]['team_member_id_filter'] = {}
body['query']['filter']['segment_filters'][0]['team_member_id_filter']['all'] = ['all7']
body['query']['filter']['segment_filters'][0]['team_member_id_filter']['any'] = ['any0', 'any1']
body['query']['filter']['segment_filters'][0]['team_member_id_filter']['none'] = ['none5']

body['query']['filter']['segment_filters'].append({})
body['query']['filter']['segment_filters'][1]['service_variation_id'] = 'service_variation_id7'
body['query']['filter']['segment_filters'][1]['team_member_id_filter'] = {}
body['query']['filter']['segment_filters'][1]['team_member_id_filter']['all'] = ['all6', 'all7', 'all8']
body['query']['filter']['segment_filters'][1]['team_member_id_filter']['any'] = ['any1', 'any2', 'any3']
body['query']['filter']['segment_filters'][1]['team_member_id_filter']['none'] = ['none6', 'none7']

body['query']['filter']['booking_id'] = 'booking_id6'

result = bookings_api.search_availability(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Business Booking Profile

Retrieves a seller's booking profile.

```python
def retrieve_business_booking_profile(self)
```

## Response Type

[`Retrieve Business Booking Profile Response`](/doc/models/retrieve-business-booking-profile-response.md)

## Example Usage

```python
result = bookings_api.retrieve_business_booking_profile()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Team Member Booking Profiles

Lists booking profiles for team members.

```python
def list_team_member_booking_profiles(self,
                                     bookable_only=False,
                                     limit=None,
                                     cursor=None,
                                     location_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bookable_only` | `bool` | Query, Optional | Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`). |
| `limit` | `int` | Query, Optional | The maximum number of results to return. |
| `cursor` | `string` | Query, Optional | The cursor for paginating through the results. |
| `location_id` | `string` | Query, Optional | Indicates whether to include only team members enabled at the given location in the returned result. |

## Response Type

[`List Team Member Booking Profiles Response`](/doc/models/list-team-member-booking-profiles-response.md)

## Example Usage

```python
bookable_only = False
limit = 172
cursor = 'cursor6'
location_id = 'location_id4'

result = bookings_api.list_team_member_booking_profiles(bookable_only, limit, cursor, location_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Team Member Booking Profile

Retrieves a team member's booking profile.

```python
def retrieve_team_member_booking_profile(self,
                                        team_member_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Template, Required | The ID of the team member to retrieve. |

## Response Type

[`Retrieve Team Member Booking Profile Response`](/doc/models/retrieve-team-member-booking-profile-response.md)

## Example Usage

```python
team_member_id = 'team_member_id0'

result = bookings_api.retrieve_team_member_booking_profile(team_member_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Booking

Retrieves a booking.

```python
def retrieve_booking(self,
                    booking_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `string` | Template, Required | The ID of the [Booking](#type-booking) object representing the to-be-retrieved booking. |

## Response Type

[`Retrieve Booking Response`](/doc/models/retrieve-booking-response.md)

## Example Usage

```python
booking_id = 'booking_id4'

result = bookings_api.retrieve_booking(booking_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Booking

Updates a booking.

```python
def update_booking(self,
                  booking_id,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `string` | Template, Required | The ID of the [Booking](#type-booking) object representing the to-be-updated booking. |
| `body` | [`Update Booking Request`](/doc/models/update-booking-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Update Booking Response`](/doc/models/update-booking-response.md)

## Example Usage

```python
booking_id = 'booking_id4'
body = {}
body['idempotency_key'] = 'idempotency_key2'
body['booking'] = {}
body['booking']['id'] = 'id8'
body['booking']['version'] = 148
body['booking']['status'] = 'ACCEPTED'
body['booking']['created_at'] = 'created_at6'
body['booking']['updated_at'] = 'updated_at4'

result = bookings_api.update_booking(booking_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Cancel Booking

Cancels an existing booking.

```python
def cancel_booking(self,
                  booking_id,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `string` | Template, Required | The ID of the [Booking](#type-booking) object representing the to-be-cancelled booking. |
| `body` | [`Cancel Booking Request`](/doc/models/cancel-booking-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`Cancel Booking Response`](/doc/models/cancel-booking-response.md)

## Example Usage

```python
booking_id = 'booking_id4'
body = {}
body['idempotency_key'] = 'idempotency_key2'
body['booking_version'] = 8

result = bookings_api.cancel_booking(booking_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

