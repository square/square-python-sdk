
# Search Orders State Filter

Filter by the current order `state`.

## Structure

`Search Orders State Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `states` | [`str (List Order State)`](../../doc/models/order-state.md) | Required | States to filter for.<br>See [OrderState](#type-orderstate) for possible values |

## Example (as JSON)

```json
{
  "states": [
    "CANCELED",
    "DRAFT",
    "OPEN"
  ]
}
```

