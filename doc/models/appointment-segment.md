
# Appointment Segment

Defines an appointment segment of a booking.

## Structure

`Appointment Segment`

## Fields

| Name | Type | Description |
|  --- | --- | --- |
| `duration_minutes` | `int` | The time span in minutes of an appointment segment. |
| `service_variation_id` | `string` | The ID of the [CatalogItemVariation](#type-CatalogItemVariation) object representing the service booked in this segment. |
| `team_member_id` | `string` | The ID of the [TeamMember](#type-TeamMember) object representing the team member booked in this segment. |
| `service_variation_version` | `long|int` | The current version of the item variation representing the service booked in this segment. |

## Example (as JSON)

```json
{
  "duration_minutes": 144,
  "service_variation_id": "service_variation_id6",
  "team_member_id": "team_member_id0",
  "service_variation_version": 56
}
```

