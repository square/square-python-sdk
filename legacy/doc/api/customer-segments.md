# Customer Segments

```python
customer_segments_api = client.customer_segments
```

## Class Name

`CustomerSegmentsApi`

## Methods

* [List Customer Segments](../../doc/api/customer-segments.md#list-customer-segments)
* [Retrieve Customer Segment](../../doc/api/customer-segments.md#retrieve-customer-segment)


# List Customer Segments

Retrieves the list of customer segments of a business.

```python
def list_customer_segments(self,
                          cursor=None,
                          limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by previous calls to `ListCustomerSegments`.<br>This cursor is used to retrieve the next set of query results.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |
| `limit` | `int` | Query, Optional | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.<br>If the specified limit is less than 1 or greater than 50, Square returns a `400 VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default value is 50.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Customer Segments Response`](../../doc/models/list-customer-segments-response.md).

## Example Usage

```python
result = customer_segments_api.list_customer_segments()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Customer Segment

Retrieves a specific customer segment as identified by the `segment_id` value.

```python
def retrieve_customer_segment(self,
                             segment_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segment_id` | `str` | Template, Required | The Square-issued ID of the customer segment. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Customer Segment Response`](../../doc/models/retrieve-customer-segment-response.md).

## Example Usage

```python
segment_id = 'segment_id4'

result = customer_segments_api.retrieve_customer_segment(segment_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

