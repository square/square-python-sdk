# Employees

```python
employees_api = client.employees
```

## Class Name

`EmployeesApi`

## Methods

* [List Employees](../../doc/api/employees.md#list-employees)
* [Retrieve Employee](../../doc/api/employees.md#retrieve-employee)


# List Employees

**This endpoint is deprecated.**

```python
def list_employees(self,
                  location_id=None,
                  status=None,
                  limit=None,
                  cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_id` | `str` | Query, Optional | - |
| `status` | [`str (Employee Status)`](../../doc/models/employee-status.md) | Query, Optional | Specifies the EmployeeStatus to filter the employee by. |
| `limit` | `int` | Query, Optional | The number of employees to be returned on each page. |
| `cursor` | `str` | Query, Optional | The token required to retrieve the specified page of results. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Employees Response`](../../doc/models/list-employees-response.md).

## Example Usage

```python
result = employees_api.list_employees()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Employee

**This endpoint is deprecated.**

```python
def retrieve_employee(self,
                     id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | UUID for the employee that was requested. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Employee Response`](../../doc/models/retrieve-employee-response.md).

## Example Usage

```python
id = 'id0'

result = employees_api.retrieve_employee(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

