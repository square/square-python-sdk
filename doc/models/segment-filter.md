
# Segment Filter

A query filter to search for appointment segments by.

## Structure

`Segment Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_variation_id` | `string` |  | The ID of the [CatalogItemVariation](#type-CatalogItemVariation) representing the service booked in this segment. |
| `team_member_id_filter` | [`Filter Value`](/doc/models/filter-value.md) | Optional | A filter to select resources based on an exact field value. For any given<br>value, the value can only be in one property. Depending on the field, either<br>all properties can be set or only a subset will be available.<br><br>Refer to the documentation of the field. |

## Example (as JSON)

```json
{
  "service_variation_id": "service_variation_id6",
  "team_member_id_filter": {
    "all": [
      "all5",
      "all6",
      "all7"
    ],
    "any": [
      "any2",
      "any3",
      "any4"
    ],
    "none": [
      "none7",
      "none8"
    ]
  }
}
```

