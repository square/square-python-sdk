
# Team Member Booking Profile

The booking profile of a seller's team member, including the team member's ID, display name, description and whether the team member can be booked as a service provider.

## Structure

`Team Member Booking Profile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_member_id` | `string` | Optional | The ID of the [TeamMember](#type-TeamMember) object for the team member associated with the booking profile. |
| `description` | `string` | Optional | The description of the team member. |
| `display_name` | `string` | Optional | The display name of the team member. |
| `is_bookable` | `bool` | Optional | Indicates whether the team member can be booked through the Bookings API or the seller's online booking channel or site (`true) or not (`false`). |
| `profile_image_url` | `string` | Optional | The URL of the team member's image for the bookings profile. |

## Example (as JSON)

```json
{
  "team_member_id": "team_member_id0",
  "description": "description0",
  "display_name": "display_name0",
  "is_bookable": false,
  "profile_image_url": "profile_image_url6"
}
```

