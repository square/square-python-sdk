# Catalog

```python
catalog_api = client.catalog
```

## Class Name

`CatalogApi`

## Methods

* [Batch Delete Catalog Objects](/doc/catalog.md#batch-delete-catalog-objects)
* [Batch Retrieve Catalog Objects](/doc/catalog.md#batch-retrieve-catalog-objects)
* [Batch Upsert Catalog Objects](/doc/catalog.md#batch-upsert-catalog-objects)
* [Create Catalog Image](/doc/catalog.md#create-catalog-image)
* [Catalog Info](/doc/catalog.md#catalog-info)
* [List Catalog](/doc/catalog.md#list-catalog)
* [Upsert Catalog Object](/doc/catalog.md#upsert-catalog-object)
* [Delete Catalog Object](/doc/catalog.md#delete-catalog-object)
* [Retrieve Catalog Object](/doc/catalog.md#retrieve-catalog-object)
* [Search Catalog Objects](/doc/catalog.md#search-catalog-objects)
* [Search Catalog Items](/doc/catalog.md#search-catalog-items)
* [Update Item Modifier Lists](/doc/catalog.md#update-item-modifier-lists)
* [Update Item Taxes](/doc/catalog.md#update-item-taxes)

## Batch Delete Catalog Objects

Deletes a set of [CatalogItem](#type-catalogitem)s based on the
provided list of target IDs and returns a set of successfully deleted IDs in
the response. Deletion is a cascading event such that all children of the
targeted object are also deleted. For example, deleting a CatalogItem will
also delete all of its [CatalogItemVariation](#type-catalogitemvariation)
children.

`BatchDeleteCatalogObjects` succeeds even if only a portion of the targeted
IDs can be deleted. The response will only include IDs that were
actually deleted.

```python
def batch_delete_catalog_objects(self,
                                body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Delete Catalog Objects Request`](/doc/models/batch-delete-catalog-objects-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Delete Catalog Objects Response`](/doc/models/batch-delete-catalog-objects-response.md)

### Example Usage

```python
body = {}
body['object_ids'] = ['W62UWFY35CWMYGVWK6TWJDNI', 'AA27W3M2GGTF3H6AVPNB77CK']

result = catalog_api.batch_delete_catalog_objects(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Batch Retrieve Catalog Objects

Returns a set of objects based on the provided ID.
Each [CatalogItem](#type-catalogitem) returned in the set includes all of its
child information including: all of its
[CatalogItemVariation](#type-catalogitemvariation) objects, references to
its [CatalogModifierList](#type-catalogmodifierlist) objects, and the ids of
any [CatalogTax](#type-catalogtax) objects that apply to it.

```python
def batch_retrieve_catalog_objects(self,
                                  body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Retrieve Catalog Objects Request`](/doc/models/batch-retrieve-catalog-objects-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Retrieve Catalog Objects Response`](/doc/models/batch-retrieve-catalog-objects-response.md)

### Example Usage

```python
body = {}
body['object_ids'] = ['W62UWFY35CWMYGVWK6TWJDNI', 'AA27W3M2GGTF3H6AVPNB77CK']
body['include_related_objects'] = True

result = catalog_api.batch_retrieve_catalog_objects(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Batch Upsert Catalog Objects

Creates or updates up to 10,000 target objects based on the provided
list of objects. The target objects are grouped into batches and each batch is
inserted/updated in an all-or-nothing manner. If an object within a batch is
malformed in some way, or violates a database constraint, the entire batch
containing that item will be disregarded. However, other batches in the same
request may still succeed. Each batch may contain up to 1,000 objects, and
batches will be processed in order as long as the total object count for the
request (items, variations, modifier lists, discounts, and taxes) is no more
than 10,000.

```python
def batch_upsert_catalog_objects(self,
                                body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Batch Upsert Catalog Objects Request`](/doc/models/batch-upsert-catalog-objects-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Batch Upsert Catalog Objects Response`](/doc/models/batch-upsert-catalog-objects-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = '789ff020-f723-43a9-b4b5-43b5dc1fa3dc'
body['batches'] = []

body['batches'].append({})
body['batches'][0]['objects'] = []

body['batches'][0]['objects'].append({})
body['batches'][0]['objects'][0]['type'] = 'ITEM'
body['batches'][0]['objects'][0]['id'] = '#Tea'
body['batches'][0]['objects'][0]['updated_at'] = 'updated_at6'
body['batches'][0]['objects'][0]['version'] = 252
body['batches'][0]['objects'][0]['is_deleted'] = False
body['batches'][0]['objects'][0]['custom_attribute_values'] = {}
body['batches'][0]['objects'][0]['catalog_v1_ids'] = []

body['batches'][0]['objects'][0]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][0]['catalog_v1_ids'][0]['catalog_v1_id'] = 'catalog_v1_id4'
body['batches'][0]['objects'][0]['catalog_v1_ids'][0]['location_id'] = 'location_id4'

body['batches'][0]['objects'][0]['present_at_all_locations'] = True
body['batches'][0]['objects'][0]['item_data'] = {}
body['batches'][0]['objects'][0]['item_data']['name'] = 'Tea'
body['batches'][0]['objects'][0]['item_data']['description'] = 'Hot Leaf Juice'
body['batches'][0]['objects'][0]['item_data']['abbreviation'] = 'abbreviation0'
body['batches'][0]['objects'][0]['item_data']['label_color'] = 'label_color0'
body['batches'][0]['objects'][0]['item_data']['available_online'] = False
body['batches'][0]['objects'][0]['item_data']['category_id'] = '#Beverages'
body['batches'][0]['objects'][0]['item_data']['tax_ids'] = ['#SalesTax']
body['batches'][0]['objects'][0]['item_data']['variations'] = []

body['batches'][0]['objects'][0]['item_data']['variations'].append({})
body['batches'][0]['objects'][0]['item_data']['variations'][0]['type'] = 'ITEM_VARIATION'
body['batches'][0]['objects'][0]['item_data']['variations'][0]['id'] = '#Tea_Mug'
body['batches'][0]['objects'][0]['item_data']['variations'][0]['updated_at'] = 'updated_at5'
body['batches'][0]['objects'][0]['item_data']['variations'][0]['version'] = 99
body['batches'][0]['objects'][0]['item_data']['variations'][0]['is_deleted'] = True
body['batches'][0]['objects'][0]['item_data']['variations'][0]['custom_attribute_values'] = {}
body['batches'][0]['objects'][0]['item_data']['variations'][0]['catalog_v1_ids'] = []

body['batches'][0]['objects'][0]['item_data']['variations'][0]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][0]['item_data']['variations'][0]['catalog_v1_ids'][0]['catalog_v1_id'] = 'catalog_v1_id3'
body['batches'][0]['objects'][0]['item_data']['variations'][0]['catalog_v1_ids'][0]['location_id'] = 'location_id3'

body['batches'][0]['objects'][0]['item_data']['variations'][0]['present_at_all_locations'] = True
body['batches'][0]['objects'][0]['item_data']['variations'][0]['item_variation_data'] = {}
body['batches'][0]['objects'][0]['item_data']['variations'][0]['item_variation_data']['item_id'] = '#Tea'
body['batches'][0]['objects'][0]['item_data']['variations'][0]['item_variation_data']['name'] = 'Mug'
body['batches'][0]['objects'][0]['item_data']['variations'][0]['item_variation_data']['sku'] = 'sku9'
body['batches'][0]['objects'][0]['item_data']['variations'][0]['item_variation_data']['upc'] = 'upc7'
body['batches'][0]['objects'][0]['item_data']['variations'][0]['item_variation_data']['ordinal'] = 149
body['batches'][0]['objects'][0]['item_data']['variations'][0]['item_variation_data']['pricing_type'] = 'FIXED_PRICING'


body['batches'][0]['objects'].append({})
body['batches'][0]['objects'][1]['type'] = 'ITEM'
body['batches'][0]['objects'][1]['id'] = '#Coffee'
body['batches'][0]['objects'][1]['updated_at'] = 'updated_at7'
body['batches'][0]['objects'][1]['version'] = 253
body['batches'][0]['objects'][1]['is_deleted'] = True
body['batches'][0]['objects'][1]['custom_attribute_values'] = {}
body['batches'][0]['objects'][1]['catalog_v1_ids'] = []

body['batches'][0]['objects'][1]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][1]['catalog_v1_ids'][0]['catalog_v1_id'] = 'catalog_v1_id5'
body['batches'][0]['objects'][1]['catalog_v1_ids'][0]['location_id'] = 'location_id5'

body['batches'][0]['objects'][1]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][1]['catalog_v1_ids'][1]['catalog_v1_id'] = 'catalog_v1_id6'
body['batches'][0]['objects'][1]['catalog_v1_ids'][1]['location_id'] = 'location_id6'

body['batches'][0]['objects'][1]['present_at_all_locations'] = True
body['batches'][0]['objects'][1]['item_data'] = {}
body['batches'][0]['objects'][1]['item_data']['name'] = 'Coffee'
body['batches'][0]['objects'][1]['item_data']['description'] = 'Hot Bean Juice'
body['batches'][0]['objects'][1]['item_data']['abbreviation'] = 'abbreviation9'
body['batches'][0]['objects'][1]['item_data']['label_color'] = 'label_color9'
body['batches'][0]['objects'][1]['item_data']['available_online'] = True
body['batches'][0]['objects'][1]['item_data']['category_id'] = '#Beverages'
body['batches'][0]['objects'][1]['item_data']['tax_ids'] = ['#SalesTax']
body['batches'][0]['objects'][1]['item_data']['variations'] = []

body['batches'][0]['objects'][1]['item_data']['variations'].append({})
body['batches'][0]['objects'][1]['item_data']['variations'][0]['type'] = 'ITEM_VARIATION'
body['batches'][0]['objects'][1]['item_data']['variations'][0]['id'] = '#Coffee_Regular'
body['batches'][0]['objects'][1]['item_data']['variations'][0]['updated_at'] = 'updated_at4'
body['batches'][0]['objects'][1]['item_data']['variations'][0]['version'] = 100
body['batches'][0]['objects'][1]['item_data']['variations'][0]['is_deleted'] = False
body['batches'][0]['objects'][1]['item_data']['variations'][0]['custom_attribute_values'] = {}
body['batches'][0]['objects'][1]['item_data']['variations'][0]['catalog_v1_ids'] = []

body['batches'][0]['objects'][1]['item_data']['variations'][0]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][1]['item_data']['variations'][0]['catalog_v1_ids'][0]['catalog_v1_id'] = 'catalog_v1_id4'
body['batches'][0]['objects'][1]['item_data']['variations'][0]['catalog_v1_ids'][0]['location_id'] = 'location_id4'

body['batches'][0]['objects'][1]['item_data']['variations'][0]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][1]['item_data']['variations'][0]['catalog_v1_ids'][1]['catalog_v1_id'] = 'catalog_v1_id5'
body['batches'][0]['objects'][1]['item_data']['variations'][0]['catalog_v1_ids'][1]['location_id'] = 'location_id5'

body['batches'][0]['objects'][1]['item_data']['variations'][0]['present_at_all_locations'] = True
body['batches'][0]['objects'][1]['item_data']['variations'][0]['item_variation_data'] = {}
body['batches'][0]['objects'][1]['item_data']['variations'][0]['item_variation_data']['item_id'] = '#Coffee'
body['batches'][0]['objects'][1]['item_data']['variations'][0]['item_variation_data']['name'] = 'Regular'
body['batches'][0]['objects'][1]['item_data']['variations'][0]['item_variation_data']['sku'] = 'sku8'
body['batches'][0]['objects'][1]['item_data']['variations'][0]['item_variation_data']['upc'] = 'upc6'
body['batches'][0]['objects'][1]['item_data']['variations'][0]['item_variation_data']['ordinal'] = 150
body['batches'][0]['objects'][1]['item_data']['variations'][0]['item_variation_data']['pricing_type'] = 'FIXED_PRICING'

body['batches'][0]['objects'][1]['item_data']['variations'].append({})
body['batches'][0]['objects'][1]['item_data']['variations'][1]['type'] = 'ITEM_VARIATION'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['id'] = '#Coffee_Large'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['updated_at'] = 'updated_at3'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['version'] = 101
body['batches'][0]['objects'][1]['item_data']['variations'][1]['is_deleted'] = True
body['batches'][0]['objects'][1]['item_data']['variations'][1]['custom_attribute_values'] = {}
body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'] = []

body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'][0]['catalog_v1_id'] = 'catalog_v1_id5'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'][0]['location_id'] = 'location_id5'

body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'][1]['catalog_v1_id'] = 'catalog_v1_id6'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'][1]['location_id'] = 'location_id6'

body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'][2]['catalog_v1_id'] = 'catalog_v1_id7'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['catalog_v1_ids'][2]['location_id'] = 'location_id7'

body['batches'][0]['objects'][1]['item_data']['variations'][1]['present_at_all_locations'] = True
body['batches'][0]['objects'][1]['item_data']['variations'][1]['item_variation_data'] = {}
body['batches'][0]['objects'][1]['item_data']['variations'][1]['item_variation_data']['item_id'] = '#Coffee'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['item_variation_data']['name'] = 'Large'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['item_variation_data']['sku'] = 'sku7'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['item_variation_data']['upc'] = 'upc5'
body['batches'][0]['objects'][1]['item_data']['variations'][1]['item_variation_data']['ordinal'] = 151
body['batches'][0]['objects'][1]['item_data']['variations'][1]['item_variation_data']['pricing_type'] = 'FIXED_PRICING'


body['batches'][0]['objects'].append({})
body['batches'][0]['objects'][2]['type'] = 'CATEGORY'
body['batches'][0]['objects'][2]['id'] = '#Beverages'
body['batches'][0]['objects'][2]['updated_at'] = 'updated_at8'
body['batches'][0]['objects'][2]['version'] = 254
body['batches'][0]['objects'][2]['is_deleted'] = False
body['batches'][0]['objects'][2]['custom_attribute_values'] = {}
body['batches'][0]['objects'][2]['catalog_v1_ids'] = []

body['batches'][0]['objects'][2]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][2]['catalog_v1_ids'][0]['catalog_v1_id'] = 'catalog_v1_id6'
body['batches'][0]['objects'][2]['catalog_v1_ids'][0]['location_id'] = 'location_id6'

body['batches'][0]['objects'][2]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][2]['catalog_v1_ids'][1]['catalog_v1_id'] = 'catalog_v1_id7'
body['batches'][0]['objects'][2]['catalog_v1_ids'][1]['location_id'] = 'location_id7'

body['batches'][0]['objects'][2]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][2]['catalog_v1_ids'][2]['catalog_v1_id'] = 'catalog_v1_id8'
body['batches'][0]['objects'][2]['catalog_v1_ids'][2]['location_id'] = 'location_id8'

body['batches'][0]['objects'][2]['present_at_all_locations'] = True
body['batches'][0]['objects'][2]['category_data'] = {}
body['batches'][0]['objects'][2]['category_data']['name'] = 'Beverages'

body['batches'][0]['objects'].append({})
body['batches'][0]['objects'][3]['type'] = 'TAX'
body['batches'][0]['objects'][3]['id'] = '#SalesTax'
body['batches'][0]['objects'][3]['updated_at'] = 'updated_at9'
body['batches'][0]['objects'][3]['version'] = 255
body['batches'][0]['objects'][3]['is_deleted'] = True
body['batches'][0]['objects'][3]['custom_attribute_values'] = {}
body['batches'][0]['objects'][3]['catalog_v1_ids'] = []

body['batches'][0]['objects'][3]['catalog_v1_ids'].append({})
body['batches'][0]['objects'][3]['catalog_v1_ids'][0]['catalog_v1_id'] = 'catalog_v1_id7'
body['batches'][0]['objects'][3]['catalog_v1_ids'][0]['location_id'] = 'location_id7'

body['batches'][0]['objects'][3]['present_at_all_locations'] = True
body['batches'][0]['objects'][3]['tax_data'] = {}
body['batches'][0]['objects'][3]['tax_data']['name'] = 'Sales Tax'
body['batches'][0]['objects'][3]['tax_data']['calculation_phase'] = 'TAX_SUBTOTAL_PHASE'
body['batches'][0]['objects'][3]['tax_data']['inclusion_type'] = 'ADDITIVE'
body['batches'][0]['objects'][3]['tax_data']['percentage'] = '5.0'
body['batches'][0]['objects'][3]['tax_data']['applies_to_custom_amounts'] = True
body['batches'][0]['objects'][3]['tax_data']['enabled'] = True



result = catalog_api.batch_upsert_catalog_objects(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Catalog Image

Uploads an image file to be represented by an [CatalogImage](#type-catalogimage) object linked to an existing
[CatalogObject](#type-catalogobject) instance. A call to this endpoint can upload an image, link an image to
a catalog object, or do both.

This `CreateCatalogImage` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image file part in
JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

Additional information and an example cURL request can be found in the [Create a Catalog Image recipe](https://developer.squareup.com/docs/more-apis/catalog/cookbook/create-catalog-images).

```python
def create_catalog_image(self,
                        request=None,
                        image_file=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`Create Catalog Image Request`](/doc/models/create-catalog-image-request.md) | Form, Optional | - |
| `image_file` | `typing.BinaryIO` | Form, Optional | - |

### Response Type

[`Create Catalog Image Response`](/doc/models/create-catalog-image-response.md)

### Example Usage

```python
request = {}
request['idempotency_key'] = '528dea59-7bfb-43c1-bd48-4a6bba7dd61f86'
request['object_id'] = 'ND6EA5AAJEO5WL3JNNIAQA32'
request['image'] = {}
request['image']['type'] = 'IMAGE'
request['image']['id'] = '#TEMP_ID'
request['image']['updated_at'] = 'updated_at4'
request['image']['version'] = 68
request['image']['is_deleted'] = False
request['image']['custom_attribute_values'] = {}
request['image']['catalog_v1_ids'] = []

request['image']['catalog_v1_ids'].append({})
request['image']['catalog_v1_ids'][0]['catalog_v1_id'] = 'catalog_v1_id4'
request['image']['catalog_v1_ids'][0]['location_id'] = 'location_id4'

request['image']['image_data'] = {}
request['image']['image_data']['name'] = 'name0'
request['image']['image_data']['url'] = 'url4'
request['image']['image_data']['caption'] = 'A picture of a cup of coffee'
image_file = FileWrapper(open('dummy_file', 'rb'), 'optional-content-type')

result = catalog_api.create_catalog_image(request, image_file)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Catalog Info

Retrieves information about the Square Catalog API, such as batch size
limits that can be used by the `BatchUpsertCatalogObjects` endpoint.

```python
def catalog_info(self)
```

### Response Type

[`Catalog Info Response`](/doc/models/catalog-info-response.md)

### Example Usage

```python
result = catalog_api.catalog_info()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Catalog

Returns a list of [CatalogObject](#type-catalogobject)s that includes
all objects of a set of desired types (for example, all [CatalogItem](#type-catalogitem)
and [CatalogTax](#type-catalogtax) objects) in the catalog. The `types` parameter
is specified as a comma-separated list of valid [CatalogObject](#type-catalogobject) types:
`ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`.

__Important:__ ListCatalog does not return deleted catalog items. To retrieve
deleted catalog items, use SearchCatalogObjects and set `include_deleted_objects`
to `true`.

```python
def list_catalog(self,
                cursor=None,
                types=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Query, Optional | The pagination cursor returned in the previous response. Leave unset for an initial request.<br>See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |
| `types` | `string` | Query, Optional | An optional case-insensitive, comma-separated list of object types to retrieve, for example<br>`ITEM,ITEM_VARIATION,CATEGORY,IMAGE`.<br><br>The legal values are taken from the CatalogObjectType enum:<br>`ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`,<br>`MODIFIER`, `MODIFIER_LIST`, or `IMAGE`. |

### Response Type

[`List Catalog Response`](/doc/models/list-catalog-response.md)

### Example Usage

```python
cursor = 'cursor6'
types = 'types6'

result = catalog_api.list_catalog(cursor, types)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Upsert Catalog Object

Creates or updates the target [CatalogObject](#type-catalogobject).

```python
def upsert_catalog_object(self,
                         body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Upsert Catalog Object Request`](/doc/models/upsert-catalog-object-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Upsert Catalog Object Response`](/doc/models/upsert-catalog-object-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = 'af3d1afc-7212-4300-b463-0bfc5314a5ae'
body['object'] = {}
body['object']['type'] = 'ITEM'
body['object']['id'] = '#Cocoa'
body['object']['updated_at'] = 'updated_at8'
body['object']['version'] = 252
body['object']['is_deleted'] = False
body['object']['custom_attribute_values'] = {}
body['object']['catalog_v1_ids'] = []

body['object']['catalog_v1_ids'].append({})
body['object']['catalog_v1_ids'][0]['catalog_v1_id'] = 'catalog_v1_id0'
body['object']['catalog_v1_ids'][0]['location_id'] = 'location_id0'

body['object']['catalog_v1_ids'].append({})
body['object']['catalog_v1_ids'][1]['catalog_v1_id'] = 'catalog_v1_id1'
body['object']['catalog_v1_ids'][1]['location_id'] = 'location_id1'

body['object']['catalog_v1_ids'].append({})
body['object']['catalog_v1_ids'][2]['catalog_v1_id'] = 'catalog_v1_id2'
body['object']['catalog_v1_ids'][2]['location_id'] = 'location_id2'

body['object']['item_data'] = {}
body['object']['item_data']['name'] = 'Cocoa'
body['object']['item_data']['description'] = 'Hot chocolate'
body['object']['item_data']['abbreviation'] = 'Ch'
body['object']['item_data']['label_color'] = 'label_color4'
body['object']['item_data']['available_online'] = False

result = catalog_api.upsert_catalog_object(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Delete Catalog Object

Deletes a single [CatalogObject](#type-catalogobject) based on the
provided ID and returns the set of successfully deleted IDs in the response.
Deletion is a cascading event such that all children of the targeted object
are also deleted. For example, deleting a [CatalogItem](#type-catalogitem)
will also delete all of its
[CatalogItemVariation](#type-catalogitemvariation) children.

```python
def delete_catalog_object(self,
                         object_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object_id` | `string` | Template, Required | The ID of the catalog object to be deleted. When an object is deleted, other<br>objects in the graph that depend on that object will be deleted as well (for example, deleting a<br>catalog item will delete its catalog item variations). |

### Response Type

[`Delete Catalog Object Response`](/doc/models/delete-catalog-object-response.md)

### Example Usage

```python
object_id = 'object_id8'

result = catalog_api.delete_catalog_object(object_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Catalog Object

Returns a single [CatalogItem](#type-catalogitem) as a
[CatalogObject](#type-catalogobject) based on the provided ID. The returned
object includes all of the relevant [CatalogItem](#type-catalogitem)
information including: [CatalogItemVariation](#type-catalogitemvariation)
children, references to its
[CatalogModifierList](#type-catalogmodifierlist) objects, and the ids of
any [CatalogTax](#type-catalogtax) objects that apply to it.

```python
def retrieve_catalog_object(self,
                           object_id,
                           include_related_objects=False)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object_id` | `string` | Template, Required | The object ID of any type of catalog objects to be retrieved. |
| `include_related_objects` | `bool` | Query, Optional | If `true`, the response will include additional objects that are related to the<br>requested object, as follows:<br><br>If the `object` field of the response contains a CatalogItem,<br>its associated CatalogCategory, CatalogTax objects,<br>CatalogImages and CatalogModifierLists<br>will be returned in the `related_objects` field of the response. If the `object`<br>field of the response contains a CatalogItemVariation,<br>its parent CatalogItem will be returned in the `related_objects` field of<br>the response.<br><br>Default value: `false` |

### Response Type

[`Retrieve Catalog Object Response`](/doc/models/retrieve-catalog-object-response.md)

### Example Usage

```python
object_id = 'object_id8'
include_related_objects = False

result = catalog_api.retrieve_catalog_object(object_id, include_related_objects)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Catalog Objects

Searches for [CatalogObject](#type-CatalogObject) of any types against supported search attribute values, 
excluding custom attribute values on items or item variations, against one or more of the specified query expressions, 

This (`SearchCatalogObjects`) endpoint differs from the [SearchCatalogItems](#endpoint-Catalog-SearchCatalogItems)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints have different call conventions, including the query filter formats.

```python
def search_catalog_objects(self,
                          body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Catalog Objects Request`](/doc/models/search-catalog-objects-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Catalog Objects Response`](/doc/models/search-catalog-objects-response.md)

### Example Usage

```python
body = {}
body['cursor'] = 'cursor0'
body['object_types'] = ['ITEM']
body['include_deleted_objects'] = False
body['include_related_objects'] = False
body['begin_time'] = 'begin_time4'
body['query'] = {}
body['query']['sorted_attribute_query'] = {}
body['query']['sorted_attribute_query']['attribute_name'] = 'attribute_name6'
body['query']['sorted_attribute_query']['initial_attribute_value'] = 'initial_attribute_value4'
body['query']['sorted_attribute_query']['sort_order'] = 'DESC'
body['query']['exact_query'] = {}
body['query']['exact_query']['attribute_name'] = 'attribute_name2'
body['query']['exact_query']['attribute_value'] = 'attribute_value2'
body['query']['prefix_query'] = {}
body['query']['prefix_query']['attribute_name'] = 'name'
body['query']['prefix_query']['attribute_prefix'] = 'tea'
body['query']['range_query'] = {}
body['query']['range_query']['attribute_name'] = 'attribute_name6'
body['query']['range_query']['attribute_min_value'] = 14
body['query']['range_query']['attribute_max_value'] = 180
body['query']['text_query'] = {}
body['query']['text_query']['keywords'] = ['keywords7']
body['limit'] = 100

result = catalog_api.search_catalog_objects(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Catalog Items

Searches for catalog items or item variations by matching supported search attribute values, including
custom attribute values, against one or more of the specified query expressions, 

This (`SearchCatalogItems`) endpoint differs from the [SearchCatalogObjects](#endpoint-Catalog-SearchCatalogObjects)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints use different call conventions, including the query filter formats.

```python
def search_catalog_items(self,
                        body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Catalog Items Request`](/doc/models/search-catalog-items-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Catalog Items Response`](/doc/models/search-catalog-items-response.md)

### Example Usage

```python
body = {}
body['text_filter'] = 'red'
body['category_ids'] = ['WINE_CATEGORY_ID']
body['stock_levels'] = ['OUT', 'LOW']
body['enabled_location_ids'] = ['ATL_LOCATION_ID']
body['cursor'] = 'cursor0'
body['limit'] = 100
body['sort_order'] = 'ASC'
body['product_types'] = ['REGULAR']
body['custom_attribute_filters'] = []

body['custom_attribute_filters'].append({})
body['custom_attribute_filters'][0]['custom_attribute_definition_id'] = 'VEGAN_DEFINITION_ID'
body['custom_attribute_filters'][0]['key'] = 'key2'
body['custom_attribute_filters'][0]['string_filter'] = 'string_filter4'
body['custom_attribute_filters'][0]['number_filter'] = {}
body['custom_attribute_filters'][0]['number_filter']['min'] = 'min0'
body['custom_attribute_filters'][0]['number_filter']['max'] = 'max2'
body['custom_attribute_filters'][0]['selection_uids_filter'] = ['selection_uids_filter2', 'selection_uids_filter3']
body['custom_attribute_filters'][0]['bool_filter'] = True

body['custom_attribute_filters'].append({})
body['custom_attribute_filters'][1]['custom_attribute_definition_id'] = 'BRAND_DEFINITION_ID'
body['custom_attribute_filters'][1]['key'] = 'key3'
body['custom_attribute_filters'][1]['string_filter'] = 'Dark Horse'
body['custom_attribute_filters'][1]['number_filter'] = {}
body['custom_attribute_filters'][1]['number_filter']['min'] = 'min1'
body['custom_attribute_filters'][1]['number_filter']['max'] = 'max1'
body['custom_attribute_filters'][1]['selection_uids_filter'] = ['selection_uids_filter1']

body['custom_attribute_filters'].append({})
body['custom_attribute_filters'][2]['custom_attribute_definition_id'] = 'custom_attribute_definition_id8'
body['custom_attribute_filters'][2]['key'] = 'VINTAGE'
body['custom_attribute_filters'][2]['string_filter'] = 'string_filter6'
body['custom_attribute_filters'][2]['number_filter'] = {}
body['custom_attribute_filters'][2]['number_filter']['min'] = '2017'
body['custom_attribute_filters'][2]['number_filter']['max'] = '2018'
body['custom_attribute_filters'][2]['selection_uids_filter'] = ['selection_uids_filter0', 'selection_uids_filter1', 'selection_uids_filter2']

body['custom_attribute_filters'].append({})
body['custom_attribute_filters'][3]['custom_attribute_definition_id'] = 'VARIETAL_DEFINITION_ID'
body['custom_attribute_filters'][3]['key'] = 'key5'
body['custom_attribute_filters'][3]['string_filter'] = 'string_filter7'
body['custom_attribute_filters'][3]['number_filter'] = {}
body['custom_attribute_filters'][3]['number_filter']['min'] = 'min3'
body['custom_attribute_filters'][3]['number_filter']['max'] = 'max9'
body['custom_attribute_filters'][3]['selection_uids_filter'] = ['selection_uids_filter9', 'selection_uids_filter0']


result = catalog_api.search_catalog_items(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Item Modifier Lists

Updates the [CatalogModifierList](#type-catalogmodifierlist) objects
that apply to the targeted [CatalogItem](#type-catalogitem) without having
to perform an upsert on the entire item.

```python
def update_item_modifier_lists(self,
                              body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Update Item Modifier Lists Request`](/doc/models/update-item-modifier-lists-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Item Modifier Lists Response`](/doc/models/update-item-modifier-lists-response.md)

### Example Usage

```python
body = {}
body['item_ids'] = ['H42BRLUJ5KTZTTMPVSLFAACQ', '2JXOBJIHCWBQ4NZ3RIXQGJA6']
body['modifier_lists_to_enable'] = ['H42BRLUJ5KTZTTMPVSLFAACQ', '2JXOBJIHCWBQ4NZ3RIXQGJA6']
body['modifier_lists_to_disable'] = ['7WRC16CJZDVLSNDQ35PP6YAD']

result = catalog_api.update_item_modifier_lists(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Item Taxes

Updates the [CatalogTax](#type-catalogtax) objects that apply to the
targeted [CatalogItem](#type-catalogitem) without having to perform an
upsert on the entire item.

```python
def update_item_taxes(self,
                     body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Update Item Taxes Request`](/doc/models/update-item-taxes-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Item Taxes Response`](/doc/models/update-item-taxes-response.md)

### Example Usage

```python
body = {}
body['item_ids'] = ['H42BRLUJ5KTZTTMPVSLFAACQ', '2JXOBJIHCWBQ4NZ3RIXQGJA6']
body['taxes_to_enable'] = ['4WRCNHCJZDVLSNDQ35PP6YAD']
body['taxes_to_disable'] = ['AQCEGCEBBQONINDOHRGZISEX']

result = catalog_api.update_item_taxes(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

