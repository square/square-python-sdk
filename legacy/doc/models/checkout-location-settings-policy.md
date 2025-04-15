
# Checkout Location Settings Policy

## Structure

`Checkout Location Settings Policy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | A unique ID to identify the policy when making changes. You must set the UID for policy updates, but it’s optional when setting new policies. |
| `title` | `str` | Optional | The title of the policy. This is required when setting the description, though you can update it in a different request.<br>**Constraints**: *Maximum Length*: `50` |
| `description` | `str` | Optional | The description of the policy.<br>**Constraints**: *Maximum Length*: `4096` |

## Example (as JSON)

```json
{
  "uid": "uid0",
  "title": "title6",
  "description": "description0"
}
```

