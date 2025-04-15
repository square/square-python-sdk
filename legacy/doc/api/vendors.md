# Vendors

```python
vendors_api = client.vendors
```

## Class Name

`VendorsApi`

## Methods

* [Bulk Create Vendors](../../doc/api/vendors.md#bulk-create-vendors)
* [Bulk Retrieve Vendors](../../doc/api/vendors.md#bulk-retrieve-vendors)
* [Bulk Update Vendors](../../doc/api/vendors.md#bulk-update-vendors)
* [Create Vendor](../../doc/api/vendors.md#create-vendor)
* [Search Vendors](../../doc/api/vendors.md#search-vendors)
* [Retrieve Vendor](../../doc/api/vendors.md#retrieve-vendor)
* [Update Vendor](../../doc/api/vendors.md#update-vendor)


# Bulk Create Vendors

Creates one or more [Vendor](../../doc/models/vendor.md) objects to represent suppliers to a seller.

```python
def bulk_create_vendors(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Create Vendors Request`](../../doc/models/bulk-create-vendors-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Create Vendors Response`](../../doc/models/bulk-create-vendors-response.md).

## Example Usage

```python
body = {
    'vendors': {
        'key0': {},
        'key1': {}
    }
}

result = vendors_api.bulk_create_vendors(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Retrieve Vendors

Retrieves one or more vendors of specified [Vendor](../../doc/models/vendor.md) IDs.

```python
def bulk_retrieve_vendors(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Retrieve Vendors Request`](../../doc/models/bulk-retrieve-vendors-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Retrieve Vendors Response`](../../doc/models/bulk-retrieve-vendors-response.md).

## Example Usage

```python
body = {
    'vendor_ids': [
        'INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4'
    ]
}

result = vendors_api.bulk_retrieve_vendors(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Bulk Update Vendors

Updates one or more of existing [Vendor](../../doc/models/vendor.md) objects as suppliers to a seller.

```python
def bulk_update_vendors(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Bulk Update Vendors Request`](../../doc/models/bulk-update-vendors-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Bulk Update Vendors Response`](../../doc/models/bulk-update-vendors-response.md).

## Example Usage

```python
body = {
    'vendors': {
        'key0': {
            'vendor': {}
        },
        'key1': {
            'vendor': {}
        }
    }
}

result = vendors_api.bulk_update_vendors(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Vendor

Creates a single [Vendor](../../doc/models/vendor.md) object to represent a supplier to a seller.

```python
def create_vendor(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Vendor Request`](../../doc/models/create-vendor-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Vendor Response`](../../doc/models/create-vendor-response.md).

## Example Usage

```python
body = {
    'idempotency_key': 'idempotency_key2'
}

result = vendors_api.create_vendor(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Vendors

Searches for vendors using a filter against supported [Vendor](../../doc/models/vendor.md) properties and a supported sorter.

```python
def search_vendors(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Vendors Request`](../../doc/models/search-vendors-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Search Vendors Response`](../../doc/models/search-vendors-response.md).

## Example Usage

```python
body = {}

result = vendors_api.search_vendors(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Vendor

Retrieves the vendor of a specified [Vendor](../../doc/models/vendor.md) ID.

```python
def retrieve_vendor(self,
                   vendor_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vendor_id` | `str` | Template, Required | ID of the [Vendor](entity:Vendor) to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Vendor Response`](../../doc/models/retrieve-vendor-response.md).

## Example Usage

```python
vendor_id = 'vendor_id8'

result = vendors_api.retrieve_vendor(vendor_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Vendor

Updates an existing [Vendor](../../doc/models/vendor.md) object as a supplier to a seller.

```python
def update_vendor(self,
                 body,
                 vendor_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Update Vendor Request`](../../doc/models/update-vendor-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| `vendor_id` | `str` | Template, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Vendor Response`](../../doc/models/update-vendor-response.md).

## Example Usage

```python
body = {
    'vendor': {
        'id': 'INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4',
        'name': 'Jack\'s Chicken Shack',
        'version': 1,
        'status': 'ACTIVE'
    },
    'idempotency_key': '8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe'
}

vendor_id = 'vendor_id8'

result = vendors_api.update_vendor(
    body,
    vendor_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

