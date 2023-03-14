
# Employee

An employee object that is used by the external API.

## Structure

`Employee`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | UUID for this object. |
| `first_name` | `string` | Optional | The employee's first name. |
| `last_name` | `string` | Optional | The employee's last name. |
| `email` | `string` | Optional | The employee's email address |
| `phone_number` | `string` | Optional | The employee's phone number in E.164 format, i.e. "+12125554250" |
| `location_ids` | `List of string` | Optional | A list of location IDs where this employee has access to. |
| `status` | [`str (Employee Status)`](../../doc/models/employee-status.md) | Optional | The status of the Employee being retrieved. |
| `is_owner` | `bool` | Optional | Whether this employee is the owner of the merchant. Each merchant<br>has one owner employee, and that employee has full authority over<br>the account. |
| `created_at` | `string` | Optional | A read-only timestamp in RFC 3339 format. |
| `updated_at` | `string` | Optional | A read-only timestamp in RFC 3339 format. |

## Example (as JSON)

```json
{
  "id": null,
  "first_name": null,
  "last_name": null,
  "email": null,
  "phone_number": null,
  "location_ids": null,
  "status": null,
  "is_owner": null,
  "created_at": null,
  "updated_at": null
}
```

