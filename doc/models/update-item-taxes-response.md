## Update Item Taxes Response

### Structure

`UpdateItemTaxesResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | The set of [Error](./models/error.md)s encountered. |
| `updated_at` | `string` | Optional | The database [timestamp](#workingwithdates) of this update in RFC 3339 format, e.g., "2016-09-04T23:59:33.123Z". |

### Example (as JSON)

```json
{
  "updated_at": "2016-11-16T22:25:24.878Z"
}
```

