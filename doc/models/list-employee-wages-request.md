
# List Employee Wages Request

A request for a set of `EmployeeWage` objects.

## Structure

`List Employee Wages Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_id` | `string` | Optional | Filter the returned wages to only those that are associated with the specified employee. |
| `limit` | `int` | Optional | The maximum number of `EmployeeWage` results to return per page. The number can range between<br>1 and 200. The default is 200.<br>**Constraints**: `>= 1`, `<= 200` |
| `cursor` | `string` | Optional | A pointer to the next page of `EmployeeWage` results to fetch. |

## Example (as JSON)

```json
{
  "employee_id": "employee_id0",
  "limit": 172,
  "cursor": "cursor6"
}
```

