
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `square_version` | `string` | Square Connect API versions<br>*Default*: `'2020-12-16'` |
| `access_token` | `string` | The OAuth 2.0 Access Token to use for API requests. |
| `environment` | `string` | The API environment. <br> **Default: `production`** |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 3** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 0** |
| `additional_headers` | `dict` | Additional headers to add to each API request |

The API client can be initialized as follows:

```python
from square.client import Client

client = Client(
    square_version='2020-12-16',
    access_token='AccessToken',
    environment = 'production',)
```

API calls return an `ApiResponse` object that includes the following fields:

| Field | Description |
|  --- | --- |
| `status_code` | Status code of the HTTP response |
| `reason_phrase` | Reason phrase of the HTTP response |
| `headers` | Headers of the HTTP response as a dictionary |
| `text` | The body of the HTTP response as a string |
| `request` | HTTP request info |
| `errors` | Errors, if they exist |
| `body` | The deserialized body of the HTTP response |
| `cursor` | Cursor, if it exists |

## Make Calls with the API Client

```python
from square.configuration import Configuration
from square.client import Client

client = Client(
    square_version='2020-12-16',
    access_token='AccessToken',)

locations_api = client.locations
result = locations_api.list_locations()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## SquareClient

The gateway for the SDK. This class acts as a factory for the Apis and also holds the configuration of the SDK.

## API

| Name | Description |
|  --- | --- |
| mobile_authorization | Provides access to MobileAuthorizationApi |
| o_auth | Provides access to OAuthApi |
| v1_employees | Provides access to V1EmployeesApi |
| v1_transactions | Provides access to V1TransactionsApi |
| v1_items | Provides access to V1ItemsApi |
| apple_pay | Provides access to ApplePayApi |
| bank_accounts | Provides access to BankAccountsApi |
| bookings | Provides access to BookingsApi |
| cash_drawers | Provides access to CashDrawersApi |
| catalog | Provides access to CatalogApi |
| customers | Provides access to CustomersApi |
| customer_groups | Provides access to CustomerGroupsApi |
| customer_segments | Provides access to CustomerSegmentsApi |
| devices | Provides access to DevicesApi |
| disputes | Provides access to DisputesApi |
| employees | Provides access to EmployeesApi |
| inventory | Provides access to InventoryApi |
| invoices | Provides access to InvoicesApi |
| labor | Provides access to LaborApi |
| locations | Provides access to LocationsApi |
| checkout | Provides access to CheckoutApi |
| transactions | Provides access to TransactionsApi |
| loyalty | Provides access to LoyaltyApi |
| merchants | Provides access to MerchantsApi |
| orders | Provides access to OrdersApi |
| payments | Provides access to PaymentsApi |
| refunds | Provides access to RefundsApi |
| subscriptions | Provides access to SubscriptionsApi |
| team | Provides access to TeamApi |
| terminal | Provides access to TerminalApi |

