## Shift Query

The parameters of a `Shift` search query. Includes filter and sort options.

### Structure

`ShiftQuery`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter` | [`Shift Filter`]($m/ShiftFilter) | Optional | Defines a filter used in a search for `Shift` records. `AND` logic is<br>used by Square's servers to apply each filter property specified. |
| `sort` | [`Shift Sort`]($m/ShiftSort) | Optional | Sets the sort order of search results. |

### Example (as JSON)

```json
{
  "filter": null,
  "sort": null
}
```

