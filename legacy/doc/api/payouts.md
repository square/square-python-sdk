# Payouts

```python
payouts_api = client.payouts
```

## Class Name

`PayoutsApi`

## Methods

* [List Payouts](../../doc/api/payouts.md#list-payouts)
* [Get Payout](../../doc/api/payouts.md#get-payout)
* [List Payout Entries](../../doc/api/payouts.md#list-payout-entries)


# List Payouts

Retrieves a list of all payouts for the default location.
You can filter payouts by location ID, status, time range, and order them in ascending or descending order.
To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

```python
def list_payouts(self,
                location_id=None,
                status=None,
                begin_time=None,
                end_time=None,
                sort_order=None,
                cursor=None,
                limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Query, Optional | The ID of the location for which to list the payouts.<br>By default, payouts are returned for the default (main) location associated with the seller. |
| `status` | [`str (Payout Status)`](../../doc/models/payout-status.md) | Query, Optional | If provided, only payouts with the given status are returned. |
| `begin_time` | `str` | Query, Optional | The timestamp for the beginning of the payout creation time, in RFC 3339 format.<br>Inclusive. Default: The current time minus one year. |
| `end_time` | `str` | Query, Optional | The timestamp for the end of the payout creation time, in RFC 3339 format.<br>Default: The current time. |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Query, Optional | The order in which payouts are listed. |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>If request parameters change between requests, subsequent results may contain duplicates or missing records. |
| `limit` | `int` | Query, Optional | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br>The default value of 100 is also the maximum allowed value. If the provided value is<br>greater than 100, it is ignored and the default value is used instead.<br>Default: `100` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Payouts Response`](../../doc/models/list-payouts-response.md).

## Example Usage

```python
result = payouts_api.list_payouts()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Payout

Retrieves details of a specific payout identified by a payout ID.
To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

```python
def get_payout(self,
              payout_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payout_id` | `str` | Template, Required | The ID of the payout to retrieve the information for. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Get Payout Response`](../../doc/models/get-payout-response.md).

## Example Usage

```python
payout_id = 'payout_id6'

result = payouts_api.get_payout(payout_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Payout Entries

Retrieves a list of all payout entries for a specific payout.
To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

```python
def list_payout_entries(self,
                       payout_id,
                       sort_order=None,
                       cursor=None,
                       limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payout_id` | `str` | Template, Required | The ID of the payout to retrieve the information for. |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Query, Optional | The order in which payout entries are listed. |
| `cursor` | `str` | Query, Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>If request parameters change between requests, subsequent results may contain duplicates or missing records. |
| `limit` | `int` | Query, Optional | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br>The default value of 100 is also the maximum allowed value. If the provided value is<br>greater than 100, it is ignored and the default value is used instead.<br>Default: `100` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Payout Entries Response`](../../doc/models/list-payout-entries-response.md).

## Example Usage

```python
payout_id = 'payout_id6'

result = payouts_api.list_payout_entries(payout_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

