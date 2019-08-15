## Standard Unit Description

Contains the name and abbreviation for standard measurement unit.

### Structure

`StandardUnitDescription`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit` | [`Measurement Unit`](/doc/models/measurement-unit.md) | Optional | Represents a unit of measurement to use with a quantity, such as ounces<br>or inches. Exactly one of the following fields are required: `custom_unit`,<br>`area_unit`, `length_unit`, `volume_unit`, and `weight_unit`.<br><br>The `family` field describes the type of measurement. For example,<br>ounces are in the weight family. |
| `name` | `string` | Optional | Display name of the measurement unit. For example, 'Pound'. |
| `abbreviation` | `string` | Optional | Abbreviation for the measurement unit. For example, 'lb'. |

### Example (as JSON)

```json
{
  "unit": null,
  "name": null,
  "abbreviation": null
}
```

