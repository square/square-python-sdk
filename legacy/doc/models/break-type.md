
# Break Type

A defined break template that sets an expectation for possible `Break`
instances on a `Shift`.

## Structure

`Break Type`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The UUID for this object.<br>**Constraints**: *Maximum Length*: `255` |
| `location_id` | `str` | Required | The ID of the business location this type of break applies to.<br>**Constraints**: *Minimum Length*: `1` |
| `break_name` | `str` | Required | A human-readable name for this type of break. The name is displayed to<br>employees in Square products.<br>**Constraints**: *Minimum Length*: `1` |
| `expected_duration` | `str` | Required | Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of<br>this break. Precision less than minutes is truncated.<br><br>Example for break expected duration of 15 minutes: T15M<br>**Constraints**: *Minimum Length*: `1` |
| `is_paid` | `bool` | Required | Whether this break counts towards time worked for compensation<br>purposes. |
| `version` | `int` | Optional | Used for resolving concurrency issues. The request fails if the version<br>provided does not match the server version at the time of the request. If a value is not<br>provided, Square's servers execute a "blind" write; potentially<br>overwriting another writer's data. |
| `created_at` | `str` | Optional | A read-only timestamp in RFC 3339 format. |
| `updated_at` | `str` | Optional | A read-only timestamp in RFC 3339 format. |

## Example (as JSON)

```json
{
  "id": "id4",
  "location_id": "location_id8",
  "break_name": "break_name4",
  "expected_duration": "expected_duration0",
  "is_paid": false,
  "version": 236,
  "created_at": "created_at8",
  "updated_at": "updated_at0"
}
```

