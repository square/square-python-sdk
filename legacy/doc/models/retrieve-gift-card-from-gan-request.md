
# Retrieve Gift Card From GAN Request

A request to retrieve gift cards by their GANs.

## Structure

`Retrieve Gift Card From GAN Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gan` | `str` | Required | The gift card account number (GAN) of the gift card to retrieve.<br>The maximum length of a GAN is 255 digits to account for third-party GANs that have been imported.<br>Square-issued gift cards have 16-digit GANs.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "gan": "7783320001001635"
}
```

