
# Availability

Defines an appointment slot that encapsulates the appointment segments, location and  starting time avaialable for booking.

## Structure

`Availability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_at` | `string` | Optional | The RFC 3339 timestamp specifying the beginning time of the slot available for booking. |
| `location_id` | `string` | Optional | The ID of the location available for booking. |
| `appointment_segments` | [`List of Appointment Segment`](/doc/models/appointment-segment.md) | Optional | The list of appointment segments available for booking |

## Example (as JSON)

```json
{
  "start_at": "start_at2",
  "location_id": "location_id4",
  "appointment_segments": [
    {
      "duration_minutes": 4,
      "service_variation_id": "service_variation_id4",
      "team_member_id": "team_member_id0",
      "service_variation_version": 172,
      "intermission_minutes": 178,
      "any_team_member": false,
      "resource_ids": [
        "resource_ids0",
        "resource_ids1"
      ]
    }
  ]
}
```

