
# Phase Input

Represents the arguments used to construct a new phase.

## Structure

`Phase Input`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ordinal` | `int` | Required | index of phase in total subscription plan |
| `order_template_id` | `string` | Optional | id of order to be used in billing |

## Example (as JSON)

```json
{
  "ordinal": 80,
  "order_template_id": "order_template_id2"
}
```

