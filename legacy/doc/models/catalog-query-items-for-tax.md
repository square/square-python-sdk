
# Catalog Query Items for Tax

The query filter to return the items containing the specified tax IDs.

## Structure

`Catalog Query Items for Tax`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_ids` | `List[str]` | Required | A set of `CatalogTax` IDs to be used to find associated `CatalogItem`s. |

## Example (as JSON)

```json
{
  "tax_ids": [
    "tax_ids9",
    "tax_ids8"
  ]
}
```

