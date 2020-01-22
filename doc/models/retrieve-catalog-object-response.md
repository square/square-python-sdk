## Retrieve Catalog Object Response

### Structure

`RetrieveCatalogObjectResponse`

### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List of Error`](/doc/models/error.md) | Optional | Information on any errors encountered. |
| `object` | [`Catalog Object`](/doc/models/catalog-object.md) | Optional | - |
| `related_objects` | [`List of Catalog Object`](/doc/models/catalog-object.md) | Optional | A list of CatalogObjects referenced by the object in the `object` field. |

### Example (as JSON)

```json
{
  "object": {
    "type": "ITEM",
    "id": "W62UWFY35CWMYGVWK6TWJDNI",
    "updated_at": "2016-11-16T22:25:24.878Z",
    "version": 1479335124878,
    "is_deleted": false,
    "present_at_all_locations": true,
    "item_data": {
      "name": "Tea",
      "description": "Hot Leaf Juice",
      "category_id": "BJNQCF2FJ6S6UIDT65ABHLRX",
      "tax_ids": [
        "HURXQOOAIC4IZSI2BEXQRYFY"
      ],
      "variations": [
        {
          "type": "ITEM_VARIATION",
          "id": "2TZFAOHWGG7PAK2QEXWYPZSP",
          "updated_at": "2016-11-16T22:25:24.878Z",
          "version": 1479335124878,
          "is_deleted": false,
          "present_at_all_locations": true,
          "item_variation_data": {
            "item_id": "W62UWFY35CWMYGVWK6TWJDNI",
            "name": "Mug",
            "ordinal": 0,
            "pricing_type": "FIXED_PRICING",
            "price_money": {
              "amount": 150,
              "currency": "USD"
            }
          }
        }
      ]
    }
  },
  "related_objects": [
    {
      "type": "CATEGORY",
      "id": "BJNQCF2FJ6S6UIDT65ABHLRX",
      "updated_at": "2016-11-16T22:25:24.878Z",
      "version": 1479335124878,
      "is_deleted": false,
      "present_at_all_locations": true,
      "category_data": {
        "name": "Beverages"
      }
    },
    {
      "type": "TAX",
      "id": "HURXQOOAIC4IZSI2BEXQRYFY",
      "updated_at": "2016-11-16T22:25:24.878Z",
      "version": 1479335124878,
      "is_deleted": false,
      "present_at_all_locations": true,
      "tax_data": {
        "name": "Sales Tax",
        "calculation_phase": "TAX_SUBTOTAL_PHASE",
        "inclusion_type": "ADDITIVE",
        "percentage": "5.0",
        "enabled": true
      }
    }
  ]
}
```

