# Customer Segments

```python
customer_segments_api = client.customer_segments
```

## Class Name

`CustomerSegmentsApi`

## Methods

* [List Customer Segments](/doc/customer-segments.md#list-customer-segments)
* [Retrieve Customer Segment](/doc/customer-segments.md#retrieve-customer-segment)

## List Customer Segments

Retrieves the list of customer segments of a business.

```python
def list_customer_segments(self,
                          cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Query, Optional | A pagination cursor returned by previous calls to __ListCustomerSegments__.<br>Used to retrieve the next set of query results.<br><br>See the [Pagination guide](https://developer.squareup.com/docs/docs/working-with-apis/pagination) for more information. |

### Response Type

[`List Customer Segments Response`](/doc/models/list-customer-segments-response.md)

### Example Usage

```python
cursor = 'cursor6'

result = customer_segments_api.list_customer_segments(cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Customer Segment

Retrieves a specific customer segment as identified by the `segment_id` value.

```python
def retrieve_customer_segment(self,
                             segment_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segment_id` | `string` | Template, Required | The Square-issued ID of the customer segment. |

### Response Type

[`Retrieve Customer Segment Response`](/doc/models/retrieve-customer-segment-response.md)

### Example Usage

```python
segment_id = 'segment_id4'

result = customer_segments_api.retrieve_customer_segment(segment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

