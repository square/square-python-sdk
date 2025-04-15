
# Custom Field

Describes a custom form field to add to the checkout page to collect more information from buyers during checkout.
For more information,
see [Specify checkout options](https://developer.squareup.com/docs/checkout-api/optional-checkout-configurations#specify-checkout-options-1).

## Structure

`Custom Field`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Required | The title of the custom field.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |

## Example (as JSON)

```json
{
  "title": "title4"
}
```

