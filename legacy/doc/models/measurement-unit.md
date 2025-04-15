
# Measurement Unit

Represents a unit of measurement to use with a quantity, such as ounces
or inches. Exactly one of the following fields are required: `custom_unit`,
`area_unit`, `length_unit`, `volume_unit`, and `weight_unit`.

## Structure

`Measurement Unit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_unit` | [`Measurement Unit Custom`](../../doc/models/measurement-unit-custom.md) | Optional | The information needed to define a custom unit, provided by the seller. |
| `area_unit` | [`str (Measurement Unit Area)`](../../doc/models/measurement-unit-area.md) | Optional | Unit of area used to measure a quantity. |
| `length_unit` | [`str (Measurement Unit Length)`](../../doc/models/measurement-unit-length.md) | Optional | The unit of length used to measure a quantity. |
| `volume_unit` | [`str (Measurement Unit Volume)`](../../doc/models/measurement-unit-volume.md) | Optional | The unit of volume used to measure a quantity. |
| `weight_unit` | [`str (Measurement Unit Weight)`](../../doc/models/measurement-unit-weight.md) | Optional | Unit of weight used to measure a quantity. |
| `generic_unit` | [`str (Measurement Unit Generic)`](../../doc/models/measurement-unit-generic.md) | Optional | - |
| `time_unit` | [`str (Measurement Unit Time)`](../../doc/models/measurement-unit-time.md) | Optional | Unit of time used to measure a quantity (a duration). |
| `type` | [`str (Measurement Unit Unit Type)`](../../doc/models/measurement-unit-unit-type.md) | Optional | Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’ enum. |

## Example (as JSON)

```json
{
  "custom_unit": {
    "name": "name2",
    "abbreviation": "abbreviation4"
  },
  "area_unit": "IMPERIAL_SQUARE_MILE",
  "length_unit": "METRIC_MILLIMETER",
  "volume_unit": "IMPERIAL_CUBIC_INCH",
  "weight_unit": "IMPERIAL_WEIGHT_OUNCE"
}
```

