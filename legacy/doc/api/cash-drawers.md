# Cash Drawers

```python
cash_drawers_api = client.cash_drawers
```

## Class Name

`CashDrawersApi`

## Methods

* [List Cash Drawer Shifts](../../doc/api/cash-drawers.md#list-cash-drawer-shifts)
* [Retrieve Cash Drawer Shift](../../doc/api/cash-drawers.md#retrieve-cash-drawer-shift)
* [List Cash Drawer Shift Events](../../doc/api/cash-drawers.md#list-cash-drawer-shift-events)


# List Cash Drawer Shifts

Provides the details for all of the cash drawer shifts for a location
in a date range.

```python
def list_cash_drawer_shifts(self,
                           location_id,
                           sort_order=None,
                           begin_time=None,
                           end_time=None,
                           limit=None,
                           cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Query, Required | The ID of the location to query for a list of cash drawer shifts. |
| `sort_order` | [`str (Sort Order)`](../../doc/models/sort-order.md) | Query, Optional | The order in which cash drawer shifts are listed in the response,<br>based on their opened_at field. Default value: ASC |
| `begin_time` | `str` | Query, Optional | The inclusive start time of the query on opened_at, in ISO 8601 format. |
| `end_time` | `str` | Query, Optional | The exclusive end date of the query on opened_at, in ISO 8601 format. |
| `limit` | `int` | Query, Optional | Number of cash drawer shift events in a page of results (200 by<br>default, 1000 max). |
| `cursor` | `str` | Query, Optional | Opaque cursor for fetching the next page of results. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Cash Drawer Shifts Response`](../../doc/models/list-cash-drawer-shifts-response.md).

## Example Usage

```python
location_id = 'location_id4'

result = cash_drawers_api.list_cash_drawer_shifts(location_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Cash Drawer Shift

Provides the summary details for a single cash drawer shift. See
[ListCashDrawerShiftEvents](../../doc/api/cash-drawers.md#list-cash-drawer-shift-events) for a list of cash drawer shift events.

```python
def retrieve_cash_drawer_shift(self,
                              location_id,
                              shift_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Query, Required | The ID of the location to retrieve cash drawer shifts from. |
| `shift_id` | `str` | Template, Required | The shift ID. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Cash Drawer Shift Response`](../../doc/models/retrieve-cash-drawer-shift-response.md).

## Example Usage

```python
location_id = 'location_id4'

shift_id = 'shift_id0'

result = cash_drawers_api.retrieve_cash_drawer_shift(
    location_id,
    shift_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Cash Drawer Shift Events

Provides a paginated list of events for a single cash drawer shift.

```python
def list_cash_drawer_shift_events(self,
                                 location_id,
                                 shift_id,
                                 limit=None,
                                 cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Query, Required | The ID of the location to list cash drawer shifts for. |
| `shift_id` | `str` | Template, Required | The shift ID. |
| `limit` | `int` | Query, Optional | Number of resources to be returned in a page of results (200 by<br>default, 1000 max). |
| `cursor` | `str` | Query, Optional | Opaque cursor for fetching the next page of results. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Cash Drawer Shift Events Response`](../../doc/models/list-cash-drawer-shift-events-response.md).

## Example Usage

```python
location_id = 'location_id4'

shift_id = 'shift_id0'

result = cash_drawers_api.list_cash_drawer_shift_events(
    location_id,
    shift_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

