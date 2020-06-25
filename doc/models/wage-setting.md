## Wage Setting

An object representing a team member's wage information.

### Structure

`WageSetting`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Optional | The unique ID of the `TeamMember` whom this wage setting describes. |
| `job_assignments` | [`List of Job Assignment`](/doc/models/job-assignment.md) | Optional | <b>Required</b> The ordered list of jobs that the team member is assigned to.<br>The first job assignment is considered the team member's "Primary Job".<br><br><br><b>Min Length 1    Max Length 12</b> |
| `is_overtime_exempt` | `bool` | Optional | Whether the team member is exempt from the overtime rules of the seller country. |
| `version` | `int` | Optional | Used for resolving concurrency issues; request will fail if version<br>provided does not match server version at time of request. If not provided,<br>Square executes a blind write, potentially overwriting data from another write. Read<br>about [optimistic concurrency](https://developer.squareup.com/docs/docs/working-with-apis/optimistic-concurrency)<br>in Square APIs for more information. |
| `created_at` | `string` | Optional | The timestamp in RFC 3339 format describing when the wage setting object was created.<br>Ex: "2018-10-04T04:00:00-07:00" or "2019-02-05T12:00:00Z" |
| `updated_at` | `string` | Optional | The timestamp in RFC 3339 format describing when the wage setting object was last updated.<br>Ex: "2018-10-04T04:00:00-07:00" or "2019-02-05T12:00:00Z" |

### Example (as JSON)

```json
{
  "team_member_id": null,
  "job_assignments": null,
  "is_overtime_exempt": null,
  "version": null,
  "created_at": null,
  "updated_at": null
}
```

