
# Update Item Taxes Request

## Structure

`Update Item Taxes Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_ids` | `List[str]` | Required | IDs for the CatalogItems associated with the CatalogTax objects being updated.<br>No more than 1,000 IDs may be provided. |
| `taxes_to_enable` | `List[str]` | Optional | IDs of the CatalogTax objects to enable.<br>At least one of `taxes_to_enable` or `taxes_to_disable` must be specified. |
| `taxes_to_disable` | `List[str]` | Optional | IDs of the CatalogTax objects to disable.<br>At least one of `taxes_to_enable` or `taxes_to_disable` must be specified. |

## Example (as JSON)

```json
{
  "item_ids": [
    "H42BRLUJ5KTZTTMPVSLFAACQ",
    "2JXOBJIHCWBQ4NZ3RIXQGJA6"
  ],
  "taxes_to_disable": [
    "AQCEGCEBBQONINDOHRGZISEX"
  ],
  "taxes_to_enable": [
    "4WRCNHCJZDVLSNDQ35PP6YAD"
  ]
}
```

