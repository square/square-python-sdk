
# Buy Now Pay Later Details

Additional details about a Buy Now Pay Later payment type.

## Structure

`Buy Now Pay Later Details`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `string` | Optional | The brand used for the Buy Now Pay Later payment.<br>The brand can be `AFTERPAY` or `UNKNOWN`.<br>**Constraints**: *Maximum Length*: `50` |
| `afterpay_details` | [`Afterpay Details`](../../doc/models/afterpay-details.md) | Optional | Additional details about Afterpay payments. |

## Example (as JSON)

```json
{
  "brand": null,
  "afterpay_details": null
}
```

