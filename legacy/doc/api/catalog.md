# Catalog

```python
catalog_api = client.catalog
```

## Class Name

`CatalogApi`

## Methods

* [Batch Delete Catalog Objects](../../doc/api/catalog.md#batch-delete-catalog-objects)
* [Batch Retrieve Catalog Objects](../../doc/api/catalog.md#batch-retrieve-catalog-objects)
* [Batch Upsert Catalog Objects](../../doc/api/catalog.md#batch-upsert-catalog-objects)
* [Create Catalog Image](../../doc/api/catalog.md#create-catalog-image)
* [Update Catalog Image](../../doc/api/catalog.md#update-catalog-image)
* [Catalog Info](../../doc/api/catalog.md#catalog-info)
* [List Catalog](../../doc/api/catalog.md#list-catalog)
* [Upsert Catalog Object](../../doc/api/catalog.md#upsert-catalog-object)
* [Delete Catalog Object](../../doc/api/catalog.md#delete-catalog-object)
* [Retrieve Catalog Object](../../doc/api/catalog.md#retrieve-catalog-object)
* [Search Catalog Objects](../../doc/api/catalog.md#search-catalog-objects)
* [Search Catalog Items](../../doc/api/catalog.md#search-catalog-items)
* [Update Item Modifier Lists](../../doc/api/catalog.md#update-item-modifier-lists)
* [Update Item Taxes](../../doc/api/catalog.md#update-item-taxes)


# Batch Delete Catalog Objects

Deletes a set of [CatalogItem](../../doc/models/catalog-item.md)s based on the
provided list of target IDs and returns a set of successfully deleted IDs in
the response. Deletion is a cascading event such that all children of the
targeted object are also deleted. For example, deleting a CatalogItem will
also delete all of its [CatalogItemVariation](../../doc/models/catalog-item-variation.md)
children.

`BatchDeleteCatalogObjects` succeeds even if only a portion of the targeted
IDs can be deleted. The response will only include IDs that were
actually deleted.

To ensure consistency, only one delete request is processed at a time per seller account.
While one (batch or non-batch) delete request is being processed, other (batched and non-batched)
delete requests are rejected with the `429` error code.

```python
def batch_delete_catalog_objects(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Delete Catalog Objects Request`](../../doc/models/batch-delete-catalog-objects-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Delete Catalog Objects Response`](../../doc/models/batch-delete-catalog-objects-response.md).

## Example Usage

```python
body = {
    'object_ids': [
        'W62UWFY35CWMYGVWK6TWJDNI',
        'AA27W3M2GGTF3H6AVPNB77CK'
    ]
}

result = catalog_api.batch_delete_catalog_objects(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Batch Retrieve Catalog Objects

Returns a set of objects based on the provided ID.
Each [CatalogItem](../../doc/models/catalog-item.md) returned in the set includes all of its
child information including: all of its
[CatalogItemVariation](../../doc/models/catalog-item-variation.md) objects, references to
its [CatalogModifierList](../../doc/models/catalog-modifier-list.md) objects, and the ids of
any [CatalogTax](../../doc/models/catalog-tax.md) objects that apply to it.

```python
def batch_retrieve_catalog_objects(self,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Retrieve Catalog Objects Request`](../../doc/models/batch-retrieve-catalog-objects-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Retrieve Catalog Objects Response`](../../doc/models/batch-retrieve-catalog-objects-response.md).

## Example Usage

```python
body = {
    'object_ids': [
        'W62UWFY35CWMYGVWK6TWJDNI',
        'AA27W3M2GGTF3H6AVPNB77CK'
    ],
    'include_related_objects': True
}

result = catalog_api.batch_retrieve_catalog_objects(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Batch Upsert Catalog Objects

Creates or updates up to 10,000 target objects based on the provided
list of objects. The target objects are grouped into batches and each batch is
inserted/updated in an all-or-nothing manner. If an object within a batch is
malformed in some way, or violates a database constraint, the entire batch
containing that item will be disregarded. However, other batches in the same
request may still succeed. Each batch may contain up to 1,000 objects, and
batches will be processed in order as long as the total object count for the
request (items, variations, modifier lists, discounts, and taxes) is no more
than 10,000.

To ensure consistency, only one update request is processed at a time per seller account.
While one (batch or non-batch) update request is being processed, other (batched and non-batched)
update requests are rejected with the `429` error code.

```python
def batch_upsert_catalog_objects(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Upsert Catalog Objects Request`](../../doc/models/batch-upsert-catalog-objects-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Batch Upsert Catalog Objects Response`](../../doc/models/batch-upsert-catalog-objects-response.md).

## Example Usage

```python
body = {
    'idempotency_key': '789ff020-f723-43a9-b4b5-43b5dc1fa3dc',
    'batches': [
        {
            'objects': [
                {
                    'type': 'ITEM',
                    'id': '#Tea',
                    'present_at_all_locations': True,
                    'item_data': {
                        'name': 'Tea',
                        'tax_ids': [
                            '#SalesTax'
                        ],
                        'variations': [
                            {
                                'type': 'ITEM_VARIATION',
                                'id': '#Tea_Mug',
                                'present_at_all_locations': True,
                                'item_variation_data': {
                                    'item_id': '#Tea',
                                    'name': 'Mug',
                                    'pricing_type': 'FIXED_PRICING',
                                    'price_money': {
                                        'amount': 150,
                                        'currency': 'USD'
                                    }
                                }
                            }
                        ],
                        'categories': [
                            {
                                'id': '#Beverages'
                            }
                        ],
                        'description_html': '<p><strong>Hot</strong> Leaf Juice</p>'
                    }
                },
                {
                    'type': 'ITEM',
                    'id': '#Coffee',
                    'present_at_all_locations': True,
                    'item_data': {
                        'name': 'Coffee',
                        'tax_ids': [
                            '#SalesTax'
                        ],
                        'variations': [
                            {
                                'type': 'ITEM_VARIATION',
                                'id': '#Coffee_Regular',
                                'present_at_all_locations': True,
                                'item_variation_data': {
                                    'item_id': '#Coffee',
                                    'name': 'Regular',
                                    'pricing_type': 'FIXED_PRICING',
                                    'price_money': {
                                        'amount': 250,
                                        'currency': 'USD'
                                    }
                                }
                            },
                            {
                                'type': 'ITEM_VARIATION',
                                'id': '#Coffee_Large',
                                'present_at_all_locations': True,
                                'item_variation_data': {
                                    'item_id': '#Coffee',
                                    'name': 'Large',
                                    'pricing_type': 'FIXED_PRICING',
                                    'price_money': {
                                        'amount': 350,
                                        'currency': 'USD'
                                    }
                                }
                            }
                        ],
                        'categories': [
                            {
                                'id': '#Beverages'
                            }
                        ],
                        'description_html': '<p>Hot <em>Bean Juice</em></p>'
                    }
                },
                {
                    'type': 'CATEGORY',
                    'id': '#Beverages',
                    'present_at_all_locations': True,
                    'category_data': {
                        'name': 'Beverages'
                    }
                },
                {
                    'type': 'TAX',
                    'id': '#SalesTax',
                    'present_at_all_locations': True,
                    'tax_data': {
                        'name': 'Sales Tax',
                        'calculation_phase': 'TAX_SUBTOTAL_PHASE',
                        'inclusion_type': 'ADDITIVE',
                        'percentage': '5.0',
                        'applies_to_custom_amounts': True,
                        'enabled': True
                    }
                }
            ]
        }
    ]
}

result = catalog_api.batch_upsert_catalog_objects(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Catalog Image

Uploads an image file to be represented by a [CatalogImage](../../doc/models/catalog-image.md) object that can be linked to an existing
[CatalogObject](../../doc/models/catalog-object.md) instance. The resulting `CatalogImage` is unattached to any `CatalogObject` if the `object_id`
is not specified.

This `CreateCatalogImage` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image file part in
JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

```python
def create_catalog_image(self,
                        request=None,
                        image_file=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`Create Catalog Image Request`](../../doc/models/create-catalog-image-request.md) | Form (JSON-Encoded), Optional | - |
| `image_file` | `typing.BinaryIO` | Form, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Catalog Image Response`](../../doc/models/create-catalog-image-response.md).

## Example Usage

```python
request = {
    'idempotency_key': '528dea59-7bfb-43c1-bd48-4a6bba7dd61f86',
    'image': {
        'type': 'IMAGE',
        'id': '#TEMP_ID',
        'image_data': {
            'caption': 'A picture of a cup of coffee'
        }
    },
    'object_id': 'ND6EA5AAJEO5WL3JNNIAQA32'
}

result = catalog_api.create_catalog_image(
    request=request
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Catalog Image

Uploads a new image file to replace the existing one in the specified [CatalogImage](../../doc/models/catalog-image.md) object.

This `UpdateCatalogImage` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image file part in
JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

```python
def update_catalog_image(self,
                        image_id,
                        request=None,
                        image_file=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `image_id` | `str` | Template, Required | The ID of the `CatalogImage` object to update the encapsulated image file. |
| `request` | [`Update Catalog Image Request`](../../doc/models/update-catalog-image-request.md) | Form (JSON-Encoded), Optional | - |
| `image_file` | `typing.BinaryIO` | Form, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Catalog Image Response`](../../doc/models/update-catalog-image-response.md).

## Example Usage

```python
image_id = 'image_id4'

request = {
    'idempotency_key': '528dea59-7bfb-43c1-bd48-4a6bba7dd61f86'
}

result = catalog_api.update_catalog_image(
    image_id,
    request=request
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Catalog Info

Retrieves information about the Square Catalog API, such as batch size
limits that can be used by the `BatchUpsertCatalogObjects` endpoint.

```python
def catalog_info(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Catalog Info Response`](../../doc/models/catalog-info-response.md).

## Example Usage

```python
result = catalog_api.catalog_info()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Catalog

Returns a list of all [CatalogObject](../../doc/models/catalog-object.md)s of the specified types in the catalog.

The `types` parameter is specified as a comma-separated list of the [CatalogObjectType](../../doc/models/catalog-object-type.md) values,
for example, "`ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`".

__Important:__ ListCatalog does not return deleted catalog items. To retrieve
deleted catalog items, use [SearchCatalogObjects](../../doc/api/catalog.md#search-catalog-objects)
and set the `include_deleted_objects` attribute value to `true`.

```python
def list_catalog(self,
                cursor=None,
                types=None,
                catalog_version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Query, Optional | The pagination cursor returned in the previous response. Leave unset for an initial request.<br>The page size is currently set to be 100.<br>See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information. |
| `types` | `str` | Query, Optional | An optional case-insensitive, comma-separated list of object types to retrieve.<br><br>The valid values are defined in the [CatalogObjectType](entity:CatalogObjectType) enum, for example,<br>`ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`,<br>`MODIFIER`, `MODIFIER_LIST`, `IMAGE`, etc.<br><br>If this is unspecified, the operation returns objects of all the top level types at the version<br>of the Square API used to make the request. Object types that are nested onto other object types<br>are not included in the defaults.<br><br>At the current API version the default object types are:<br>ITEM, CATEGORY, TAX, DISCOUNT, MODIFIER_LIST,<br>PRICING_RULE, PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT,<br>SUBSCRIPTION_PLAN, ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION, QUICK_AMOUNT_SETTINGS. |
| `catalog_version` | `long\|int` | Query, Optional | The specific version of the catalog objects to be included in the response.<br>This allows you to retrieve historical versions of objects. The specified version value is matched against<br>the [CatalogObject](../../doc/models/catalog-object.md)s' `version` attribute.  If not included, results will be from the<br>current version of the catalog. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Catalog Response`](../../doc/models/list-catalog-response.md).

## Example Usage

```python
result = catalog_api.list_catalog()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upsert Catalog Object

Creates a new or updates the specified [CatalogObject](../../doc/models/catalog-object.md).

To ensure consistency, only one update request is processed at a time per seller account.
While one (batch or non-batch) update request is being processed, other (batched and non-batched)
update requests are rejected with the `429` error code.

```python
def upsert_catalog_object(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Upsert Catalog Object Request`](../../doc/models/upsert-catalog-object-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Upsert Catalog Object Response`](../../doc/models/upsert-catalog-object-response.md).

## Example Usage

```python
body = {
    'idempotency_key': 'af3d1afc-7212-4300-b463-0bfc5314a5ae',
    'object': {
        'type': 'ITEM',
        'id': '#Cocoa',
        'item_data': {
            'name': 'Cocoa',
            'abbreviation': 'Ch',
            'variations': [
                {
                    'type': 'ITEM_VARIATION',
                    'id': '#Small',
                    'item_variation_data': {
                        'item_id': '#Cocoa',
                        'name': 'Small',
                        'pricing_type': 'VARIABLE_PRICING'
                    }
                },
                {
                    'type': 'ITEM_VARIATION',
                    'id': '#Large',
                    'item_variation_data': {
                        'item_id': '#Cocoa',
                        'name': 'Large',
                        'pricing_type': 'FIXED_PRICING',
                        'price_money': {
                            'amount': 400,
                            'currency': 'USD'
                        }
                    }
                }
            ],
            'description_html': '<p><strong>Hot</strong> Chocolate</p>'
        }
    }
}

result = catalog_api.upsert_catalog_object(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Catalog Object

Deletes a single [CatalogObject](../../doc/models/catalog-object.md) based on the
provided ID and returns the set of successfully deleted IDs in the response.
Deletion is a cascading event such that all children of the targeted object
are also deleted. For example, deleting a [CatalogItem](../../doc/models/catalog-item.md)
will also delete all of its
[CatalogItemVariation](../../doc/models/catalog-item-variation.md) children.

To ensure consistency, only one delete request is processed at a time per seller account.
While one (batch or non-batch) delete request is being processed, other (batched and non-batched)
delete requests are rejected with the `429` error code.

```python
def delete_catalog_object(self,
                         object_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object_id` | `str` | Template, Required | The ID of the catalog object to be deleted. When an object is deleted, other<br>objects in the graph that depend on that object will be deleted as well (for example, deleting a<br>catalog item will delete its catalog item variations). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Catalog Object Response`](../../doc/models/delete-catalog-object-response.md).

## Example Usage

```python
object_id = 'object_id8'

result = catalog_api.delete_catalog_object(object_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Catalog Object

Returns a single [CatalogItem](../../doc/models/catalog-item.md) as a
[CatalogObject](../../doc/models/catalog-object.md) based on the provided ID. The returned
object includes all of the relevant [CatalogItem](../../doc/models/catalog-item.md)
information including: [CatalogItemVariation](../../doc/models/catalog-item-variation.md)
children, references to its
[CatalogModifierList](../../doc/models/catalog-modifier-list.md) objects, and the ids of
any [CatalogTax](../../doc/models/catalog-tax.md) objects that apply to it.

```python
def retrieve_catalog_object(self,
                           object_id,
                           include_related_objects=False,
                           catalog_version=None,
                           include_category_path_to_root=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object_id` | `str` | Template, Required | The object ID of any type of catalog objects to be retrieved. |
| `include_related_objects` | `bool` | Query, Optional | If `true`, the response will include additional objects that are related to the<br>requested objects. Related objects are defined as any objects referenced by ID by the results in the `objects` field<br>of the response. These objects are put in the `related_objects` field. Setting this to `true` is<br>helpful when the objects are needed for immediate display to a user.<br>This process only goes one level deep. Objects referenced by the related objects will not be included. For example,<br><br>if the `objects` field of the response contains a CatalogItem, its associated<br>CatalogCategory objects, CatalogTax objects, CatalogImage objects and<br>CatalogModifierLists will be returned in the `related_objects` field of the<br>response. If the `objects` field of the response contains a CatalogItemVariation,<br>its parent CatalogItem will be returned in the `related_objects` field of<br>the response.<br><br>Default value: `false`<br>**Default**: `False` |
| `catalog_version` | `long\|int` | Query, Optional | Requests objects as of a specific version of the catalog. This allows you to retrieve historical<br>versions of objects. The value to retrieve a specific version of an object can be found<br>in the version field of [CatalogObject](../../doc/models/catalog-object.md)s. If not included, results will<br>be from the current version of the catalog. |
| `include_category_path_to_root` | `bool` | Query, Optional | Specifies whether or not to include the `path_to_root` list for each returned category instance. The `path_to_root` list consists<br>of `CategoryPathToRootNode` objects and specifies the path that starts with the immediate parent category of the returned category<br>and ends with its root category. If the returned category is a top-level category, the `path_to_root` list is empty and is not returned<br>in the response payload.<br>**Default**: `False` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Catalog Object Response`](../../doc/models/retrieve-catalog-object-response.md).

## Example Usage

```python
object_id = 'object_id8'

include_related_objects = False

include_category_path_to_root = False

result = catalog_api.retrieve_catalog_object(
    object_id,
    include_related_objects=include_related_objects,
    include_category_path_to_root=include_category_path_to_root
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Catalog Objects

Searches for [CatalogObject](../../doc/models/catalog-object.md) of any type by matching supported search attribute values,
excluding custom attribute values on items or item variations, against one or more of the specified query filters.

This (`SearchCatalogObjects`) endpoint differs from the [SearchCatalogItems](../../doc/api/catalog.md#search-catalog-items)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints have different call conventions, including the query filter formats.

```python
def search_catalog_objects(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Catalog Objects Request`](../../doc/models/search-catalog-objects-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Search Catalog Objects Response`](../../doc/models/search-catalog-objects-response.md).

## Example Usage

```python
body = {
    'object_types': [
        'ITEM'
    ],
    'query': {
        'prefix_query': {
            'attribute_name': 'name',
            'attribute_prefix': 'tea'
        }
    },
    'limit': 100
}

result = catalog_api.search_catalog_objects(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Catalog Items

Searches for catalog items or item variations by matching supported search attribute values, including
custom attribute values, against one or more of the specified query filters.

This (`SearchCatalogItems`) endpoint differs from the [SearchCatalogObjects](../../doc/api/catalog.md#search-catalog-objects)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints use different call conventions, including the query filter formats.

```python
def search_catalog_items(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Catalog Items Request`](../../doc/models/search-catalog-items-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Search Catalog Items Response`](../../doc/models/search-catalog-items-response.md).

## Example Usage

```python
body = {
    'text_filter': 'red',
    'category_ids': [
        'WINE_CATEGORY_ID'
    ],
    'stock_levels': [
        'OUT',
        'LOW'
    ],
    'enabled_location_ids': [
        'ATL_LOCATION_ID'
    ],
    'limit': 100,
    'sort_order': 'ASC',
    'product_types': [
        'REGULAR'
    ],
    'custom_attribute_filters': [
        {
            'custom_attribute_definition_id': 'VEGAN_DEFINITION_ID',
            'bool_filter': True
        },
        {
            'custom_attribute_definition_id': 'BRAND_DEFINITION_ID',
            'string_filter': 'Dark Horse'
        },
        {
            'key': 'VINTAGE',
            'number_filter': {
                'min': '2017',
                'max': '2018'
            }
        },
        {
            'custom_attribute_definition_id': 'VARIETAL_DEFINITION_ID'
        }
    ]
}

result = catalog_api.search_catalog_items(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Item Modifier Lists

Updates the [CatalogModifierList](../../doc/models/catalog-modifier-list.md) objects
that apply to the targeted [CatalogItem](../../doc/models/catalog-item.md) without having
to perform an upsert on the entire item.

```python
def update_item_modifier_lists(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Update Item Modifier Lists Request`](../../doc/models/update-item-modifier-lists-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Item Modifier Lists Response`](../../doc/models/update-item-modifier-lists-response.md).

## Example Usage

```python
body = {
    'item_ids': [
        'H42BRLUJ5KTZTTMPVSLFAACQ',
        '2JXOBJIHCWBQ4NZ3RIXQGJA6'
    ],
    'modifier_lists_to_enable': [
        'H42BRLUJ5KTZTTMPVSLFAACQ',
        '2JXOBJIHCWBQ4NZ3RIXQGJA6'
    ],
    'modifier_lists_to_disable': [
        '7WRC16CJZDVLSNDQ35PP6YAD'
    ]
}

result = catalog_api.update_item_modifier_lists(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Item Taxes

Updates the [CatalogTax](../../doc/models/catalog-tax.md) objects that apply to the
targeted [CatalogItem](../../doc/models/catalog-item.md) without having to perform an
upsert on the entire item.

```python
def update_item_taxes(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Update Item Taxes Request`](../../doc/models/update-item-taxes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Item Taxes Response`](../../doc/models/update-item-taxes-response.md).

## Example Usage

```python
body = {
    'item_ids': [
        'H42BRLUJ5KTZTTMPVSLFAACQ',
        '2JXOBJIHCWBQ4NZ3RIXQGJA6'
    ],
    'taxes_to_enable': [
        '4WRCNHCJZDVLSNDQ35PP6YAD'
    ],
    'taxes_to_disable': [
        'AQCEGCEBBQONINDOHRGZISEX'
    ]
}

result = catalog_api.update_item_taxes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

