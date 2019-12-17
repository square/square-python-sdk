## V1 List Settlements Request

### Structure

`V1ListSettlementsRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`str (Sort Order)`]($m/SortOrder) | Optional | The order (e.g., chronological or alphabetical) in which results from a request are returned. |
| `begin_time` | `string` | Optional | The beginning of the requested reporting period, in ISO 8601 format. If this value is before January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns an error. Default value: The current time minus one year. |
| `end_time` | `string` | Optional | The end of the requested reporting period, in ISO 8601 format. If this value is more than one year greater than begin_time, this endpoint returns an error. Default value: The current time. |
| `limit` | `int` | Optional | The maximum number of payments to return in a single response. This value cannot exceed 200. |
| `status` | [`str (V1 List Settlements Request Status)`]($m/V1ListSettlementsRequestStatus) | Optional | - |
| `batch_token` | `string` | Optional | A pagination cursor to retrieve the next set of results for your<br>original query to the endpoint. |

### Example (as JSON)

```json
{
  "order": null,
  "begin_time": null,
  "end_time": null,
  "limit": null,
  "status": null,
  "batch_token": null
}
```

