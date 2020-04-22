## Catalog Quick Amounts Settings

A parent Catalog Object model represents a set of Quick Amounts and the settings control the amounts.

### Structure

`CatalogQuickAmountsSettings`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `option` | [`str (Catalog Quick Amounts Settings Option)`](/doc/models/catalog-quick-amounts-settings-option.md) |  | Determines a seller's option on Quick Amounts feature. |
| `eligible_for_auto_amounts` | `bool` | Optional | Represents location's eligibility for auto amounts<br>The boolean should be consistent with whether there are AUTO amounts in the `amounts`. |
| `amounts` | [`List of Catalog Quick Amount`](/doc/models/catalog-quick-amount.md) | Optional | Represents a set of Quick Amounts at this location. |

### Example (as JSON)

```json
{
  "option": "AUTO",
  "eligible_for_auto_amounts": null,
  "amounts": null
}
```

