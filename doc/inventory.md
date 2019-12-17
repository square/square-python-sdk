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

[`Retrieve Inventory Adjustment Response`]($m/RetrieveInventoryAdjustmentResponse)

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
| `body` | [`Batch Change Inventory Request`]($m/BatchChangeInventoryRequest) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Change Inventory Response`]($m/BatchChangeInventoryResponse)

### Example Usage

```python
body = {}
body['idempotency_key'] = '8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe'
body['changes'] = []

body['changes'].append({})
body['changes'][0]['type'] = 'PHYSICAL_COUNT'
body['changes'][0]['physical_count'] = {}
body['changes'][0]['physical_count']['reference_id'] = '1536bfbf-efed-48bf-b17d-a197141b2a92'
body['changes'][0]['physical_count']['catalog_object_id'] = 'W62UWFY35CWMYGVWK6TWJDNI'
body['changes'][0]['physical_count']['state'] = 'IN_STOCK'
body['changes'][0]['physical_count']['location_id'] = 'C6W5YS5QM06F5'
body['changes'][0]['physical_count']['quantity'] = '53'
body['changes'][0]['physical_count']['employee_id'] = 'LRK57NSQ5X7PUD05'
body['changes'][0]['physical_count']['occurred_at'] = '2016-11-16T22:25:24.878Z'

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
| `body` | [`Batch Retrieve Inventory Changes Request`]($m/BatchRetrieveInventoryChangesRequest) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Retrieve Inventory Changes Response`]($m/BatchRetrieveInventoryChangesResponse)

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
| `body` | [`Batch Retrieve Inventory Counts Request`]($m/BatchRetrieveInventoryCountsRequest) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Retrieve Inventory Counts Response`]($m/BatchRetrieveInventoryCountsResponse)

### Example Usage

```python
body = {}
body['catalog_object_ids'] = ['W62UWFY35CWMYGVWK6TWJDNI']
body['location_ids'] = ['59TNP9SA8VGDA']
body['updated_after'] = '2016-11-16T00:00:00.000Z'

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

[`Retrieve Inventory Physical Count Response`]($m/RetrieveInventoryPhysicalCountResponse)

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

[`Retrieve Inventory Count Response`]($m/RetrieveInventoryCountResponse)

### Example Usage

```python
catalog_object_id = 'catalog_object_id6'

result = inventory_api.retrieve_inventory_count(catalog_object_id)

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

There are no limits on how far back the caller can page. This endpoint is
useful when displaying recent changes for a specific item. For more
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
| `cursor` | `string` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>See the [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination) guide for more information. |

### Response Type

[`Retrieve Inventory Changes Response`]($m/RetrieveInventoryChangesResponse)

### Example Usage

```python
catalog_object_id = 'catalog_object_id6'

result = inventory_api.retrieve_inventory_changes(catalog_object_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

