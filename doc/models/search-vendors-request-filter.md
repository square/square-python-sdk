
# Search Vendors Request Filter

Defines supported query expressions to search for vendors by.

## Structure

`Search Vendors Request Filter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `List[str]` | Optional | The names of the [Vendor](entity:Vendor) objects to retrieve. |
| `status` | [`str (List Vendor Status)`](../../doc/models/vendor-status.md) | Optional | The statuses of the [Vendor](entity:Vendor) objects to retrieve.<br>See [VendorStatus](#type-vendorstatus) for possible values |

## Example (as JSON)

```json
{
  "name": [
    "name0",
    "name1",
    "name2"
  ],
  "status": [
    "ACTIVE",
    "INACTIVE",
    "ACTIVE"
  ]
}
```

