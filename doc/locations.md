# Locations

```python
locations_api = client.locations
```

## Class Name

`LocationsApi`

## List Locations

Provides the details for all of a business's locations.

Most other Connect API endpoints have a required `location_id` path parameter.
The `id` field of the [Location](./models/location.md) objects returned by this
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
    print(result.data)
elif result.is_error():
    print(result.errors)
```

