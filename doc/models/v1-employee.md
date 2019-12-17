## V1 Employee

Represents one of a business's employees.

### Structure

`V1Employee`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The employee's unique ID. |
| `first_name` | `string` |  | The employee's first name. |
| `last_name` | `string` |  | The employee's last name. |
| `role_ids` | `List of string` | Optional | The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee. |
| `authorized_location_ids` | `List of string` | Optional | The IDs of the locations the employee is allowed to clock in at. |
| `email` | `string` | Optional | The employee's email address. |
| `status` | [`str (V1 Employee Status)`]($m/V1EmployeeStatus) | Optional | - |
| `external_id` | `string` | Optional | An ID the merchant can set to associate the employee with an entity in another system. |
| `created_at` | `string` | Optional | The time when the employee entity was created, in ISO 8601 format. |
| `updated_at` | `string` | Optional | The time when the employee entity was most recently updated, in ISO 8601 format. |

### Example (as JSON)

```json
{
  "id": null,
  "first_name": "first_name0",
  "last_name": "last_name8",
  "role_ids": null,
  "authorized_location_ids": null,
  "email": null,
  "status": null,
  "external_id": null,
  "created_at": null,
  "updated_at": null
}
```

