## List Team Member Wages Response

The response to a request for a set of `TeamMemberWage` objects. Contains
a set of `TeamMemberWage`.

### Structure

`ListTeamMemberWagesResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_wages` | [`List of Team Member Wage`](/doc/models/team-member-wage.md) | Optional | A page of Team Member Wage results. |
| `cursor` | `string` | Optional | Value supplied in the subsequent request to fetch the next next page<br>of Team Member Wage results. |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |

### Example (as JSON)

```json
{
  "team_member_wages": [
    {
      "id": "pXS3qCv7BERPnEGedM4S8mhm",
      "team_member_id": "33fJchumvVdJwxV0H6L9",
      "title": "Manager",
      "hourly_rate": {
        "amount": 3250,
        "currency": "USD"
      }
    },
    {
      "id": "rZduCkzYDUVL3ovh1sQgbue6",
      "team_member_id": "33fJchumvVdJwxV0H6L9",
      "title": "Cook",
      "hourly_rate": {
        "amount": 2600,
        "currency": "USD"
      }
    },
    {
      "id": "FxLbs5KpPUHa8wyt5ctjubDX",
      "team_member_id": "33fJchumvVdJwxV0H6L9",
      "title": "Barista",
      "hourly_rate": {
        "amount": 1600,
        "currency": "USD"
      }
    },
    {
      "id": "vD1wCgijMDR3cX5TPnu7VXto",
      "team_member_id": "33fJchumvVdJwxV0H6L9",
      "title": "Cashier",
      "hourly_rate": {
        "amount": 1700,
        "currency": "USD"
      }
    }
  ],
  "cursor": "2fofTniCgT0yIPAq26kmk0YyFQJZfbWkh73OOnlTHmTAx13NgED"
}
```

