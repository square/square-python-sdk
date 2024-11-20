
# Update Wage Setting Request

Represents an update request for the `WageSetting` object describing a `TeamMember`.

## Structure

`Update Wage Setting Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wage_setting` | [`Wage Setting`](../../doc/models/wage-setting.md) | Required | An object representing a team member's wage information. |

## Example (as JSON)

```json
{
  "wage_setting": {
    "is_overtime_exempt": true,
    "job_assignments": [
      {
        "annual_rate": {
          "amount": 3000000,
          "currency": "USD"
        },
        "job_title": "Manager",
        "pay_type": "SALARY",
        "weekly_hours": 40,
        "hourly_rate": {
          "amount": 172,
          "currency": "LAK"
        }
      },
      {
        "hourly_rate": {
          "amount": 1200,
          "currency": "USD"
        },
        "job_title": "Cashier",
        "pay_type": "HOURLY",
        "annual_rate": {
          "amount": 232,
          "currency": "NIO"
        },
        "weekly_hours": 98
      }
    ],
    "team_member_id": "team_member_id8",
    "version": 130,
    "created_at": "created_at6"
  }
}
```

