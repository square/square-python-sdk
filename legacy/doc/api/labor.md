# Labor

```python
labor_api = client.labor
```

## Class Name

`LaborApi`

## Methods

* [List Break Types](../../doc/api/labor.md#list-break-types)
* [Create Break Type](../../doc/api/labor.md#create-break-type)
* [Delete Break Type](../../doc/api/labor.md#delete-break-type)
* [Get Break Type](../../doc/api/labor.md#get-break-type)
* [Update Break Type](../../doc/api/labor.md#update-break-type)
* [List Employee Wages](../../doc/api/labor.md#list-employee-wages)
* [Get Employee Wage](../../doc/api/labor.md#get-employee-wage)
* [Create Shift](../../doc/api/labor.md#create-shift)
* [Search Shifts](../../doc/api/labor.md#search-shifts)
* [Delete Shift](../../doc/api/labor.md#delete-shift)
* [Get Shift](../../doc/api/labor.md#get-shift)
* [Update Shift](../../doc/api/labor.md#update-shift)
* [List Team Member Wages](../../doc/api/labor.md#list-team-member-wages)
* [Get Team Member Wage](../../doc/api/labor.md#get-team-member-wage)
* [List Workweek Configs](../../doc/api/labor.md#list-workweek-configs)
* [Update Workweek Config](../../doc/api/labor.md#update-workweek-config)


# List Break Types

Returns a paginated list of `BreakType` instances for a business.

```python
def list_break_types(self,
                    location_id=None,
                    limit=None,
                    cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Query, Optional | Filter the returned `BreakType` results to only those that are associated with the<br>specified location. |
| `limit` | `int` | Query, Optional | The maximum number of `BreakType` results to return per page. The number can range between 1<br>and 200. The default is 200. |
| `cursor` | `str` | Query, Optional | A pointer to the next page of `BreakType` results to fetch. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Break Types Response`](../../doc/models/list-break-types-response.md).

## Example Usage

```python
result = labor_api.list_break_types()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Break Type

Creates a new `BreakType`.

A `BreakType` is a template for creating `Break` objects.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `break_name`
- `expected_duration`
- `is_paid`

You can only have three `BreakType` instances per location. If you attempt to add a fourth
`BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit of 3 breaks per location."
is returned.

```python
def create_break_type(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Break Type Request`](../../doc/models/create-break-type-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Break Type Response`](../../doc/models/create-break-type-response.md).

## Example Usage

```python
body = {
    'break_type': {
        'location_id': 'CGJN03P1D08GF',
        'break_name': 'Lunch Break',
        'expected_duration': 'PT30M',
        'is_paid': True
    },
    'idempotency_key': 'PAD3NG5KSN2GL'
}

result = labor_api.create_break_type(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Break Type

Deletes an existing `BreakType`.

A `BreakType` can be deleted even if it is referenced from a `Shift`.

```python
def delete_break_type(self,
                     id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The UUID for the `BreakType` being deleted. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Break Type Response`](../../doc/models/delete-break-type-response.md).

## Example Usage

```python
id = 'id0'

result = labor_api.delete_break_type(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Break Type

Returns a single `BreakType` specified by `id`.

```python
def get_break_type(self,
                  id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The UUID for the `BreakType` being retrieved. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Get Break Type Response`](../../doc/models/get-break-type-response.md).

## Example Usage

```python
id = 'id0'

result = labor_api.get_break_type(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Break Type

Updates an existing `BreakType`.

```python
def update_break_type(self,
                     id,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The UUID for the `BreakType` being updated. |
| `body` | [`Update Break Type Request`](../../doc/models/update-break-type-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Break Type Response`](../../doc/models/update-break-type-response.md).

## Example Usage

```python
id = 'id0'

body = {
    'break_type': {
        'location_id': '26M7H24AZ9N6R',
        'break_name': 'Lunch',
        'expected_duration': 'PT50M',
        'is_paid': True,
        'version': 1
    }
}

result = labor_api.update_break_type(
    id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Employee Wages

**This endpoint is deprecated.**

Returns a paginated list of `EmployeeWage` instances for a business.

```python
def list_employee_wages(self,
                       employee_id=None,
                       limit=None,
                       cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_id` | `str` | Query, Optional | Filter the returned wages to only those that are associated with the specified employee. |
| `limit` | `int` | Query, Optional | The maximum number of `EmployeeWage` results to return per page. The number can range between<br>1 and 200. The default is 200. |
| `cursor` | `str` | Query, Optional | A pointer to the next page of `EmployeeWage` results to fetch. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Employee Wages Response`](../../doc/models/list-employee-wages-response.md).

## Example Usage

```python
result = labor_api.list_employee_wages()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Employee Wage

**This endpoint is deprecated.**

Returns a single `EmployeeWage` specified by `id`.

```python
def get_employee_wage(self,
                     id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The UUID for the `EmployeeWage` being retrieved. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Get Employee Wage Response`](../../doc/models/get-employee-wage-response.md).

## Example Usage

```python
id = 'id0'

result = labor_api.get_employee_wage(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Shift

Creates a new `Shift`.

A `Shift` represents a complete workday for a single team member.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `team_member_id`
- `start_at`

An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when:

- The `status` of the new `Shift` is `OPEN` and the team member has another
  shift with an `OPEN` status.
- The `start_at` date is in the future.
- The `start_at` or `end_at` date overlaps another shift for the same team member.
- The `Break` instances are set in the request and a break `start_at`
  is before the `Shift.start_at`, a break `end_at` is after
  the `Shift.end_at`, or both.

```python
def create_shift(self,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Shift Request`](../../doc/models/create-shift-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Create Shift Response`](../../doc/models/create-shift-response.md).

## Example Usage

```python
body = {
    'shift': {
        'location_id': 'PAA1RJZZKXBFG',
        'start_at': '2019-01-25T03:11:00-05:00',
        'end_at': '2019-01-25T13:11:00-05:00',
        'wage': {
            'title': 'Barista',
            'hourly_rate': {
                'amount': 1100,
                'currency': 'USD'
            },
            'tip_eligible': True
        },
        'breaks': [
            {
                'start_at': '2019-01-25T06:11:00-05:00',
                'break_type_id': 'REGS1EQR1TPZ5',
                'name': 'Tea Break',
                'expected_duration': 'PT5M',
                'is_paid': True,
                'end_at': '2019-01-25T06:16:00-05:00'
            }
        ],
        'team_member_id': 'ormj0jJJZ5OZIzxrZYJI',
        'declared_cash_tip_money': {
            'amount': 500,
            'currency': 'USD'
        }
    },
    'idempotency_key': 'HIDSNG5KS478L'
}

result = labor_api.create_shift(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Search Shifts

Returns a paginated list of `Shift` records for a business.
The list to be returned can be filtered by:

- Location IDs
- Team member IDs
- Shift status (`OPEN` or `CLOSED`)
- Shift start
- Shift end
- Workday details

The list can be sorted by:

- `START_AT`
- `END_AT`
- `CREATED_AT`
- `UPDATED_AT`

```python
def search_shifts(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Shifts Request`](../../doc/models/search-shifts-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Search Shifts Response`](../../doc/models/search-shifts-response.md).

## Example Usage

```python
body = {
    'query': {
        'filter': {
            'workday': {
                'date_range': {
                    'start_date': '2019-01-20',
                    'end_date': '2019-02-03'
                },
                'match_shifts_by': 'START_AT',
                'default_timezone': 'America/Los_Angeles'
            }
        }
    },
    'limit': 100
}

result = labor_api.search_shifts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Shift

Deletes a `Shift`.

```python
def delete_shift(self,
                id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The UUID for the `Shift` being deleted. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Shift Response`](../../doc/models/delete-shift-response.md).

## Example Usage

```python
id = 'id0'

result = labor_api.delete_shift(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Shift

Returns a single `Shift` specified by `id`.

```python
def get_shift(self,
             id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The UUID for the `Shift` being retrieved. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Get Shift Response`](../../doc/models/get-shift-response.md).

## Example Usage

```python
id = 'id0'

result = labor_api.get_shift(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Shift

Updates an existing `Shift`.

When adding a `Break` to a `Shift`, any earlier `Break` instances in the `Shift` have
the `end_at` property set to a valid RFC-3339 datetime string.

When closing a `Shift`, all `Break` instances in the `Shift` must be complete with `end_at`
set on each `Break`.

```python
def update_shift(self,
                id,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the object being updated. |
| `body` | [`Update Shift Request`](../../doc/models/update-shift-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Shift Response`](../../doc/models/update-shift-response.md).

## Example Usage

```python
id = 'id0'

body = {
    'shift': {
        'location_id': 'PAA1RJZZKXBFG',
        'start_at': '2019-01-25T03:11:00-05:00',
        'end_at': '2019-01-25T13:11:00-05:00',
        'wage': {
            'title': 'Bartender',
            'hourly_rate': {
                'amount': 1500,
                'currency': 'USD'
            },
            'tip_eligible': True
        },
        'breaks': [
            {
                'start_at': '2019-01-25T06:11:00-05:00',
                'break_type_id': 'REGS1EQR1TPZ5',
                'name': 'Tea Break',
                'expected_duration': 'PT5M',
                'is_paid': True,
                'id': 'X7GAQYVVRRG6P',
                'end_at': '2019-01-25T06:16:00-05:00'
            }
        ],
        'version': 1,
        'team_member_id': 'ormj0jJJZ5OZIzxrZYJI',
        'declared_cash_tip_money': {
            'amount': 500,
            'currency': 'USD'
        }
    }
}

result = labor_api.update_shift(
    id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Team Member Wages

Returns a paginated list of `TeamMemberWage` instances for a business.

```python
def list_team_member_wages(self,
                          team_member_id=None,
                          limit=None,
                          cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `str` | Query, Optional | Filter the returned wages to only those that are associated with the<br>specified team member. |
| `limit` | `int` | Query, Optional | The maximum number of `TeamMemberWage` results to return per page. The number can range between<br>1 and 200. The default is 200. |
| `cursor` | `str` | Query, Optional | A pointer to the next page of `EmployeeWage` results to fetch. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Team Member Wages Response`](../../doc/models/list-team-member-wages-response.md).

## Example Usage

```python
result = labor_api.list_team_member_wages()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Team Member Wage

Returns a single `TeamMemberWage` specified by `id`.

```python
def get_team_member_wage(self,
                        id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The UUID for the `TeamMemberWage` being retrieved. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Get Team Member Wage Response`](../../doc/models/get-team-member-wage-response.md).

## Example Usage

```python
id = 'id0'

result = labor_api.get_team_member_wage(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Workweek Configs

Returns a list of `WorkweekConfig` instances for a business.

```python
def list_workweek_configs(self,
                         limit=None,
                         cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | The maximum number of `WorkweekConfigs` results to return per page. |
| `cursor` | `str` | Query, Optional | A pointer to the next page of `WorkweekConfig` results to fetch. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Workweek Configs Response`](../../doc/models/list-workweek-configs-response.md).

## Example Usage

```python
result = labor_api.list_workweek_configs()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Workweek Config

Updates a `WorkweekConfig`.

```python
def update_workweek_config(self,
                          id,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The UUID for the `WorkweekConfig` object being updated. |
| `body` | [`Update Workweek Config Request`](../../doc/models/update-workweek-config-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Update Workweek Config Response`](../../doc/models/update-workweek-config-response.md).

## Example Usage

```python
id = 'id0'

body = {
    'workweek_config': {
        'start_of_week': 'MON',
        'start_of_day_local_time': '10:00',
        'version': 10
    }
}

result = labor_api.update_workweek_config(
    id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

