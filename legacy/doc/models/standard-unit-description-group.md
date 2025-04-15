
# Standard Unit Description Group

Group of standard measurement units.

## Structure

`Standard Unit Description Group`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `standard_unit_descriptions` | [`List Standard Unit Description`](../../doc/models/standard-unit-description.md) | Optional | List of standard (non-custom) measurement units in this description group. |
| `language_code` | `str` | Optional | IETF language tag. |

## Example (as JSON)

```json
{
  "standard_unit_descriptions": [
    {
      "unit": {
        "custom_unit": {
          "name": "name2",
          "abbreviation": "abbreviation4"
        },
        "area_unit": "IMPERIAL_ACRE",
        "length_unit": "IMPERIAL_INCH",
        "volume_unit": "METRIC_MILLILITER",
        "weight_unit": "IMPERIAL_STONE"
      },
      "name": "name4",
      "abbreviation": "abbreviation6"
    },
    {
      "unit": {
        "custom_unit": {
          "name": "name2",
          "abbreviation": "abbreviation4"
        },
        "area_unit": "IMPERIAL_ACRE",
        "length_unit": "IMPERIAL_INCH",
        "volume_unit": "METRIC_MILLILITER",
        "weight_unit": "IMPERIAL_STONE"
      },
      "name": "name4",
      "abbreviation": "abbreviation6"
    },
    {
      "unit": {
        "custom_unit": {
          "name": "name2",
          "abbreviation": "abbreviation4"
        },
        "area_unit": "IMPERIAL_ACRE",
        "length_unit": "IMPERIAL_INCH",
        "volume_unit": "METRIC_MILLILITER",
        "weight_unit": "IMPERIAL_STONE"
      },
      "name": "name4",
      "abbreviation": "abbreviation6"
    }
  ],
  "language_code": "language_code4"
}
```

