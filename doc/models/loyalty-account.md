
# Loyalty Account

Describes a loyalty account. For more information, see
[Loyalty Overview](https://developer.squareup.com/docs/loyalty/overview).

## Structure

`Loyalty Account`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The Square-assigned ID of the loyalty account.<br>**Constraints**: *Maximum Length*: `36` |
| `mappings` | [`List of Loyalty Account Mapping`](/doc/models/loyalty-account-mapping.md) | Optional | The list of mappings that the account is associated with.<br>Currently, a buyer can only be mapped to a loyalty account using<br>a phone number. Therefore, the list can only have one mapping.<br><br>One of the following is required when creating a loyalty account:<br><br>- (Preferred) The `mapping` field, with the buyer's phone number specified in the `phone_number` field.<br>- This `mappings` field. |
| `program_id` | `string` | Required | The Square-assigned ID of the [loyalty program](/doc/models/loyalty-program.md) to which the account belongs.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `36` |
| `balance` | `int` | Optional | The available point balance in the loyalty account.<br><br>Your application should be able to handle loyalty accounts that have a negative point balance (`balance` is less than 0). This might occur if a seller makes a manual adjustment or as a result of a refund or exchange. |
| `lifetime_points` | `int` | Optional | The total points accrued during the lifetime of the account. |
| `customer_id` | `string` | Optional | The Square-assigned ID of the [customer](/doc/models/customer.md) that is associated with the account. |
| `enrolled_at` | `string` | Optional | The timestamp when enrollment occurred, in RFC 3339 format. |
| `created_at` | `string` | Optional | The timestamp when the loyalty account was created, in RFC 3339 format. |
| `updated_at` | `string` | Optional | The timestamp when the loyalty account was last updated, in RFC 3339 format. |
| `mapping` | [`Loyalty Account Mapping`](/doc/models/loyalty-account-mapping.md) | Optional | Represents the mapping that associates a loyalty account with a buyer.<br><br>Currently, a loyalty account can only be mapped to a buyer by phone number. For more information, see<br>[Loyalty Overview](https://developer.squareup.com/docs/loyalty/overview). |

## Example (as JSON)

```json
{
  "id": "id0",
  "mappings": [
    {
      "id": "id4",
      "type": "PHONE",
      "value": "value6",
      "created_at": "created_at8",
      "phone_number": "phone_number8"
    }
  ],
  "program_id": "program_id0",
  "balance": 64,
  "lifetime_points": 88,
  "customer_id": "customer_id8"
}
```

