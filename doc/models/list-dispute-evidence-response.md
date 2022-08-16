
# List Dispute Evidence Response

Defines the fields in a `ListDisputeEvidence` response.

## Structure

`List Dispute Evidence Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `evidence` | [`List of Dispute Evidence`](../../doc/models/dispute-evidence.md) | Optional | The list of evidence previously uploaded to the specified dispute. |
| `errors` | [`List of Error`](../../doc/models/error.md) | Optional | Information about errors encountered during the request. |
| `cursor` | `string` | Optional | The pagination cursor to be used in a subsequent request.<br>If unset, this is the final response. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination). |

## Example (as JSON)

```json
{
  "evidence": null,
  "errors": null,
  "cursor": null
}
```

