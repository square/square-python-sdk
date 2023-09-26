
# Site

Represents a Square Online site, which is an online store for a Square seller.

## Structure

`Site`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The Square-assigned ID of the site.<br>**Constraints**: *Maximum Length*: `32` |
| `site_title` | `str` | Optional | The title of the site. |
| `domain` | `str` | Optional | The domain of the site (without the protocol). For example, `mysite1.square.site`. |
| `is_published` | `bool` | Optional | Indicates whether the site is published. |
| `created_at` | `str` | Optional | The timestamp of when the site was created, in RFC 3339 format. |
| `updated_at` | `str` | Optional | The timestamp of when the site was last updated, in RFC 3339 format. |

## Example (as JSON)

```json
{
  "id": "id0",
  "site_title": "site_title6",
  "domain": "domain6",
  "is_published": false,
  "created_at": "created_at8"
}
```

