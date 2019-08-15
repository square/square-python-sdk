## Retrieve Employee Response

Defines the fields that are included in the response body of
a request to the RetrieveEmployee endpoint.

One of `errors` or `employee` is present in a given response (never both).

### Structure

`RetrieveEmployeeResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee` | [`Employee`](/doc/models/employee.md) | Optional | An employee created in the **Square Dashboard** account of a business. <br>Used by the Labor API. |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |

### Example (as JSON)

```json
{
  "employee": null,
  "errors": null
}
```

