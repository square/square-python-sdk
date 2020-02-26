## Create Order Request

### Structure

`CreateOrderRequest`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`Order`](/doc/models/order.md) | Optional | Contains all information related to a single order to process with Square,<br>including line items that specify the products to purchase. Order objects also<br>include information on any associated tenders, refunds, and returns.<br><br>All Connect V2 Transactions have all been converted to Orders including all associated<br>itemization data. |
| `idempotency_key` | `string` | Optional | A value you specify that uniquely identifies this<br>order among orders you've created.<br><br>If you're unsure whether a particular order was created successfully,<br>you can reattempt it with the same idempotency key without<br>worrying about creating duplicate orders.<br><br>See [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency) for more information. |

### Example (as JSON)

```json
{
  "order": null,
  "idempotency_key": null
}
```

