## Webhook Events

The type of an event that triggers a webhook notification to an application.

### Enumeration

`WebhookEvents`

### Fields

| Name | Description |
|  --- | --- |
| `Enum_inventorycountupdated` | The quantity was updated for a catalog item variation.<br>Webhook notification data is packaged as: [`InventoryCount[]`](#type-inventorychange). |
| `Enum_catalogversionupdated` | The catalog was updated.<br>Webhook notification data is packaged as:<br>"catalog_version": { "updated_at": "2019-05-14T17:51:27Z"}. |

