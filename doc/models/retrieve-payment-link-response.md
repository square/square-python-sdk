
# Retrieve Payment Link Response

## Structure

`Retrieve Payment Link Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `payment_link` | [`Payment Link`](../../doc/models/payment-link.md) | Optional | - |

## Example (as JSON)

```json
{
  "payment_link": {
    "created_at": "2022-04-26T00:10:29Z",
    "id": "LLO5Q3FRCFICDB4B",
    "order_id": "4uKASDATqSd1QQ9jV86sPhMdVEbSJc4F",
    "url": "https://square.link/u/EXAMPLE",
    "version": 1
  }
}
```

