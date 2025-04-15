# Bookings

```python
bookings_api = client.bookings
```

## Class Name

`BookingsApi`

## Methods

* [List Bookings](../../doc/api/bookings.md#list-bookings)
* [Create Booking](../../doc/api/bookings.md#create-booking)
* [Search Availability](../../doc/api/bookings.md#search-availability)
* [Bulk Retrieve Bookings](../../doc/api/bookings.md#bulk-retrieve-bookings)
* [Retrieve Business Booking Profile](../../doc/api/bookings.md#retrieve-business-booking-profile)
* [List Location Booking Profiles](../../doc/api/bookings.md#list-location-booking-profiles)
* [Retrieve Location Booking Profile](../../doc/api/bookings.md#retrieve-location-booking-profile)
* [List Team Member Booking Profiles](../../doc/api/bookings.md#list-team-member-booking-profiles)
* [Bulk Retrieve Team Member Booking Profiles](../../doc/api/bookings.md#bulk-retrieve-team-member-booking-profiles)
* [Retrieve Team Member Booking Profile](../../doc/api/bookings.md#retrieve-team-member-booking-profile)
* [Retrieve Booking](../../doc/api/bookings.md#retrieve-booking)
* [Update Booking](../../doc/api/bookings.md#update-booking)
* [Cancel Booking](../../doc/api/bookings.md#cancel-booking)


# List Bookings

Retrieve a collection of bookings.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

```python
def list_bookings(self,
                 limit=None,
                 cursor=None,
                 customer_id=None,
                 team_member_id=None,
                 location_id=None,
                 start_at_min=None,
                 start_at_max=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | The maximum number of results per page to return in a paged response. |
| `cursor` | `str` | Query, Optional | The pagination cursor from the preceding response to return the next page of the results. Do not set this when retrieving the first page of the results. |
| `customer_id` | `str` | Query, Optional | The [customer](entity:Customer) for whom to retrieve bookings. If this is not set, bookings for all customers are retrieved. |
| `team_member_id` | `str` | Query, Optional | The team member for whom to retrieve bookings. If this is not set, bookings of all members are retrieved. |
| `location_id` | `str` | Query, Optional | The location for which to retrieve bookings. If this is not set, all locations' bookings are retrieved. |
| `start_at_min` | `str` | Query, Optional | The RFC 3339 timestamp specifying the earliest of the start time. If this is not set, the current time is used. |
| `start_at_max` | `str` | Query, Optional | The RFC 3339 timestamp specifying the latest of the start time. If this is not set, the time of 31 days after `start_at_min` is used. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Bookings Response`](../../doc/models/list-bookings-response.md).

## Example Usage

```python
result = bookings_api.list_bookings()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Booking

Creates a booking.

The required input must include the following:

- `Booking.location_id`
- `Booking.start_at`
- `Booking.AppointmentSegment.team_member_id`
- `Booking.AppointmentSegment.service_variation_id`
- `Booking.AppointmentSegment.service_variation_version`

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def create_booking(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Booking Request`](../../doc/models/create-booking-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Booking Response`](../../doc/models/create-booking-response.md).

## Example Usage

```python
body = {
    'booking': {}
}

result = bookings_api.create_booking(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Availability

Searches for availabilities for booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

```python
def search_availability(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Availability Request`](../../doc/models/search-availability-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Search Availability Response`](../../doc/models/search-availability-response.md).

## Example Usage

```python
body = {
    'query': {
        'filter': {
            'start_at_range': {}
        }
    }
}

result = bookings_api.search_availability(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Retrieve Bookings

Bulk-Retrieves a list of bookings by booking IDs.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

```python
def bulk_retrieve_bookings(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Retrieve Bookings Request`](../../doc/models/bulk-retrieve-bookings-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Retrieve Bookings Response`](../../doc/models/bulk-retrieve-bookings-response.md).

## Example Usage

```python
body = {
    'booking_ids': [
        'booking_ids8',
        'booking_ids9',
        'booking_ids0'
    ]
}

result = bookings_api.bulk_retrieve_bookings(body)

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

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Business Booking Profile Response`](../../doc/models/retrieve-business-booking-profile-response.md).

## Example Usage

```python
result = bookings_api.retrieve_business_booking_profile()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Location Booking Profiles

Lists location booking profiles of a seller.

```python
def list_location_booking_profiles(self,
                                  limit=None,
                                  cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a paged response. |
| `cursor` | `str` | Query, Optional | The pagination cursor from the preceding response to return the next page of the results. Do not set this when retrieving the first page of the results. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Location Booking Profiles Response`](../../doc/models/list-location-booking-profiles-response.md).

## Example Usage

```python
result = bookings_api.list_location_booking_profiles()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Location Booking Profile

Retrieves a seller's location booking profile.

```python
def retrieve_location_booking_profile(self,
                                     location_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Template, Required | The ID of the location to retrieve the booking profile. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Location Booking Profile Response`](../../doc/models/retrieve-location-booking-profile-response.md).

## Example Usage

```python
location_id = 'location_id4'

result = bookings_api.retrieve_location_booking_profile(location_id)

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
| `bookable_only` | `bool` | Query, Optional | Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`).<br>**Default**: `False` |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a paged response. |
| `cursor` | `str` | Query, Optional | The pagination cursor from the preceding response to return the next page of the results. Do not set this when retrieving the first page of the results. |
| `location_id` | `str` | Query, Optional | Indicates whether to include only team members enabled at the given location in the returned result. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Team Member Booking Profiles Response`](../../doc/models/list-team-member-booking-profiles-response.md).

## Example Usage

```python
bookable_only = False

result = bookings_api.list_team_member_booking_profiles(
    bookable_only=bookable_only
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Retrieve Team Member Booking Profiles

Retrieves one or more team members' booking profiles.

```python
def bulk_retrieve_team_member_booking_profiles(self,
                                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Retrieve Team Member Booking Profiles Request`](../../doc/models/bulk-retrieve-team-member-booking-profiles-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Retrieve Team Member Booking Profiles Response`](../../doc/models/bulk-retrieve-team-member-booking-profiles-response.md).

## Example Usage

```python
body = {
    'team_member_ids': [
        'team_member_ids3',
        'team_member_ids4',
        'team_member_ids5'
    ]
}

result = bookings_api.bulk_retrieve_team_member_booking_profiles(body)

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
| `team_member_id` | `str` | Template, Required | The ID of the team member to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Team Member Booking Profile Response`](../../doc/models/retrieve-team-member-booking-profile-response.md).

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

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

```python
def retrieve_booking(self,
                    booking_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `str` | Template, Required | The ID of the [Booking](entity:Booking) object representing the to-be-retrieved booking. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Booking Response`](../../doc/models/retrieve-booking-response.md).

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

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def update_booking(self,
                  booking_id,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `str` | Template, Required | The ID of the [Booking](entity:Booking) object representing the to-be-updated booking. |
| `body` | [`Update Booking Request`](../../doc/models/update-booking-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Booking Response`](../../doc/models/update-booking-response.md).

## Example Usage

```python
booking_id = 'booking_id4'

body = {
    'booking': {}
}

result = bookings_api.update_booking(
    booking_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Cancel Booking

Cancels an existing booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

```python
def cancel_booking(self,
                  booking_id,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `booking_id` | `str` | Template, Required | The ID of the [Booking](entity:Booking) object representing the to-be-cancelled booking. |
| `body` | [`Cancel Booking Request`](../../doc/models/cancel-booking-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Cancel Booking Response`](../../doc/models/cancel-booking-response.md).

## Example Usage

```python
booking_id = 'booking_id4'

body = {}

result = bookings_api.cancel_booking(
    booking_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

