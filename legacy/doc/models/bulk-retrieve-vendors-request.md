
# Bulk Retrieve Vendors Request

Represents an input to a call to [BulkRetrieveVendors](../../doc/api/vendors.md#bulk-retrieve-vendors).

## Structure

`Bulk Retrieve Vendors Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vendor_ids` | `List[str]` | Optional | IDs of the [Vendor](entity:Vendor) objects to retrieve. |

## Example (as JSON)

```json
{
  "vendor_ids": [
    "INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4"
  ]
}
```

