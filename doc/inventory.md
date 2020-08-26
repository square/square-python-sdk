# Inventory

```python
inventory_api = client.inventory
```

## Class Name

`InventoryApi`

## Methods

* [Retrieve Inventory Adjustment](/doc/inventory.md#retrieve-inventory-adjustment)
* [Batch Change Inventory](/doc/inventory.md#batch-change-inventory)
* [Batch Retrieve Inventory Changes](/doc/inventory.md#batch-retrieve-inventory-changes)
* [Batch Retrieve Inventory Counts](/doc/inventory.md#batch-retrieve-inventory-counts)
* [Retrieve Inventory Physical Count](/doc/inventory.md#retrieve-inventory-physical-count)
* [Retrieve Inventory Count](/doc/inventory.md#retrieve-inventory-count)
* [Retrieve Inventory Changes](/doc/inventory.md#retrieve-inventory-changes)

## Retrieve Inventory Adjustment

Returns the [InventoryAdjustment](#type-inventoryadjustment) object
with the provided `adjustment_id`.

```python
def retrieve_inventory_adjustment(self,
                                 adjustment_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adjustment_id` | `string` | Template, Required | ID of the [InventoryAdjustment](#type-inventoryadjustment) to retrieve. |

### Response Type

[`Retrieve Inventory Adjustment Response`](/doc/models/retrieve-inventory-adjustment-response.md)

### Example Usage

```python
adjustment_id = 'adjustment_id0'

result = inventory_api.retrieve_inventory_adjustment(adjustment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Batch Change Inventory

Applies adjustments and counts to the provided item quantities.

On success: returns the current calculated counts for all objects
referenced in the request.
On failure: returns a list of related errors.

```python
def batch_change_inventory(self,
                          body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Change Inventory Request`](/doc/models/batch-change-inventory-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Change Inventory Response`](/doc/models/batch-change-inventory-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = '8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe'
body['changes'] = []

body['changes'].append({})
body['changes'][0]['type'] = 'PHYSICAL_COUNT'
body['changes'][0]['physical_count'] = {}
body['changes'][0]['physical_count']['id'] = 'id0'
body['changes'][0]['physical_count']['reference_id'] = '1536bfbf-efed-48bf-b17d-a197141b2a92'
body['changes'][0]['physical_count']['catalog_object_id'] = 'W62UWFY35CWMYGVWK6TWJDNI'
body['changes'][0]['physical_count']['catalog_object_type'] = 'catalog_object_type4'
body['changes'][0]['physical_count']['state'] = 'IN_STOCK'
body['changes'][0]['physical_count']['location_id'] = 'C6W5YS5QM06F5'
body['changes'][0]['physical_count']['quantity'] = '53'
body['changes'][0]['physical_count']['employee_id'] = 'LRK57NSQ5X7PUD05'
body['changes'][0]['physical_count']['occurred_at'] = '2016-11-16T22:25:24.878Z'
body['changes'][0]['adjustment'] = {}
body['changes'][0]['adjustment']['id'] = 'id6'
body['changes'][0]['adjustment']['reference_id'] = 'reference_id4'
body['changes'][0]['adjustment']['from_state'] = 'SOLD'
body['changes'][0]['adjustment']['to_state'] = 'IN_TRANSIT_TO'
body['changes'][0]['adjustment']['location_id'] = 'location_id0'
body['changes'][0]['transfer'] = {}
body['changes'][0]['transfer']['id'] = 'id0'
body['changes'][0]['transfer']['reference_id'] = 'reference_id8'
body['changes'][0]['transfer']['state'] = 'SOLD'
body['changes'][0]['transfer']['from_location_id'] = 'from_location_id2'
body['changes'][0]['transfer']['to_location_id'] = 'to_location_id2'

body['ignore_unchanged_counts'] = True

result = inventory_api.batch_change_inventory(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Batch Retrieve Inventory Changes

Returns historical physical counts and adjustments based on the
provided filter criteria.

Results are paginated and sorted in ascending order according their
`occurred_at` timestamp (oldest first).

BatchRetrieveInventoryChanges is a catch-all query endpoint for queries
that cannot be handled by other, simpler endpoints.

```python
def batch_retrieve_inventory_changes(self,
                                    body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Retrieve Inventory Changes Request`](/doc/models/batch-retrieve-inventory-changes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Retrieve Inventory Changes Response`](/doc/models/batch-retrieve-inventory-changes-response.md)

### Example Usage

```python
body = {}
body['catalog_object_ids'] = ['W62UWFY35CWMYGVWK6TWJDNI']
body['location_ids'] = ['C6W5YS5QM06F5']
body['types'] = ['PHYSICAL_COUNT']
body['states'] = ['IN_STOCK']
body['updated_after'] = '2016-11-01T00:00:00.000Z'
body['updated_before'] = '2016-12-01T00:00:00.000Z'

result = inventory_api.batch_retrieve_inventory_changes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Batch Retrieve Inventory Counts

Returns current counts for the provided
[CatalogObject](#type-catalogobject)s at the requested
[Location](#type-location)s.

Results are paginated and sorted in descending order according to their
`calculated_at` timestamp (newest first).

When `updated_after` is specified, only counts that have changed since that
time (based on the server timestamp for the most recent change) are
returned. This allows clients to perform a "sync" operation, for example
in response to receiving a Webhook notification.

```python
def batch_retrieve_inventory_counts(self,
                                   body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Retrieve Inventory Counts Request`](/doc/models/batch-retrieve-inventory-counts-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Retrieve Inventory Counts Response`](/doc/models/batch-retrieve-inventory-counts-response.md)

### Example Usage

```python
body = {}
body['catalog_object_ids'] = ['W62UWFY35CWMYGVWK6TWJDNI']
body['location_ids'] = ['59TNP9SA8VGDA']
body['updated_after'] = '2016-11-16T00:00:00.000Z'
body['cursor'] = 'cursor0'
body['states'] = ['IN_TRANSIT_TO']

result = inventory_api.batch_retrieve_inventory_counts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Inventory Physical Count

Returns the [InventoryPhysicalCount](#type-inventoryphysicalcount)
object with the provided `physical_count_id`.

```python
def retrieve_inventory_physical_count(self,
                                     physical_count_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `physical_count_id` | `string` | Template, Required | ID of the<br>[InventoryPhysicalCount](#type-inventoryphysicalcount) to retrieve. |

### Response Type

[`Retrieve Inventory Physical Count Response`](/doc/models/retrieve-inventory-physical-count-response.md)

### Example Usage

```python
physical_count_id = 'physical_count_id2'

result = inventory_api.retrieve_inventory_physical_count(physical_count_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Inventory Count

Retrieves the current calculated stock count for a given
[CatalogObject](#type-catalogobject) at a given set of
[Location](#type-location)s. Responses are paginated and unsorted.
For more sophisticated queries, use a batch endpoint.

```python
def retrieve_inventory_count(self,
                            catalog_object_id,
                            location_ids=None,
                            cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `catalog_object_id` | `string` | Template, Required | ID of the [CatalogObject](#type-catalogobject) to retrieve. |
| `location_ids` | `string` | Query, Optional | The [Location](#type-location) IDs to look up as a comma-separated<br>list. An empty list queries all locations. |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>See the [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination) guide for more information. |

### Response Type

[`Retrieve Inventory Count Response`](/doc/models/retrieve-inventory-count-response.md)

### Example Usage

```python
catalog_object_id = 'catalog_object_id6'
location_ids = 'location_ids0'
cursor = 'cursor6'

result = inventory_api.retrieve_inventory_count(catalog_object_id, location_ids, cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Inventory Changes

Returns a set of physical counts and inventory adjustments for the
provided [CatalogObject](#type-catalogobject) at the requested
[Location](#type-location)s.

Results are paginated and sorted in descending order according to their
`occurred_at` timestamp (newest first).

There are no limits on how far back the caller can page. This endpoint can be 
used to display recent changes for a specific item. For more
sophisticated queries, use a batch endpoint.

```python
def retrieve_inventory_changes(self,
                              catalog_object_id,
                              location_ids=None,
                              cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `catalog_object_id` | `string` | Template, Required | ID of the [CatalogObject](#type-catalogobject) to retrieve. |
| `location_ids` | `string` | Query, Optional | The [Location](#type-location) IDs to look up as a comma-separated<br>list. An empty list queries all locations. |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. |

### Response Type

[`Retrieve Inventory Changes Response`](/doc/models/retrieve-inventory-changes-response.md)

### Example Usage

```python
catalog_object_id = 'catalog_object_id6'
location_ids = 'location_ids0'
cursor = 'cursor6'

result = inventory_api.retrieve_inventory_changes(catalog_object_id, location_ids, cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

