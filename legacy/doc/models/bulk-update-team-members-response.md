
# Bulk Update Team Members Response

Represents a response from a bulk update request containing the updated `TeamMember` objects or error messages.

## Structure

`Bulk Update Team Members Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_members` | [`Dict Str Update Team Member Response`](../../doc/models/update-team-member-response.md) | Optional | The successfully updated `TeamMember` objects. Each key is the `team_member_id` that maps to the `UpdateTeamMemberRequest`. |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | The errors that occurred during the request. |

## Example (as JSON)

```json
{
  "team_members": {
    "AFMwA08kR-MIF-3Vs0OE": {
      "team_member": {
        "assigned_locations": {
          "assignment_type": "ALL_CURRENT_AND_FUTURE_LOCATIONS"
        },
        "created_at": "2020-03-24T18:14:00Z",
        "email_address": "jane_smith@example.com",
        "family_name": "Smith",
        "given_name": "Jane",
        "id": "AFMwA08kR-MIF-3Vs0OE",
        "is_owner": false,
        "phone_number": "+14159223334",
        "reference_id": "reference_id_2",
        "status": "ACTIVE",
        "updated_at": "2020-03-24T18:18:00Z"
      },
      "errors": [
        {
          "category": "MERCHANT_SUBSCRIPTION_ERROR",
          "code": "INVALID_EXPIRATION",
          "detail": "detail6",
          "field": "field4"
        },
        {
          "category": "MERCHANT_SUBSCRIPTION_ERROR",
          "code": "INVALID_EXPIRATION",
          "detail": "detail6",
          "field": "field4"
        }
      ]
    },
    "fpgteZNMaf0qOK-a4t6P": {
      "team_member": {
        "assigned_locations": {
          "assignment_type": "EXPLICIT_LOCATIONS",
          "location_ids": [
            "GA2Y9HSJ8KRYT",
            "YSGH2WBKG94QZ"
          ]
        },
        "created_at": "2020-03-24T18:14:00Z",
        "email_address": "joe_doe@example.com",
        "family_name": "Doe",
        "given_name": "Joe",
        "id": "fpgteZNMaf0qOK-a4t6P",
        "is_owner": false,
        "phone_number": "+14159283333",
        "reference_id": "reference_id_1",
        "status": "ACTIVE",
        "updated_at": "2020-03-24T18:18:00Z"
      },
      "errors": [
        {
          "category": "MERCHANT_SUBSCRIPTION_ERROR",
          "code": "INVALID_EXPIRATION",
          "detail": "detail6",
          "field": "field4"
        },
        {
          "category": "MERCHANT_SUBSCRIPTION_ERROR",
          "code": "INVALID_EXPIRATION",
          "detail": "detail6",
          "field": "field4"
        }
      ]
    }
  },
  "errors": [
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "INVALID_EXPIRATION",
      "detail": "detail6",
      "field": "field4"
    }
  ]
}
```

