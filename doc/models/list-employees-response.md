
# List Employees Response

## Structure

`List Employees Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employees` | [`List of Employee`](../../doc/models/employee.md) | Optional | - |
| `cursor` | `string` | Optional | The token to be used to retrieve the next page of results. |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |

## Example (as JSON)

```json
{
  "employees": null,
  "cursor": null,
  "errors": null
}
```

