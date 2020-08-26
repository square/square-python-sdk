## Tip Settings

### Structure

`TipSettings`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_tipping` | `bool` | Optional | Indicates whether tipping is enabled for this checkout. Defaults to false. |
| `separate_tip_screen` | `bool` | Optional | Indicates whether tip options should be presented on their own screen before presenting<br>the signature screen during card payment. Defaults to false. |
| `custom_tip_field` | `bool` | Optional | Indicates whether custom tip amounts are allowed during the checkout flow. Defaults to false. |

### Example (as JSON)

```json
{
  "allow_tipping": false,
  "separate_tip_screen": false,
  "custom_tip_field": false
}
```

