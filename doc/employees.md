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

Gets a list of `Employee` objects for a business.

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
| `location_id` | `string` | Query, Optional | Filter employees returned to only those that are associated with the<br>specified location. |
| `status` | [`str (Employee Status)`](/doc/models/employee-status.md) | Query, Optional | Specifies the EmployeeStatus to filter the employee by. |
| `limit` | `int` | Query, Optional | The number of employees to be returned on each page. |
| `cursor` | `string` | Query, Optional | The token required to retrieve the specified page of results. |

### Response Type

[`List Employees Response`](/doc/models/list-employees-response.md)

### Example Usage

```python
result = employees_api.list_employees()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Retrieve Employee

Gets an `Employee` by Square-assigned employee `ID` (UUID)

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

