# Labor

```python
labor_api = client.labor
```

## Class Name

`LaborApi`

## Methods

* [List Break Types](/doc/labor.md#list-break-types)
* [Create Break Type](/doc/labor.md#create-break-type)
* [Delete Break Type](/doc/labor.md#delete-break-type)
* [Get Break Type](/doc/labor.md#get-break-type)
* [Update Break Type](/doc/labor.md#update-break-type)
* [List Employee Wages](/doc/labor.md#list-employee-wages)
* [Get Employee Wage](/doc/labor.md#get-employee-wage)
* [Create Shift](/doc/labor.md#create-shift)
* [Search Shifts](/doc/labor.md#search-shifts)
* [Delete Shift](/doc/labor.md#delete-shift)
* [Get Shift](/doc/labor.md#get-shift)
* [Update Shift](/doc/labor.md#update-shift)
* [List Team Member Wages](/doc/labor.md#list-team-member-wages)
* [Get Team Member Wage](/doc/labor.md#get-team-member-wage)
* [List Workweek Configs](/doc/labor.md#list-workweek-configs)
* [Update Workweek Config](/doc/labor.md#update-workweek-config)

## List Break Types

Returns a paginated list of `BreakType` instances for a business.

```python
def list_break_types(self,
                    location_id=None,
                    limit=None,
                    cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Query, Optional | Filter Break Types returned to only those that are associated with the<br>specified location. |
| `limit` | `int` | Query, Optional | Maximum number of Break Types to return per page. Can range between 1<br>and 200. The default is the maximum at 200. |
| `cursor` | `string` | Query, Optional | Pointer to the next page of Break Type results to fetch. |

### Response Type

[`List Break Types Response`](/doc/models/list-break-types-response.md)

### Example Usage

```python
location_id = 'location_id4'
limit = 172
cursor = 'cursor6'

result = labor_api.list_break_types(location_id, limit, cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Break Type

Creates a new `BreakType`.

A `BreakType` is a template for creating `Break` objects.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `break_name`
- `expected_duration`
- `is_paid`

You can only have 3 `BreakType` instances per location. If you attempt to add a 4th
`BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit of 3 breaks per location."
is returned.

```python
def create_break_type(self,
                     body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Break Type Request`](/doc/models/create-break-type-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Break Type Response`](/doc/models/create-break-type-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = 'PAD3NG5KSN2GL'
body['break_type'] = {}
body['break_type']['id'] = 'id2'
body['break_type']['location_id'] = 'CGJN03P1D08GF'
body['break_type']['break_name'] = 'Lunch Break'
body['break_type']['expected_duration'] = 'PT30M'
body['break_type']['is_paid'] = True
body['break_type']['version'] = 124
body['break_type']['created_at'] = 'created_at0'
body['break_type']['updated_at'] = 'updated_at8'

result = labor_api.create_break_type(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Delete Break Type

Deletes an existing `BreakType`.

A `BreakType` can be deleted even if it is referenced from a `Shift`.

```python
def delete_break_type(self,
                     id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | UUID for the `BreakType` being deleted. |

### Response Type

[`Delete Break Type Response`](/doc/models/delete-break-type-response.md)

### Example Usage

```python
id = 'id0'

result = labor_api.delete_break_type(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Break Type

Returns a single `BreakType` specified by id.

```python
def get_break_type(self,
                  id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | UUID for the `BreakType` being retrieved. |

### Response Type

[`Get Break Type Response`](/doc/models/get-break-type-response.md)

### Example Usage

```python
id = 'id0'

result = labor_api.get_break_type(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Break Type

Updates an existing `BreakType`.

```python
def update_break_type(self,
                     id,
                     body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | UUID for the `BreakType` being updated. |
| `body` | [`Update Break Type Request`](/doc/models/update-break-type-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Break Type Response`](/doc/models/update-break-type-response.md)

### Example Usage

```python
id = 'id0'
body = {}
body['break_type'] = {}
body['break_type']['id'] = 'id2'
body['break_type']['location_id'] = '26M7H24AZ9N6R'
body['break_type']['break_name'] = 'Lunch'
body['break_type']['expected_duration'] = 'PT50M'
body['break_type']['is_paid'] = True
body['break_type']['version'] = 1
body['break_type']['created_at'] = 'created_at0'
body['break_type']['updated_at'] = 'updated_at8'

result = labor_api.update_break_type(id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Employee Wages

Returns a paginated list of `EmployeeWage` instances for a business.

```python
def list_employee_wages(self,
                       employee_id=None,
                       limit=None,
                       cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_id` | `string` | Query, Optional | Filter wages returned to only those that are associated with the specified employee. |
| `limit` | `int` | Query, Optional | Maximum number of Employee Wages to return per page. Can range between<br>1 and 200. The default is the maximum at 200. |
| `cursor` | `string` | Query, Optional | Pointer to the next page of Employee Wage results to fetch. |

### Response Type

[`List Employee Wages Response`](/doc/models/list-employee-wages-response.md)

### Example Usage

```python
employee_id = 'employee_id0'
limit = 172
cursor = 'cursor6'

result = labor_api.list_employee_wages(employee_id, limit, cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Employee Wage

Returns a single `EmployeeWage` specified by id.

```python
def get_employee_wage(self,
                     id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | UUID for the `EmployeeWage` being retrieved. |

### Response Type

[`Get Employee Wage Response`](/doc/models/get-employee-wage-response.md)

### Example Usage

```python
id = 'id0'

result = labor_api.get_employee_wage(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Create Shift

Creates a new `Shift`.

A `Shift` represents a complete work day for a single employee.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `employee_id`
- `start_at`

An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when:
- The `status` of the new `Shift` is `OPEN` and the employee has another
shift with an `OPEN` status.
- The `start_at` date is in the future
- the `start_at` or `end_at` overlaps another shift for the same employee
- If `Break`s are set in the request, a break `start_at`
must not be before the `Shift.start_at`. A break `end_at` must not be after
the `Shift.end_at`

```python
def create_shift(self,
                body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Create Shift Request`](/doc/models/create-shift-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Create Shift Response`](/doc/models/create-shift-response.md)

### Example Usage

```python
body = {}
body['idempotency_key'] = 'HIDSNG5KS478L'
body['shift'] = {}
body['shift']['id'] = 'id8'
body['shift']['employee_id'] = 'employee_id2'
body['shift']['location_id'] = 'PAA1RJZZKXBFG'
body['shift']['timezone'] = 'timezone2'
body['shift']['start_at'] = '2019-01-25T03:11:00-05:00'
body['shift']['end_at'] = '2019-01-25T13:11:00-05:00'
body['shift']['wage'] = {}
body['shift']['wage']['title'] = 'Barista'
body['shift']['wage']['hourly_rate'] = {}
body['shift']['wage']['hourly_rate']['amount'] = 1100
body['shift']['wage']['hourly_rate']['currency'] = 'USD'
body['shift']['breaks'] = []

body['shift']['breaks'].append({})
body['shift']['breaks'][0]['id'] = 'id4'
body['shift']['breaks'][0]['start_at'] = '2019-01-25T06:11:00-05:00'
body['shift']['breaks'][0]['end_at'] = '2019-01-25T06:16:00-05:00'
body['shift']['breaks'][0]['break_type_id'] = 'REGS1EQR1TPZ5'
body['shift']['breaks'][0]['name'] = 'Tea Break'
body['shift']['breaks'][0]['expected_duration'] = 'PT5M'
body['shift']['breaks'][0]['is_paid'] = True

body['shift']['team_member_id'] = 'ormj0jJJZ5OZIzxrZYJI'

result = labor_api.create_shift(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Search Shifts

Returns a paginated list of `Shift` records for a business.
The list to be returned can be filtered by:
- Location IDs **and**
- employee IDs **and**
- shift status (`OPEN`, `CLOSED`) **and**
- shift start **and**
- shift end **and**
- work day details

The list can be sorted by:
- `start_at`
- `end_at`
- `created_at`
- `updated_at`

```python
def search_shifts(self,
                 body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Search Shifts Request`](/doc/models/search-shifts-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Search Shifts Response`](/doc/models/search-shifts-response.md)

### Example Usage

```python
body = {}
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['location_ids'] = ['location_ids2']
body['query']['filter']['employee_ids'] = ['employee_ids7']
body['query']['filter']['status'] = 'OPEN'
body['query']['filter']['start'] = {}
body['query']['filter']['start']['start_at'] = 'start_at8'
body['query']['filter']['start']['end_at'] = 'end_at4'
body['query']['filter']['end'] = {}
body['query']['filter']['end']['start_at'] = 'start_at2'
body['query']['filter']['end']['end_at'] = 'end_at0'
body['query']['filter']['workday'] = {}
body['query']['filter']['workday']['date_range'] = {}
body['query']['filter']['workday']['date_range']['start_date'] = 'start_date8'
body['query']['filter']['workday']['date_range']['end_date'] = 'end_date4'
body['query']['filter']['workday']['match_shifts_by'] = 'START_AT'
body['query']['filter']['workday']['default_timezone'] = 'default_timezone8'
body['query']['filter']['team_member_ids'] = ['team_member_ids9', 'team_member_ids0']
body['query']['sort'] = {}
body['query']['sort']['field'] = 'CREATED_AT'
body['query']['sort']['order'] = 'DESC'
body['limit'] = 164
body['cursor'] = 'cursor0'

result = labor_api.search_shifts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Delete Shift

Deletes a `Shift`.

```python
def delete_shift(self,
                id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | UUID for the `Shift` being deleted. |

### Response Type

[`Delete Shift Response`](/doc/models/delete-shift-response.md)

### Example Usage

```python
id = 'id0'

result = labor_api.delete_shift(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Shift

Returns a single `Shift` specified by id.

```python
def get_shift(self,
             id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | UUID for the `Shift` being retrieved. |

### Response Type

[`Get Shift Response`](/doc/models/get-shift-response.md)

### Example Usage

```python
id = 'id0'

result = labor_api.get_shift(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Shift

Updates an existing `Shift`.

When adding a `Break` to a `Shift`, any earlier `Breaks` in the `Shift` have
the `end_at` property set to a valid RFC-3339 datetime string.

When closing a `Shift`, all `Break` instances in the shift must be complete with `end_at`
set on each `Break`.

```python
def update_shift(self,
                id,
                body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | ID of the object being updated. |
| `body` | [`Update Shift Request`](/doc/models/update-shift-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Shift Response`](/doc/models/update-shift-response.md)

### Example Usage

```python
id = 'id0'
body = {}
body['shift'] = {}
body['shift']['id'] = 'id8'
body['shift']['employee_id'] = 'employee_id2'
body['shift']['location_id'] = 'PAA1RJZZKXBFG'
body['shift']['timezone'] = 'timezone2'
body['shift']['start_at'] = '2019-01-25T03:11:00-05:00'
body['shift']['end_at'] = '2019-01-25T13:11:00-05:00'
body['shift']['wage'] = {}
body['shift']['wage']['title'] = 'Bartender'
body['shift']['wage']['hourly_rate'] = {}
body['shift']['wage']['hourly_rate']['amount'] = 1500
body['shift']['wage']['hourly_rate']['currency'] = 'USD'
body['shift']['breaks'] = []

body['shift']['breaks'].append({})
body['shift']['breaks'][0]['id'] = 'X7GAQYVVRRG6P'
body['shift']['breaks'][0]['start_at'] = '2019-01-25T06:11:00-05:00'
body['shift']['breaks'][0]['end_at'] = '2019-01-25T06:16:00-05:00'
body['shift']['breaks'][0]['break_type_id'] = 'REGS1EQR1TPZ5'
body['shift']['breaks'][0]['name'] = 'Tea Break'
body['shift']['breaks'][0]['expected_duration'] = 'PT5M'
body['shift']['breaks'][0]['is_paid'] = True

body['shift']['version'] = 1
body['shift']['team_member_id'] = 'ormj0jJJZ5OZIzxrZYJI'

result = labor_api.update_shift(id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Team Member Wages

Returns a paginated list of `TeamMemberWage` instances for a business.

```python
def list_team_member_wages(self,
                          team_member_id=None,
                          limit=None,
                          cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Query, Optional | Filter wages returned to only those that are associated with the<br>specified team member. |
| `limit` | `int` | Query, Optional | Maximum number of Team Member Wages to return per page. Can range between<br>1 and 200. The default is the maximum at 200. |
| `cursor` | `string` | Query, Optional | Pointer to the next page of Employee Wage results to fetch. |

### Response Type

[`List Team Member Wages Response`](/doc/models/list-team-member-wages-response.md)

### Example Usage

```python
team_member_id = 'team_member_id0'
limit = 172
cursor = 'cursor6'

result = labor_api.list_team_member_wages(team_member_id, limit, cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Team Member Wage

Returns a single `TeamMemberWage` specified by id.

```python
def get_team_member_wage(self,
                        id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | UUID for the `TeamMemberWage` being retrieved. |

### Response Type

[`Get Team Member Wage Response`](/doc/models/get-team-member-wage-response.md)

### Example Usage

```python
id = 'id0'

result = labor_api.get_team_member_wage(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## List Workweek Configs

Returns a list of `WorkweekConfig` instances for a business.

```python
def list_workweek_configs(self,
                         limit=None,
                         cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Maximum number of Workweek Configs to return per page. |
| `cursor` | `string` | Query, Optional | Pointer to the next page of Workweek Config results to fetch. |

### Response Type

[`List Workweek Configs Response`](/doc/models/list-workweek-configs-response.md)

### Example Usage

```python
limit = 172
cursor = 'cursor6'

result = labor_api.list_workweek_configs(limit, cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Update Workweek Config

Updates a `WorkweekConfig`.

```python
def update_workweek_config(self,
                          id,
                          body)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | UUID for the `WorkweekConfig` object being updated. |
| `body` | [`Update Workweek Config Request`](/doc/models/update-workweek-config-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

### Response Type

[`Update Workweek Config Response`](/doc/models/update-workweek-config-response.md)

### Example Usage

```python
id = 'id0'
body = {}
body['workweek_config'] = {}
body['workweek_config']['id'] = 'id4'
body['workweek_config']['start_of_week'] = 'MON'
body['workweek_config']['start_of_day_local_time'] = '10:00'
body['workweek_config']['version'] = 10
body['workweek_config']['created_at'] = 'created_at2'
body['workweek_config']['updated_at'] = 'updated_at0'

result = labor_api.update_workweek_config(id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

