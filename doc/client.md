
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `square_version` | `str` | Square Connect API versions<br>*Default*: `'2025-01-23'` |
| `custom_url` | `str` | Sets the base URL requests are made to. Defaults to `https://connect.squareup.com`<br>*Default*: `'https://connect.squareup.com'` |
| `environment` | `string` | The API environment. <br> **Default: `production`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `additional_headers` | `dict` | Additional headers to add to each API request |
| `user_agent_detail` | `string` | User agent detail, to be appended with user-agent header. |
| `bearer_auth_credentials` | [`BearerAuthCredentials`](auth/oauth-2-bearer-token.md) | The credential object for OAuth 2 Bearer token |

The API client can be initialized as follows:

```python
client = Client(
    square_version='2025-01-23',
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment='production',
    custom_url='https://connect.squareup.com'
)
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
from square.http.auth.o_auth_2 import BearerAuthCredentials
from square.client import Client

client = Client(
    square_version='2025-01-23',
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment='production',
    custom_url='https://connect.squareup.com'
)

locations_api = client.locations
result = locations_api.list_locations()
print(result)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Square Client

The gateway for the SDK. This class acts as a factory for the Apis and also holds the configuration of the SDK.

## API

| Name | Description |
|  --- | --- |
| mobile_authorization | Gets MobileAuthorizationApi |
| o_auth | Gets OAuthApi |
| v1_transactions | Gets V1TransactionsApi |
| apple_pay | Gets ApplePayApi |
| bank_accounts | Gets BankAccountsApi |
| bookings | Gets BookingsApi |
| booking_custom_attributes | Gets BookingCustomAttributesApi |
| cards | Gets CardsApi |
| cash_drawers | Gets CashDrawersApi |
| catalog | Gets CatalogApi |
| customers | Gets CustomersApi |
| customer_custom_attributes | Gets CustomerCustomAttributesApi |
| customer_groups | Gets CustomerGroupsApi |
| customer_segments | Gets CustomerSegmentsApi |
| devices | Gets DevicesApi |
| disputes | Gets DisputesApi |
| employees | Gets EmployeesApi |
| events | Gets EventsApi |
| gift_cards | Gets GiftCardsApi |
| gift_card_activities | Gets GiftCardActivitiesApi |
| inventory | Gets InventoryApi |
| invoices | Gets InvoicesApi |
| labor | Gets LaborApi |
| locations | Gets LocationsApi |
| location_custom_attributes | Gets LocationCustomAttributesApi |
| checkout | Gets CheckoutApi |
| transactions | Gets TransactionsApi |
| loyalty | Gets LoyaltyApi |
| merchants | Gets MerchantsApi |
| merchant_custom_attributes | Gets MerchantCustomAttributesApi |
| orders | Gets OrdersApi |
| order_custom_attributes | Gets OrderCustomAttributesApi |
| payments | Gets PaymentsApi |
| payouts | Gets PayoutsApi |
| refunds | Gets RefundsApi |
| sites | Gets SitesApi |
| snippets | Gets SnippetsApi |
| subscriptions | Gets SubscriptionsApi |
| team | Gets TeamApi |
| terminal | Gets TerminalApi |
| vendors | Gets VendorsApi |
| webhook_subscriptions | Gets WebhookSubscriptionsApi |

