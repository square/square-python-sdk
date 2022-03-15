
# List Team Member Booking Profiles Response

## Structure

`List Team Member Booking Profiles Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_booking_profiles` | [`List of Team Member Booking Profile`](../../doc/models/team-member-booking-profile.md) | Optional | The list of team member booking profiles. The results are returned in the ascending order of the time<br>when the team member booking profiles were last updated. Multiple booking profiles updated at the same time<br>are further sorted in the ascending order of their IDs. |
| `cursor` | `string` | Optional | The pagination cursor to be used in the subsequent request to get the next page of the results. Stop retrieving the next page of the results when the cursor is not set.<br>**Constraints**: *Maximum Length*: `65536` |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Errors that occurred during the request. |

## Example (as JSON)

```json
{
  "errors": [],
  "team_member_booking_profiles": [
    {
      "display_name": "Sandbox Seller",
      "is_bookable": true,
      "team_member_id": "TMXUrsBWWcHTt79t"
    },
    {
      "display_name": "Sandbox Staff",
      "is_bookable": true,
      "team_member_id": "TMaJcbiRqPIGZuS9"
    }
  ]
}
```

