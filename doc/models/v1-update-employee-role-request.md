## V1 Update Employee Role Request

### Structure

`V1UpdateEmployeeRoleRequest`

### Fields

| Name | Type | Description |
|  --- | --- | --- |
| `body` | [`V1 Employee Role`](/doc/models/v1-employee-role.md) | V1EmployeeRole |

### Example (as JSON)

```json
{
  "body": {
    "id": null,
    "name": "name6",
    "permissions": [
      "REGISTER_APPLY_RESTRICTED_DISCOUNTS",
      "REGISTER_CHANGE_SETTINGS",
      "REGISTER_EDIT_ITEM"
    ],
    "is_owner": null,
    "created_at": null,
    "updated_at": null
  }
}
```

