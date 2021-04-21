# V1 Employees

```python
v1_employees_api = client.v1_employees
```

## Class Name

`V1EmployeesApi`

## Methods

* [List Employees](/doc/api/v1-employees.md#list-employees)
* [Create Employee](/doc/api/v1-employees.md#create-employee)
* [Retrieve Employee](/doc/api/v1-employees.md#retrieve-employee)
* [Update Employee](/doc/api/v1-employees.md#update-employee)
* [List Employee Roles](/doc/api/v1-employees.md#list-employee-roles)
* [Create Employee Role](/doc/api/v1-employees.md#create-employee-role)
* [Retrieve Employee Role](/doc/api/v1-employees.md#retrieve-employee-role)
* [Update Employee Role](/doc/api/v1-employees.md#update-employee-role)


# List Employees

Provides summary information for all of a business's employees.

```python
def list_employees(self,
                  order=None,
                  begin_updated_at=None,
                  end_updated_at=None,
                  begin_created_at=None,
                  end_created_at=None,
                  status=None,
                  external_id=None,
                  limit=None,
                  batch_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Query, Optional | The order in which employees are listed in the response, based on their created_at field.      Default value: ASC |
| `begin_updated_at` | `string` | Query, Optional | If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format |
| `end_updated_at` | `string` | Query, Optional | If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format. |
| `begin_created_at` | `string` | Query, Optional | If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format. |
| `end_created_at` | `string` | Query, Optional | If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format. |
| `status` | [`str (V1 List Employees Request Status)`](/doc/models/v1-list-employees-request-status.md) | Query, Optional | If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE). |
| `external_id` | `string` | Query, Optional | If provided, the endpoint returns only employee entities with the specified external_id. |
| `limit` | `int` | Query, Optional | The maximum integer number of employee entities to return in a single response. Default 100, maximum 200. |
| `batch_token` | `string` | Query, Optional | A pagination cursor to retrieve the next set of results for your<br>original query to the endpoint. |

## Response Type

[`List of V1 Employee`](/doc/models/v1-employee.md)

## Example Usage

```python
order = 'DESC'
begin_updated_at = 'begin_updated_at6'
end_updated_at = 'end_updated_at4'
begin_created_at = 'begin_created_at6'
end_created_at = 'end_created_at8'
status = 'ACTIVE'
external_id = 'external_id6'
limit = 172
batch_token = 'batch_token2'

result = v1_employees_api.list_employees(order, begin_updated_at, end_updated_at, begin_created_at, end_created_at, status, external_id, limit, batch_token)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.body)
```


# Create Employee

Use the CreateEmployee endpoint to add an employee to a Square
account. Employees created with the Connect API have an initial status
of `INACTIVE`. Inactive employees cannot sign in to Square Point of Sale
until they are activated from the Square Dashboard. Employee status
cannot be changed with the Connect API.

Employee entities cannot be deleted. To disable employee profiles,
set the employee's status to <code>INACTIVE</code>

```python
def create_employee(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`V1 Employee`](/doc/models/v1-employee.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`V1 Employee`](/doc/models/v1-employee.md)

## Example Usage

```python
body = {}
body['id'] = 'id6'
body['first_name'] = 'first_name6'
body['last_name'] = 'last_name4'
body['role_ids'] = ['role_ids0', 'role_ids1']
body['authorized_location_ids'] = ['authorized_location_ids7', 'authorized_location_ids8']
body['email'] = 'email0'
body['status'] = 'ACTIVE'

result = v1_employees_api.create_employee(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.body)
```


# Retrieve Employee

Provides the details for a single employee.

```python
def retrieve_employee(self,
                     employee_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_id` | `string` | Template, Required | The employee's ID. |

## Response Type

[`V1 Employee`](/doc/models/v1-employee.md)

## Example Usage

```python
employee_id = 'employee_id0'

result = v1_employees_api.retrieve_employee(employee_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.body)
```


# Update Employee

UpdateEmployee

```python
def update_employee(self,
                   employee_id,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_id` | `string` | Template, Required | The ID of the role to modify. |
| `body` | [`V1 Employee`](/doc/models/v1-employee.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`V1 Employee`](/doc/models/v1-employee.md)

## Example Usage

```python
employee_id = 'employee_id0'
body = {}
body['id'] = 'id6'
body['first_name'] = 'first_name6'
body['last_name'] = 'last_name4'
body['role_ids'] = ['role_ids0', 'role_ids1']
body['authorized_location_ids'] = ['authorized_location_ids7', 'authorized_location_ids8']
body['email'] = 'email0'
body['status'] = 'ACTIVE'

result = v1_employees_api.update_employee(employee_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.body)
```


# List Employee Roles

Provides summary information for all of a business's employee roles.

```python
def list_employee_roles(self,
                       order=None,
                       limit=None,
                       batch_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`str (Sort Order)`](/doc/models/sort-order.md) | Query, Optional | The order in which employees are listed in the response, based on their created_at field.Default value: ASC |
| `limit` | `int` | Query, Optional | The maximum integer number of employee entities to return in a single response. Default 100, maximum 200. |
| `batch_token` | `string` | Query, Optional | A pagination cursor to retrieve the next set of results for your<br>original query to the endpoint. |

## Response Type

[`List of V1 Employee Role`](/doc/models/v1-employee-role.md)

## Example Usage

```python
order = 'DESC'
limit = 172
batch_token = 'batch_token2'

result = v1_employees_api.list_employee_roles(order, limit, batch_token)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.body)
```


# Create Employee Role

Creates an employee role you can then assign to employees.

Square accounts can include any number of roles that can be assigned to
employees. These roles define the actions and permissions granted to an
employee with that role. For example, an employee with a "Shift Manager"
role might be able to issue refunds in Square Point of Sale, whereas an
employee with a "Clerk" role might not.

Roles are assigned with the [V1UpdateEmployee](/doc/api/v1-employees.md#update-employee-role)
endpoint. An employee can have only one role at a time.

If an employee has no role, they have none of the permissions associated
with roles. All employees can accept payments with Square Point of Sale.

```python
def create_employee_role(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`V1 Employee Role`](/doc/models/v1-employee-role.md) | Body, Required | An EmployeeRole object with a name and permissions, and an optional owner flag. |

## Response Type

[`V1 Employee Role`](/doc/models/v1-employee-role.md)

## Example Usage

```python
body = {}
body['id'] = 'id6'
body['name'] = 'name6'
body['permissions'] = ['REGISTER_APPLY_RESTRICTED_DISCOUNTS', 'REGISTER_CHANGE_SETTINGS', 'REGISTER_EDIT_ITEM']
body['is_owner'] = False
body['created_at'] = 'created_at4'
body['updated_at'] = 'updated_at8'

result = v1_employees_api.create_employee_role(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.body)
```


# Retrieve Employee Role

Provides the details for a single employee role.

```python
def retrieve_employee_role(self,
                          role_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_id` | `string` | Template, Required | The role's ID. |

## Response Type

[`V1 Employee Role`](/doc/models/v1-employee-role.md)

## Example Usage

```python
role_id = 'role_id6'

result = v1_employees_api.retrieve_employee_role(role_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.body)
```


# Update Employee Role

Modifies the details of an employee role.

```python
def update_employee_role(self,
                        role_id,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_id` | `string` | Template, Required | The ID of the role to modify. |
| `body` | [`V1 Employee Role`](/doc/models/v1-employee-role.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

[`V1 Employee Role`](/doc/models/v1-employee-role.md)

## Example Usage

```python
role_id = 'role_id6'
body = {}
body['id'] = 'id6'
body['name'] = 'name6'
body['permissions'] = ['REGISTER_APPLY_RESTRICTED_DISCOUNTS', 'REGISTER_CHANGE_SETTINGS', 'REGISTER_EDIT_ITEM']
body['is_owner'] = False
body['created_at'] = 'created_at4'
body['updated_at'] = 'updated_at8'

result = v1_employees_api.update_employee_role(role_id, body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.body)
```

