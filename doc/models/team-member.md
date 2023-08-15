
# Team Member

A record representing an individual team member for a business.

## Structure

`Team Member`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique ID for the team member. |
| `reference_id` | `str` | Optional | A second ID used to associate the team member with an entity in another system. |
| `is_owner` | `bool` | Optional | Whether the team member is the owner of the Square account. |
| `status` | [`str (Team Member Status)`](../../doc/models/team-member-status.md) | Optional | Enumerates the possible statuses the team member can have within a business. |
| `given_name` | `str` | Optional | The given name (that is, the first name) associated with the team member. |
| `family_name` | `str` | Optional | The family name (that is, the last name) associated with the team member. |
| `email_address` | `str` | Optional | The email address associated with the team member. |
| `phone_number` | `str` | Optional | The team member's phone number, in E.164 format. For example:<br>+14155552671 - the country code is 1 for US<br>+551155256325 - the country code is 55 for BR |
| `created_at` | `str` | Optional | The timestamp, in RFC 3339 format, describing when the team member was created.<br>For example, "2018-10-04T04:00:00-07:00" or "2019-02-05T12:00:00Z". |
| `updated_at` | `str` | Optional | The timestamp, in RFC 3339 format, describing when the team member was last updated.<br>For example, "2018-10-04T04:00:00-07:00" or "2019-02-05T12:00:00Z". |
| `assigned_locations` | [`Team Member Assigned Locations`](../../doc/models/team-member-assigned-locations.md) | Optional | An object that represents a team member's assignment to locations. |

## Example (as JSON)

```json
{
  "id": "id0",
  "reference_id": "reference_id2",
  "is_owner": false,
  "status": "ACTIVE",
  "given_name": "given_name2"
}
```

