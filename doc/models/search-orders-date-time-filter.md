## Search Orders Date Time Filter

Filter for `Order` objects based on whether their `CREATED_AT`,
`CLOSED_AT` or `UPDATED_AT` timestamps fall within a specified time range.
You can specify the time range and which timestamp to filter for. You can filter
for only one time range at a time.

For each time range, the start time and end time are inclusive. If the end time
is absent, it defaults to the time of the first request for the cursor.

__Important:__ If you use the DateTimeFilter to filter for `CLOSED_AT` or `UPDATED_AT`,
you must also set the [OrdersSort](./models/orders-sort.md).
The TimeRange used in DateTimeFilter must correspond to the `sort_field` in
the [OrdersSort](./models/orders-sort.md) object.

### Structure

`SearchOrdersDateTimeFilter`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_at` | [`Time Range`](/doc/models/time-range.md) | Optional | Represents a generic time range. The start and end values are<br>represented in RFC-3339 format. Time ranges are customized to be<br>inclusive or exclusive based on the needs of a particular endpoint.<br>Refer to the relevent endpoint-specific documentation to determine<br>how time ranges are handled. |
| `updated_at` | [`Time Range`](/doc/models/time-range.md) | Optional | Represents a generic time range. The start and end values are<br>represented in RFC-3339 format. Time ranges are customized to be<br>inclusive or exclusive based on the needs of a particular endpoint.<br>Refer to the relevent endpoint-specific documentation to determine<br>how time ranges are handled. |
| `closed_at` | [`Time Range`](/doc/models/time-range.md) | Optional | Represents a generic time range. The start and end values are<br>represented in RFC-3339 format. Time ranges are customized to be<br>inclusive or exclusive based on the needs of a particular endpoint.<br>Refer to the relevent endpoint-specific documentation to determine<br>how time ranges are handled. |

### Example (as JSON)

```json
{
  "created_at": null,
  "updated_at": null,
  "closed_at": null
}
```

