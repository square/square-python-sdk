## V1 Fee

V1Fee

### Structure

`V1Fee`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The fee's unique ID. |
| `name` | `string` | Optional | The fee's name. |
| `rate` | `string` | Optional | The rate of the fee, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%. |
| `calculation_phase` | [`str (V1 Fee Calculation Phase)`]($m/V1FeeCalculationPhase) | Optional | - |
| `adjustment_type` | [`str (V1 Fee Adjustment Type)`]($m/V1FeeAdjustmentType) | Optional | - |
| `applies_to_custom_amounts` | `bool` | Optional | If true, the fee applies to custom amounts entered into Square Point of Sale that are not associated with a particular item. |
| `enabled` | `bool` | Optional | If true, the fee is applied to all appropriate items. If false, the fee is not applied at all. |
| `inclusion_type` | [`str (V1 Fee Inclusion Type)`]($m/V1FeeInclusionType) | Optional | - |
| `type` | [`str (V1 Fee Type)`]($m/V1FeeType) | Optional | - |
| `v2_id` | `string` | Optional | The ID of the CatalogObject in the Connect v2 API. Objects that are shared across multiple locations share the same v2 ID. |

### Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "rate": null,
  "calculation_phase": null,
  "adjustment_type": null,
  "applies_to_custom_amounts": null,
  "enabled": null,
  "inclusion_type": null,
  "type": null,
  "v2_id": null
}
```

