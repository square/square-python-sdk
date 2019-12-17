## Measurement Unit

Represents a unit of measurement to use with a quantity, such as ounces
or inches. Exactly one of the following fields are required: `custom_unit`,
`area_unit`, `length_unit`, `volume_unit`, and `weight_unit`.

### Structure

`MeasurementUnit`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_unit` | [`Measurement Unit Custom`]($m/MeasurementUnitCustom) | Optional | The information needed to define a custom unit, provided by the seller. |
| `area_unit` | [`str (Measurement Unit Area)`]($m/MeasurementUnitArea) | Optional | Unit of area used to measure a quantity. |
| `length_unit` | [`str (Measurement Unit Length)`]($m/MeasurementUnitLength) | Optional | The unit of length used to measure a quantity. |
| `volume_unit` | [`str (Measurement Unit Volume)`]($m/MeasurementUnitVolume) | Optional | The unit of volume used to measure a quantity. |
| `weight_unit` | [`str (Measurement Unit Weight)`]($m/MeasurementUnitWeight) | Optional | Unit of weight used to measure a quantity. |
| `generic_unit` | [`str (Measurement Unit Generic)`]($m/MeasurementUnitGeneric) | Optional | - |
| `time_unit` | [`str (Measurement Unit Time)`]($m/MeasurementUnitTime) | Optional | Unit of time used to measure a quantity (a duration). |
| `type` | [`str (Measurement Unit Unit Type)`]($m/MeasurementUnitUnitType) | Optional | Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’ enum. |

### Example (as JSON)

```json
{
  "custom_unit": null,
  "area_unit": null,
  "length_unit": null,
  "volume_unit": null,
  "weight_unit": null,
  "generic_unit": null,
  "time_unit": null,
  "type": null
}
```

