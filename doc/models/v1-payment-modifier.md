## V1 Payment Modifier

V1PaymentModifier

### Structure

`V1PaymentModifier`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | The modifier option's name. |
| `applied_money` | [`V1 Money`]($m/V1Money) | Optional | - |
| `modifier_option_id` | `string` | Optional | TThe ID of the applied modifier option, if available. Modifier options applied in older versions of Square Register might not have an ID. |

### Example (as JSON)

```json
{
  "name": null,
  "applied_money": null,
  "modifier_option_id": null
}
```

