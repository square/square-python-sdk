
# Create Device Code Request

## Structure

`Create Device Code Request`

## Fields

| Name | Type | Description |
|  --- | --- | --- |
| `idempotency_key` | `string` | A unique string that identifies this CreateCheckout request. Keys can be any valid string but<br>must be unique for every CreateCheckout request.<br><br>See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information. |
| `device_code` | [`Device Code`](/doc/models/device-code.md) | - |

## Example (as JSON)

```json
{
  "device_code": {
    "location_id": "B5E4484SHHNYH",
    "name": "Counter 1",
    "product_type": "TERMINAL_API"
  },
  "idempotency_key": "01bb00a6-0c86-4770-94ed-f5fca973cd56"
}
```

