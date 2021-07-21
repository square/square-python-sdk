
# Snippet Response

## Structure

`Snippet Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `snippet` | [`Snippet`](/doc/models/snippet.md) | Optional | Represents the snippet that is added to a Square Online site. The snippet code is injected into the `head` element of all pages on the site, except for checkout pages. |

## Example (as JSON)

```json
{
  "errors": [
    {
      "category": "AUTHENTICATION_ERROR",
      "code": "NOT_ACCEPTABLE",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "INVALID_REQUEST_ERROR",
      "code": "REQUEST_TIMEOUT",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "RATE_LIMIT_ERROR",
      "code": "CONFLICT",
      "detail": "detail3",
      "field": "field1"
    }
  ],
  "snippet": {
    "id": "id0",
    "site_id": "site_id6",
    "content": "content4",
    "created_at": "created_at8",
    "updated_at": "updated_at4"
  }
}
```

