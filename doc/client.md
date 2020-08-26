## Client

### Overview

The following parameters are configurable for the API Client.

| Parameter | Type | Description |
|  --- | --- | --- |
| `access_token` | `string` | OAuth 2.0 Access Token |
| `environment` | `string` | The API environment. <br> **Default: `production`** |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 3** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 0** |

The API client can be initialized as following.

```python
client = Client(
    access_token='AccessToken',
    environment = 'production',)
```

### Available APIs

| API | Instance |
| --- | --- |
| [Apple Pay](apple-pay.md) | ```apple_pay_api = client.apple_pay``` |
| [Bank Accounts](bank-accounts.md) | ```bank_accounts_api = client.bank_accounts``` |
| [Cash Drawers](cash-drawers.md) | ```cash_drawers_api = client.cash_drawers``` |
| [Catalog](catalog.md) | ```catalog_api = client.catalog``` |
| [Checkout](checkout.md) | ```checkout_api = client.checkout``` |
| [Customer Groups](customer-groups.md) | ```customer_groups_api = client.customer_groups``` |
| [Customer Segments](customer-segments.md) | ```customer_segments_api = client.customer_segments``` |
| [Customers](customers.md) | ```customers_api = client.customers``` |
| [Devices](devices.md) | ```devices_api = client.devices``` |
| [Disputes](disputes.md) | ```disputes_api = client.disputes``` |
| [Employees](employees.md) | ```employees_api = client.employees``` |
| [Inventory](inventory.md) | ```inventory_api = client.inventory``` |
| [Labor](labor.md) | ```labor_api = client.labor``` |
| [Locations](locations.md) | ```locations_api = client.locations``` |
| [Loyalty](loyalty.md) | ```loyalty_api = client.loyalty``` |
| [Merchants](merchants.md) | ```loyalty_api = client.loyalty``` |
| [Orders](orders.md) | ```orders_api = client.orders``` |
| [Payments](payments.md) | ```payments_api = client.payments``` |
| [Refunds](refunds.md) | ```refunds_api = client.refunds``` |
| [Team](team.md) | ```team_api = client.team``` |
| [Terminal](terminal.md) | ```terminal_api = client.terminal``` |
| [Transactions](transactions.md) | ```transactions_api = client.transactions``` |

### Authorization

| API | Instance |
| --- | --- |
| [Mobile Authorization](mobile-authorization.md) | ```mobile_authorization_api = client.mobile_authorization``` |
| [O Auth](o-auth.md) | ```o_auth_api = client.o_auth``` |

### V1

| API | Instance |
| --- | --- |
| [V1 Locations](v1-locations.md) | ```v1_locations_api = client.v1_locations``` |
| [V1 Employees](v1-employees.md) | ```v1_employees_api = client.v1_employees``` |
| [V1 Transactions](v1-transactions.md) |  ```v1_transactions_api = client.v1_transactions``` |
| [V1 Items](v1-items.md) | ```v1_items_api = client.v1_items``` |