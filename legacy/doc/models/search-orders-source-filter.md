
# Search Orders Source Filter

A filter based on order `source` information.

## Structure

`Search Orders Source Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_names` | `List[str]` | Optional | Filters by the [Source](entity:OrderSource) `name`. The filter returns any orders<br>with a `source.name` that matches any of the listed source names.<br><br>Max: 10 source names. |

## Example (as JSON)

```json
{
  "source_names": [
    "source_names4",
    "source_names5",
    "source_names6"
  ]
}
```

