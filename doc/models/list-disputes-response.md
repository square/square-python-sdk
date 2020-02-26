## List Disputes Response

Defines fields in a ListDisputes response.

### Structure

`ListDisputesResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on errors encountered during the request. |
| `disputes` | [`List of Dispute`](/doc/models/dispute.md) | Optional | The list of Disputes. |
| `cursor` | `string` | Optional | The pagination cursor to be used in a subsequent request.<br>If unset, this is the final response.<br>For more information, see [Paginating](https://developer.squareup.com/docs/basics/api101/pagination). |

### Example (as JSON)

```json
{
  "errors": null,
  "disputes": null,
  "cursor": null
}
```

