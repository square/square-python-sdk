# V1 Locations

```python
v1_locations_api = client.v1_locations
```

## Class Name

`V1LocationsApi`

## Methods

* [Retrieve Business](/doc/v1-locations.md#retrieve-business)
* [List Locations](/doc/v1-locations.md#list-locations)

## Retrieve Business

Get a business's information.

```python
def retrieve_business(self)
```

### Response Type

[`V1 Merchant`](/doc/models/v1-merchant.md)

### Example Usage

```python
result = v1_locations_api.retrieve_business()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Locations

Provides details for a business's locations, including their IDs.

```python
def list_locations(self)
```

### Response Type

[`List of V1 Merchant`](/doc/models/v1-merchant.md)

### Example Usage

```python
result = v1_locations_api.list_locations()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

