## Search Orders Source Filter

Filter based on Order `source` information.

### Structure

`SearchOrdersSourceFilter`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_names` | `List of string` | Optional | Filters by [Source](./models/source.md) `name`. Will return any orders<br>with with `source.name`s that match any of the listed source names.<br><br>Max: 10 `source_names`. |

### Example (as JSON)

```json
{
  "source_names": null
}
```

