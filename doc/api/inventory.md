# Inventory

```python
inventory_api = client.inventory
```

## Class Name

`InventoryApi`

## Methods

* [Deprecated Retrieve Inventory Adjustment](../../doc/api/inventory.md#deprecated-retrieve-inventory-adjustment)
* [Retrieve Inventory Adjustment](../../doc/api/inventory.md#retrieve-inventory-adjustment)
* [Deprecated Batch Change Inventory](../../doc/api/inventory.md#deprecated-batch-change-inventory)
* [Deprecated Batch Retrieve Inventory Changes](../../doc/api/inventory.md#deprecated-batch-retrieve-inventory-changes)
* [Deprecated Batch Retrieve Inventory Counts](../../doc/api/inventory.md#deprecated-batch-retrieve-inventory-counts)
* [Batch Change Inventory](../../doc/api/inventory.md#batch-change-inventory)
* [Batch Retrieve Inventory Changes](../../doc/api/inventory.md#batch-retrieve-inventory-changes)
* [Batch Retrieve Inventory Counts](../../doc/api/inventory.md#batch-retrieve-inventory-counts)
* [Deprecated Retrieve Inventory Physical Count](../../doc/api/inventory.md#deprecated-retrieve-inventory-physical-count)
* [Retrieve Inventory Physical Count](../../doc/api/inventory.md#retrieve-inventory-physical-count)
* [Retrieve Inventory Transfer](../../doc/api/inventory.md#retrieve-inventory-transfer)
* [Retrieve Inventory Count](../../doc/api/inventory.md#retrieve-inventory-count)
* [Retrieve Inventory Changes](../../doc/api/inventory.md#retrieve-inventory-changes)


# Deprecated Retrieve Inventory Adjustment

**This endpoint is deprecated.**

Deprecated version of [RetrieveInventoryAdjustment](api-endpoint:Inventory-RetrieveInventoryAdjustment) after the endpoint URL
is updated to conform to the standard convention.

```python
def deprecated_retrieve_inventory_adjustment(self,
                                            adjustment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adjustment_id` | `str` | Template, Required | ID of the [InventoryAdjustment](entity:InventoryAdjustment) to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Inventory Adjustment Response`](../../doc/models/retrieve-inventory-adjustment-response.md).

## Example Usage

```python
adjustment_id = 'adjustment_id0'

result = inventory_api.deprecated_retrieve_inventory_adjustment(adjustment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Inventory Adjustment

Returns the [InventoryAdjustment](../../doc/models/inventory-adjustment.md) object
with the provided `adjustment_id`.

```python
def retrieve_inventory_adjustment(self,
                                 adjustment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adjustment_id` | `str` | Template, Required | ID of the [InventoryAdjustment](entity:InventoryAdjustment) to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Inventory Adjustment Response`](../../doc/models/retrieve-inventory-adjustment-response.md).

## Example Usage

```python
adjustment_id = 'adjustment_id0'

result = inventory_api.retrieve_inventory_adjustment(adjustment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Deprecated Batch Change Inventory

**This endpoint is deprecated.**

Deprecated version of [BatchChangeInventory](api-endpoint:Inventory-BatchChangeInventory) after the endpoint URL
is updated to conform to the standard convention.

```python
def deprecated_batch_change_inventory(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Change Inventory Request`](../../doc/models/batch-change-inventory-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Change Inventory Response`](../../doc/models/batch-change-inventory-response.md).

## Example Usage

```python
body = {
    'idempotency_key': '8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe',
    'changes': [
        {
            'type': 'PHYSICAL_COUNT',
            'physical_count': {
                'reference_id': '1536bfbf-efed-48bf-b17d-a197141b2a92',
                'catalog_object_id': 'W62UWFY35CWMYGVWK6TWJDNI',
                'state': 'IN_STOCK',
                'location_id': 'C6W5YS5QM06F5',
                'quantity': '53',
                'team_member_id': 'LRK57NSQ5X7PUD05',
                'occurred_at': '2016-11-16T22:25:24.878Z'
            }
        }
    ],
    'ignore_unchanged_counts': True
}

result = inventory_api.deprecated_batch_change_inventory(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Deprecated Batch Retrieve Inventory Changes

**This endpoint is deprecated.**

Deprecated version of [BatchRetrieveInventoryChanges](api-endpoint:Inventory-BatchRetrieveInventoryChanges) after the endpoint URL
is updated to conform to the standard convention.

```python
def deprecated_batch_retrieve_inventory_changes(self,
                                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Retrieve Inventory Changes Request`](../../doc/models/batch-retrieve-inventory-changes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Retrieve Inventory Changes Response`](../../doc/models/batch-retrieve-inventory-changes-response.md).

## Example Usage

```python
body = {
    'catalog_object_ids': [
        'W62UWFY35CWMYGVWK6TWJDNI'
    ],
    'location_ids': [
        'C6W5YS5QM06F5'
    ],
    'types': [
        'PHYSICAL_COUNT'
    ],
    'states': [
        'IN_STOCK'
    ],
    'updated_after': '2016-11-01T00:00:00.000Z',
    'updated_before': '2016-12-01T00:00:00.000Z'
}

result = inventory_api.deprecated_batch_retrieve_inventory_changes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Deprecated Batch Retrieve Inventory Counts

**This endpoint is deprecated.**

Deprecated version of [BatchRetrieveInventoryCounts](api-endpoint:Inventory-BatchRetrieveInventoryCounts) after the endpoint URL
is updated to conform to the standard convention.

```python
def deprecated_batch_retrieve_inventory_counts(self,
                                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Retrieve Inventory Counts Request`](../../doc/models/batch-retrieve-inventory-counts-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Retrieve Inventory Counts Response`](../../doc/models/batch-retrieve-inventory-counts-response.md).

## Example Usage

```python
body = {
    'catalog_object_ids': [
        'W62UWFY35CWMYGVWK6TWJDNI'
    ],
    'location_ids': [
        '59TNP9SA8VGDA'
    ],
    'updated_after': '2016-11-16T00:00:00.000Z'
}

result = inventory_api.deprecated_batch_retrieve_inventory_counts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Batch Change Inventory

Applies adjustments and counts to the provided item quantities.

On success: returns the current calculated counts for all objects
referenced in the request.
On failure: returns a list of related errors.

```python
def batch_change_inventory(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Change Inventory Request`](../../doc/models/batch-change-inventory-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Change Inventory Response`](../../doc/models/batch-change-inventory-response.md).

## Example Usage

```python
body = {
    'idempotency_key': '8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe',
    'changes': [
        {
            'type': 'PHYSICAL_COUNT',
            'physical_count': {
                'reference_id': '1536bfbf-efed-48bf-b17d-a197141b2a92',
                'catalog_object_id': 'W62UWFY35CWMYGVWK6TWJDNI',
                'state': 'IN_STOCK',
                'location_id': 'C6W5YS5QM06F5',
                'quantity': '53',
                'team_member_id': 'LRK57NSQ5X7PUD05',
                'occurred_at': '2016-11-16T22:25:24.878Z'
            }
        }
    ],
    'ignore_unchanged_counts': True
}

result = inventory_api.batch_change_inventory(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Batch Retrieve Inventory Changes

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

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Retrieve Inventory Changes Request`](../../doc/models/batch-retrieve-inventory-changes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Retrieve Inventory Changes Response`](../../doc/models/batch-retrieve-inventory-changes-response.md).

## Example Usage

```python
body = {
    'catalog_object_ids': [
        'W62UWFY35CWMYGVWK6TWJDNI'
    ],
    'location_ids': [
        'C6W5YS5QM06F5'
    ],
    'types': [
        'PHYSICAL_COUNT'
    ],
    'states': [
        'IN_STOCK'
    ],
    'updated_after': '2016-11-01T00:00:00.000Z',
    'updated_before': '2016-12-01T00:00:00.000Z'
}

result = inventory_api.batch_retrieve_inventory_changes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Batch Retrieve Inventory Counts

Returns current counts for the provided
[CatalogObject](../../doc/models/catalog-object.md)s at the requested
[Location](../../doc/models/location.md)s.

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

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Retrieve Inventory Counts Request`](../../doc/models/batch-retrieve-inventory-counts-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Retrieve Inventory Counts Response`](../../doc/models/batch-retrieve-inventory-counts-response.md).

## Example Usage

```python
body = {
    'catalog_object_ids': [
        'W62UWFY35CWMYGVWK6TWJDNI'
    ],
    'location_ids': [
        '59TNP9SA8VGDA'
    ],
    'updated_after': '2016-11-16T00:00:00.000Z'
}

result = inventory_api.batch_retrieve_inventory_counts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Deprecated Retrieve Inventory Physical Count

**This endpoint is deprecated.**

Deprecated version of [RetrieveInventoryPhysicalCount](api-endpoint:Inventory-RetrieveInventoryPhysicalCount) after the endpoint URL
is updated to conform to the standard convention.

```python
def deprecated_retrieve_inventory_physical_count(self,
                                                physical_count_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `physical_count_id` | `str` | Template, Required | ID of the<br>[InventoryPhysicalCount](entity:InventoryPhysicalCount) to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Inventory Physical Count Response`](../../doc/models/retrieve-inventory-physical-count-response.md).

## Example Usage

```python
physical_count_id = 'physical_count_id2'

result = inventory_api.deprecated_retrieve_inventory_physical_count(physical_count_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Inventory Physical Count

Returns the [InventoryPhysicalCount](../../doc/models/inventory-physical-count.md)
object with the provided `physical_count_id`.

```python
def retrieve_inventory_physical_count(self,
                                     physical_count_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `physical_count_id` | `str` | Template, Required | ID of the<br>[InventoryPhysicalCount](entity:InventoryPhysicalCount) to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Inventory Physical Count Response`](../../doc/models/retrieve-inventory-physical-count-response.md).

## Example Usage

```python
physical_count_id = 'physical_count_id2'

result = inventory_api.retrieve_inventory_physical_count(physical_count_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Inventory Transfer

Returns the [InventoryTransfer](../../doc/models/inventory-transfer.md) object
with the provided `transfer_id`.

```python
def retrieve_inventory_transfer(self,
                               transfer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_id` | `str` | Template, Required | ID of the [InventoryTransfer](entity:InventoryTransfer) to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Inventory Transfer Response`](../../doc/models/retrieve-inventory-transfer-response.md).

## Example Usage

```python
transfer_id = 'transfer_id6'

result = inventory_api.retrieve_inventory_transfer(transfer_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Inventory Count

Retrieves the current calculated stock count for a given
[CatalogObject](../../doc/models/catalog-object.md) at a given set of
[Location](../../doc/models/location.md)s. Responses are paginated and unsorted.
For more sophisticated queries, use a batch endpoint.

```python
def retrieve_inventory_count(self,
                            catalog_object_id,
                            location_ids=None,
                            cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `catalog_object_id` | `str` | Template, Required | ID of the [CatalogObject](entity:CatalogObject) to retrieve. |
| `location_ids` | `str` | Query, Optional | The [Location](entity:Location) IDs to look up as a comma-separated<br>list. An empty list queries all locations. |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Inventory Count Response`](../../doc/models/retrieve-inventory-count-response.md).

## Example Usage

```python
catalog_object_id = 'catalog_object_id6'

result = inventory_api.retrieve_inventory_count(catalog_object_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Inventory Changes

**This endpoint is deprecated.**

Returns a set of physical counts and inventory adjustments for the
provided [CatalogObject](entity:CatalogObject) at the requested
[Location](entity:Location)s.

You can achieve the same result by calling [BatchRetrieveInventoryChanges](api-endpoint:Inventory-BatchRetrieveInventoryChanges)
and having the `catalog_object_ids` list contain a single element of the `CatalogObject` ID.

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

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `catalog_object_id` | `str` | Template, Required | ID of the [CatalogObject](entity:CatalogObject) to retrieve. |
| `location_ids` | `str` | Query, Optional | The [Location](entity:Location) IDs to look up as a comma-separated<br>list. An empty list queries all locations. |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Inventory Changes Response`](../../doc/models/retrieve-inventory-changes-response.md).

## Example Usage

```python
catalog_object_id = 'catalog_object_id6'

result = inventory_api.retrieve_inventory_changes(catalog_object_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

