
# Customer Group

Represents a group of customer profiles.

Customer groups can be created, be modified, and have their membership defined using
the Customers API or within the Customer Directory in the Square Seller Dashboard or Point of Sale.

## Structure

`Customer Group`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | A unique Square-generated ID for the customer group.<br>**Constraints**: *Maximum Length*: `255` |
| `name` | `str` | Required | The name of the customer group. |
| `created_at` | `str` | Optional | The timestamp when the customer group was created, in RFC 3339 format. |
| `updated_at` | `str` | Optional | The timestamp when the customer group was last updated, in RFC 3339 format. |

## Example (as JSON)

```json
{
  "id": "id0",
  "name": "name0",
  "created_at": "created_at8",
  "updated_at": "updated_at6"
}
```

