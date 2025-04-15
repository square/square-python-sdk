
# Loyalty Account Expiring Point Deadline

Represents a set of points for a loyalty account that are scheduled to expire on a specific date.

## Structure

`Loyalty Account Expiring Point Deadline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `points` | `int` | Required | The number of points scheduled to expire at the `expires_at` timestamp. |
| `expires_at` | `str` | Required | The timestamp of when the points are scheduled to expire, in RFC 3339 format.<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "points": 104,
  "expires_at": "expires_at6"
}
```

