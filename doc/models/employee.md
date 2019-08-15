## Employee

An employee created in the **Square Dashboard** account of a business. 
Used by the Labor API.

### Structure

`Employee`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | UUID for this `Employee`. |
| `first_name` | `string` | Optional | Given (first) name of the employee. |
| `last_name` | `string` | Optional | Family (last) name of the employee |
| `email` | `string` | Optional | Email of the employee |
| `phone_number` | `string` | Optional | Phone number of the employee in E.164 format, i.e. "+12125554250" |
| `location_ids` | `List of string` | Optional | A list of location IDs where this employee has access. |
| `status` | [`str (Employee Status)`](/doc/models/employee-status.md) | Optional | The status of the Employee being retrieved. |
| `created_at` | `string` | Optional | A read-only timestamp in RFC 3339 format. |
| `updated_at` | `string` | Optional | A read-only timestamp in RFC 3339 format. |

### Example (as JSON)

```json
{
  "id": null,
  "first_name": null,
  "last_name": null,
  "email": null,
  "phone_number": null,
  "location_ids": null,
  "status": null,
  "created_at": null,
  "updated_at": null
}
```

