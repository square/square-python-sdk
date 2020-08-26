# Employees

```python
employees_api = client.employees
```

## Class Name

`EmployeesApi`

## Methods

* [List Employees](/doc/employees.md#list-employees)
* [Retrieve Employee](/doc/employees.md#retrieve-employee)

## List Employees

ListEmployees

```python
def list_employees(self,
                  location_id=None,
                  status=None,
                  limit=None,
                  cursor=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `string` | Query, Optional | - |
| `status` | [`str (Employee Status)`](/doc/models/employee-status.md) | Query, Optional | Specifies the EmployeeStatus to filter the employee by. |
| `limit` | `int` | Query, Optional | The number of employees to be returned on each page. |
| `cursor` | `string` | Query, Optional | The token required to retrieve the specified page of results. |

### Response Type

[`List Employees Response`](/doc/models/list-employees-response.md)

### Example Usage

```python
location_id = 'location_id4'
status = 'ACTIVE'
limit = 172
cursor = 'cursor6'

result = employees_api.list_employees(location_id, status, limit, cursor)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Employee

RetrieveEmployee

```python
def retrieve_employee(self,
                     id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | UUID for the employee that was requested. |

### Response Type

[`Retrieve Employee Response`](/doc/models/retrieve-employee-response.md)

### Example Usage

```python
id = 'id0'

result = employees_api.retrieve_employee(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

