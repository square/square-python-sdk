# Devices

```python
devices_api = client.devices
```

## Class Name

`DevicesApi`

## Methods

* [List Device Codes](/doc/devices.md#list-device-codes)
* [Create Device Code](/doc/devices.md#create-device-code)
* [Get Device Code](/doc/devices.md#get-device-code)

## List Device Codes

Lists all DeviceCodes associated with the merchant.

```python
def list_device_codes(self,
                     cursor=None,
                     location_id=None,
                     product_type=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Paginating results](#paginatingresults) for more information. |
| `location_id` | `string` | Query, Optional | If specified, only returns DeviceCodes of the specified location.<br>Returns DeviceCodes of all locations if empty. |
| `product_type` | [`str (Product Type)`](/doc/models/product-type.md) | Query, Optional | If specified, only returns DeviceCodes targeting the specified product type.<br>Returns DeviceCodes of all product types if empty. |

### Response Type

[`List Device Codes Response`](/doc/models/list-device-codes-response.md)

### Example Usage

```python
cursor = 'cursor6'
location_id = 'location_id4'
product_type = 'TERMINAL_API'

result = devices_api.list_device_codes(cursor, location_id, product_type)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Device Code

Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected
terminal mode.

```python
def create_device_code(self,
                      body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Device Code Request`](/doc/models/create-device-code-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Device Code Response`](/doc/models/create-device-code-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = '01bb00a6-0c86-4770-94ed-f5fca973cd56'
body['device_code'] = {}
body['device_code']['id'] = 'id0'
body['device_code']['name'] = 'Counter 1'
body['device_code']['code'] = 'code8'
body['device_code']['device_id'] = 'device_id6'
body['device_code']['product_type'] = 'TERMINAL_API'
body['device_code']['location_id'] = 'B5E4484SHHNYH'

result = devices_api.create_device_code(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Device Code

Retrieves DeviceCode with the associated ID.

```python
def get_device_code(self,
                   id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | The unique identifier for the device code. |

### Response Type

[`Get Device Code Response`](/doc/models/get-device-code-response.md)

### Example Usage

```python
id = 'id0'

result = devices_api.get_device_code(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

