## List Cash Drawer Shifts Response

### Structure

`ListCashDrawerShiftsResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List of Cash Drawer Shift Summary`]($m/CashDrawerShiftSummary) | Optional | A collection of CashDrawerShiftSummary objects for shifts that match<br>the query. |
| `cursor` | `string` | Optional | Opaque cursor for fetching the next page of results. Cursor is not<br>present in the last page of results. |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |

### Example (as JSON)

```json
{
  "items": null,
  "cursor": null,
  "errors": null
}
```

