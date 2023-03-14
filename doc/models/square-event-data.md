
# Square Event Data

## Structure

`Square Event Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | `string` | Optional | Name of the affected object’s type. |
| `id` | `string` | Optional | ID of the affected object. |
| `deleted` | `bool` | Optional | Is true if the affected object was deleted. Otherwise absent. |
| `object` | `dict` | Optional | An object containing fields and values relevant to the event. Is absent if affected object was deleted. |

## Example (as JSON)

```json
{
  "type": null,
  "id": null,
  "deleted": null,
  "object": null
}
```

