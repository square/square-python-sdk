## Update Location Response

Response object returned by the [UpdateLocation](#endpoint-updatelocation) endpoint.

### Structure

`UpdateLocationResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `location` | [`Location`](/doc/models/location.md) | Optional | Represents one of a business's locations. |

### Example (as JSON)

```json
{
  "errors": null,
  "location": null
}
```

