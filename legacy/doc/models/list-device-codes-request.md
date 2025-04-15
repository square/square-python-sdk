
# List Device Codes Request

## Structure

`List Device Codes Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Optional | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information. |
| `location_id` | `str` | Optional | If specified, only returns DeviceCodes of the specified location.<br>Returns DeviceCodes of all locations if empty. |
| `product_type` | [`str (Product Type)`](../../doc/models/product-type.md) | Optional | - |
| `status` | [`str (List Device Code Status)`](../../doc/models/device-code-status.md) | Optional | If specified, returns DeviceCodes with the specified statuses.<br>Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.<br>See [DeviceCodeStatus](#type-devicecodestatus) for possible values |

## Example (as JSON)

```json
{
  "cursor": "cursor6",
  "location_id": "location_id4",
  "product_type": "TERMINAL_API",
  "status": [
    "UNKNOWN",
    "UNPAIRED",
    "PAIRED"
  ]
}
```

