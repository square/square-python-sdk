
# Catalog Object Category

A category that can be assigned to an item or a parent category that can be assigned
to another category. For example, a clothing category can be assigned to a t-shirt item or
be made as the parent category to the pants category.

## Structure

`Catalog Object Category`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of the object's category. |
| `ordinal` | `long\|int` | Optional | The order of the object within the context of the category. |

## Example (as JSON)

```json
{
  "id": "id4",
  "ordinal": 8
}
```

