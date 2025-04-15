
# Catalog Modifier Override

Options to control how to override the default behavior of the specified modifier.

## Structure

`Catalog Modifier Override`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `modifier_id` | `str` | Required | The ID of the `CatalogModifier` whose default behavior is being overridden.<br>**Constraints**: *Minimum Length*: `1` |
| `on_by_default` | `bool` | Optional | If `true`, this `CatalogModifier` should be selected by default for this `CatalogItem`. |

## Example (as JSON)

```json
{
  "modifier_id": "modifier_id2",
  "on_by_default": false
}
```

