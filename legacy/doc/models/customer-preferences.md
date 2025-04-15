
# Customer Preferences

Represents communication preferences for the customer profile.

## Structure

`Customer Preferences`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email_unsubscribed` | `bool` | Optional | Indicates whether the customer has unsubscribed from marketing campaign emails. A value of `true` means that the customer chose to opt out of email marketing from the current Square seller or from all Square sellers. This value is read-only from the Customers API. |

## Example (as JSON)

```json
{
  "email_unsubscribed": false
}
```

