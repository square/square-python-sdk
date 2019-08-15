## Catalog Measurement Unit

Represents the unit used to measure a
[CatalogItemVariation](./models/catalog-item-variation.md) and specifies the precision
for decimal quantities.

### Structure

`CatalogMeasurementUnit`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `measurement_unit` | [`Measurement Unit`](/doc/models/measurement-unit.md) | Optional | Represents a unit of measurement to use with a quantity, such as ounces<br>or inches. Exactly one of the following fields are required: `custom_unit`,<br>`area_unit`, `length_unit`, `volume_unit`, and `weight_unit`.<br><br>The `family` field describes the type of measurement. For example,<br>ounces are in the weight family. |
| `precision` | `int` | Optional | Represents the maximum number of positions allowed after the decimal<br>in quantities measured with this unit. For example, if the precision is 2,<br>then an itemization’s quantity can be 0.01, 0.12, etc.<br><br>Min: 0<br><br>Max: 5<br><br>Default: 3 |

### Example (as JSON)

```json
{
  "measurement_unit": null,
  "precision": null
}
```

