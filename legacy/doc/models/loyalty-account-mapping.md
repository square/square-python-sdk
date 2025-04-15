
# Loyalty Account Mapping

Represents the mapping that associates a loyalty account with a buyer.

Currently, a loyalty account can only be mapped to a buyer by phone number. For more information, see
[Loyalty Overview](https://developer.squareup.com/docs/loyalty/overview).

## Structure

`Loyalty Account Mapping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The Square-assigned ID of the mapping.<br>**Constraints**: *Maximum Length*: `36` |
| `created_at` | `str` | Optional | The timestamp when the mapping was created, in RFC 3339 format. |
| `phone_number` | `str` | Optional | The phone number of the buyer, in E.164 format. For example, "+14155551111". |

## Example (as JSON)

```json
{
  "id": "id2",
  "created_at": "created_at0",
  "phone_number": "phone_number0"
}
```

