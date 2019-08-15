## Customer

Represents one of a business's customers, which can have one or more
cards on file associated with it.

### Structure

`Customer`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` |  | The customer's unique ID. |
| `created_at` | `string` |  | The time when the customer was created, in RFC 3339 format. |
| `updated_at` | `string` |  | The time when the customer was last updated, in RFC 3339 format. |
| `cards` | [`List of Card`](/doc/models/card.md) | Optional | The payment details of the customer's cards on file. |
| `given_name` | `string` | Optional | The customer's given (i.e., first) name. |
| `family_name` | `string` | Optional | The customer's family (i.e., last) name. |
| `nickname` | `string` | Optional | The customer's nickname. |
| `company_name` | `string` | Optional | The name of the customer's company. |
| `email_address` | `string` | Optional | The customer's email address. |
| `address` | [`Address`](/doc/models/address.md) | Optional | Represents a physical address. |
| `phone_number` | `string` | Optional | The customer's phone number. |
| `birthday` | `string` | Optional | The customer's birthday in RFC-3339 format. Year is optional,<br>timezone and times are not allowed. Example: `0000-09-01T00:00:00-00:00`<br>for a birthday on September 1st. `1998-09-01T00:00:00-00:00` for a birthday<br>on September 1st 1998. |
| `reference_id` | `string` | Optional | A second ID you can set to associate the customer with an<br>entity in another system. |
| `note` | `string` | Optional | A note to associate with the customer. |
| `preferences` | [`Customer Preferences`](/doc/models/customer-preferences.md) | Optional | Represents a particular customer's preferences. |
| `groups` | [`List of Customer Group Info`](/doc/models/customer-group-info.md) | Optional | The groups the customer belongs to. |
| `creation_source` | [`str (Customer Creation Source)`](/doc/models/customer-creation-source.md) | Optional | Indicates the method used to create the customer profile. |

### Example (as JSON)

```json
{
  "id": "id0",
  "created_at": "created_at2",
  "updated_at": "updated_at4",
  "cards": null,
  "given_name": null,
  "family_name": null,
  "nickname": null,
  "company_name": null,
  "email_address": null,
  "address": null,
  "phone_number": null,
  "birthday": null,
  "reference_id": null,
  "note": null,
  "preferences": null,
  "groups": null,
  "creation_source": null
}
```

