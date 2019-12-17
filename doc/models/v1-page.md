## V1 Page

V1Page

### Structure

`V1Page`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The page's unique identifier. |
| `name` | `string` | Optional | The page's name, if any. |
| `page_index` | `int` | Optional | The page's position in the merchant's list of pages. Always an integer between 0 and 6, inclusive. |
| `cells` | [`List of V1 Page Cell`]($m/V1PageCell) | Optional | The cells included on the page. |

### Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "page_index": null,
  "cells": null
}
```

