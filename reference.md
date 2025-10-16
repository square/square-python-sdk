# Reference
## Mobile
<details><summary><code>client.mobile.<a href="src/square/mobile/client.py">authorization_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

__Note:__ This endpoint is used by the deprecated Reader SDK. 
Developers should update their integration to use the [Mobile Payments SDK](https://developer.squareup.com/docs/mobile-payments-sdk), which includes its own authorization methods. 

Generates code to authorize a mobile application to connect to a Square card reader.

Authorization codes are one-time-use codes and expire 60 minutes after being issued.

The `Authorization` header you provide to this endpoint must have the following format:

```
Authorization: Bearer ACCESS_TOKEN
```

Replace `ACCESS_TOKEN` with a
[valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.mobile.authorization_code(
    location_id="YOUR_LOCATION_ID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `typing.Optional[str]` — The Square location ID that the authorization code should be tied to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OAuth
<details><summary><code>client.o_auth.<a href="src/square/o_auth/client.py">revoke_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes an access token generated with the OAuth flow.

If an account has more than one OAuth access token for your application, this
endpoint revokes all of them, regardless of which token you specify. 

__Important:__ The `Authorization` header for this endpoint must have the
following format:

```
Authorization: Client APPLICATION_SECRET
```

Replace `APPLICATION_SECRET` with the application secret on the **OAuth**
page for your application in the Developer Dashboard.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.o_auth.revoke_token(
    client_id="CLIENT_ID",
    access_token="ACCESS_TOKEN",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 

The Square-issued ID for your application, which is available on the **OAuth** page in the
[Developer Dashboard](https://developer.squareup.com/apps).
    
</dd>
</dl>

<dl>
<dd>

**access_token:** `typing.Optional[str]` 

The access token of the merchant whose token you want to revoke.
Do not provide a value for `merchant_id` if you provide this parameter.
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` 

The ID of the merchant whose token you want to revoke.
Do not provide a value for `access_token` if you provide this parameter.
    
</dd>
</dl>

<dl>
<dd>

**revoke_only_access_token:** `typing.Optional[bool]` 

If `true`, terminate the given single access token, but do not
terminate the entire authorization.
Default: `false`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth.<a href="src/square/o_auth/client.py">obtain_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an OAuth access token and refresh token using the `authorization_code`
or `refresh_token` grant type.

When `grant_type` is `authorization_code`:
- With the [code flow](https://developer.squareup.com/docs/oauth-api/overview#code-flow),
provide `code`, `client_id`, and `client_secret`.
- With the [PKCE flow](https://developer.squareup.com/docs/oauth-api/overview#pkce-flow),
provide `code`, `client_id`, and `code_verifier`. 

When `grant_type` is `refresh_token`:
- With the code flow, provide `refresh_token`, `client_id`, and `client_secret`.
The response returns the same refresh token provided in the request.
- With the PKCE flow, provide `refresh_token` and `client_id`. The response returns
a new refresh token.

You can use the `scopes` parameter to limit the set of permissions authorized by the
access token. You can use the `short_lived` parameter to create an access token that
expires in 24 hours.

__Important:__ OAuth tokens should be encrypted and stored on a secure server.
Application clients should never interact directly with OAuth tokens.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.o_auth.obtain_token(
    client_id="sq0idp-uaPHILoPzWZk3tlJqlML0g",
    client_secret="sq0csp-30a-4C_tVOnTh14Piza2BfTPBXyLafLPWSzY1qAjeBfM",
    code="sq0cgb-l0SBqxs4uwxErTVyYOdemg",
    grant_type="authorization_code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 

The Square-issued ID of your application, which is available as the **Application ID**
on the **OAuth** page in the [Developer Console](https://developer.squareup.com/apps).

Required for the code flow and PKCE flow for any grant type.
    
</dd>
</dl>

<dl>
<dd>

**grant_type:** `str` 

The method used to obtain an OAuth access token. The request must include the
credential that corresponds to the specified grant type. Valid values are:
- `authorization_code` - Requires the `code` field.
- `refresh_token` - Requires the `refresh_token` field.
- `migration_token` - LEGACY for access tokens obtained using a Square API version prior
to 2019-03-13. Requires the `migration_token` field.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` 

The secret key for your application, which is available as the **Application secret**
on the **OAuth** page in the [Developer Console](https://developer.squareup.com/apps).

Required for the code flow for any grant type. Don't confuse your client secret with your
personal access token.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 

The authorization code to exchange for an OAuth access token. This is the `code`
value that Square sent to your redirect URL in the authorization response.

Required for the code flow and PKCE flow if `grant_type` is `authorization_code`.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `typing.Optional[str]` 

The redirect URL for your application, which you registered as the **Redirect URL**
on the **OAuth** page in the [Developer Console](https://developer.squareup.com/apps).

Required for the code flow and PKCE flow if `grant_type` is `authorization_code` and
you provided the `redirect_uri` parameter in your authorization URL.
    
</dd>
</dl>

<dl>
<dd>

**refresh_token:** `typing.Optional[str]` 

A valid refresh token used to generate a new OAuth access token. This is a
refresh token that was returned in a previous `ObtainToken` response.

Required for the code flow and PKCE flow if `grant_type` is `refresh_token`.
    
</dd>
</dl>

<dl>
<dd>

**migration_token:** `typing.Optional[str]` 

__LEGACY__ A valid access token (obtained using a Square API version prior to 2019-03-13)
used to generate a new OAuth access token.

Required if `grant_type` is `migration_token`. For more information, see
[Migrate to Using Refresh Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[typing.Sequence[str]]` 

The list of permissions that are explicitly requested for the access token.
For example, ["MERCHANT_PROFILE_READ","PAYMENTS_READ","BANK_ACCOUNTS_READ"].

The returned access token is limited to the permissions that are the intersection
of these requested permissions and those authorized by the provided `refresh_token`.

Optional for the code flow and PKCE flow if `grant_type` is `refresh_token`.
    
</dd>
</dl>

<dl>
<dd>

**short_lived:** `typing.Optional[bool]` 

Indicates whether the returned access token should expire in 24 hours.

Optional for the code flow and PKCE flow for any grant type. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**code_verifier:** `typing.Optional[str]` 

The secret your application generated for the authorization request used to
obtain the authorization code. This is the source of the `code_challenge` hash you
provided in your authorization URL.

Required for the PKCE flow if `grant_type` is `authorization_code`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth.<a href="src/square/o_auth/client.py">retrieve_token_status</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about an [OAuth access token](https://developer.squareup.com/docs/build-basics/access-tokens#get-an-oauth-access-token) or an application’s [personal access token](https://developer.squareup.com/docs/build-basics/access-tokens#get-a-personal-access-token).

Add the access token to the Authorization header of the request.

__Important:__ The `Authorization` header you provide to this endpoint must have the following format:

```
Authorization: Bearer ACCESS_TOKEN
```

where `ACCESS_TOKEN` is a
[valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

If the access token is expired or not a valid access token, the endpoint returns an `UNAUTHORIZED` error.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.o_auth.retrieve_token_status()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth.<a href="src/square/o_auth/client.py">authorize</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.o_auth.authorize()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## V1Transactions
<details><summary><code>client.v1transactions.<a href="src/square/v1transactions/client.py">v1list_orders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides summary information for a merchant's online store orders.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.v1transactions.v1list_orders(
    location_id="location_id",
    order="DESC",
    limit=1,
    batch_token="batch_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list online store orders for.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[SortOrder]` — The order in which payments are listed in the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of payments to return in a single response. This value cannot exceed 200.
    
</dd>
</dl>

<dl>
<dd>

**batch_token:** `typing.Optional[str]` 

A pagination cursor to retrieve the next set of results for your
original query to the endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/square/v1transactions/client.py">v1retrieve_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides comprehensive information for a single online store order, including the order's history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.v1transactions.v1retrieve_order(
    location_id="location_id",
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the order's associated location.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.v1transactions.<a href="src/square/v1transactions/client.py">v1update_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the details of an online store order. Every update you perform on an order corresponds to one of three actions:
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.v1transactions.v1update_order(
    location_id="location_id",
    order_id="order_id",
    action="COMPLETE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the order's associated location.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint
    
</dd>
</dl>

<dl>
<dd>

**action:** `V1UpdateOrderRequestAction` 

The action to perform on the order (COMPLETE, CANCEL, or REFUND).
See [V1UpdateOrderRequestAction](#type-v1updateorderrequestaction) for possible values
    
</dd>
</dl>

<dl>
<dd>

**shipped_tracking_number:** `typing.Optional[str]` — The tracking number of the shipment associated with the order. Only valid if action is COMPLETE.
    
</dd>
</dl>

<dl>
<dd>

**completed_note:** `typing.Optional[str]` — A merchant-specified note about the completion of the order. Only valid if action is COMPLETE.
    
</dd>
</dl>

<dl>
<dd>

**refunded_note:** `typing.Optional[str]` — A merchant-specified note about the refunding of the order. Only valid if action is REFUND.
    
</dd>
</dl>

<dl>
<dd>

**canceled_note:** `typing.Optional[str]` — A merchant-specified note about the canceling of the order. Only valid if action is CANCEL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApplePay
<details><summary><code>client.apple_pay.<a href="src/square/apple_pay/client.py">register_domain</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Activates a domain for use with Apple Pay on the Web and Square. A validation
is performed on this domain by Apple to ensure that it is properly set up as
an Apple Pay enabled domain.

This endpoint provides an easy way for platform developers to bulk activate
Apple Pay on the Web with Square for merchants using their platform.

Note: You will need to host a valid domain verification file on your domain to support Apple Pay.  The
current version of this file is always available at https://app.squareup.com/digital-wallets/apple-pay/apple-developer-merchantid-domain-association,
and should be hosted at `.well_known/apple-developer-merchantid-domain-association` on your
domain.  This file is subject to change; we strongly recommend checking for updates regularly and avoiding
long-lived caches that might not keep in sync with the correct file version.

To learn more about the Web Payments SDK and how to add Apple Pay, see [Take an Apple Pay Payment](https://developer.squareup.com/docs/web-payments/apple-pay).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.apple_pay.register_domain(
    domain_name="example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_name:** `str` — A domain name as described in RFC-1034 that will be registered with ApplePay.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BankAccounts
<details><summary><code>client.bank_accounts.<a href="src/square/bank_accounts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of [BankAccount](entity:BankAccount) objects linked to a Square account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.bank_accounts.list(
    cursor="cursor",
    limit=1,
    location_id="location_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The pagination cursor returned by a previous call to this endpoint.
Use it in the next `ListBankAccounts` request to retrieve the next set 
of results.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Upper limit on the number of bank accounts to return in the response. 
Currently, 1000 is the largest supported limit. You can specify a limit 
of up to 1000 bank accounts. This is also the default limit.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

Location ID. You can specify this optional filter 
to retrieve only the linked bank accounts belonging to a specific location.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bank_accounts.<a href="src/square/bank_accounts/client.py">get_by_v1id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details of a [BankAccount](entity:BankAccount) identified by V1 bank account ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bank_accounts.get_by_v1id(
    v1bank_account_id="v1_bank_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**v1bank_account_id:** `str` 

Connect V1 ID of the desired `BankAccount`. For more information, see 
[Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bank_accounts.<a href="src/square/bank_accounts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details of a [BankAccount](entity:BankAccount)
linked to a Square account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bank_accounts.get(
    bank_account_id="bank_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` — Square-issued ID of the desired `BankAccount`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Bookings
<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a collection of bookings.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.bookings.list(
    limit=1,
    cursor="cursor",
    customer_id="customer_id",
    team_member_id="team_member_id",
    location_id="location_id",
    start_at_min="start_at_min",
    start_at_max="start_at_max",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results per page to return in a paged response.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor from the preceding response to return the next page of the results. Do not set this when retrieving the first page of the results.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — The [customer](entity:Customer) for whom to retrieve bookings. If this is not set, bookings for all customers are retrieved.
    
</dd>
</dl>

<dl>
<dd>

**team_member_id:** `typing.Optional[str]` — The team member for whom to retrieve bookings. If this is not set, bookings of all members are retrieved.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` — The location for which to retrieve bookings. If this is not set, all locations' bookings are retrieved.
    
</dd>
</dl>

<dl>
<dd>

**start_at_min:** `typing.Optional[str]` — The RFC 3339 timestamp specifying the earliest of the start time. If this is not set, the current time is used.
    
</dd>
</dl>

<dl>
<dd>

**start_at_max:** `typing.Optional[str]` — The RFC 3339 timestamp specifying the latest of the start time. If this is not set, the time of 31 days after `start_at_min` is used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a booking.

The required input must include the following:
- `Booking.location_id`
- `Booking.start_at`
- `Booking.AppointmentSegment.team_member_id`
- `Booking.AppointmentSegment.service_variation_id`
- `Booking.AppointmentSegment.service_variation_version`

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.create(
    booking={},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking:** `BookingParams` — The details of the booking to be created.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique key to make this request an idempotent operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">search_availability</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for availabilities for booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.search_availability(
    query={"filter": {"start_at_range": {}}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `SearchAvailabilityQueryParams` — Query conditions used to filter buyer-accessible booking availabilities.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">bulk_retrieve_bookings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk-Retrieves a list of bookings by booking IDs.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.bulk_retrieve_bookings(
    booking_ids=["booking_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_ids:** `typing.Sequence[str]` — A non-empty list of [Booking](entity:Booking) IDs specifying bookings to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">get_business_profile</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a seller's booking profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.get_business_profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">retrieve_location_booking_profile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a seller's location booking profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.retrieve_location_booking_profile(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to retrieve the booking profile.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">bulk_retrieve_team_member_booking_profiles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves one or more team members' booking profiles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.bulk_retrieve_team_member_booking_profiles(
    team_member_ids=["team_member_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_ids:** `typing.Sequence[str]` — A non-empty list of IDs of team members whose booking profiles you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.get(
    booking_id="booking_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_id:** `str` — The ID of the [Booking](entity:Booking) object representing the to-be-retrieved booking.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.update(
    booking_id="booking_id",
    booking={},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_id:** `str` — The ID of the [Booking](entity:Booking) object representing the to-be-updated booking.
    
</dd>
</dl>

<dl>
<dd>

**booking:** `BookingParams` — The booking to be updated. Individual attributes explicitly specified here override the corresponding values of the existing booking.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique key to make this request an idempotent operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.<a href="src/square/bookings/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels an existing booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.cancel(
    booking_id="booking_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_id:** `str` — The ID of the [Booking](entity:Booking) object representing the to-be-cancelled booking.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique key to make this request an idempotent operation.
    
</dd>
</dl>

<dl>
<dd>

**booking_version:** `typing.Optional[int]` — The revision number for the booking used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Cards
<details><summary><code>client.cards.<a href="src/square/cards/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of cards owned by the account making the request.
A max of 25 cards will be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.cards.list(
    cursor="cursor",
    customer_id="customer_id",
    include_disabled=True,
    reference_id="reference_id",
    sort_order="DESC",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.

See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 

Limit results to cards associated with the customer supplied.
By default, all cards owned by the merchant are returned.
    
</dd>
</dl>

<dl>
<dd>

**include_disabled:** `typing.Optional[bool]` 

Includes disabled cards.
By default, all enabled cards owned by the merchant are returned.
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — Limit results to cards associated with the reference_id supplied.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SortOrder]` 

Sorts the returned list by when the card was created with the specified order.
This field defaults to ASC.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cards.<a href="src/square/cards/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a card on file to an existing merchant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.cards.create(
    idempotency_key="4935a656-a929-4792-b97c-8848be85c27c",
    source_id="cnon:uIbfJXhXETSP197M3GB",
    card={
        "cardholder_name": "Amelia Earhart",
        "billing_address": {
            "address_line1": "500 Electric Ave",
            "address_line2": "Suite 600",
            "locality": "New York",
            "administrative_district_level1": "NY",
            "postal_code": "10003",
            "country": "US",
        },
        "customer_id": "VDKXEEKPJN48QDG3BGGFAK05P8",
        "reference_id": "user-id-1",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this CreateCard request. Keys can be
any valid string and must be unique for every request.

Max: 45 characters

See [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `str` — The ID of the source which represents the card information to be stored. This can be a card nonce or a payment id.
    
</dd>
</dl>

<dl>
<dd>

**card:** `CardParams` — Payment details associated with the card to be stored.
    
</dd>
</dl>

<dl>
<dd>

**verification_token:** `typing.Optional[str]` 

An identifying token generated by [Payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
Verification tokens encapsulate customer device information and 3-D Secure
challenge results to indicate that Square has verified the buyer identity.

See the [SCA Overview](https://developer.squareup.com/docs/sca-overview).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cards.<a href="src/square/cards/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details for a specific Card.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.cards.get(
    card_id="card_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**card_id:** `str` — Unique ID for the desired Card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cards.<a href="src/square/cards/client.py">disable</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables the card, preventing any further updates or charges.
Disabling an already disabled card is allowed but has no effect.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.cards.disable(
    card_id="card_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**card_id:** `str` — Unique ID for the desired Card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Catalog
<details><summary><code>client.catalog.<a href="src/square/catalog/client.py">batch_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a set of [CatalogItem](entity:CatalogItem)s based on the
provided list of target IDs and returns a set of successfully deleted IDs in
the response. Deletion is a cascading event such that all children of the
targeted object are also deleted. For example, deleting a CatalogItem will
also delete all of its [CatalogItemVariation](entity:CatalogItemVariation)
children.

`BatchDeleteCatalogObjects` succeeds even if only a portion of the targeted
IDs can be deleted. The response will only include IDs that were
actually deleted.

To ensure consistency, only one delete request is processed at a time per seller account.
While one (batch or non-batch) delete request is being processed, other (batched and non-batched)
delete requests are rejected with the `429` error code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.batch_delete(
    object_ids=["W62UWFY35CWMYGVWK6TWJDNI", "AA27W3M2GGTF3H6AVPNB77CK"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_ids:** `typing.Sequence[str]` 

The IDs of the CatalogObjects to be deleted. When an object is deleted, other objects
in the graph that depend on that object will be deleted as well (for example, deleting a
CatalogItem will delete its CatalogItemVariation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/square/catalog/client.py">batch_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a set of objects based on the provided ID.
Each [CatalogItem](entity:CatalogItem) returned in the set includes all of its
child information including: all of its
[CatalogItemVariation](entity:CatalogItemVariation) objects, references to
its [CatalogModifierList](entity:CatalogModifierList) objects, and the ids of
any [CatalogTax](entity:CatalogTax) objects that apply to it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.batch_get(
    object_ids=["W62UWFY35CWMYGVWK6TWJDNI", "AA27W3M2GGTF3H6AVPNB77CK"],
    include_related_objects=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_ids:** `typing.Sequence[str]` — The IDs of the CatalogObjects to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**include_related_objects:** `typing.Optional[bool]` 

If `true`, the response will include additional objects that are related to the
requested objects. Related objects are defined as any objects referenced by ID by the results in the `objects` field
of the response. These objects are put in the `related_objects` field. Setting this to `true` is
helpful when the objects are needed for immediate display to a user.
This process only goes one level deep. Objects referenced by the related objects will not be included. For example,

if the `objects` field of the response contains a CatalogItem, its associated
CatalogCategory objects, CatalogTax objects, CatalogImage objects and
CatalogModifierLists will be returned in the `related_objects` field of the
response. If the `objects` field of the response contains a CatalogItemVariation,
its parent CatalogItem will be returned in the `related_objects` field of
the response.

Default value: `false`
    
</dd>
</dl>

<dl>
<dd>

**catalog_version:** `typing.Optional[int]` 

The specific version of the catalog objects to be included in the response. 
This allows you to retrieve historical versions of objects. The specified version value is matched against
the [CatalogObject](entity:CatalogObject)s' `version` attribute. If not included, results will
be from the current version of the catalog.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_objects:** `typing.Optional[bool]` — Indicates whether to include (`true`) or not (`false`) in the response deleted objects, namely, those with the `is_deleted` attribute set to `true`.
    
</dd>
</dl>

<dl>
<dd>

**include_category_path_to_root:** `typing.Optional[bool]` 

Specifies whether or not to include the `path_to_root` list for each returned category instance. The `path_to_root` list consists
of `CategoryPathToRootNode` objects and specifies the path that starts with the immediate parent category of the returned category
and ends with its root category. If the returned category is a top-level category, the `path_to_root` list is empty and is not returned
in the response payload.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/square/catalog/client.py">batch_upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates up to 10,000 target objects based on the provided
list of objects. The target objects are grouped into batches and each batch is
inserted/updated in an all-or-nothing manner. If an object within a batch is
malformed in some way, or violates a database constraint, the entire batch
containing that item will be disregarded. However, other batches in the same
request may still succeed. Each batch may contain up to 1,000 objects, and
batches will be processed in order as long as the total object count for the
request (items, variations, modifier lists, discounts, and taxes) is no more
than 10,000.

To ensure consistency, only one update request is processed at a time per seller account.
While one (batch or non-batch) update request is being processed, other (batched and non-batched)
update requests are rejected with the `429` error code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.batch_upsert(
    idempotency_key="789ff020-f723-43a9-b4b5-43b5dc1fa3dc",
    batches=[
        {
            "objects": [
                {
                    "type": "IMAGE",
                    "id": "#Tea",
                    "present_at_all_locations": True,
                },
                {
                    "type": "IMAGE",
                    "id": "#Coffee",
                    "present_at_all_locations": True,
                },
                {
                    "type": "ITEM",
                    "id": "#Beverages",
                    "present_at_all_locations": True,
                },
                {
                    "type": "TAX",
                    "id": "#SalesTax",
                    "present_at_all_locations": True,
                    "tax_data": {
                        "name": "Sales Tax",
                        "calculation_phase": "TAX_SUBTOTAL_PHASE",
                        "inclusion_type": "ADDITIVE",
                        "percentage": "5.0",
                        "applies_to_custom_amounts": True,
                        "enabled": True,
                    },
                },
            ]
        }
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A value you specify that uniquely identifies this
request among all your requests. A common way to create
a valid idempotency key is to use a Universally unique
identifier (UUID).

If you're unsure whether a particular request was successful,
you can reattempt it with the same idempotency key without
worrying about creating duplicate objects.

See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**batches:** `typing.Sequence[CatalogObjectBatchParams]` 

A batch of CatalogObjects to be inserted/updated atomically.
The objects within a batch will be inserted in an all-or-nothing fashion, i.e., if an error occurs
attempting to insert or update an object within a batch, the entire batch will be rejected. However, an error
in one batch will not affect other batches within the same request.

For each object, its `updated_at` field is ignored and replaced with a current [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates), and its
`is_deleted` field must not be set to `true`.

To modify an existing object, supply its ID. To create a new object, use an ID starting
with `#`. These IDs may be used to create relationships between an object and attributes of
other objects that reference it. For example, you can create a CatalogItem with
ID `#ABC` and a CatalogItemVariation with its `item_id` attribute set to
`#ABC` in order to associate the CatalogItemVariation with its parent
CatalogItem.

Any `#`-prefixed IDs are valid only within a single atomic batch, and will be replaced by server-generated IDs.

Each batch may contain up to 1,000 objects. The total number of objects across all batches for a single request
may not exceed 10,000. If either of these limits is violated, an error will be returned and no objects will
be inserted or updated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/square/catalog/client.py">info</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves information about the Square Catalog API, such as batch size
limits that can be used by the `BatchUpsertCatalogObjects` endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.info()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/square/catalog/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all [CatalogObject](entity:CatalogObject)s of the specified types in the catalog.

The `types` parameter is specified as a comma-separated list of the [CatalogObjectType](entity:CatalogObjectType) values,
for example, "`ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`".

__Important:__ ListCatalog does not return deleted catalog items. To retrieve
deleted catalog items, use [SearchCatalogObjects](api-endpoint:Catalog-SearchCatalogObjects)
and set the `include_deleted_objects` attribute value to `true`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.catalog.list(
    cursor="cursor",
    types="types",
    catalog_version=1000000,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The pagination cursor returned in the previous response. Leave unset for an initial request.
The page size is currently set to be 100.
See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[str]` 

An optional case-insensitive, comma-separated list of object types to retrieve.

The valid values are defined in the [CatalogObjectType](entity:CatalogObjectType) enum, for example,
`ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`,
`MODIFIER`, `MODIFIER_LIST`, `IMAGE`, etc.

If this is unspecified, the operation returns objects of all the top level types at the version
of the Square API used to make the request. Object types that are nested onto other object types
are not included in the defaults.

At the current API version the default object types are:
ITEM, CATEGORY, TAX, DISCOUNT, MODIFIER_LIST, 
PRICING_RULE, PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT,
SUBSCRIPTION_PLAN, ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION, QUICK_AMOUNT_SETTINGS.
    
</dd>
</dl>

<dl>
<dd>

**catalog_version:** `typing.Optional[int]` 

The specific version of the catalog objects to be included in the response.
This allows you to retrieve historical versions of objects. The specified version value is matched against
the [CatalogObject](entity:CatalogObject)s' `version` attribute.  If not included, results will be from the
current version of the catalog.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/square/catalog/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for [CatalogObject](entity:CatalogObject) of any type by matching supported search attribute values,
excluding custom attribute values on items or item variations, against one or more of the specified query filters.

This (`SearchCatalogObjects`) endpoint differs from the [SearchCatalogItems](api-endpoint:Catalog-SearchCatalogItems)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints have different call conventions, including the query filter formats.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.catalog.search(
    object_types=["ITEM"],
    query={
        "prefix_query": {"attribute_name": "name", "attribute_prefix": "tea"}
    },
    limit=100,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The pagination cursor returned in the previous response. Leave unset for an initial request.
See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**object_types:** `typing.Optional[typing.Sequence[CatalogObjectType]]` 

The desired set of object types to appear in the search results.

If this is unspecified, the operation returns objects of all the top level types at the version
of the Square API used to make the request. Object types that are nested onto other object types
are not included in the defaults.

At the current API version the default object types are:
ITEM, CATEGORY, TAX, DISCOUNT, MODIFIER_LIST, 
PRICING_RULE, PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT,
SUBSCRIPTION_PLAN, ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION, QUICK_AMOUNT_SETTINGS.

Note that if you wish for the query to return objects belonging to nested types (i.e., COMPONENT, IMAGE,
ITEM_OPTION_VAL, ITEM_VARIATION, or MODIFIER), you must explicitly include all the types of interest
in this field.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_objects:** `typing.Optional[bool]` — If `true`, deleted objects will be included in the results. Defaults to `false`. Deleted objects will have their `is_deleted` field set to `true`. If `include_deleted_objects` is `true`, then the `include_category_path_to_root` request parameter must be `false`. Both properties cannot be `true` at the same time.
    
</dd>
</dl>

<dl>
<dd>

**include_related_objects:** `typing.Optional[bool]` 

If `true`, the response will include additional objects that are related to the
requested objects. Related objects are objects that are referenced by object ID by the objects
in the response. This is helpful if the objects are being fetched for immediate display to a user.
This process only goes one level deep. Objects referenced by the related objects will not be included.
For example:

If the `objects` field of the response contains a CatalogItem, its associated
CatalogCategory objects, CatalogTax objects, CatalogImage objects and
CatalogModifierLists will be returned in the `related_objects` field of the
response. If the `objects` field of the response contains a CatalogItemVariation,
its parent CatalogItem will be returned in the `related_objects` field of
the response.

Default value: `false`
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

Return objects modified after this [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates), in RFC 3339
format, e.g., `2016-09-04T23:59:33.123Z`. The timestamp is exclusive - objects with a
timestamp equal to `begin_time` will not be included in the response.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[CatalogQueryParams]` — A query to be used to filter or sort the results. If no query is specified, the entire catalog will be returned.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

A limit on the number of results to be returned in a single page. The limit is advisory -
the implementation may return more or fewer results. If the supplied limit is negative, zero, or
is higher than the maximum limit of 1,000, it will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**include_category_path_to_root:** `typing.Optional[bool]` — Specifies whether or not to include the `path_to_root` list for each returned category instance. The `path_to_root` list consists of `CategoryPathToRootNode` objects and specifies the path that starts with the immediate parent category of the returned category and ends with its root category. If the returned category is a top-level category, the `path_to_root` list is empty and is not returned in the response payload. If `include_category_path_to_root` is `true`, then the `include_deleted_objects` request parameter must be `false`. Both properties cannot be `true` at the same time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/square/catalog/client.py">search_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for catalog items or item variations by matching supported search attribute values, including
custom attribute values, against one or more of the specified query filters.

This (`SearchCatalogItems`) endpoint differs from the [SearchCatalogObjects](api-endpoint:Catalog-SearchCatalogObjects)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints use different call conventions, including the query filter formats.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.catalog.search_items(
    text_filter="red",
    category_ids=["WINE_CATEGORY_ID"],
    stock_levels=["OUT", "LOW"],
    enabled_location_ids=["ATL_LOCATION_ID"],
    limit=100,
    sort_order="ASC",
    product_types=["REGULAR"],
    custom_attribute_filters=[
        {
            "custom_attribute_definition_id": "VEGAN_DEFINITION_ID",
            "bool_filter": True,
        },
        {
            "custom_attribute_definition_id": "BRAND_DEFINITION_ID",
            "string_filter": "Dark Horse",
        },
        {"key": "VINTAGE", "number_filter": {"min": "min", "max": "max"}},
        {"custom_attribute_definition_id": "VARIETAL_DEFINITION_ID"},
    ],
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_filter:** `typing.Optional[str]` 

The text filter expression to return items or item variations containing specified text in
the `name`, `description`, or `abbreviation` attribute value of an item, or in
the `name`, `sku`, or `upc` attribute value of an item variation.
    
</dd>
</dl>

<dl>
<dd>

**category_ids:** `typing.Optional[typing.Sequence[str]]` — The category id query expression to return items containing the specified category IDs.
    
</dd>
</dl>

<dl>
<dd>

**stock_levels:** `typing.Optional[typing.Sequence[SearchCatalogItemsRequestStockLevel]]` 

The stock-level query expression to return item variations with the specified stock levels.
See [SearchCatalogItemsRequestStockLevel](#type-searchcatalogitemsrequeststocklevel) for possible values
    
</dd>
</dl>

<dl>
<dd>

**enabled_location_ids:** `typing.Optional[typing.Sequence[str]]` — The enabled-location query expression to return items and item variations having specified enabled locations.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination token, returned in the previous response, used to fetch the next batch of pending results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return per page. The default value is 100.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SortOrder]` 

The order to sort the results by item names. The default sort order is ascending (`ASC`).
See [SortOrder](#type-sortorder) for possible values
    
</dd>
</dl>

<dl>
<dd>

**product_types:** `typing.Optional[typing.Sequence[CatalogItemProductType]]` — The product types query expression to return items or item variations having the specified product types.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_filters:** `typing.Optional[typing.Sequence[CustomAttributeFilterParams]]` 

The customer-attribute filter to return items or item variations matching the specified
custom attribute expressions. A maximum number of 10 custom attribute expressions are supported in
a single call to the [SearchCatalogItems](api-endpoint:Catalog-SearchCatalogItems) endpoint.
    
</dd>
</dl>

<dl>
<dd>

**archived_state:** `typing.Optional[ArchivedState]` — The query filter to return not archived (`ARCHIVED_STATE_NOT_ARCHIVED`), archived (`ARCHIVED_STATE_ARCHIVED`), or either type (`ARCHIVED_STATE_ALL`) of items.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/square/catalog/client.py">update_item_modifier_lists</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the [CatalogModifierList](entity:CatalogModifierList) objects
that apply to the targeted [CatalogItem](entity:CatalogItem) without having
to perform an upsert on the entire item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.update_item_modifier_lists(
    item_ids=["H42BRLUJ5KTZTTMPVSLFAACQ", "2JXOBJIHCWBQ4NZ3RIXQGJA6"],
    modifier_lists_to_enable=[
        "H42BRLUJ5KTZTTMPVSLFAACQ",
        "2JXOBJIHCWBQ4NZ3RIXQGJA6",
    ],
    modifier_lists_to_disable=["7WRC16CJZDVLSNDQ35PP6YAD"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_ids:** `typing.Sequence[str]` — The IDs of the catalog items associated with the CatalogModifierList objects being updated.
    
</dd>
</dl>

<dl>
<dd>

**modifier_lists_to_enable:** `typing.Optional[typing.Sequence[str]]` 

The IDs of the CatalogModifierList objects to enable for the CatalogItem.
At least one of `modifier_lists_to_enable` or `modifier_lists_to_disable` must be specified.
    
</dd>
</dl>

<dl>
<dd>

**modifier_lists_to_disable:** `typing.Optional[typing.Sequence[str]]` 

The IDs of the CatalogModifierList objects to disable for the CatalogItem.
At least one of `modifier_lists_to_enable` or `modifier_lists_to_disable` must be specified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.<a href="src/square/catalog/client.py">update_item_taxes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the [CatalogTax](entity:CatalogTax) objects that apply to the
targeted [CatalogItem](entity:CatalogItem) without having to perform an
upsert on the entire item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.update_item_taxes(
    item_ids=["H42BRLUJ5KTZTTMPVSLFAACQ", "2JXOBJIHCWBQ4NZ3RIXQGJA6"],
    taxes_to_enable=["4WRCNHCJZDVLSNDQ35PP6YAD"],
    taxes_to_disable=["AQCEGCEBBQONINDOHRGZISEX"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**item_ids:** `typing.Sequence[str]` 

IDs for the CatalogItems associated with the CatalogTax objects being updated.
No more than 1,000 IDs may be provided.
    
</dd>
</dl>

<dl>
<dd>

**taxes_to_enable:** `typing.Optional[typing.Sequence[str]]` 

IDs of the CatalogTax objects to enable.
At least one of `taxes_to_enable` or `taxes_to_disable` must be specified.
    
</dd>
</dl>

<dl>
<dd>

**taxes_to_disable:** `typing.Optional[typing.Sequence[str]]` 

IDs of the CatalogTax objects to disable.
At least one of `taxes_to_enable` or `taxes_to_disable` must be specified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Channels
<details><summary><code>client.channels.<a href="src/square/channels/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.channels.list(
    reference_type="UNKNOWN_TYPE",
    reference_id="reference_id",
    status="ACTIVE",
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reference_type:** `typing.Optional[ReferenceType]` — Type of reference associated to channel
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — id of reference associated to channel
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ChannelStatus]` — Status of channel
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor to fetch the next result
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Maximum number of results to return.
When not provided the returned results will be cap at 100 channels.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/square/channels/client.py">bulk_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.channels.bulk_retrieve(
    channel_ids=["CH_9C03D0B59", "CH_6X139B5MN", "NOT_EXISTING"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**channel_ids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.channels.<a href="src/square/channels/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.channels.get(
    channel_id="channel_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**channel_id:** `str` — A channel id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customers
<details><summary><code>client.customers.<a href="src/square/customers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists customer profiles associated with a Square account.

Under normal operating conditions, newly created or updated customer profiles become available
for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated
profiles can take closer to one minute or longer, especially during network incidents and outages.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.customers.list(
    cursor="cursor",
    limit=1,
    sort_field="DEFAULT",
    sort_order="DESC",
    count=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
If the specified limit is less than 1 or greater than 100, Square returns a `400 VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default value is 100.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[CustomerSortField]` 

Indicates how customers should be sorted.

The default value is `DEFAULT`.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SortOrder]` 

Indicates whether customers should be sorted in ascending (`ASC`) or
descending (`DESC`) order.

The default value is `ASC`.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` 

Indicates whether to return the total count of customers in the `count` field of the response.

The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/square/customers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new customer for a business.

You must provide at least one of the following values in your request to this
endpoint:

- `given_name`
- `family_name`
- `company_name`
- `email_address`
- `phone_number`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.create(
    given_name="Amelia",
    family_name="Earhart",
    email_address="Amelia.Earhart@example.com",
    address={
        "address_line1": "500 Electric Ave",
        "address_line2": "Suite 600",
        "locality": "New York",
        "administrative_district_level1": "NY",
        "postal_code": "10003",
        "country": "US",
    },
    phone_number="+1-212-555-4240",
    reference_id="YOUR_REFERENCE_ID",
    note="a customer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

The idempotency key for the request.	For more information, see
[Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[str]` 

The given name (that is, the first name) associated with the customer profile.

The maximum length for this value is 300 characters.
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` 

The family name (that is, the last name) associated with the customer profile.

The maximum length for this value is 300 characters.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` 

A business name associated with the customer profile.

The maximum length for this value is 500 characters.
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[str]` 

A nickname for the customer profile.

The maximum length for this value is 100 characters.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` 

The email address associated with the customer profile.

The maximum length for this value is 254 characters.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[AddressParams]` 

The physical address associated with the customer profile. For maximum length constraints, see 
[Customer addresses](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#address).
The `first_name` and `last_name` fields are ignored if they are present in the request.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` 

The phone number associated with the customer profile. The phone number must be valid and can contain
9–16 digits, with an optional `+` prefix and country code. For more information, see
[Customer phone numbers](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#phone-number).
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` 

An optional second ID used to associate the customer profile with an
entity in another system.

The maximum length for this value is 100 characters.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — A custom note associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[str]` 

The birthday associated with the customer profile, in `YYYY-MM-DD` or `MM-DD` format. For example,
specify `1998-09-21` for September 21, 1998, or `09-21` for September 21. Birthdays are returned in `YYYY-MM-DD`
format, where `YYYY` is the specified birth year or `0000` if a birth year is not specified.
    
</dd>
</dl>

<dl>
<dd>

**tax_ids:** `typing.Optional[CustomerTaxIdsParams]` 

The tax ID associated with the customer profile. This field is available only for customers of sellers
in EU countries or the United Kingdom. For more information,
see [Customer tax IDs](https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/square/customers/client.py">batch_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates multiple [customer profiles](entity:Customer) for a business.

This endpoint takes a map of individual create requests and returns a map of responses.

You must provide at least one of the following values in each create request:

- `given_name`
- `family_name`
- `company_name`
- `email_address`
- `phone_number`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.batch_create(
    customers={
        "8bb76c4f-e35d-4c5b-90de-1194cd9179f0": {
            "given_name": "Amelia",
            "family_name": "Earhart",
            "email_address": "Amelia.Earhart@example.com",
            "address": {
                "address_line1": "500 Electric Ave",
                "address_line2": "Suite 600",
                "locality": "New York",
                "administrative_district_level1": "NY",
                "postal_code": "10003",
                "country": "US",
            },
            "phone_number": "+1-212-555-4240",
            "reference_id": "YOUR_REFERENCE_ID",
            "note": "a customer",
        },
        "d1689f23-b25d-4932-b2f0-aed00f5e2029": {
            "given_name": "Marie",
            "family_name": "Curie",
            "email_address": "Marie.Curie@example.com",
            "address": {
                "address_line1": "500 Electric Ave",
                "address_line2": "Suite 601",
                "locality": "New York",
                "administrative_district_level1": "NY",
                "postal_code": "10003",
                "country": "US",
            },
            "phone_number": "+1-212-444-4240",
            "reference_id": "YOUR_REFERENCE_ID",
            "note": "another customer",
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customers:** `typing.Dict[str, BulkCreateCustomerDataParams]` 

A map of 1 to 100 individual create requests, represented by `idempotency key: { customer data }`
key-value pairs.

Each key is an [idempotency key](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency)
that uniquely identifies the create request. Each value contains the customer data used to create the
customer profile.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/square/customers/client.py">bulk_delete_customers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes multiple customer profiles.

The endpoint takes a list of customer IDs and returns a map of responses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.bulk_delete_customers(
    customer_ids=[
        "8DDA5NZVBZFGAX0V3HPF81HHE0",
        "N18CPRVXR5214XPBBA6BZQWF3C",
        "2GYD7WNXF7BJZW1PMGNXZ3Y8M8",
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_ids:** `typing.Sequence[str]` — The IDs of the [customer profiles](entity:Customer) to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/square/customers/client.py">bulk_retrieve_customers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves multiple customer profiles.

This endpoint takes a list of customer IDs and returns a map of responses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.bulk_retrieve_customers(
    customer_ids=[
        "8DDA5NZVBZFGAX0V3HPF81HHE0",
        "N18CPRVXR5214XPBBA6BZQWF3C",
        "2GYD7WNXF7BJZW1PMGNXZ3Y8M8",
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_ids:** `typing.Sequence[str]` — The IDs of the [customer profiles](entity:Customer) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/square/customers/client.py">bulk_update_customers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates multiple customer profiles.

This endpoint takes a map of individual update requests and returns a map of responses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.bulk_update_customers(
    customers={
        "8DDA5NZVBZFGAX0V3HPF81HHE0": {
            "email_address": "New.Amelia.Earhart@example.com",
            "note": "updated customer note",
            "version": 2,
        },
        "N18CPRVXR5214XPBBA6BZQWF3C": {
            "given_name": "Marie",
            "family_name": "Curie",
            "version": 0,
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customers:** `typing.Dict[str, BulkUpdateCustomerDataParams]` 

A map of 1 to 100 individual update requests, represented by `customer ID: { customer data }`
key-value pairs.

Each key is the ID of the [customer profile](entity:Customer) to update. To update a customer profile
that was created by merging existing profiles, provide the ID of the newly created profile.

Each value contains the updated customer data. Only new or changed fields are required. To add or
update a field, specify the new value. To remove a field, specify `null`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/square/customers/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches the customer profiles associated with a Square account using one or more supported query filters.

Calling `SearchCustomers` without any explicit query filter returns all
customer profiles ordered alphabetically based on `given_name` and
`family_name`.

Under normal operating conditions, newly created or updated customer profiles become available
for the search operation in well under 30 seconds. Occasionally, propagation of the new or updated
profiles can take closer to one minute or longer, especially during network incidents and outages.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.customers.search(
    limit=2,
    query={
        "filter": {
            "creation_source": {"values": ["THIRD_PARTY"], "rule": "INCLUDE"},
            "created_at": {
                "start_at": "2018-01-01T00:00:00-00:00",
                "end_at": "2018-02-01T00:00:00-00:00",
            },
            "email_address": {"fuzzy": "example.com"},
            "group_ids": {"all_": ["545AXB44B4XXWMVQ4W8SBT3HHF"]},
        },
        "sort": {"field": "CREATED_AT", "order": "ASC"},
    },
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

Include the pagination cursor in subsequent calls to this endpoint to retrieve
the next set of results associated with the original query.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
If the specified limit is invalid, Square returns a `400 VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default value is 100.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[CustomerQueryParams]` 

The filtering and sorting criteria for the search request. If a query is not specified,
Square returns all customer profiles ordered alphabetically by `given_name` and `family_name`.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[bool]` 

Indicates whether to return the total count of matching customers in the `count` field of the response.

The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/square/customers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details for a single customer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.get(
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/square/customers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a customer profile. This endpoint supports sparse updates, so only new or changed fields are required in the request.
To add or update a field, specify the new value. To remove a field, specify `null`.

To update a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.update(
    customer_id="customer_id",
    email_address="New.Amelia.Earhart@example.com",
    note="updated customer note",
    version=2,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to update.
    
</dd>
</dl>

<dl>
<dd>

**given_name:** `typing.Optional[str]` 

The given name (that is, the first name) associated with the customer profile.

The maximum length for this value is 300 characters.
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` 

The family name (that is, the last name) associated with the customer profile.

The maximum length for this value is 300 characters.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `typing.Optional[str]` 

A business name associated with the customer profile.

The maximum length for this value is 500 characters.
    
</dd>
</dl>

<dl>
<dd>

**nickname:** `typing.Optional[str]` 

A nickname for the customer profile.

The maximum length for this value is 100 characters.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` 

The email address associated with the customer profile.

The maximum length for this value is 254 characters.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[AddressParams]` 

The physical address associated with the customer profile. Only new or changed fields are required in the request.

For maximum length constraints, see [Customer addresses](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#address).
The `first_name` and `last_name` fields are ignored if they are present in the request.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[str]` 

The phone number associated with the customer profile. The phone number must be valid and can contain
9–16 digits, with an optional `+` prefix and country code. For more information, see
[Customer phone numbers](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#phone-number).
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` 

An optional second ID used to associate the customer profile with an
entity in another system.

The maximum length for this value is 100 characters.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — A custom note associated with the customer profile.
    
</dd>
</dl>

<dl>
<dd>

**birthday:** `typing.Optional[str]` 

The birthday associated with the customer profile, in `YYYY-MM-DD` or `MM-DD` format. For example,
specify `1998-09-21` for September 21, 1998, or `09-21` for September 21. Birthdays are returned in `YYYY-MM-DD`
format, where `YYYY` is the specified birth year or `0000` if a birth year is not specified.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the customer profile.

As a best practice, you should include this field to enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency) control. For more information, see [Update a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#update-a-customer-profile).
    
</dd>
</dl>

<dl>
<dd>

**tax_ids:** `typing.Optional[CustomerTaxIdsParams]` 

The tax ID associated with the customer profile. This field is available only for customers of sellers
in EU countries or the United Kingdom. For more information,
see [Customer tax IDs](https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/square/customers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a customer profile from a business.

To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.delete(
    customer_id="customer_id",
    version=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to delete.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the customer profile.

As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Devices
<details><summary><code>client.devices.<a href="src/square/devices/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List devices associated with the merchant. Currently, only Terminal API
devices are supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.devices.list(
    cursor="cursor",
    sort_order="DESC",
    limit=1,
    location_id="location_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SortOrder]` 

The order in which results are listed.
- `ASC` - Oldest to newest.
- `DESC` - Newest to oldest (default).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of results to return in a single page.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` — If present, only returns devices at the target location.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.devices.<a href="src/square/devices/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves Device with the associated `device_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.devices.get(
    device_id="device_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_id:** `str` — The unique ID for the desired `Device`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Disputes
<details><summary><code>client.disputes.<a href="src/square/disputes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of disputes associated with a particular account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.disputes.list(
    cursor="cursor",
    states="INQUIRY_EVIDENCE_REQUIRED",
    location_id="location_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[DisputeState]` — The dispute states used to filter the result. If not specified, the endpoint returns all disputes.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

The ID of the location for which to return a list of disputes.
If not specified, the endpoint returns disputes associated with all locations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/square/disputes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns details about a specific dispute.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.disputes.get(
    dispute_id="dispute_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute you want more details about.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/square/disputes/client.py">accept</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
updates the dispute state to ACCEPTED.

Square debits the disputed amount from the seller’s Square account. If the Square account
does not have sufficient funds, Square debits the associated bank account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.disputes.accept(
    dispute_id="dispute_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute you want to accept.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/square/disputes/client.py">create_evidence_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a file to use as evidence in a dispute challenge. The endpoint accepts HTTP
multipart/form-data file uploads in HEIC, HEIF, JPEG, PDF, PNG, and TIFF formats.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.disputes.create_evidence_file(
    dispute_id="dispute_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute for which you want to upload evidence.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[CreateDisputeEvidenceFileRequestParams]` 
    
</dd>
</dl>

<dl>
<dd>

**image_file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/square/disputes/client.py">create_evidence_text</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads text to use as evidence for a dispute challenge.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.disputes.create_evidence_text(
    dispute_id="dispute_id",
    idempotency_key="ed3ee3933d946f1514d505d173c82648",
    evidence_type="TRACKING_NUMBER",
    evidence_text="1Z8888888888888888",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute for which you want to upload evidence.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` — A unique key identifying the request. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**evidence_text:** `str` — The evidence string.
    
</dd>
</dl>

<dl>
<dd>

**evidence_type:** `typing.Optional[DisputeEvidenceType]` 

The type of evidence you are uploading.
See [DisputeEvidenceType](#type-disputeevidencetype) for possible values
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.<a href="src/square/disputes/client.py">submit_evidence</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits evidence to the cardholder's bank.

The evidence submitted by this endpoint includes evidence uploaded
using the [CreateDisputeEvidenceFile](api-endpoint:Disputes-CreateDisputeEvidenceFile) and
[CreateDisputeEvidenceText](api-endpoint:Disputes-CreateDisputeEvidenceText) endpoints and
evidence automatically provided by Square, when available. Evidence cannot be removed from
a dispute after submission.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.disputes.submit_evidence(
    dispute_id="dispute_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute for which you want to submit evidence.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Employees
<details><summary><code>client.employees.<a href="src/square/employees/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.employees.list(
    location_id="location_id",
    status="ACTIVE",
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[EmployeeStatus]` — Specifies the EmployeeStatus to filter the employee by.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of employees to be returned on each page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The token required to retrieve the specified page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.employees.<a href="src/square/employees/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.employees.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — UUID for the employee that was requested.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/square/events/client.py">search_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for Square API events that occur within a 28-day timeframe.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.events.search_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of events for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of events to return in a single page. The response might contain fewer events. The default value is 100, which is also the maximum allowed value.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).

Default: 100
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[SearchEventsQueryParams]` — The filtering and sorting criteria for the search request. To retrieve additional pages using a cursor, you must use the original query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/square/events/client.py">disable_events</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables events to prevent them from being searchable.
All events are disabled by default. You must enable events to make them searchable.
Disabling events for a specific time period prevents them from being searchable, even if you re-enable them later.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.events.disable_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/square/events/client.py">enable_events</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables events to make them searchable. Only events that occur while in the enabled state are searchable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.events.enable_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/square/events/client.py">list_event_types</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all event types that you can subscribe to as webhooks or query using the Events API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.events.list_event_types(
    api_version="api_version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — The API version for which to list event types. Setting this field overrides the default version used by the application.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GiftCards
<details><summary><code>client.gift_cards.<a href="src/square/gift_cards/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all gift cards. You can specify optional filters to retrieve 
a subset of the gift cards. Results are sorted by `created_at` in ascending order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.gift_cards.list(
    type="type",
    state="state",
    limit=1,
    cursor="cursor",
    customer_id="customer_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[str]` 

If a [type](entity:GiftCardType) is provided, the endpoint returns gift cards of the specified type.
Otherwise, the endpoint returns gift cards of all types.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` 

If a [state](entity:GiftCardStatus) is provided, the endpoint returns the gift cards in the specified state.
Otherwise, the endpoint returns the gift cards of all states.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

If a limit is provided, the endpoint returns only the specified number of results per page.
The maximum value is 200. The default value is 30.
For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
If a cursor is not provided, the endpoint returns the first page of the results. 
For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — If a customer ID is provided, the endpoint returns only the gift cards linked to the specified customer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/square/gift_cards/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a digital gift card or registers a physical (plastic) gift card. The resulting gift card
has a `PENDING` state. To activate a gift card so that it can be redeemed for purchases, call
[CreateGiftCardActivity](api-endpoint:GiftCardActivities-CreateGiftCardActivity) and create an `ACTIVATE`
activity with the initial balance. Alternatively, you can use [RefundPayment](api-endpoint:Refunds-RefundPayment)
to refund a payment to the new gift card.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.gift_cards.create(
    idempotency_key="NC9Tm69EjbjtConu",
    location_id="81FN9BNFZTKS4",
    gift_card={"type": "DIGITAL"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A unique identifier for this request, used to ensure idempotency. For more information, 
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` 

The ID of the [location](entity:Location) where the gift card should be registered for 
reporting purposes. Gift cards can be redeemed at any of the seller's locations.
    
</dd>
</dl>

<dl>
<dd>

**gift_card:** `GiftCardParams` 

The gift card to create. The `type` field is required for this request. The `gan_source` 
and `gan` fields are included as follows: 

To direct Square to generate a 16-digit GAN, omit `gan_source` and `gan`.

To provide a custom GAN, include `gan_source` and `gan`.
- For `gan_source`, specify `OTHER`. 
- For `gan`, provide a custom GAN containing 8 to 20 alphanumeric characters. The GAN must be 
unique for the seller and cannot start with the same bank identification number (BIN) as major 
credit cards. Do not use GANs that are easy to guess (such as 12345678) because they greatly 
increase the risk of fraud. It is the responsibility of the developer to ensure the security 
of their custom GANs. For more information, see 
[Custom GANs](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#custom-gans). 

To register an unused, physical gift card that the seller previously ordered from Square, 
include `gan` and provide the GAN that is printed on the gift card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/square/gift_cards/client.py">get_from_gan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a gift card using the gift card account number (GAN).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.gift_cards.get_from_gan(
    gan="7783320001001635",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gan:** `str` 

The gift card account number (GAN) of the gift card to retrieve.
The maximum length of a GAN is 255 digits to account for third-party GANs that have been imported.
Square-issued gift cards have 16-digit GANs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/square/gift_cards/client.py">get_from_nonce</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a gift card using a secure payment token that represents the gift card.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.gift_cards.get_from_nonce(
    nonce="cnon:7783322135245171",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**nonce:** `str` 

The payment token of the gift card to retrieve. Payment tokens are generated by the 
Web Payments SDK or In-App Payments SDK.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/square/gift_cards/client.py">link_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Links a customer to a gift card, which is also referred to as adding a card on file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.gift_cards.link_customer(
    gift_card_id="gift_card_id",
    customer_id="GKY0FZ3V717AH8Q2D821PNT2ZW",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gift_card_id:** `str` — The ID of the gift card to be linked.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to link to the gift card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/square/gift_cards/client.py">unlink_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unlinks a customer from a gift card, which is also referred to as removing a card on file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.gift_cards.unlink_customer(
    gift_card_id="gift_card_id",
    customer_id="GKY0FZ3V717AH8Q2D821PNT2ZW",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gift_card_id:** `str` — The ID of the gift card to be unlinked.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to unlink from the gift card.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.<a href="src/square/gift_cards/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a gift card using the gift card ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.gift_cards.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the gift card to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Inventory
<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">deprecated_get_adjustment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [RetrieveInventoryAdjustment](api-endpoint:Inventory-RetrieveInventoryAdjustment) after the endpoint URL
is updated to conform to the standard convention.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.inventory.deprecated_get_adjustment(
    adjustment_id="adjustment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**adjustment_id:** `str` — ID of the [InventoryAdjustment](entity:InventoryAdjustment) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">get_adjustment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the [InventoryAdjustment](entity:InventoryAdjustment) object
with the provided `adjustment_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.inventory.get_adjustment(
    adjustment_id="adjustment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**adjustment_id:** `str` — ID of the [InventoryAdjustment](entity:InventoryAdjustment) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">deprecated_batch_change</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [BatchChangeInventory](api-endpoint:Inventory-BatchChangeInventory) after the endpoint URL
is updated to conform to the standard convention.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.inventory.deprecated_batch_change(
    idempotency_key="8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe",
    changes=[
        {
            "type": "PHYSICAL_COUNT",
            "physical_count": {
                "reference_id": "1536bfbf-efed-48bf-b17d-a197141b2a92",
                "catalog_object_id": "W62UWFY35CWMYGVWK6TWJDNI",
                "state": "IN_STOCK",
                "location_id": "C6W5YS5QM06F5",
                "quantity": "53",
                "team_member_id": "LRK57NSQ5X7PUD05",
                "occurred_at": "2016-11-16T22:25:24.878Z",
            },
        }
    ],
    ignore_unchanged_counts=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A client-supplied, universally unique identifier (UUID) for the
request.

See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) in the
[API Development 101](https://developer.squareup.com/docs/buildbasics) section for more
information.
    
</dd>
</dl>

<dl>
<dd>

**changes:** `typing.Optional[typing.Sequence[InventoryChangeParams]]` 

The set of physical counts and inventory adjustments to be made.
Changes are applied based on the client-supplied timestamp and may be sent
out of order.
    
</dd>
</dl>

<dl>
<dd>

**ignore_unchanged_counts:** `typing.Optional[bool]` 

Indicates whether the current physical count should be ignored if
the quantity is unchanged since the last physical count. Default: `true`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">deprecated_batch_get_changes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [BatchRetrieveInventoryChanges](api-endpoint:Inventory-BatchRetrieveInventoryChanges) after the endpoint URL
is updated to conform to the standard convention.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.inventory.deprecated_batch_get_changes(
    catalog_object_ids=["W62UWFY35CWMYGVWK6TWJDNI"],
    location_ids=["C6W5YS5QM06F5"],
    types=["PHYSICAL_COUNT"],
    states=["IN_STOCK"],
    updated_after="2016-11-01T00:00:00.000Z",
    updated_before="2016-12-01T00:00:00.000Z",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `CatalogObject` ID.
The filter is only applicable when set. The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `Location` ID.
The filter is only applicable when set. The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Sequence[InventoryChangeType]]` 

The filter to return results by `InventoryChangeType` values other than `TRANSFER`.
The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Sequence[InventoryState]]` 

The filter to return `ADJUSTMENT` query results by
`InventoryState`. This filter is only applied when set.
The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` 

The filter to return results with their `calculated_at` value
after the given time as specified in an RFC 3339 timestamp.
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[str]` 

The filter to return results with their `created_at` or `calculated_at` value
strictly before the given time as specified in an RFC 3339 timestamp.
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of [records](entity:InventoryChange) to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">deprecated_batch_get_counts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [BatchRetrieveInventoryCounts](api-endpoint:Inventory-BatchRetrieveInventoryCounts) after the endpoint URL
is updated to conform to the standard convention.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.inventory.deprecated_batch_get_counts(
    catalog_object_ids=["W62UWFY35CWMYGVWK6TWJDNI"],
    location_ids=["59TNP9SA8VGDA"],
    updated_after="2016-11-16T00:00:00.000Z",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `CatalogObject` ID.
The filter is applicable only when set.  The default is null.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `Location` ID.
This filter is applicable only when set. The default is null.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` 

The filter to return results with their `calculated_at` value
after the given time as specified in an RFC 3339 timestamp.
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Sequence[InventoryState]]` 

The filter to return results by `InventoryState`. The filter is only applicable when set.
Ignored are untracked states of `NONE`, `SOLD`, and `UNLINKED_RETURN`.
The default is null.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of [records](entity:InventoryCount) to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">batch_create_changes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies adjustments and counts to the provided item quantities.

On success: returns the current calculated counts for all objects
referenced in the request.
On failure: returns a list of related errors.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.inventory.batch_create_changes(
    idempotency_key="8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe",
    changes=[
        {
            "type": "PHYSICAL_COUNT",
            "physical_count": {
                "reference_id": "1536bfbf-efed-48bf-b17d-a197141b2a92",
                "catalog_object_id": "W62UWFY35CWMYGVWK6TWJDNI",
                "state": "IN_STOCK",
                "location_id": "C6W5YS5QM06F5",
                "quantity": "53",
                "team_member_id": "LRK57NSQ5X7PUD05",
                "occurred_at": "2016-11-16T22:25:24.878Z",
            },
        }
    ],
    ignore_unchanged_counts=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A client-supplied, universally unique identifier (UUID) for the
request.

See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) in the
[API Development 101](https://developer.squareup.com/docs/buildbasics) section for more
information.
    
</dd>
</dl>

<dl>
<dd>

**changes:** `typing.Optional[typing.Sequence[InventoryChangeParams]]` 

The set of physical counts and inventory adjustments to be made.
Changes are applied based on the client-supplied timestamp and may be sent
out of order.
    
</dd>
</dl>

<dl>
<dd>

**ignore_unchanged_counts:** `typing.Optional[bool]` 

Indicates whether the current physical count should be ignored if
the quantity is unchanged since the last physical count. Default: `true`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">batch_get_changes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns historical physical counts and adjustments based on the
provided filter criteria.

Results are paginated and sorted in ascending order according their
`occurred_at` timestamp (oldest first).

BatchRetrieveInventoryChanges is a catch-all query endpoint for queries
that cannot be handled by other, simpler endpoints.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.inventory.batch_get_changes(
    catalog_object_ids=["W62UWFY35CWMYGVWK6TWJDNI"],
    location_ids=["C6W5YS5QM06F5"],
    types=["PHYSICAL_COUNT"],
    states=["IN_STOCK"],
    updated_after="2016-11-01T00:00:00.000Z",
    updated_before="2016-12-01T00:00:00.000Z",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `CatalogObject` ID.
The filter is only applicable when set. The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `Location` ID.
The filter is only applicable when set. The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Sequence[InventoryChangeType]]` 

The filter to return results by `InventoryChangeType` values other than `TRANSFER`.
The default value is `[PHYSICAL_COUNT, ADJUSTMENT]`.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Sequence[InventoryState]]` 

The filter to return `ADJUSTMENT` query results by
`InventoryState`. This filter is only applied when set.
The default value is null.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` 

The filter to return results with their `calculated_at` value
after the given time as specified in an RFC 3339 timestamp.
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[str]` 

The filter to return results with their `created_at` or `calculated_at` value
strictly before the given time as specified in an RFC 3339 timestamp.
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of [records](entity:InventoryChange) to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">batch_get_counts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns current counts for the provided
[CatalogObject](entity:CatalogObject)s at the requested
[Location](entity:Location)s.

Results are paginated and sorted in descending order according to their
`calculated_at` timestamp (newest first).

When `updated_after` is specified, only counts that have changed since that
time (based on the server timestamp for the most recent change) are
returned. This allows clients to perform a "sync" operation, for example
in response to receiving a Webhook notification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.inventory.batch_get_counts(
    catalog_object_ids=["W62UWFY35CWMYGVWK6TWJDNI"],
    location_ids=["59TNP9SA8VGDA"],
    updated_after="2016-11-16T00:00:00.000Z",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `CatalogObject` ID.
The filter is applicable only when set.  The default is null.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The filter to return results by `Location` ID.
This filter is applicable only when set. The default is null.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` 

The filter to return results with their `calculated_at` value
after the given time as specified in an RFC 3339 timestamp.
The default value is the UNIX epoch of (`1970-01-01T00:00:00Z`).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Sequence[InventoryState]]` 

The filter to return results by `InventoryState`. The filter is only applicable when set.
Ignored are untracked states of `NONE`, `SOLD`, and `UNLINKED_RETURN`.
The default is null.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of [records](entity:InventoryCount) to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">deprecated_get_physical_count</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated version of [RetrieveInventoryPhysicalCount](api-endpoint:Inventory-RetrieveInventoryPhysicalCount) after the endpoint URL
is updated to conform to the standard convention.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.inventory.deprecated_get_physical_count(
    physical_count_id="physical_count_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**physical_count_id:** `str` 

ID of the
[InventoryPhysicalCount](entity:InventoryPhysicalCount) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">get_physical_count</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the [InventoryPhysicalCount](entity:InventoryPhysicalCount)
object with the provided `physical_count_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.inventory.get_physical_count(
    physical_count_id="physical_count_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**physical_count_id:** `str` 

ID of the
[InventoryPhysicalCount](entity:InventoryPhysicalCount) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">get_transfer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the [InventoryTransfer](entity:InventoryTransfer) object
with the provided `transfer_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.inventory.get_transfer(
    transfer_id="transfer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_id:** `str` — ID of the [InventoryTransfer](entity:InventoryTransfer) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the current calculated stock count for a given
[CatalogObject](entity:CatalogObject) at a given set of
[Location](entity:Location)s. Responses are paginated and unsorted.
For more sophisticated queries, use a batch endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.inventory.get(
    catalog_object_id="catalog_object_id",
    location_ids="location_ids",
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_id:** `str` — ID of the [CatalogObject](entity:CatalogObject) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[str]` 

The [Location](entity:Location) IDs to look up as a comma-separated
list. An empty list queries all locations.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inventory.<a href="src/square/inventory/client.py">changes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a set of physical counts and inventory adjustments for the
provided [CatalogObject](entity:CatalogObject) at the requested
[Location](entity:Location)s.

You can achieve the same result by calling [BatchRetrieveInventoryChanges](api-endpoint:Inventory-BatchRetrieveInventoryChanges)
and having the `catalog_object_ids` list contain a single element of the `CatalogObject` ID.

Results are paginated and sorted in descending order according to their
`occurred_at` timestamp (newest first).

There are no limits on how far back the caller can page. This endpoint can be
used to display recent changes for a specific item. For more
sophisticated queries, use a batch endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.inventory.changes(
    catalog_object_id="catalog_object_id",
    location_ids="location_ids",
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**catalog_object_id:** `str` — ID of the [CatalogObject](entity:CatalogObject) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**location_ids:** `typing.Optional[str]` 

The [Location](entity:Location) IDs to look up as a comma-separated
list. An empty list queries all locations.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoices
<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of invoices for a given location. The response 
is paginated. If truncated, the response includes a `cursor` that you    
use in a subsequent request to retrieve the next set of invoices.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.invoices.list(
    location_id="location_id",
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location for which to list invoices.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint. 
Provide this cursor to retrieve the next set of results for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of invoices to return (200 is the maximum `limit`). 
If not provided, the server uses a default limit of 100 invoices.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a draft [invoice](entity:Invoice) 
for an order created using the Orders API.

A draft invoice remains in your account and no action is taken. 
You must publish the invoice before Square can process it (send it to the customer's email address or charge the customer’s card on file).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.invoices.create(
    invoice={
        "location_id": "ES0RJRZYEC39A",
        "order_id": "CAISENgvlJ6jLWAzERDzjyHVybY",
        "primary_recipient": {"customer_id": "JDKYHBWT1D4F8MFH63DBMEN8Y4"},
        "payment_requests": [
            {
                "request_type": "BALANCE",
                "due_date": "2030-01-24",
                "tipping_enabled": True,
                "automatic_payment_source": "NONE",
                "reminders": [
                    {
                        "relative_scheduled_days": -1,
                        "message": "Your invoice is due tomorrow",
                    }
                ],
            }
        ],
        "delivery_method": "EMAIL",
        "invoice_number": "inv-100",
        "title": "Event Planning Services",
        "description": "We appreciate your business!",
        "scheduled_at": "2030-01-13T10:00:00Z",
        "accepted_payment_methods": {
            "card": True,
            "square_gift_card": False,
            "bank_account": False,
            "buy_now_pay_later": False,
            "cash_app_pay": False,
        },
        "custom_fields": [
            {
                "label": "Event Reference Number",
                "value": "Ref. #1234",
                "placement": "ABOVE_LINE_ITEMS",
            },
            {
                "label": "Terms of Service",
                "value": "The terms of service are...",
                "placement": "BELOW_LINE_ITEMS",
            },
        ],
        "sale_or_service_date": "2030-01-24",
        "store_payment_method_enabled": False,
    },
    idempotency_key="ce3748f9-5fc1-4762-aa12-aae5e843f1f4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice:** `InvoiceParams` — The invoice to create.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies the `CreateInvoice` request. If you do not 
provide `idempotency_key` (or provide an empty string as the value), the endpoint 
treats each request as independent.

For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for invoices from a location specified in 
the filter. You can optionally specify customers in the filter for whom to 
retrieve invoices. In the current implementation, you can only specify one location and 
optionally one customer.

The response is paginated. If truncated, the response includes a `cursor` 
that you use in a subsequent request to retrieve the next set of invoices.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.invoices.search(
    query={
        "filter": {
            "location_ids": ["ES0RJRZYEC39A"],
            "customer_ids": ["JDKYHBWT1D4F8MFH63DBMEN8Y4"],
        },
        "sort": {"field": "INVOICE_SORT_DATE", "order": "DESC"},
    },
    limit=100,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `InvoiceQueryParams` — Describes the query criteria for searching invoices.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of invoices to return (200 is the maximum `limit`). 
If not provided, the server uses a default limit of 100 invoices.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint. 
Provide this cursor to retrieve the next set of results for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an invoice by invoice ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.invoices.get(
    invoice_id="invoice_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the invoice to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an invoice. This endpoint supports sparse updates, so you only need
to specify the fields you want to change along with the required `version` field.
Some restrictions apply to updating invoices. For example, you cannot change the
`order_id` or `location_id` field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.invoices.update(
    invoice_id="invoice_id",
    invoice={
        "version": 1,
        "payment_requests": [
            {
                "uid": "2da7964f-f3d2-4f43-81e8-5aa220bf3355",
                "tipping_enabled": False,
            }
        ],
    },
    idempotency_key="4ee82288-0910-499e-ab4c-5d0071dad1be",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the invoice to update.
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `InvoiceParams` 

The invoice fields to add, change, or clear. Fields can be cleared using
null values or the `remove` field (for individual payment requests or reminders).
The current invoice `version` is also required. For more information, including requirements,
limitations, and more examples, see [Update an Invoice](https://developer.squareup.com/docs/invoices-api/update-invoices).
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies the `UpdateInvoice` request. If you do not
provide `idempotency_key` (or provide an empty string as the value), the endpoint
treats each request as independent.

For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**fields_to_clear:** `typing.Optional[typing.Sequence[str]]` 

The list of fields to clear. Although this field is currently supported, we
recommend using null values or the `remove` field when possible. For examples, see
[Update an Invoice](https://developer.squareup.com/docs/invoices-api/update-invoices).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified invoice. When an invoice is deleted, the 
associated order status changes to CANCELED. You can only delete a draft 
invoice (you cannot delete a published invoice, including one that is scheduled for processing).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.invoices.delete(
    invoice_id="invoice_id",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the invoice to delete.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The version of the [invoice](entity:Invoice) to delete.
If you do not know the version, you can call [GetInvoice](api-endpoint:Invoices-GetInvoice) or 
[ListInvoices](api-endpoint:Invoices-ListInvoices).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">create_invoice_attachment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a file and attaches it to an invoice. This endpoint accepts HTTP multipart/form-data file uploads
with a JSON `request` part and a `file` part. The `file` part must be a `readable stream` that contains a file
in a supported format: GIF, JPEG, PNG, TIFF, BMP, or PDF.

Invoices can have up to 10 attachments with a total file size of 25 MB. Attachments can be added only to invoices
in the `DRAFT`, `SCHEDULED`, `UNPAID`, or `PARTIALLY_PAID` state.

__NOTE:__ When testing in the Sandbox environment, the total file size is limited to 1 KB.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.invoices.create_invoice_attachment(
    invoice_id="invoice_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the [invoice](entity:Invoice) to attach the file to.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[CreateInvoiceAttachmentRequestDataParams]` 
    
</dd>
</dl>

<dl>
<dd>

**image_file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">delete_invoice_attachment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes an attachment from an invoice and permanently deletes the file. Attachments can be removed only
from invoices in the `DRAFT`, `SCHEDULED`, `UNPAID`, or `PARTIALLY_PAID` state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.invoices.delete_invoice_attachment(
    invoice_id="invoice_id",
    attachment_id="attachment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the [invoice](entity:Invoice) to delete the attachment from.
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `str` — The ID of the [attachment](entity:InvoiceAttachment) to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels an invoice. The seller cannot collect payments for 
the canceled invoice.

You cannot cancel an invoice in the `DRAFT` state or in a terminal state: `PAID`, `REFUNDED`, `CANCELED`, or `FAILED`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.invoices.cancel(
    invoice_id="invoice_id",
    version=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the [invoice](entity:Invoice) to cancel.
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` 

The version of the [invoice](entity:Invoice) to cancel.
If you do not know the version, you can call 
[GetInvoice](api-endpoint:Invoices-GetInvoice) or [ListInvoices](api-endpoint:Invoices-ListInvoices).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/square/invoices/client.py">publish</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publishes the specified draft invoice. 

After an invoice is published, Square 
follows up based on the invoice configuration. For example, Square 
sends the invoice to the customer's email address, charges the customer's card on file, or does 
nothing. Square also makes the invoice available on a Square-hosted invoice page. 

The invoice `status` also changes from `DRAFT` to a status 
based on the invoice configuration. For example, the status changes to `UNPAID` if 
Square emails the invoice or `PARTIALLY_PAID` if Square charges a card on file for a portion of the 
invoice amount.

In addition to the required `ORDERS_WRITE` and `INVOICES_WRITE` permissions, `CUSTOMERS_READ`
and `PAYMENTS_WRITE` are required when publishing invoices configured for card-on-file payments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.invoices.publish(
    invoice_id="invoice_id",
    version=1,
    idempotency_key="32da42d0-1997-41b0-826b-f09464fc2c2e",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — The ID of the invoice to publish.
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` 

The version of the [invoice](entity:Invoice) to publish.
This must match the current version of the invoice; otherwise, the request is rejected.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies the `PublishInvoice` request. If you do not 
provide `idempotency_key` (or provide an empty string as the value), the endpoint 
treats each request as independent.

For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Labor
<details><summary><code>client.labor.<a href="src/square/labor/client.py">create_scheduled_shift</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a scheduled shift by providing draft shift details such as job ID,
team member assignment, and start and end times.

The following `draft_shift_details` fields are required:
- `location_id`
- `job_id`
- `start_at`
- `end_at`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.create_scheduled_shift(
    idempotency_key="HIDSNG5KS478L",
    scheduled_shift={
        "draft_shift_details": {
            "team_member_id": "ormj0jJJZ5OZIzxrZYJI",
            "location_id": "PAA1RJZZKXBFG",
            "job_id": "FzbJAtt9qEWncK1BWgVCxQ6M",
            "start_at": "2019-01-25T03:11:00-05:00",
            "end_at": "2019-01-25T13:11:00-05:00",
            "notes": "Dont forget to prep the vegetables",
            "is_deleted": False,
        }
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scheduled_shift:** `ScheduledShiftParams` 

The scheduled shift with `draft_shift_details`.
If needed, call [ListLocations](api-endpoint:Locations-ListLocations) to get location IDs,
[ListJobs](api-endpoint:Team-ListJobs) to get job IDs, and [SearchTeamMembers](api-endpoint:Team-SearchTeamMembers)
to get team member IDs and current job assignments.

The `start_at` and `end_at` timestamps must be provided in the time zone + offset of the
shift location specified in `location_id`. Example for Pacific Standard Time: 2024-10-31T12:30:00-08:00
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for the `CreateScheduledShift` request, used to ensure the
[idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency)
of the operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">bulk_publish_scheduled_shifts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publishes 1 - 100 scheduled shifts. This endpoint takes a map of individual publish
requests and returns a map of responses. When a scheduled shift is published, Square keeps
the `draft_shift_details` field as is and copies it to the `published_shift_details` field.

The minimum `start_at` and maximum `end_at` timestamps of all shifts in a
`BulkPublishScheduledShifts` request must fall within a two-week period.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.bulk_publish_scheduled_shifts(
    scheduled_shifts={"key": {}},
    scheduled_shift_notification_audience="AFFECTED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scheduled_shifts:** `typing.Dict[str, BulkPublishScheduledShiftsDataParams]` 

A map of 1 to 100 key-value pairs that represent individual publish requests.

- Each key is the ID of a scheduled shift you want to publish.
- Each value is a `BulkPublishScheduledShiftsData` object that contains the
`version` field or is an empty object.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_shift_notification_audience:** `typing.Optional[ScheduledShiftNotificationAudience]` 

Indicates whether Square should send email notifications to team members and
which team members should receive the notifications. This setting applies to all shifts
specified in the bulk operation. The default value is `AFFECTED`.
See [ScheduledShiftNotificationAudience](#type-scheduledshiftnotificationaudience) for possible values
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">search_scheduled_shifts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of scheduled shifts, with optional filter and sort settings.
By default, results are sorted by `start_at` in ascending order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.search_scheduled_shifts(
    query={
        "filter": {"assignment_status": "ASSIGNED"},
        "sort": {"field": "CREATED_AT", "order": "ASC"},
    },
    limit=2,
    cursor="xoxp-1234-5678-90123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[ScheduledShiftQueryParams]` — Query conditions used to filter and sort the results.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return in a single response page. The default value is 50.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The pagination cursor returned by the previous call to this endpoint. Provide
this cursor to retrieve the next page of results for your original request. For more
information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">retrieve_scheduled_shift</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a scheduled shift by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.retrieve_scheduled_shift(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the scheduled shift to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">update_scheduled_shift</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the draft shift details for a scheduled shift. This endpoint supports
sparse updates, so only new, changed, or removed fields are required in the request.
You must publish the shift to make updates public.

You can make the following updates to `draft_shift_details`:
- Change the `location_id`, `job_id`, `start_at`, and `end_at` fields.
- Add, change, or clear the `team_member_id` and `notes` fields. To clear these fields,
set the value to null.
- Change the `is_deleted` field. To delete a scheduled shift, set `is_deleted` to true
and then publish the shift.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.update_scheduled_shift(
    id="id",
    scheduled_shift={
        "draft_shift_details": {
            "team_member_id": "ormj0jJJZ5OZIzxrZYJI",
            "location_id": "PAA1RJZZKXBFG",
            "job_id": "FzbJAtt9qEWncK1BWgVCxQ6M",
            "start_at": "2019-03-25T03:11:00-05:00",
            "end_at": "2019-03-25T13:18:00-05:00",
            "notes": "Dont forget to prep the vegetables",
            "is_deleted": False,
        },
        "version": 1,
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the scheduled shift to update.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_shift:** `ScheduledShiftParams` 

The scheduled shift with any updates in the `draft_shift_details` field.
If needed, call [ListLocations](api-endpoint:Locations-ListLocations) to get location IDs,
[ListJobs](api-endpoint:Team-ListJobs) to get job IDs, and [SearchTeamMembers](api-endpoint:Team-SearchTeamMembers)
to get team member IDs and current job assignments. Updates made to `published_shift_details`
are ignored.

If provided, the `start_at` and `end_at` timestamps must be in the time zone + offset of the
shift location specified in `location_id`. Example for Pacific Standard Time: 2024-10-31T12:30:00-08:00

To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control for the request, provide the current version of the shift in the `version` field.
If the provided version doesn't match the server version, the request fails. If `version` is
omitted, Square executes a blind write, potentially overwriting data from another publish request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">publish_scheduled_shift</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publishes a scheduled shift. When a scheduled shift is published, Square keeps the
`draft_shift_details` field as is and copies it to the `published_shift_details` field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.publish_scheduled_shift(
    id="id",
    idempotency_key="HIDSNG5KS478L",
    version=2,
    scheduled_shift_notification_audience="ALL",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the scheduled shift to publish.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique identifier for the `PublishScheduledShift` request, used to ensure the
[idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency)
of the operation.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the scheduled shift, used to enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control. If the provided version doesn't match the server version, the request fails.
If omitted, Square executes a blind write, potentially overwriting data from another publish request.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_shift_notification_audience:** `typing.Optional[ScheduledShiftNotificationAudience]` 

Indicates whether Square should send an email notification to team members and
which team members should receive the notification. The default value is `AFFECTED`.
See [ScheduledShiftNotificationAudience](#type-scheduledshiftnotificationaudience) for possible values
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">create_timecard</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new `Timecard`.

A `Timecard` represents a complete workday for a single team member.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `team_member_id`
- `start_at`

An attempt to create a new `Timecard` can result in a `BAD_REQUEST` error when:
- The `status` of the new `Timecard` is `OPEN` and the team member has another
timecard with an `OPEN` status.
- The `start_at` date is in the future.
- The `start_at` or `end_at` date overlaps another timecard for the same team member.
- The `Break` instances are set in the request and a break `start_at`
is before the `Timecard.start_at`, a break `end_at` is after
the `Timecard.end_at`, or both.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.create_timecard(
    idempotency_key="HIDSNG5KS478L",
    timecard={
        "location_id": "PAA1RJZZKXBFG",
        "start_at": "2019-01-25T03:11:00-05:00",
        "end_at": "2019-01-25T13:11:00-05:00",
        "wage": {
            "title": "Barista",
            "hourly_rate": {"amount": 1100, "currency": "USD"},
            "tip_eligible": True,
        },
        "breaks": [
            {
                "start_at": "2019-01-25T06:11:00-05:00",
                "end_at": "2019-01-25T06:16:00-05:00",
                "break_type_id": "REGS1EQR1TPZ5",
                "name": "Tea Break",
                "expected_duration": "PT5M",
                "is_paid": True,
            }
        ],
        "team_member_id": "ormj0jJJZ5OZIzxrZYJI",
        "declared_cash_tip_money": {"amount": 500, "currency": "USD"},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**timecard:** `TimecardParams` — The `Timecard` to be created.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique string value to ensure the idempotency of the operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">search_timecards</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `Timecard` records for a business.
The list to be returned can be filtered by:
- Location IDs
- Team member IDs
- Timecard status (`OPEN` or `CLOSED`)
- Timecard start
- Timecard end
- Workday details

The list can be sorted by:
- `START_AT`
- `END_AT`
- `CREATED_AT`
- `UPDATED_AT`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.search_timecards(
    query={
        "filter": {
            "workday": {
                "date_range": {
                    "start_date": "2019-01-20",
                    "end_date": "2019-02-03",
                },
                "match_timecards_by": "START_AT",
                "default_timezone": "America/Los_Angeles",
            }
        }
    },
    limit=100,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[TimecardQueryParams]` — Query filters.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of resources in a page (200 by default).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — An opaque cursor for fetching the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">retrieve_timecard</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single `Timecard` specified by `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.retrieve_timecard(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID for the `Timecard` being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">update_timecard</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing `Timecard`.

When adding a `Break` to a `Timecard`, any earlier `Break` instances in the `Timecard` have
the `end_at` property set to a valid RFC-3339 datetime string.

When closing a `Timecard`, all `Break` instances in the `Timecard` must be complete with `end_at`
set on each `Break`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.update_timecard(
    id="id",
    timecard={
        "location_id": "PAA1RJZZKXBFG",
        "start_at": "2019-01-25T03:11:00-05:00",
        "end_at": "2019-01-25T13:11:00-05:00",
        "wage": {
            "title": "Bartender",
            "hourly_rate": {"amount": 1500, "currency": "USD"},
            "tip_eligible": True,
        },
        "breaks": [
            {
                "id": "X7GAQYVVRRG6P",
                "start_at": "2019-01-25T06:11:00-05:00",
                "end_at": "2019-01-25T06:16:00-05:00",
                "break_type_id": "REGS1EQR1TPZ5",
                "name": "Tea Break",
                "expected_duration": "PT5M",
                "is_paid": True,
            }
        ],
        "status": "CLOSED",
        "version": 1,
        "team_member_id": "ormj0jJJZ5OZIzxrZYJI",
        "declared_cash_tip_money": {"amount": 500, "currency": "USD"},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the object being updated.
    
</dd>
</dl>

<dl>
<dd>

**timecard:** `TimecardParams` — The updated `Timecard` object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.<a href="src/square/labor/client.py">delete_timecard</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a `Timecard`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.delete_timecard(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID for the `Timecard` being deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Locations
<details><summary><code>client.locations.<a href="src/square/locations/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides details about all of the seller's [locations](https://developer.squareup.com/docs/locations-api),
including those with an inactive status. Locations are listed alphabetically by `name`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.<a href="src/square/locations/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a [location](https://developer.squareup.com/docs/locations-api).
Creating new locations allows for separate configuration of receipt layouts, item prices,
and sales reports. Developers can use locations to separate sales activity through applications
that integrate with Square from sales activity elsewhere in a seller's account.
Locations created programmatically with the Locations API last forever and
are visible to the seller for their own management. Therefore, ensure that
each location has a sensible and unique name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.create(
    location={
        "name": "Midtown",
        "address": {
            "address_line1": "1234 Peachtree St. NE",
            "locality": "Atlanta",
            "administrative_district_level1": "GA",
            "postal_code": "30309",
        },
        "description": "Midtown Atlanta store",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location:** `typing.Optional[LocationParams]` 

The initial values of the location being created. The `name` field is required and must be unique within a seller account.
All other fields are optional, but any information you care about for the location should be included.
The remaining fields are automatically added based on the data from the [main location](https://developer.squareup.com/docs/locations-api#about-the-main-location).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.<a href="src/square/locations/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details of a single location. Specify "main"
as the location ID to retrieve details of the [main location](https://developer.squareup.com/docs/locations-api#about-the-main-location).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.get(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` 

The ID of the location to retrieve. Specify the string
"main" to return the main location.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.<a href="src/square/locations/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a [location](https://developer.squareup.com/docs/locations-api).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.update(
    location_id="location_id",
    location={
        "business_hours": {
            "periods": [
                {
                    "day_of_week": "FRI",
                    "start_local_time": "07:00",
                    "end_local_time": "18:00",
                },
                {
                    "day_of_week": "SAT",
                    "start_local_time": "07:00",
                    "end_local_time": "18:00",
                },
                {
                    "day_of_week": "SUN",
                    "start_local_time": "09:00",
                    "end_local_time": "15:00",
                },
            ]
        },
        "description": "Midtown Atlanta store - Open weekends",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to update.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[LocationParams]` — The `Location` object with only the fields to update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.<a href="src/square/locations/client.py">checkouts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Links a `checkoutId` to a `checkout_page_url` that customers are
directed to in order to provide their payment information using a
payment processing workflow hosted on connect.squareup.com. 


NOTE: The Checkout API has been updated with new features. 
For more information, see [Checkout API highlights](https://developer.squareup.com/docs/checkout-api#checkout-api-highlights).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.checkouts(
    location_id="location_id",
    idempotency_key="86ae1696-b1e3-4328-af6d-f1e04d947ad6",
    order={
        "order": {
            "location_id": "location_id",
            "reference_id": "reference_id",
            "customer_id": "customer_id",
            "line_items": [
                {
                    "name": "Printed T Shirt",
                    "quantity": "2",
                    "applied_taxes": [
                        {"tax_uid": "38ze1696-z1e3-5628-af6d-f1e04d947fg3"}
                    ],
                    "applied_discounts": [
                        {"discount_uid": "56ae1696-z1e3-9328-af6d-f1e04d947gd4"}
                    ],
                    "base_price_money": {"amount": 1500, "currency": "USD"},
                },
                {
                    "name": "Slim Jeans",
                    "quantity": "1",
                    "base_price_money": {"amount": 2500, "currency": "USD"},
                },
                {
                    "name": "Woven Sweater",
                    "quantity": "3",
                    "base_price_money": {"amount": 3500, "currency": "USD"},
                },
            ],
            "taxes": [
                {
                    "uid": "38ze1696-z1e3-5628-af6d-f1e04d947fg3",
                    "type": "INCLUSIVE",
                    "percentage": "7.75",
                    "scope": "LINE_ITEM",
                }
            ],
            "discounts": [
                {
                    "uid": "56ae1696-z1e3-9328-af6d-f1e04d947gd4",
                    "type": "FIXED_AMOUNT",
                    "amount_money": {"amount": 100, "currency": "USD"},
                    "scope": "LINE_ITEM",
                }
            ],
        },
        "idempotency_key": "12ae1696-z1e3-4328-af6d-f1e04d947gd4",
    },
    ask_for_shipping_address=True,
    merchant_support_email="merchant+support@website.com",
    pre_populate_buyer_email="example@email.com",
    pre_populate_shipping_address={
        "address_line1": "1455 Market St.",
        "address_line2": "Suite 600",
        "locality": "San Francisco",
        "administrative_district_level1": "CA",
        "postal_code": "94103",
        "country": "US",
        "first_name": "Jane",
        "last_name": "Doe",
    },
    redirect_url="https://merchant.website.com/order-confirm",
    additional_recipients=[
        {
            "location_id": "057P5VYJ4A5X1",
            "description": "Application fees",
            "amount_money": {"amount": 60, "currency": "USD"},
        }
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the business location to associate the checkout with.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this checkout among others you have created. It can be
any valid string but must be unique for every order sent to Square Checkout for a given location ID.

The idempotency key is used to avoid processing the same order more than once. If you are 
unsure whether a particular checkout was created successfully, you can attempt it again with
the same idempotency key and all the same other parameters without worrying about creating duplicates.

You should use a random number/string generator native to the language
you are working in to generate strings for your idempotency keys.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**order:** `CreateOrderRequestParams` — The order including line items to be checked out.
    
</dd>
</dl>

<dl>
<dd>

**ask_for_shipping_address:** `typing.Optional[bool]` 

If `true`, Square Checkout collects shipping information on your behalf and stores 
that information with the transaction information in the Square Seller Dashboard.

Default: `false`.
    
</dd>
</dl>

<dl>
<dd>

**merchant_support_email:** `typing.Optional[str]` 

The email address to display on the Square Checkout confirmation page
and confirmation email that the buyer can use to contact the seller.

If this value is not set, the confirmation page and email display the
primary email address associated with the seller's Square account.

Default: none; only exists if explicitly set.
    
</dd>
</dl>

<dl>
<dd>

**pre_populate_buyer_email:** `typing.Optional[str]` 

If provided, the buyer's email is prepopulated on the checkout page
as an editable text field.

Default: none; only exists if explicitly set.
    
</dd>
</dl>

<dl>
<dd>

**pre_populate_shipping_address:** `typing.Optional[AddressParams]` 

If provided, the buyer's shipping information is prepopulated on the
checkout page as editable text fields.

Default: none; only exists if explicitly set.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` 

The URL to redirect to after the checkout is completed with `checkoutId`,
`transactionId`, and `referenceId` appended as URL parameters. For example,
if the provided redirect URL is `http://www.example.com/order-complete`, a
successful transaction redirects the customer to:

`http://www.example.com/order-complete?checkoutId=xxxxxx&amp;referenceId=xxxxxx&amp;transactionId=xxxxxx`

If you do not provide a redirect URL, Square Checkout displays an order
confirmation page on your behalf; however, it is strongly recommended that
you provide a redirect URL so you can verify the transaction results and
finalize the order through your existing/normal confirmation workflow.

Default: none; only exists if explicitly set.
    
</dd>
</dl>

<dl>
<dd>

**additional_recipients:** `typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipientParams]]` 

The basic primitive of a multi-party transaction. The value is optional.
The transaction facilitated by you can be split from here.

If you provide this value, the `amount_money` value in your `additional_recipients` field
cannot be more than 90% of the `total_money` calculated by Square for your order.
The `location_id` must be a valid seller location where the checkout is occurring.

This field requires `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.

This field is currently not supported in the Square Sandbox.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` 

An optional note to associate with the `checkout` object.

This value cannot exceed 60 characters.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Loyalty
<details><summary><code>client.loyalty.<a href="src/square/loyalty/client.py">search_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for loyalty events.

A Square loyalty program maintains a ledger of events that occur during the lifetime of a
buyer's loyalty account. Each change in the point balance
(for example, points earned, points redeemed, and points expired) is
recorded in the ledger. Using this endpoint, you can search the ledger for events.

Search results are sorted by `created_at` in descending order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.loyalty.search_events(
    query={
        "filter": {
            "order_filter": {"order_id": "PyATxhYLfsMqpVkcKJITPydgEYfZY"}
        }
    },
    limit=30,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[LoyaltyEventQueryParams]` 

A set of one or more predefined query filters to apply when 
searching for loyalty events. The endpoint performs a logical AND to 
evaluate multiple filters and performs a logical OR on arrays  
that specifies multiple field values.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to include in the response. 
The last page might contain fewer events. 
The default is 30 events.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants
<details><summary><code>client.merchants.<a href="src/square/merchants/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides details about the merchant associated with a given access token.

The access token used to connect your application to a Square seller is associated
with a single merchant. That means that `ListMerchants` returns a list
with a single `Merchant` object. You can specify your personal access token
to get your own merchant information or specify an OAuth token to get the
information for the merchant that granted your application access.

If you know the merchant ID, you can also use the [RetrieveMerchant](api-endpoint:Merchants-RetrieveMerchant)
endpoint to retrieve the merchant information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.merchants.list(
    cursor=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[int]` — The cursor generated by the previous response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.<a href="src/square/merchants/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the `Merchant` object for the given `merchant_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.get(
    merchant_id="merchant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` 

The ID of the merchant to retrieve. If the string "me" is supplied as the ID,
then retrieve the merchant that is currently accessible to this call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Checkout
<details><summary><code>client.checkout.<a href="src/square/checkout/client.py">retrieve_location_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the location-level settings for a Square-hosted checkout page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.checkout.retrieve_location_settings(
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location for which to retrieve settings.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.checkout.<a href="src/square/checkout/client.py">update_location_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the location-level settings for a Square-hosted checkout page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.checkout.update_location_settings(
    location_id="location_id",
    location_settings={},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location for which to retrieve settings.
    
</dd>
</dl>

<dl>
<dd>

**location_settings:** `CheckoutLocationSettingsParams` — Describe your updates using the `location_settings` object. Make sure it contains only the fields that have changed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.checkout.<a href="src/square/checkout/client.py">retrieve_merchant_settings</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the merchant-level settings for a Square-hosted checkout page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.checkout.retrieve_merchant_settings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.checkout.<a href="src/square/checkout/client.py">update_merchant_settings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the merchant-level settings for a Square-hosted checkout page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.checkout.update_merchant_settings(
    merchant_settings={},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_settings:** `CheckoutMerchantSettingsParams` — Describe your updates using the `merchant_settings` object. Make sure it contains only the fields that have changed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Orders
<details><summary><code>client.orders.<a href="src/square/orders/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new [order](entity:Order) that can include information about products for
purchase and settings to apply to the purchase.

To pay for a created order, see
[Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

You can modify open orders using the [UpdateOrder](api-endpoint:Orders-UpdateOrder) endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.create(
    order={
        "location_id": "057P5VYJ4A5X1",
        "reference_id": "my-order-001",
        "line_items": [
            {
                "name": "New York Strip Steak",
                "quantity": "1",
                "base_price_money": {"amount": 1599, "currency": "USD"},
            },
            {
                "quantity": "2",
                "catalog_object_id": "BEMYCSMIJL46OCDV4KYIKXIB",
                "modifiers": [
                    {"catalog_object_id": "CHQX7Y4KY6N5KINJKZCFURPZ"}
                ],
                "applied_discounts": [{"discount_uid": "one-dollar-off"}],
            },
        ],
        "taxes": [
            {
                "uid": "state-sales-tax",
                "name": "State Sales Tax",
                "percentage": "9",
                "scope": "ORDER",
            }
        ],
        "discounts": [
            {
                "uid": "labor-day-sale",
                "name": "Labor Day Sale",
                "percentage": "5",
                "scope": "ORDER",
            },
            {
                "uid": "membership-discount",
                "catalog_object_id": "DB7L55ZH2BGWI4H23ULIWOQ7",
                "scope": "ORDER",
            },
            {
                "uid": "one-dollar-off",
                "name": "Sale - $1.00 off",
                "amount_money": {"amount": 100, "currency": "USD"},
                "scope": "LINE_ITEM",
            },
        ],
    },
    idempotency_key="8193148c-9586-11e6-99f9-28cfe92138cf",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderParams]` 

The order to create. If this field is set, the only other top-level field that can be
set is the `idempotency_key`.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A value you specify that uniquely identifies this
order among orders you have created.

If you are unsure whether a particular order was created successfully,
you can try it again with the same idempotency key without
worrying about creating duplicate orders.

For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/square/orders/client.py">batch_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a set of [orders](entity:Order) by their IDs.

If a given order ID does not exist, the ID is ignored instead of generating an error.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.batch_get(
    location_id="057P5VYJ4A5X1",
    order_ids=["CAISEM82RcpmcFBM0TfOyiHV3es", "CAISENgvlJ6jLWAzERDzjyHVybY"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_ids:** `typing.Sequence[str]` — The IDs of the orders to retrieve. A maximum of 100 orders can be retrieved per request.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

The ID of the location for these orders. This field is optional: omit it to retrieve
orders within the scope of the current authorization's merchant ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/square/orders/client.py">calculate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables applications to preview order pricing without creating an order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.calculate(
    order={
        "location_id": "D7AVYMEAPJ3A3",
        "line_items": [
            {
                "name": "Item 1",
                "quantity": "1",
                "base_price_money": {"amount": 500, "currency": "USD"},
            },
            {
                "name": "Item 2",
                "quantity": "2",
                "base_price_money": {"amount": 300, "currency": "USD"},
            },
        ],
        "discounts": [
            {"name": "50% Off", "percentage": "50", "scope": "ORDER"}
        ],
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `OrderParams` — The order to be calculated. Expects the entire order, not a sparse update.
    
</dd>
</dl>

<dl>
<dd>

**proposed_rewards:** `typing.Optional[typing.Sequence[OrderRewardParams]]` 

Identifies one or more loyalty reward tiers to apply during the order calculation.
The discounts defined by the reward tiers are added to the order only to preview the
effect of applying the specified rewards. The rewards do not correspond to actual
redemptions; that is, no `reward`s are created. Therefore, the reward `id`s are
random strings used only to reference the reward tier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/square/orders/client.py">clone</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new order, in the `DRAFT` state, by duplicating an existing order. The newly created order has
only the core fields (such as line items, taxes, and discounts) copied from the original order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.clone(
    order_id="ZAISEM52YcpmcWAzERDOyiWS123",
    version=3,
    idempotency_key="UNIQUE_STRING",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the order to clone.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

An optional order version for concurrency protection.

If a version is provided, it must match the latest stored version of the order to clone.
If a version is not provided, the API clones the latest version.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A value you specify that uniquely identifies this clone request.

If you are unsure whether a particular order was cloned successfully,
you can reattempt the call with the same idempotency key without
worrying about creating duplicate cloned orders.
The originally cloned order is returned.

For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/square/orders/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search all orders for one or more locations. Orders include all sales,
returns, and exchanges regardless of how or when they entered the Square
ecosystem (such as Point of Sale, Invoices, and Connect APIs).

`SearchOrders` requests need to specify which locations to search and define a
[SearchOrdersQuery](entity:SearchOrdersQuery) object that controls
how to sort or filter the results. Your `SearchOrdersQuery` can:

  Set filter criteria.
  Set the sort order.
  Determine whether to return results as complete `Order` objects or as
[OrderEntry](entity:OrderEntry) objects.

Note that details for orders processed with Square Point of Sale while in
offline mode might not be transmitted to Square for up to 72 hours. Offline
orders have a `created_at` value that reflects the time the order was created,
not the time it was subsequently transmitted to Square.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.orders.search(
    location_ids=["057P5VYJ4A5X1", "18YC4JDH91E1H"],
    query={
        "filter": {
            "state_filter": {"states": ["COMPLETED"]},
            "date_time_filter": {
                "closed_at": {
                    "start_at": "2018-03-03T20:00:00+00:00",
                    "end_at": "2019-03-04T21:54:45+00:00",
                }
            },
        },
        "sort": {"sort_field": "CLOSED_AT", "sort_order": "DESC"},
    },
    limit=3,
    return_entries=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_ids:** `typing.Optional[typing.Sequence[str]]` 

The location IDs for the orders to query. All locations must belong to
the same merchant.

Max: 10 location IDs.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for your original query.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[SearchOrdersQueryParams]` 

Query conditions used to filter or sort the results. Note that when
retrieving additional pages using a cursor, you must use the original query.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to be returned in a single page.

Default: `500`
Max: `1000`
    
</dd>
</dl>

<dl>
<dd>

**return_entries:** `typing.Optional[bool]` 

A Boolean that controls the format of the search results. If `true`,
`SearchOrders` returns [OrderEntry](entity:OrderEntry) objects. If `false`, `SearchOrders`
returns complete order objects.

Default: `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/square/orders/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an [Order](entity:Order) by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.get(
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the order to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/square/orders/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an open [order](entity:Order) by adding, replacing, or deleting
fields. Orders with a `COMPLETED` or `CANCELED` state cannot be updated.

An `UpdateOrder` request requires the following:

- The `order_id` in the endpoint path, identifying the order to update.
- The latest `version` of the order to update.
- The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#sparse-order-objects)
containing only the fields to update and the version to which the update is
being applied.
- If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#identifying-fields-to-delete)
identifying the fields to clear.

To pay for an order, see
[Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.update(
    order_id="order_id",
    order={
        "location_id": "location_id",
        "line_items": [
            {
                "uid": "cookie_uid",
                "name": "COOKIE",
                "quantity": "2",
                "base_price_money": {"amount": 200, "currency": "USD"},
            }
        ],
        "version": 1,
    },
    fields_to_clear=["discounts"],
    idempotency_key="UNIQUE_STRING",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the order to update.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderParams]` 

The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#sparse-order-objects)
containing only the fields to update and the version to which the update is
being applied.
    
</dd>
</dl>

<dl>
<dd>

**fields_to_clear:** `typing.Optional[typing.Sequence[str]]` 

The [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#identifying-fields-to-delete)
fields to clear. For example, `line_items[uid].note`.
For more information, see [Deleting fields](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#deleting-fields).
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A value you specify that uniquely identifies this update request.

If you are unsure whether a particular update was applied to an order successfully,
you can reattempt it with the same idempotency key without
worrying about creating duplicate updates to the order.
The latest order version is returned.

For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/square/orders/client.py">pay</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pay for an [order](entity:Order) using one or more approved [payments](entity:Payment)
or settle an order with a total of `0`.

The total of the `payment_ids` listed in the request must be equal to the order
total. Orders with a total amount of `0` can be marked as paid by specifying an empty
array of `payment_ids` in the request.

To be used with `PayOrder`, a payment must:

- Reference the order by specifying the `order_id` when [creating the payment](api-endpoint:Payments-CreatePayment).
Any approved payments that reference the same `order_id` not specified in the
`payment_ids` is canceled.
- Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture).
Using a delayed capture payment with `PayOrder` completes the approved payment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.pay(
    order_id="order_id",
    idempotency_key="c043a359-7ad9-4136-82a9-c3f1d66dcbff",
    payment_ids=["EnZdNAlWCmfh6Mt5FMNST1o7taB", "0LRiVlbXVwe8ozu4KbZxd12mvaB"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the order being paid.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A value you specify that uniquely identifies this request among requests you have sent. If
you are unsure whether a particular payment request was completed successfully, you can reattempt
it with the same idempotency key without worrying about duplicate payments.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**order_version:** `typing.Optional[int]` — The version of the order being paid. If not supplied, the latest version will be paid.
    
</dd>
</dl>

<dl>
<dd>

**payment_ids:** `typing.Optional[typing.Sequence[str]]` 

The IDs of the [payments](entity:Payment) to collect.
The payment total must match the order total.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payments
<details><summary><code>client.payments.<a href="src/square/payments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of payments taken by the account making the request.

Results are eventually consistent, and new payments or changes to payments might take several
seconds to appear.

The maximum results per page is 100.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.payments.list(
    begin_time="begin_time",
    end_time="end_time",
    sort_order="sort_order",
    cursor="cursor",
    location_id="location_id",
    total=1000000,
    last4="last_4",
    card_brand="card_brand",
    limit=1,
    is_offline_payment=True,
    offline_begin_time="offline_begin_time",
    offline_end_time="offline_end_time",
    updated_at_begin_time="updated_at_begin_time",
    updated_at_end_time="updated_at_end_time",
    sort_field="CREATED_AT",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

Indicates the start of the time range to retrieve payments for, in RFC 3339 format.
The range is determined using the `created_at` field for each Payment.
Inclusive. Default: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

Indicates the end of the time range to retrieve payments for, in RFC 3339 format.  The
range is determined using the `created_at` field for each Payment.

Default: The current time.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

The order in which results are listed by `ListPaymentsRequest.sort_field`:
- `ASC` - Oldest to newest.
- `DESC` - Newest to oldest (default).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

Limit results to the location supplied. By default, results are returned
for the default (main) location associated with the seller.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[int]` — The exact amount in the `total_money` for a payment.
    
</dd>
</dl>

<dl>
<dd>

**last4:** `typing.Optional[str]` — The last four digits of a payment card.
    
</dd>
</dl>

<dl>
<dd>

**card_brand:** `typing.Optional[str]` — The brand of the payment card (for example, VISA).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to be returned in a single page.
It is possible to receive fewer results than the specified limit on a given page.

The default value of 100 is also the maximum allowed value. If the provided value is 
greater than 100, it is ignored and the default value is used instead.

Default: `100`
    
</dd>
</dl>

<dl>
<dd>

**is_offline_payment:** `typing.Optional[bool]` — Whether the payment was taken offline or not.
    
</dd>
</dl>

<dl>
<dd>

**offline_begin_time:** `typing.Optional[str]` 

Indicates the start of the time range for which to retrieve offline payments, in RFC 3339
format for timestamps. The range is determined using the
`offline_payment_details.client_created_at` field for each Payment. If set, payments without a
value set in `offline_payment_details.client_created_at` will not be returned.

Default: The current time.
    
</dd>
</dl>

<dl>
<dd>

**offline_end_time:** `typing.Optional[str]` 

Indicates the end of the time range for which to retrieve offline payments, in RFC 3339
format for timestamps. The range is determined using the
`offline_payment_details.client_created_at` field for each Payment. If set, payments without a
value set in `offline_payment_details.client_created_at` will not be returned.

Default: The current time.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_begin_time:** `typing.Optional[str]` 

Indicates the start of the time range to retrieve payments for, in RFC 3339 format.  The
range is determined using the `updated_at` field for each Payment.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_end_time:** `typing.Optional[str]` 

Indicates the end of the time range to retrieve payments for, in RFC 3339 format.  The
range is determined using the `updated_at` field for each Payment.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListPaymentsRequestSortField]` — The field used to sort results by. The default is `CREATED_AT`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/square/payments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a payment using the provided source. You can use this endpoint 
to charge a card (credit/debit card or    
Square gift card) or record a payment that the seller received outside of Square 
(cash payment from a buyer or a payment that an external entity 
processed on behalf of the seller).

The endpoint creates a 
`Payment` object and returns it in the response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.payments.create(
    source_id="ccof:GaJGNaZa8x4OgDJn4GB",
    idempotency_key="7b0f3ec5-086a-4871-8f13-3c81b3875218",
    amount_money={"amount": 1000, "currency": "USD"},
    app_fee_money={"amount": 10, "currency": "USD"},
    autocomplete=True,
    customer_id="W92WH6P11H4Z77CTET0RNTGFW8",
    location_id="L88917AVBK2S5",
    reference_id="123456",
    note="Brief description",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 

The ID for the source of funds for this payment.
This could be a payment token generated by the Web Payments SDK for any of its
[supported methods](https://developer.squareup.com/docs/web-payments/overview#explore-payment-methods),
including cards, bank transfers, Afterpay or Cash App Pay. If recording a payment
that the seller received outside of Square, specify either "CASH" or "EXTERNAL".
For more information, see
[Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `CreatePayment` request. Keys can be any valid string
but must be unique for every `CreatePayment` request.

Note: The number of allowed characters might be less than the stated maximum, if multi-byte
characters are used.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**amount_money:** `typing.Optional[MoneyParams]` 

The amount of money to accept for this payment, not including `tip_money`.

The amount must be specified in the smallest denomination of the applicable currency
(for example, US dollar amounts are specified in cents). For more information, see
[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts).

The currency code must match the currency associated with the business
that is accepting the payment.
    
</dd>
</dl>

<dl>
<dd>

**tip_money:** `typing.Optional[MoneyParams]` 

The amount designated as a tip, in addition to `amount_money`.

The amount must be specified in the smallest denomination of the applicable currency
(for example, US dollar amounts are specified in cents). For more information, see
[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts).

The currency code must match the currency associated with the business
that is accepting the payment.
    
</dd>
</dl>

<dl>
<dd>

**app_fee_money:** `typing.Optional[MoneyParams]` 

The amount of money that the developer is taking as a fee
for facilitating the payment on behalf of the seller.

The amount cannot be more than 90% of the total amount of the payment.

The amount must be specified in the smallest denomination of the applicable currency
(for example, US dollar amounts are specified in cents). For more information, see
[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts).

The fee currency code must match the currency associated with the seller
that is accepting the payment. The application must be from a developer
account in the same country and using the same currency code as the seller.

For more information about the application fee scenario, see
[Take Payments and Collect Fees](https://developer.squareup.com/docs/payments-api/take-payments-and-collect-fees).

To set this field, `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission is required.
For more information, see [Permissions](https://developer.squareup.com/docs/payments-api/take-payments-and-collect-fees#permissions).
    
</dd>
</dl>

<dl>
<dd>

**delay_duration:** `typing.Optional[str]` 

The duration of time after the payment's creation when Square automatically
either completes or cancels the payment depending on the `delay_action` field value.
For more information, see
[Time threshold](https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture#time-threshold).

This parameter should be specified as a time duration, in RFC 3339 format.

Note: This feature is only supported for card payments. This parameter can only be set for a delayed
capture payment (`autocomplete=false`).

Default:

- Card-present payments: "PT36H" (36 hours) from the creation time.
- Card-not-present payments: "P7D" (7 days) from the creation time.
    
</dd>
</dl>

<dl>
<dd>

**delay_action:** `typing.Optional[str]` 

The action to be applied to the payment when the `delay_duration` has elapsed. The action must be
CANCEL or COMPLETE. For more information, see
[Time Threshold](https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture#time-threshold).

Default: CANCEL
    
</dd>
</dl>

<dl>
<dd>

**autocomplete:** `typing.Optional[bool]` 

If set to `true`, this payment will be completed when possible. If
set to `false`, this payment is held in an approved state until either
explicitly completed (captured) or canceled (voided). For more information, see
[Delayed capture](https://developer.squareup.com/docs/payments-api/take-payments/card-payments#delayed-capture-of-a-card-payment).

Default: true
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `typing.Optional[str]` — Associates a previously created order with this payment.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 

The [Customer](entity:Customer) ID of the customer associated with the payment.

This is required if the `source_id` refers to a card on file created using the Cards API.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

The location ID to associate with the payment. If not specified, the [main location](https://developer.squareup.com/docs/locations-api#about-the-main-location) is
used.
    
</dd>
</dl>

<dl>
<dd>

**team_member_id:** `typing.Optional[str]` 

An optional [TeamMember](entity:TeamMember) ID to associate with
this payment.
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` 

A user-defined ID to associate with the payment.

You can use this field to associate the payment to an entity in an external system
(for example, you might specify an order ID that is generated by a third-party shopping cart).
    
</dd>
</dl>

<dl>
<dd>

**verification_token:** `typing.Optional[str]` 

An identifying token generated by [payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
Verification tokens encapsulate customer device information and 3-D Secure
challenge results to indicate that Square has verified the buyer identity.

For more information, see [SCA Overview](https://developer.squareup.com/docs/sca-overview).
    
</dd>
</dl>

<dl>
<dd>

**accept_partial_authorization:** `typing.Optional[bool]` 

If set to `true` and charging a Square Gift Card, a payment might be returned with
`amount_money` equal to less than what was requested. For example, a request for $20 when charging
a Square Gift Card with a balance of $5 results in an APPROVED payment of $5. You might choose
to prompt the buyer for an additional payment to cover the remainder or cancel the Gift Card
payment. This field cannot be `true` when `autocomplete = true`.

For more information, see
[Partial amount with Square Gift Cards](https://developer.squareup.com/docs/payments-api/take-payments#partial-payment-gift-card).

Default: false
    
</dd>
</dl>

<dl>
<dd>

**buyer_email_address:** `typing.Optional[str]` — The buyer's email address.
    
</dd>
</dl>

<dl>
<dd>

**buyer_phone_number:** `typing.Optional[str]` 

The buyer's phone number.
Must follow the following format:
1. A leading + symbol (followed by a country code)
2. The phone number can contain spaces and the special characters `(` , `)` , `-` , and `.`.
Alphabetical characters aren't allowed.
3. The phone number must contain between 9 and 16 digits.
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[AddressParams]` — The buyer's billing address.
    
</dd>
</dl>

<dl>
<dd>

**shipping_address:** `typing.Optional[AddressParams]` — The buyer's shipping address.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — An optional note to be entered by the developer when creating a payment.
    
</dd>
</dl>

<dl>
<dd>

**statement_description_identifier:** `typing.Optional[str]` 

Optional additional payment information to include on the customer's card statement
as part of the statement description. This can be, for example, an invoice number, ticket number,
or short description that uniquely identifies the purchase.

Note that the `statement_description_identifier` might get truncated on the statement description
to fit the required information including the Square identifier (SQ *) and name of the
seller taking the payment.
    
</dd>
</dl>

<dl>
<dd>

**cash_details:** `typing.Optional[CashPaymentDetailsParams]` — Additional details required when recording a cash payment (`source_id` is CASH).
    
</dd>
</dl>

<dl>
<dd>

**external_details:** `typing.Optional[ExternalPaymentDetailsParams]` — Additional details required when recording an external payment (`source_id` is EXTERNAL).
    
</dd>
</dl>

<dl>
<dd>

**customer_details:** `typing.Optional[CustomerDetailsParams]` — Details about the customer making the payment.
    
</dd>
</dl>

<dl>
<dd>

**offline_payment_details:** `typing.Optional[OfflinePaymentDetailsParams]` 

An optional field for specifying the offline payment details. This is intended for
internal 1st-party callers only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/square/payments/client.py">cancel_by_idempotency_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels (voids) a payment identified by the idempotency key that is specified in the
request.

Use this method when the status of a `CreatePayment` request is unknown (for example, after you send a
`CreatePayment` request, a network error occurs and you do not get a response). In this case, you can
direct Square to cancel the payment using this endpoint. In the request, you provide the same
idempotency key that you provided in your `CreatePayment` request that you want to cancel. After
canceling the payment, you can submit your `CreatePayment` request again.

Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint
returns successfully.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.payments.cancel_by_idempotency_key(
    idempotency_key="a7e36d40-d24b-11e8-b568-0800200c9a66",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` — The `idempotency_key` identifying the payment to be canceled.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/square/payments/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details for a specific payment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.payments.get(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — A unique ID for the desired payment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/square/payments/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a payment with the APPROVED status.
You can update the `amount_money` and `tip_money` using this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.payments.update(
    payment_id="payment_id",
    payment={
        "amount_money": {"amount": 1000, "currency": "USD"},
        "tip_money": {"amount": 100, "currency": "USD"},
        "version_token": "ODhwVQ35xwlzRuoZEwKXucfu7583sPTzK48c5zoGd0g6o",
    },
    idempotency_key="956f8b13-e4ec-45d6-85e8-d1d95ef0c5de",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — The ID of the payment to update.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `UpdatePayment` request. Keys can be any valid string
but must be unique for every `UpdatePayment` request.

For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**payment:** `typing.Optional[PaymentParams]` — The updated `Payment` object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/square/payments/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels (voids) a payment. You can use this endpoint to cancel a payment with 
the APPROVED `status`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.payments.cancel(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — The ID of the payment to cancel.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/square/payments/client.py">complete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Completes (captures) a payment.
By default, payments are set to complete immediately after they are created.

You can use this endpoint to complete a payment with the APPROVED `status`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.payments.complete(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` — The unique ID identifying the payment to be completed.
    
</dd>
</dl>

<dl>
<dd>

**version_token:** `typing.Optional[str]` 

Used for optimistic concurrency. This opaque token identifies the current `Payment`
version that the caller expects. If the server has a different version of the Payment,
the update fails and a response with a VERSION_MISMATCH error is returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payouts
<details><summary><code>client.payouts.<a href="src/square/payouts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all payouts for the default location.
You can filter payouts by location ID, status, time range, and order them in ascending or descending order.
To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.payouts.list(
    location_id="location_id",
    status="SENT",
    begin_time="begin_time",
    end_time="end_time",
    sort_order="DESC",
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

The ID of the location for which to list the payouts.
By default, payouts are returned for the default (main) location associated with the seller.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PayoutStatus]` — If provided, only payouts with the given status are returned.
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

The timestamp for the beginning of the payout creation time, in RFC 3339 format.
Inclusive. Default: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

The timestamp for the end of the payout creation time, in RFC 3339 format.
Default: The current time.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SortOrder]` — The order in which payouts are listed.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
If request parameters change between requests, subsequent results may contain duplicates or missing records.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to be returned in a single page.
It is possible to receive fewer results than the specified limit on a given page.
The default value of 100 is also the maximum allowed value. If the provided value is
greater than 100, it is ignored and the default value is used instead.
Default: `100`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payouts.<a href="src/square/payouts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details of a specific payout identified by a payout ID.
To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.payouts.get(
    payout_id="payout_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payout_id:** `str` — The ID of the payout to retrieve the information for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payouts.<a href="src/square/payouts/client.py">list_entries</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all payout entries for a specific payout.
To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.payouts.list_entries(
    payout_id="payout_id",
    sort_order="DESC",
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payout_id:** `str` — The ID of the payout to retrieve the information for.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SortOrder]` — The order in which payout entries are listed.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
If request parameters change between requests, subsequent results may contain duplicates or missing records.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to be returned in a single page.
It is possible to receive fewer results than the specified limit on a given page.
The default value of 100 is also the maximum allowed value. If the provided value is
greater than 100, it is ignored and the default value is used instead.
Default: `100`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Refunds
<details><summary><code>client.refunds.<a href="src/square/refunds/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of refunds for the account making the request.

Results are eventually consistent, and new refunds or changes to refunds might take several
seconds to appear.

The maximum results per page is 100.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.refunds.list(
    begin_time="begin_time",
    end_time="end_time",
    sort_order="sort_order",
    cursor="cursor",
    location_id="location_id",
    status="status",
    source_type="source_type",
    limit=1,
    updated_at_begin_time="updated_at_begin_time",
    updated_at_end_time="updated_at_end_time",
    sort_field="CREATED_AT",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

Indicates the start of the time range to retrieve each `PaymentRefund` for, in RFC 3339 
format.  The range is determined using the `created_at` field for each `PaymentRefund`. 

Default: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

Indicates the end of the time range to retrieve each `PaymentRefund` for, in RFC 3339 
format.  The range is determined using the `created_at` field for each `PaymentRefund`.

Default: The current time.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

The order in which results are listed by `PaymentRefund.created_at`:
- `ASC` - Oldest to newest.
- `DESC` - Newest to oldest (default).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

Limit results to the location supplied. By default, results are returned
for all locations associated with the seller.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 

If provided, only refunds with the given status are returned.
For a list of refund status values, see [PaymentRefund](entity:PaymentRefund).

Default: If omitted, refunds are returned regardless of their status.
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[str]` 

If provided, only returns refunds whose payments have the indicated source type.
Current values include `CARD`, `BANK_ACCOUNT`, `WALLET`, `CASH`, and `EXTERNAL`.
For information about these payment source types, see
[Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).

Default: If omitted, refunds are returned regardless of the source type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to be returned in a single page.

It is possible to receive fewer results than the specified limit on a given page.

If the supplied value is greater than 100, no more than 100 results are returned.

Default: 100
    
</dd>
</dl>

<dl>
<dd>

**updated_at_begin_time:** `typing.Optional[str]` 

Indicates the start of the time range to retrieve each `PaymentRefund` for, in RFC 3339
format.  The range is determined using the `updated_at` field for each `PaymentRefund`.

Default: If omitted, the time range starts at `begin_time`.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_end_time:** `typing.Optional[str]` 

Indicates the end of the time range to retrieve each `PaymentRefund` for, in RFC 3339
format.  The range is determined using the `updated_at` field for each `PaymentRefund`.

Default: The current time.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListPaymentRefundsRequestSortField]` — The field used to sort results by. The default is `CREATED_AT`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.refunds.<a href="src/square/refunds/client.py">refund_payment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refunds a payment. You can refund the entire payment amount or a
portion of it. You can use this endpoint to refund a card payment or record a 
refund of a cash or external payment. For more information, see
[Refund Payment](https://developer.squareup.com/docs/payments-api/refund-payments).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.refunds.refund_payment(
    idempotency_key="9b7f2dcf-49da-4411-b23e-a2d6af21333a",
    amount_money={"amount": 1000, "currency": "USD"},
    app_fee_money={"amount": 10, "currency": "USD"},
    payment_id="R2B3Z8WMVt3EAmzYWLZvz7Y69EbZY",
    reason="Example",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

 A unique string that identifies this `RefundPayment` request. The key can be any valid string
but must be unique for every `RefundPayment` request.

Keys are limited to a max of 45 characters - however, the number of allowed characters might be
less than 45, if multi-byte characters are used.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**amount_money:** `MoneyParams` 

The amount of money to refund.

This amount cannot be more than the `total_money` value of the payment minus the total
amount of all previously completed refunds for this payment.

This amount must be specified in the smallest denomination of the applicable currency
(for example, US dollar amounts are specified in cents). For more information, see
[Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts).

The currency code must match the currency associated with the business
that is charging the card.
    
</dd>
</dl>

<dl>
<dd>

**app_fee_money:** `typing.Optional[MoneyParams]` 

The amount of money the developer contributes to help cover the refunded amount.
This amount is specified in the smallest denomination of the applicable currency (for example,
US dollar amounts are specified in cents).

The value cannot be more than the `amount_money`.

You can specify this parameter in a refund request only if the same parameter was also included
when taking the payment. This is part of the application fee scenario the API supports. For more
information, see [Take Payments and Collect Fees](https://developer.squareup.com/docs/payments-api/take-payments-and-collect-fees).

To set this field, `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission is required.
For more information, see [Permissions](https://developer.squareup.com/docs/payments-api/take-payments-and-collect-fees#permissions).
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `typing.Optional[str]` 

The unique ID of the payment being refunded.
Required when unlinked=false, otherwise must not be set.
    
</dd>
</dl>

<dl>
<dd>

**destination_id:** `typing.Optional[str]` 

The ID indicating where funds will be refunded to. Required for unlinked refunds. For more
information, see [Process an Unlinked Refund](https://developer.squareup.com/docs/refunds-api/unlinked-refunds).

For refunds linked to Square payments, `destination_id` is usually omitted; in this case, funds
will be returned to the original payment source. The field may be specified in order to request
a cross-method refund to a gift card. For more information,
see [Cross-method refunds to gift cards](https://developer.squareup.com/docs/payments-api/refund-payments#cross-method-refunds-to-gift-cards).
    
</dd>
</dl>

<dl>
<dd>

**unlinked:** `typing.Optional[bool]` 

Indicates that the refund is not linked to a Square payment.
If set to true, `destination_id` and `location_id` must be supplied while `payment_id` must not
be provided.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

The location ID associated with the unlinked refund.
Required for requests specifying `unlinked=true`.
Otherwise, if included when `unlinked=false`, will throw an error.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 

The [Customer](entity:Customer) ID of the customer associated with the refund.
This is required if the `destination_id` refers to a card on file created using the Cards
API. Only allowed when `unlinked=true`.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — A description of the reason for the refund.
    
</dd>
</dl>

<dl>
<dd>

**payment_version_token:** `typing.Optional[str]` 

 Used for optimistic concurrency. This opaque token identifies the current `Payment`
version that the caller expects. If the server has a different version of the Payment,
the update fails and a response with a VERSION_MISMATCH error is returned.
If the versions match, or the field is not provided, the refund proceeds as normal.
    
</dd>
</dl>

<dl>
<dd>

**team_member_id:** `typing.Optional[str]` — An optional [TeamMember](entity:TeamMember) ID to associate with this refund.
    
</dd>
</dl>

<dl>
<dd>

**cash_details:** `typing.Optional[DestinationDetailsCashRefundDetailsParams]` — Additional details required when recording an unlinked cash refund (`destination_id` is CASH).
    
</dd>
</dl>

<dl>
<dd>

**external_details:** `typing.Optional[DestinationDetailsExternalRefundDetailsParams]` 

Additional details required when recording an unlinked external refund
(`destination_id` is EXTERNAL).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.refunds.<a href="src/square/refunds/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific refund using the `refund_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.refunds.get(
    refund_id="refund_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**refund_id:** `str` — The unique ID for the desired `PaymentRefund`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sites
<details><summary><code>client.sites.<a href="src/square/sites/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the Square Online sites that belong to a seller. Sites are listed in descending order by the `created_at` date.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.sites.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Snippets
<details><summary><code>client.snippets.<a href="src/square/snippets/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.snippets.get(
    site_id="site_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — The ID of the site that contains the snippet.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snippets.<a href="src/square/snippets/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a snippet to a Square Online site or updates the existing snippet on the site. 
The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site. 

You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.snippets.upsert(
    site_id="site_id",
    snippet={"content": "<script>var js = 1;</script>"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — The ID of the site where you want to add or update the snippet.
    
</dd>
</dl>

<dl>
<dd>

**snippet:** `SnippetParams` — The snippet for the site.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snippets.<a href="src/square/snippets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes your snippet from a Square Online site.

You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.snippets.delete(
    site_id="site_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**site_id:** `str` — The ID of the site that contains the snippet.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscriptions
<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enrolls a customer in a subscription.

If you provide a card on file in the request, Square charges the card for
the subscription. Otherwise, Square sends an invoice to the customer's email
address. The subscription starts immediately, unless the request includes
the optional `start_date`. Each individual subscription is associated with a particular location.

For more information, see [Create a subscription](https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions#create-a-subscription).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.create(
    idempotency_key="8193148c-9586-11e6-99f9-28cfe92138cf",
    location_id="S8GWD5R9QB376",
    plan_variation_id="6JHXF3B2CW3YKHDV4XEM674H",
    customer_id="CHFGVKYY8RSV93M5KCYTG4PN0G",
    start_date="2023-06-20",
    card_id="ccof:qy5x8hHGYsgLrp4Q4GB",
    timezone="America/Los_Angeles",
    source={"name": "My Application"},
    phases=[
        {"ordinal": 0, "order_template_id": "U2NaowWxzXwpsZU697x7ZHOAnCNZY"}
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location the subscription is associated with.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The ID of the [customer](entity:Customer) subscribing to the subscription plan variation.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies this `CreateSubscription` request.
If you do not provide a unique string (or provide an empty string as the value),
the endpoint treats each request as independent.

For more information, see [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**plan_variation_id:** `typing.Optional[str]` — The ID of the [subscription plan variation](https://developer.squareup.com/docs/subscriptions-api/plans-and-variations#plan-variations) created using the Catalog API.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` 

The `YYYY-MM-DD`-formatted date to start the subscription. 
If it is unspecified, the subscription starts immediately.
    
</dd>
</dl>

<dl>
<dd>

**canceled_date:** `typing.Optional[str]` 

The `YYYY-MM-DD`-formatted date when the newly created subscription is scheduled for cancellation. 

This date overrides the cancellation date set in the plan variation configuration.
If the cancellation date is earlier than the end date of a subscription cycle, the subscription stops
at the canceled date and the subscriber is sent a prorated invoice at the beginning of the canceled cycle. 

When the subscription plan of the newly created subscription has a fixed number of cycles and the `canceled_date`
occurs before the subscription plan completes, the specified `canceled_date` sets the date when the subscription
stops through the end of the last cycle.
    
</dd>
</dl>

<dl>
<dd>

**tax_percentage:** `typing.Optional[str]` 

The tax to add when billing the subscription.
The percentage is expressed in decimal form, using a `'.'` as the decimal
separator and without a `'%'` sign. For example, a value of 7.5
corresponds to 7.5%.
    
</dd>
</dl>

<dl>
<dd>

**price_override_money:** `typing.Optional[MoneyParams]` 

A custom price which overrides the cost of a subscription plan variation with `STATIC` pricing.
This field does not affect itemized subscriptions with `RELATIVE` pricing. Instead, 
you should edit the Subscription's [order template](https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions#phases-and-order-templates).
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `typing.Optional[str]` 

The ID of the [subscriber's](entity:Customer) [card](entity:Card) to charge.
If it is not specified, the subscriber receives an invoice via email with a link to pay for their subscription.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` 

The timezone that is used in date calculations for the subscription. If unset, defaults to
the location timezone. If a timezone is not configured for the location, defaults to "America/New_York".
Format: the IANA Timezone Database identifier for the location timezone. For
a list of time zones, see [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[SubscriptionSourceParams]` — The origination details of the subscription.
    
</dd>
</dl>

<dl>
<dd>

**monthly_billing_anchor_date:** `typing.Optional[int]` — The day-of-the-month to change the billing date to.
    
</dd>
</dl>

<dl>
<dd>

**phases:** `typing.Optional[typing.Sequence[PhaseParams]]` — array of phases for this subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">bulk_swap_plan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedules a plan variation change for all active subscriptions under a given plan
variation. For more information, see [Swap Subscription Plan Variations](https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.bulk_swap_plan(
    new_plan_variation_id="FQ7CDXXWSLUJRPM3GFJSJGZ7",
    old_plan_variation_id="6JHXF3B2CW3YKHDV4XEM674H",
    location_id="S8GWD5R9QB376",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**new_plan_variation_id:** `str` 

The ID of the new subscription plan variation.

This field is required.
    
</dd>
</dl>

<dl>
<dd>

**old_plan_variation_id:** `str` 

The ID of the plan variation whose subscriptions should be swapped. Active subscriptions
using this plan variation will be subscribed to the new plan variation on their next billing
day.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The ID of the location to associate with the swapped subscriptions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for subscriptions.

Results are ordered chronologically by subscription creation date. If
the request specifies more than one location ID,
the endpoint orders the result
by location ID, and then by creation date within each location. If no locations are given
in the query, all locations are searched.

You can also optionally specify `customer_ids` to search by customer.
If left unset, all customers
associated with the specified locations are returned.
If the request specifies customer IDs, the endpoint orders results
first by location, within location by customer ID, and within
customer by subscription creation date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.subscriptions.search(
    query={
        "filter": {
            "customer_ids": ["CHFGVKYY8RSV93M5KCYTG4PN0G"],
            "location_ids": ["S8GWD5R9QB376"],
            "source_names": ["My App"],
        }
    },
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

When the total number of resulting subscriptions exceeds the limit of a paged response, 
specify the cursor returned from a preceding response here to fetch the next set of results.
If the cursor is unset, the response contains the last page of the results.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The upper limit on the number of subscriptions to return
in a paged response.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[SearchSubscriptionsQueryParams]` 

A subscription query consisting of specified filtering conditions.

If this `query` field is unspecified, the `SearchSubscriptions` call will return all subscriptions.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Sequence[str]]` 

An option to include related information in the response. 

The supported values are: 

- `actions`: to include scheduled actions on the targeted subscriptions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.get(
    subscription_id="subscription_id",
    include="include",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` 

A query parameter to specify related information to be included in the response. 

The supported query parameter values are: 

- `actions`: to include scheduled actions on the targeted subscription.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a subscription by modifying or clearing `subscription` field values.
To clear a field, set its value to `null`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.update(
    subscription_id="subscription_id",
    subscription={"card_id": "{NEW CARD ID}"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to update.
    
</dd>
</dl>

<dl>
<dd>

**subscription:** `typing.Optional[SubscriptionParams]` 

The subscription object containing the current version, and fields to update.
Unset fields will be left at their current server values, and JSON `null` values will
be treated as a request to clear the relevant data.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">delete_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a scheduled action for a subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.delete_action(
    subscription_id="subscription_id",
    action_id="action_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription the targeted action is to act upon.
    
</dd>
</dl>

<dl>
<dd>

**action_id:** `str` — The ID of the targeted action to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">change_billing_anchor_date</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Changes the [billing anchor date](https://developer.squareup.com/docs/subscriptions-api/subscription-billing#billing-dates)
for a subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.change_billing_anchor_date(
    subscription_id="subscription_id",
    monthly_billing_anchor_date=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to update the billing anchor date.
    
</dd>
</dl>

<dl>
<dd>

**monthly_billing_anchor_date:** `typing.Optional[int]` — The anchor day for the billing cycle.
    
</dd>
</dl>

<dl>
<dd>

**effective_date:** `typing.Optional[str]` 

The `YYYY-MM-DD`-formatted date when the scheduled `BILLING_ANCHOR_CHANGE` action takes
place on the subscription.

When this date is unspecified or falls within the current billing cycle, the billing anchor date
is changed immediately.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedules a `CANCEL` action to cancel an active subscription. This 
sets the `canceled_date` field to the end of the active billing period. After this date, 
the subscription status changes from ACTIVE to CANCELED.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.cancel(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to cancel.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">list_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all [events](https://developer.squareup.com/docs/subscriptions-api/actions-events) for a specific subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.subscriptions.list_events(
    subscription_id="subscription_id",
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to retrieve the events for.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

When the total number of resulting subscription events exceeds the limit of a paged response, 
specify the cursor returned from a preceding response here to fetch the next set of results.
If the cursor is unset, the response contains the last page of the results.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The upper limit on the number of subscription events to return
in a paged response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">pause</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedules a `PAUSE` action to pause an active subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.pause(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to pause.
    
</dd>
</dl>

<dl>
<dd>

**pause_effective_date:** `typing.Optional[str]` 

The `YYYY-MM-DD`-formatted date when the scheduled `PAUSE` action takes place on the subscription.

When this date is unspecified or falls within the current billing cycle, the subscription is paused
on the starting date of the next billing cycle.
    
</dd>
</dl>

<dl>
<dd>

**pause_cycle_duration:** `typing.Optional[int]` 

The number of billing cycles the subscription will be paused before it is reactivated. 

When this is set, a `RESUME` action is also scheduled to take place on the subscription at 
the end of the specified pause cycle duration. In this case, neither `resume_effective_date` 
nor `resume_change_timing` may be specified.
    
</dd>
</dl>

<dl>
<dd>

**resume_effective_date:** `typing.Optional[str]` 

The date when the subscription is reactivated by a scheduled `RESUME` action. 
This date must be at least one billing cycle ahead of `pause_effective_date`.
    
</dd>
</dl>

<dl>
<dd>

**resume_change_timing:** `typing.Optional[ChangeTiming]` 

The timing whether the subscription is reactivated immediately or at the end of the billing cycle, relative to 
`resume_effective_date`.
See [ChangeTiming](#type-changetiming) for possible values
    
</dd>
</dl>

<dl>
<dd>

**pause_reason:** `typing.Optional[str]` — The user-provided reason to pause the subscription.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">resume</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedules a `RESUME` action to resume a paused or a deactivated subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.resume(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to resume.
    
</dd>
</dl>

<dl>
<dd>

**resume_effective_date:** `typing.Optional[str]` — The `YYYY-MM-DD`-formatted date when the subscription reactivated.
    
</dd>
</dl>

<dl>
<dd>

**resume_change_timing:** `typing.Optional[ChangeTiming]` 

The timing to resume a subscription, relative to the specified
`resume_effective_date` attribute value.
See [ChangeTiming](#type-changetiming) for possible values
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/square/subscriptions/client.py">swap_plan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedules a `SWAP_PLAN` action to swap a subscription plan variation in an existing subscription. 
For more information, see [Swap Subscription Plan Variations](https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.subscriptions.swap_plan(
    subscription_id="subscription_id",
    new_plan_variation_id="FQ7CDXXWSLUJRPM3GFJSJGZ7",
    phases=[
        {"ordinal": 0, "order_template_id": "uhhnjH9osVv3shUADwaC0b3hNxQZY"}
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — The ID of the subscription to swap the subscription plan for.
    
</dd>
</dl>

<dl>
<dd>

**new_plan_variation_id:** `typing.Optional[str]` 

The ID of the new subscription plan variation.

This field is required.
    
</dd>
</dl>

<dl>
<dd>

**phases:** `typing.Optional[typing.Sequence[PhaseInputParams]]` — A list of PhaseInputs, to pass phase-specific information used in the swap.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TeamMembers
<details><summary><code>client.team_members.<a href="src/square/team_members/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a single `TeamMember` object. The `TeamMember` object is returned on successful creates.
You must provide the following values in your request to this endpoint:
- `given_name`
- `family_name`

Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#createteammember).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team_members.create(
    idempotency_key="idempotency-key-0",
    team_member={
        "reference_id": "reference_id_1",
        "status": "ACTIVE",
        "given_name": "Joe",
        "family_name": "Doe",
        "email_address": "joe_doe@gmail.com",
        "phone_number": "+14159283333",
        "assigned_locations": {
            "assignment_type": "EXPLICIT_LOCATIONS",
            "location_ids": ["YSGH2WBKG94QZ", "GA2Y9HSJ8KRYT"],
        },
        "wage_setting": {
            "job_assignments": [
                {
                    "pay_type": "SALARY",
                    "annual_rate": {"amount": 3000000, "currency": "USD"},
                    "weekly_hours": 40,
                    "job_id": "FjS8x95cqHiMenw4f1NAUH4P",
                },
                {
                    "pay_type": "HOURLY",
                    "hourly_rate": {"amount": 2000, "currency": "USD"},
                    "job_id": "VDNpRv8da51NU8qZFC5zDWpF",
                },
            ],
            "is_overtime_exempt": True,
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies this `CreateTeamMember` request.
Keys can be any valid string, but must be unique for every request.
For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).

The minimum length is 1 and the maximum length is 45.
    
</dd>
</dl>

<dl>
<dd>

**team_member:** `typing.Optional[TeamMemberParams]` 

**Required** The data used to create the `TeamMember` object. If you include `wage_setting`, you must provide
`job_id` for each job assignment. To get job IDs, call [ListJobs](api-endpoint:Team-ListJobs).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team_members.<a href="src/square/team_members/client.py">batch_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates multiple `TeamMember` objects. The created `TeamMember` objects are returned on successful creates.
This process is non-transactional and processes as much of the request as possible. If one of the creates in
the request cannot be successfully processed, the request is not marked as failed, but the body of the response
contains explicit error information for the failed create.

Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team_members.batch_create(
    team_members={
        "idempotency-key-1": {
            "team_member": {
                "reference_id": "reference_id_1",
                "given_name": "Joe",
                "family_name": "Doe",
                "email_address": "joe_doe@gmail.com",
                "phone_number": "+14159283333",
                "assigned_locations": {
                    "assignment_type": "EXPLICIT_LOCATIONS",
                    "location_ids": ["YSGH2WBKG94QZ", "GA2Y9HSJ8KRYT"],
                },
            }
        },
        "idempotency-key-2": {
            "team_member": {
                "reference_id": "reference_id_2",
                "given_name": "Jane",
                "family_name": "Smith",
                "email_address": "jane_smith@gmail.com",
                "phone_number": "+14159223334",
                "assigned_locations": {
                    "assignment_type": "ALL_CURRENT_AND_FUTURE_LOCATIONS"
                },
            }
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_members:** `typing.Dict[str, CreateTeamMemberRequestParams]` 

The data used to create the `TeamMember` objects. Each key is the `idempotency_key` that maps to the `CreateTeamMemberRequest`.
The maximum number of create objects is 25.

If you include a team member's `wage_setting`, you must provide `job_id` for each job assignment. To get job IDs,
call [ListJobs](api-endpoint:Team-ListJobs).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team_members.<a href="src/square/team_members/client.py">batch_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates multiple `TeamMember` objects. The updated `TeamMember` objects are returned on successful updates.
This process is non-transactional and processes as much of the request as possible. If one of the updates in
the request cannot be successfully processed, the request is not marked as failed, but the body of the response
contains explicit error information for the failed update.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team_members.batch_update(
    team_members={
        "AFMwA08kR-MIF-3Vs0OE": {
            "team_member": {
                "reference_id": "reference_id_2",
                "is_owner": False,
                "status": "ACTIVE",
                "given_name": "Jane",
                "family_name": "Smith",
                "email_address": "jane_smith@gmail.com",
                "phone_number": "+14159223334",
                "assigned_locations": {
                    "assignment_type": "ALL_CURRENT_AND_FUTURE_LOCATIONS"
                },
            }
        },
        "fpgteZNMaf0qOK-a4t6P": {
            "team_member": {
                "reference_id": "reference_id_1",
                "is_owner": False,
                "status": "ACTIVE",
                "given_name": "Joe",
                "family_name": "Doe",
                "email_address": "joe_doe@gmail.com",
                "phone_number": "+14159283333",
                "assigned_locations": {
                    "assignment_type": "EXPLICIT_LOCATIONS",
                    "location_ids": ["YSGH2WBKG94QZ", "GA2Y9HSJ8KRYT"],
                },
            }
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_members:** `typing.Dict[str, UpdateTeamMemberRequestParams]` 

The data used to update the `TeamMember` objects. Each key is the `team_member_id` that maps to the `UpdateTeamMemberRequest`.
The maximum number of update objects is 25.

For each team member, include the fields to add, change, or clear. Fields can be cleared using a null value.
To update `wage_setting.job_assignments`, you must provide the complete list of job assignments. If needed,
call [ListJobs](api-endpoint:Team-ListJobs) to get the required `job_id` values.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team_members.<a href="src/square/team_members/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `TeamMember` objects for a business. 
The list can be filtered by location IDs, `ACTIVE` or `INACTIVE` status, or whether
the team member is the Square account owner.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.team_members.search(
    query={"filter": {"location_ids": ["0G5P3VGACMMQZ"], "status": "ACTIVE"}},
    limit=10,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[SearchTeamMembersQueryParams]` — The query parameters.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of `TeamMember` objects in a page (100 by default).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The opaque cursor for fetching the next page. For more information, see
[pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team_members.<a href="src/square/team_members/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a `TeamMember` object for the given `TeamMember.id`.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team_members.get(
    team_member_id="team_member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team_members.<a href="src/square/team_members/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a single `TeamMember` object. The `TeamMember` object is returned on successful updates.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team_members.update(
    team_member_id="team_member_id",
    team_member={
        "reference_id": "reference_id_1",
        "status": "ACTIVE",
        "given_name": "Joe",
        "family_name": "Doe",
        "email_address": "joe_doe@gmail.com",
        "phone_number": "+14159283333",
        "assigned_locations": {
            "assignment_type": "EXPLICIT_LOCATIONS",
            "location_ids": ["YSGH2WBKG94QZ", "GA2Y9HSJ8KRYT"],
        },
        "wage_setting": {
            "job_assignments": [
                {
                    "pay_type": "SALARY",
                    "annual_rate": {"amount": 3000000, "currency": "USD"},
                    "weekly_hours": 40,
                    "job_id": "FjS8x95cqHiMenw4f1NAUH4P",
                },
                {
                    "pay_type": "HOURLY",
                    "hourly_rate": {"amount": 1200, "currency": "USD"},
                    "job_id": "VDNpRv8da51NU8qZFC5zDWpF",
                },
            ],
            "is_overtime_exempt": True,
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member to update.
    
</dd>
</dl>

<dl>
<dd>

**team_member:** `typing.Optional[TeamMemberParams]` 

The team member fields to add, change, or clear. Fields can be cleared using a null value. To update
`wage_setting.job_assignments`, you must provide the complete list of job assignments. If needed, call
[ListJobs](api-endpoint:Team-ListJobs) to get the required `job_id` values.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Team
<details><summary><code>client.team.<a href="src/square/team/client.py">list_jobs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists jobs in a seller account. Results are sorted by title in ascending order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team.list_jobs(
    cursor="cursor",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The pagination cursor returned by the previous call to this endpoint. Provide this
cursor to retrieve the next page of results for your original request. For more information,
see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/square/team/client.py">create_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a job in a seller account. A job defines a title and tip eligibility. Note that
compensation is defined in a [job assignment](entity:JobAssignment) in a team member's wage setting.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team.create_job(
    job={"title": "Cashier", "is_tip_eligible": True},
    idempotency_key="idempotency-key-0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job:** `JobParams` — The job to create. The `title` field is required and `is_tip_eligible` defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique identifier for the `CreateJob` request. Keys can be any valid string,
but must be unique for each request. For more information, see
[Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/square/team/client.py">retrieve_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specified job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team.retrieve_job(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — The ID of the job to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team.<a href="src/square/team/client.py">update_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the title or tip eligibility of a job. Changes to the title propagate to all
`JobAssignment`, `Shift`, and `TeamMemberWage` objects that reference the job ID. Changes to
tip eligibility propagate to all `TeamMemberWage` objects that reference the job ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team.update_job(
    job_id="job_id",
    job={"title": "Cashier 1", "is_tip_eligible": True},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` — The ID of the job to update.
    
</dd>
</dl>

<dl>
<dd>

**job:** `JobParams` 

The job with the updated fields, either `title`, `is_tip_eligible`, or both. Only changed fields need
to be included in the request. Optionally include `version` to enable optimistic concurrency control.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Terminal
<details><summary><code>client.terminal.<a href="src/square/terminal/client.py">dismiss_terminal_action</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Dismisses a Terminal action request if the status and type of the request permits it.

See [Link and Dismiss Actions](https://developer.squareup.com/docs/terminal-api/advanced-features/custom-workflows/link-and-dismiss-actions) for more details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.dismiss_terminal_action(
    action_id="action_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `str` — Unique ID for the `TerminalAction` associated with the action to be dismissed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.<a href="src/square/terminal/client.py">dismiss_terminal_checkout</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Dismisses a Terminal checkout request if the status and type of the request permits it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.dismiss_terminal_checkout(
    checkout_id="checkout_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**checkout_id:** `str` — Unique ID for the `TerminalCheckout` associated with the checkout to be dismissed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.<a href="src/square/terminal/client.py">dismiss_terminal_refund</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Dismisses a Terminal refund request if the status and type of the request permits it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.dismiss_terminal_refund(
    terminal_refund_id="terminal_refund_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**terminal_refund_id:** `str` — Unique ID for the `TerminalRefund` associated with the refund to be dismissed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TransferOrders
<details><summary><code>client.transfer_orders.<a href="src/square/transfer_orders/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new transfer order in [DRAFT](entity:TransferOrderStatus) status. A transfer order represents the intent 
to move [CatalogItemVariation](entity:CatalogItemVariation)s from one [Location](entity:Location) to another. 
The source and destination locations must be different and must belong to your Square account.

In [DRAFT](entity:TransferOrderStatus) status, you can:
- Add or remove items
- Modify quantities
- Update shipping information
- Delete the entire order via [DeleteTransferOrder](api-endpoint:TransferOrders-DeleteTransferOrder)

The request requires source_location_id and destination_location_id.
Inventory levels are not affected until the order is started via 
[StartTransferOrder](api-endpoint:TransferOrders-StartTransferOrder).

Common integration points:
- Sync with warehouse management systems
- Automate regular stock transfers
- Initialize transfers from inventory optimization systems

Creates a [transfer_order.created](webhook:transfer_order.created) webhook event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.transfer_orders.create(
    idempotency_key="65cc0586-3e82-384s-b524-3885cffd52",
    transfer_order={
        "source_location_id": "EXAMPLE_SOURCE_LOCATION_ID_123",
        "destination_location_id": "EXAMPLE_DEST_LOCATION_ID_456",
        "expected_at": "2025-11-09T05:00:00Z",
        "notes": "Example transfer order for inventory redistribution between locations",
        "tracking_number": "TRACK123456789",
        "created_by_team_member_id": "EXAMPLE_TEAM_MEMBER_ID_789",
        "line_items": [
            {
                "item_variation_id": "EXAMPLE_ITEM_VARIATION_ID_001",
                "quantity_ordered": "5",
            },
            {
                "item_variation_id": "EXAMPLE_ITEM_VARIATION_ID_002",
                "quantity_ordered": "3",
            },
        ],
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this CreateTransferOrder request. Keys can be
any valid string but must be unique for every CreateTransferOrder request.
    
</dd>
</dl>

<dl>
<dd>

**transfer_order:** `CreateTransferOrderDataParams` — The transfer order to create
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfer_orders.<a href="src/square/transfer_orders/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for transfer orders using filters. Returns a paginated list of matching
[TransferOrder](entity:TransferOrder)s sorted by creation date.

Common search scenarios:
- Find orders for a source [Location](entity:Location)
- Find orders for a destination [Location](entity:Location)
- Find orders in a particular [TransferOrderStatus](entity:TransferOrderStatus)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.transfer_orders.search(
    query={
        "filter": {
            "source_location_ids": ["EXAMPLE_SOURCE_LOCATION_ID_123"],
            "destination_location_ids": ["EXAMPLE_DEST_LOCATION_ID_456"],
            "statuses": ["STARTED", "PARTIALLY_RECEIVED"],
        },
        "sort": {"field": "UPDATED_AT", "order": "DESC"},
    },
    cursor="eyJsYXN0X3VwZGF0ZWRfYXQiOjE3NTMxMTg2NjQ4NzN9",
    limit=10,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[TransferOrderQueryParams]` — The search query
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor from a previous search response
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfer_orders.<a href="src/square/transfer_orders/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific [TransferOrder](entity:TransferOrder) by ID. Returns the complete
order details including:

- Basic information (status, dates, notes)
- Line items with ordered and received quantities
- Source and destination [Location](entity:Location)s
- Tracking information (if available)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.transfer_orders.get(
    transfer_order_id="transfer_order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_order_id:** `str` — The ID of the transfer order to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfer_orders.<a href="src/square/transfer_orders/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing transfer order. This endpoint supports sparse updates,
allowing you to modify specific fields without affecting others.

Creates a [transfer_order.updated](webhook:transfer_order.updated) webhook event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.transfer_orders.update(
    transfer_order_id="transfer_order_id",
    idempotency_key="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    transfer_order={
        "source_location_id": "EXAMPLE_SOURCE_LOCATION_ID_789",
        "destination_location_id": "EXAMPLE_DEST_LOCATION_ID_101",
        "expected_at": "2025-11-10T08:00:00Z",
        "notes": "Updated: Priority transfer due to low stock at destination",
        "tracking_number": "TRACK987654321",
        "line_items": [
            {"uid": "1", "quantity_ordered": "7"},
            {
                "item_variation_id": "EXAMPLE_NEW_ITEM_VARIATION_ID_003",
                "quantity_ordered": "2",
            },
            {"uid": "2", "remove": True},
        ],
    },
    version=1753109537351,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_order_id:** `str` — The ID of the transfer order to update
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` — A unique string that identifies this UpdateTransferOrder request. Keys must contain only alphanumeric characters, dashes and underscores
    
</dd>
</dl>

<dl>
<dd>

**transfer_order:** `UpdateTransferOrderDataParams` — The transfer order updates to apply
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version for optimistic concurrency
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfer_orders.<a href="src/square/transfer_orders/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a transfer order in [DRAFT](entity:TransferOrderStatus) status.
Only draft orders can be deleted. Once an order is started via 
[StartTransferOrder](api-endpoint:TransferOrders-StartTransferOrder), it can no longer be deleted.

Creates a [transfer_order.deleted](webhook:transfer_order.deleted) webhook event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.transfer_orders.delete(
    transfer_order_id="transfer_order_id",
    version=1000000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_order_id:** `str` — The ID of the transfer order to delete
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version for optimistic concurrency
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfer_orders.<a href="src/square/transfer_orders/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a transfer order in [STARTED](entity:TransferOrderStatus) or 
[PARTIALLY_RECEIVED](entity:TransferOrderStatus) status. Any unreceived quantities will no
longer be receivable and will be immediately returned to the source [Location](entity:Location)'s inventory.

Common reasons for cancellation:
- Items no longer needed at destination
- Source location needs the inventory
- Order created in error

Creates a [transfer_order.updated](webhook:transfer_order.updated) webhook event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.transfer_orders.cancel(
    transfer_order_id="transfer_order_id",
    idempotency_key="65cc0586-3e82-4d08-b524-3885cffd52",
    version=1753117449752,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_order_id:** `str` — The ID of the transfer order to cancel. Must be in STARTED or PARTIALLY_RECEIVED status.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this UpdateTransferOrder request. Keys can be
any valid string but must be unique for every UpdateTransferOrder request.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version for optimistic concurrency
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfer_orders.<a href="src/square/transfer_orders/client.py">receive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Records receipt of [CatalogItemVariation](entity:CatalogItemVariation)s for a transfer order.
This endpoint supports partial receiving - you can receive items in multiple batches.

For each line item, you can specify:
- Quantity received in good condition (added to destination inventory with [InventoryState](entity:InventoryState) of IN_STOCK)
- Quantity damaged during transit/handling (added to destination inventory with [InventoryState](entity:InventoryState) of WASTE)
- Quantity canceled (returned to source location's inventory)

The order must be in [STARTED](entity:TransferOrderStatus) or [PARTIALLY_RECEIVED](entity:TransferOrderStatus) status.
Received quantities are added to the destination [Location](entity:Location)'s inventory according to their condition.
Canceled quantities are immediately returned to the source [Location](entity:Location)'s inventory.

When all items are either received, damaged, or canceled, the order moves to
[COMPLETED](entity:TransferOrderStatus) status.

Creates a [transfer_order.updated](webhook:transfer_order.updated) webhook event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.transfer_orders.receive(
    transfer_order_id="transfer_order_id",
    idempotency_key="EXAMPLE_IDEMPOTENCY_KEY_101",
    receipt={
        "line_items": [
            {
                "transfer_order_line_uid": "transfer_order_line_uid",
                "quantity_received": "3",
                "quantity_damaged": "1",
                "quantity_canceled": "1",
            },
            {
                "transfer_order_line_uid": "transfer_order_line_uid",
                "quantity_received": "2",
                "quantity_canceled": "1",
            },
        ]
    },
    version=1753118664873,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_order_id:** `str` — The ID of the transfer order to receive items for
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` — A unique key to make this request idempotent
    
</dd>
</dl>

<dl>
<dd>

**receipt:** `TransferOrderGoodsReceiptParams` — The receipt details
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version for optimistic concurrency
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transfer_orders.<a href="src/square/transfer_orders/client.py">start</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Changes a [DRAFT](entity:TransferOrderStatus) transfer order to [STARTED](entity:TransferOrderStatus) status.
This decrements inventory at the source [Location](entity:Location) and marks it as in-transit.

The order must be in [DRAFT](entity:TransferOrderStatus) status and have all required fields populated.
Once started, the order can no longer be deleted, but it can be canceled via 
[CancelTransferOrder](api-endpoint:TransferOrders-CancelTransferOrder).

Creates a [transfer_order.updated](webhook:transfer_order.updated) webhook event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.transfer_orders.start(
    transfer_order_id="transfer_order_id",
    idempotency_key="EXAMPLE_IDEMPOTENCY_KEY_789",
    version=1753109537351,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transfer_order_id:** `str` — The ID of the transfer order to start. Must be in DRAFT status.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this UpdateTransferOrder request. Keys can be
any valid string but must be unique for every UpdateTransferOrder request.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` — Version for optimistic concurrency
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vendors
<details><summary><code>client.vendors.<a href="src/square/vendors/client.py">batch_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one or more [Vendor](entity:Vendor) objects to represent suppliers to a seller.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.vendors.batch_create(
    vendors={
        "8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe": {
            "name": "Joe's Fresh Seafood",
            "address": {
                "address_line1": "505 Electric Ave",
                "address_line2": "Suite 600",
                "locality": "New York",
                "administrative_district_level1": "NY",
                "postal_code": "10003",
                "country": "US",
            },
            "contacts": [
                {
                    "name": "Joe Burrow",
                    "email_address": "joe@joesfreshseafood.com",
                    "phone_number": "1-212-555-4250",
                    "ordinal": 1,
                }
            ],
            "account_number": "4025391",
            "note": "a vendor",
        }
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vendors:** `typing.Dict[str, VendorParams]` — Specifies a set of new [Vendor](entity:Vendor) objects as represented by a collection of idempotency-key/`Vendor`-object pairs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vendors.<a href="src/square/vendors/client.py">batch_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves one or more vendors of specified [Vendor](entity:Vendor) IDs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.vendors.batch_get(
    vendor_ids=["INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vendor_ids:** `typing.Optional[typing.Sequence[str]]` — IDs of the [Vendor](entity:Vendor) objects to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vendors.<a href="src/square/vendors/client.py">batch_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one or more of existing [Vendor](entity:Vendor) objects as suppliers to a seller.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.vendors.batch_update(
    vendors={
        "FMCYHBWT1TPL8MFH52PBMEN92A": {"vendor": {}},
        "INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4": {"vendor": {}},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vendors:** `typing.Dict[str, UpdateVendorRequestParams]` 

A set of [UpdateVendorRequest](entity:UpdateVendorRequest) objects encapsulating to-be-updated [Vendor](entity:Vendor)
objects. The set is represented by  a collection of `Vendor`-ID/`UpdateVendorRequest`-object pairs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vendors.<a href="src/square/vendors/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a single [Vendor](entity:Vendor) object to represent a supplier to a seller.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.vendors.create(
    idempotency_key="8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe",
    vendor={
        "name": "Joe's Fresh Seafood",
        "address": {
            "address_line1": "505 Electric Ave",
            "address_line2": "Suite 600",
            "locality": "New York",
            "administrative_district_level1": "NY",
            "postal_code": "10003",
            "country": "US",
        },
        "contacts": [
            {
                "name": "Joe Burrow",
                "email_address": "joe@joesfreshseafood.com",
                "phone_number": "1-212-555-4250",
                "ordinal": 1,
            }
        ],
        "account_number": "4025391",
        "note": "a vendor",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A client-supplied, universally unique identifier (UUID) to make this [CreateVendor](api-endpoint:Vendors-CreateVendor) call idempotent.

See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) in the
[API Development 101](https://developer.squareup.com/docs/buildbasics) section for more
information.
    
</dd>
</dl>

<dl>
<dd>

**vendor:** `typing.Optional[VendorParams]` — The requested [Vendor](entity:Vendor) to be created.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vendors.<a href="src/square/vendors/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for vendors using a filter against supported [Vendor](entity:Vendor) properties and a supported sorter.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.vendors.search()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `typing.Optional[SearchVendorsRequestFilterParams]` — Specifies a filter used to search for vendors.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SearchVendorsRequestSortParams]` — Specifies a sorter used to sort the returned vendors.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.

See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vendors.<a href="src/square/vendors/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the vendor of a specified [Vendor](entity:Vendor) ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.vendors.get(
    vendor_id="vendor_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vendor_id:** `str` — ID of the [Vendor](entity:Vendor) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.vendors.<a href="src/square/vendors/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing [Vendor](entity:Vendor) object as a supplier to a seller.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.vendors.update(
    vendor_id="vendor_id",
    idempotency_key="8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe",
    vendor={
        "id": "INV_V_JDKYHBWT1D4F8MFH63DBMEN8Y4",
        "name": "Jack's Chicken Shack",
        "version": 1,
        "status": "ACTIVE",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vendor_id:** `str` — ID of the [Vendor](entity:Vendor) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**vendor:** `VendorParams` — The specified [Vendor](entity:Vendor) to be updated.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A client-supplied, universally unique identifier (UUID) for the
request.

See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) in the
[API Development 101](https://developer.squareup.com/docs/buildbasics) section for more
information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Bookings CustomAttributeDefinitions
<details><summary><code>client.bookings.custom_attribute_definitions.<a href="src/square/bookings/custom_attribute_definitions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all bookings custom attribute definitions.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.bookings.custom_attribute_definitions.list(
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory.
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint.
Provide this cursor to retrieve the next page of results for your original request.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.custom_attribute_definitions.<a href="src/square/bookings/custom_attribute_definitions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.custom_attribute_definitions.create(
    custom_attribute_definition={},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition to create, with the following fields:

- `key`

- `name`. If provided, `name` must be unique (case-sensitive) across all visible booking-related custom attribute
definitions for the seller.

- `description`

- `visibility`. Note that all custom attributes are visible in exported booking data, including those set to
`VISIBILITY_HIDDEN`.

- `schema`. With the exception of the `Selection` data type, the `schema` is specified as a
simple URL to the JSON schema definition hosted on the Square CDN. For more information, see
[Specifying the schema](https://developer.squareup.com/docs/booking-custom-attributes-api/custom-attribute-definitions#specify-schema).
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.custom_attribute_definitions.<a href="src/square/bookings/custom_attribute_definitions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.custom_attribute_definitions.get(
    key="key",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute definition to retrieve. If the requesting application
is not the definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the custom attribute definition, which is used for strongly consistent
reads to guarantee that you receive the most up-to-date data. When included in the request,
Square returns the specified version or a higher version if one exists. If the specified version
is higher than the current version, Square returns a `BAD_REQUEST` error.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.custom_attribute_definitions.<a href="src/square/bookings/custom_attribute_definitions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.custom_attribute_definitions.update(
    key="key",
    custom_attribute_definition={},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to update.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition that contains the fields to update. Only the following fields can be updated:
- `name`
- `description`
- `visibility`
- `schema` for a `Selection` data type. Only changes to the named options or the maximum number of allowed
selections are supported.

For more information, see
[Updatable definition fields](https://developer.squareup.com/docs/booking-custom-attributes-api/custom-attribute-definitions#updatable-definition-fields).

To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control, include the optional `version` field and specify the current version of the custom attribute definition.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.custom_attribute_definitions.<a href="src/square/bookings/custom_attribute_definitions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.custom_attribute_definitions.delete(
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Bookings CustomAttributes
<details><summary><code>client.bookings.custom_attributes.<a href="src/square/bookings/custom_attributes/client.py">batch_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk deletes bookings custom attributes.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.custom_attributes.batch_delete(
    values={"key": {"booking_id": "booking_id", "key": "key"}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**values:** `typing.Dict[str, BookingCustomAttributeDeleteRequestParams]` 

A map containing 1 to 25 individual Delete requests. For each request, provide an
arbitrary ID that is unique for this `BulkDeleteBookingCustomAttributes` request and the
information needed to delete a custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.custom_attributes.<a href="src/square/bookings/custom_attributes/client.py">batch_upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk upserts bookings custom attributes.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.custom_attributes.batch_upsert(
    values={"key": {"booking_id": "booking_id", "custom_attribute": {}}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**values:** `typing.Dict[str, BookingCustomAttributeUpsertRequestParams]` 

A map containing 1 to 25 individual upsert requests. For each request, provide an
arbitrary ID that is unique for this `BulkUpsertBookingCustomAttributes` request and the
information needed to create or update a custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.custom_attributes.<a href="src/square/bookings/custom_attributes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists a booking's custom attributes.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.bookings.custom_attributes.list(
    booking_id="booking_id",
    limit=1,
    cursor="cursor",
    with_definitions=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_id:** `str` — The ID of the target [booking](entity:Booking).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory.
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint.
Provide this cursor to retrieve the next page of results for your original request. For more
information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**with_definitions:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each
custom attribute. Set this parameter to `true` to get the name and description of each custom
attribute, information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.custom_attributes.<a href="src/square/bookings/custom_attributes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a bookings custom attribute.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.custom_attributes.get(
    booking_id="booking_id",
    key="key",
    with_definition=True,
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_id:** `str` — The ID of the target [booking](entity:Booking).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to retrieve. This key must match the `key` of a custom
attribute definition in the Square seller account. If the requesting application is not the
definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**with_definition:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of
the custom attribute. Set this parameter to `true` to get the name and description of the custom
attribute, information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the custom attribute, which is used for strongly consistent reads to
guarantee that you receive the most up-to-date data. When included in the request, Square
returns the specified version or a higher version if one exists. If the specified version is
higher than the current version, Square returns a `BAD_REQUEST` error.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.custom_attributes.<a href="src/square/bookings/custom_attributes/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upserts a bookings custom attribute.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.custom_attributes.upsert(
    booking_id="booking_id",
    key="key",
    custom_attribute={},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_id:** `str` — The ID of the target [booking](entity:Booking).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to create or update. This key must match the `key` of a
custom attribute definition in the Square seller account. If the requesting application is not
the definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute:** `CustomAttributeParams` 

The custom attribute to create or update, with the following fields:

- `value`. This value must conform to the `schema` specified by the definition.
For more information, see [Value data types](https://developer.squareup.com/docs/booking-custom-attributes-api/custom-attributes#value-data-types).

- `version`. To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control for an update operation, include this optional field and specify the current version
of the custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.custom_attributes.<a href="src/square/bookings/custom_attributes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a bookings custom attribute.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.custom_attributes.delete(
    booking_id="booking_id",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**booking_id:** `str` — The ID of the target [booking](entity:Booking).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to delete. This key must match the `key` of a custom
attribute definition in the Square seller account. If the requesting application is not the
definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Bookings LocationProfiles
<details><summary><code>client.bookings.location_profiles.<a href="src/square/bookings/location_profiles/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists location booking profiles of a seller.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.bookings.location_profiles.list(
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return in a paged response.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor from the preceding response to return the next page of the results. Do not set this when retrieving the first page of the results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Bookings TeamMemberProfiles
<details><summary><code>client.bookings.team_member_profiles.<a href="src/square/bookings/team_member_profiles/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists booking profiles for team members.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.bookings.team_member_profiles.list(
    bookable_only=True,
    limit=1,
    cursor="cursor",
    location_id="location_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bookable_only:** `typing.Optional[bool]` — Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return in a paged response.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor from the preceding response to return the next page of the results. Do not set this when retrieving the first page of the results.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` — Indicates whether to include only team members enabled at the given location in the returned result.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bookings.team_member_profiles.<a href="src/square/bookings/team_member_profiles/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a team member's booking profile.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.bookings.team_member_profiles.get(
    team_member_id="team_member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CashDrawers Shifts
<details><summary><code>client.cash_drawers.shifts.<a href="src/square/cash_drawers/shifts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides the details for all of the cash drawer shifts for a location
in a date range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.cash_drawers.shifts.list(
    location_id="location_id",
    sort_order="DESC",
    begin_time="begin_time",
    end_time="end_time",
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to query for a list of cash drawer shifts.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SortOrder]` 

The order in which cash drawer shifts are listed in the response,
based on their opened_at field. Default value: ASC
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` — The inclusive start time of the query on opened_at, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` — The exclusive end date of the query on opened_at, in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Number of cash drawer shift events in a page of results (200 by
default, 1000 max).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor for fetching the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cash_drawers.shifts.<a href="src/square/cash_drawers/shifts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides the summary details for a single cash drawer shift. See
[ListCashDrawerShiftEvents](api-endpoint:CashDrawers-ListCashDrawerShiftEvents) for a list of cash drawer shift events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.cash_drawers.shifts.get(
    shift_id="shift_id",
    location_id="location_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shift_id:** `str` — The shift ID.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The ID of the location to retrieve cash drawer shifts from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cash_drawers.shifts.<a href="src/square/cash_drawers/shifts/client.py">list_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides a paginated list of events for a single cash drawer shift.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.cash_drawers.shifts.list_events(
    shift_id="shift_id",
    location_id="location_id",
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shift_id:** `str` — The shift ID.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list cash drawer shifts for.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Number of resources to be returned in a page of results (200 by
default, 1000 max).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor for fetching the next page of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Catalog Images
<details><summary><code>client.catalog.images.<a href="src/square/catalog/images/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads an image file to be represented by a [CatalogImage](entity:CatalogImage) object that can be linked to an existing
[CatalogObject](entity:CatalogObject) instance. The resulting `CatalogImage` is unattached to any `CatalogObject` if the `object_id`
is not specified.

This `CreateCatalogImage` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image file part in
JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.images.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[CreateCatalogImageRequestParams]` 
    
</dd>
</dl>

<dl>
<dd>

**image_file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.images.<a href="src/square/catalog/images/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a new image file to replace the existing one in the specified [CatalogImage](entity:CatalogImage) object.

This `UpdateCatalogImage` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image file part in
JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.images.update(
    image_id="image_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**image_id:** `str` — The ID of the `CatalogImage` object to update the encapsulated image file.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[UpdateCatalogImageRequestParams]` 
    
</dd>
</dl>

<dl>
<dd>

**image_file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Catalog Object
<details><summary><code>client.catalog.object.<a href="src/square/catalog/object/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new or updates the specified [CatalogObject](entity:CatalogObject).

To ensure consistency, only one update request is processed at a time per seller account.
While one (batch or non-batch) update request is being processed, other (batched and non-batched)
update requests are rejected with the `429` error code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.object.upsert(
    idempotency_key="af3d1afc-7212-4300-b463-0bfc5314a5ae",
    object={"type": "IMAGE", "id": "#Cocoa"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A value you specify that uniquely identifies this
request among all your requests. A common way to create
a valid idempotency key is to use a Universally unique
identifier (UUID).

If you're unsure whether a particular request was successful,
you can reattempt it with the same idempotency key without
worrying about creating duplicate objects.

See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**object:** `CatalogObjectParams` 

A CatalogObject to be created or updated.

- For updates, the object must be active (the `is_deleted` field is not `true`).
- For creates, the object ID must start with `#`. The provided ID is replaced with a server-generated ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.object.<a href="src/square/catalog/object/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single [CatalogItem](entity:CatalogItem) as a
[CatalogObject](entity:CatalogObject) based on the provided ID. The returned
object includes all of the relevant [CatalogItem](entity:CatalogItem)
information including: [CatalogItemVariation](entity:CatalogItemVariation)
children, references to its
[CatalogModifierList](entity:CatalogModifierList) objects, and the ids of
any [CatalogTax](entity:CatalogTax) objects that apply to it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.object.get(
    object_id="object_id",
    include_related_objects=True,
    catalog_version=1000000,
    include_category_path_to_root=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_id:** `str` — The object ID of any type of catalog objects to be retrieved.
    
</dd>
</dl>

<dl>
<dd>

**include_related_objects:** `typing.Optional[bool]` 

If `true`, the response will include additional objects that are related to the
requested objects. Related objects are defined as any objects referenced by ID by the results in the `objects` field
of the response. These objects are put in the `related_objects` field. Setting this to `true` is
helpful when the objects are needed for immediate display to a user.
This process only goes one level deep. Objects referenced by the related objects will not be included. For example,

if the `objects` field of the response contains a CatalogItem, its associated
CatalogCategory objects, CatalogTax objects, CatalogImage objects and
CatalogModifierLists will be returned in the `related_objects` field of the
response. If the `objects` field of the response contains a CatalogItemVariation,
its parent CatalogItem will be returned in the `related_objects` field of
the response.

Default value: `false`
    
</dd>
</dl>

<dl>
<dd>

**catalog_version:** `typing.Optional[int]` 

Requests objects as of a specific version of the catalog. This allows you to retrieve historical
versions of objects. The value to retrieve a specific version of an object can be found
in the version field of [CatalogObject](entity:CatalogObject)s. If not included, results will
be from the current version of the catalog.
    
</dd>
</dl>

<dl>
<dd>

**include_category_path_to_root:** `typing.Optional[bool]` 

Specifies whether or not to include the `path_to_root` list for each returned category instance. The `path_to_root` list consists
of `CategoryPathToRootNode` objects and specifies the path that starts with the immediate parent category of the returned category
and ends with its root category. If the returned category is a top-level category, the `path_to_root` list is empty and is not returned
in the response payload.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.catalog.object.<a href="src/square/catalog/object/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a single [CatalogObject](entity:CatalogObject) based on the
provided ID and returns the set of successfully deleted IDs in the response.
Deletion is a cascading event such that all children of the targeted object
are also deleted. For example, deleting a [CatalogItem](entity:CatalogItem)
will also delete all of its
[CatalogItemVariation](entity:CatalogItemVariation) children.

To ensure consistency, only one delete request is processed at a time per seller account.
While one (batch or non-batch) delete request is being processed, other (batched and non-batched)
delete requests are rejected with the `429` error code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.catalog.object.delete(
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_id:** `str` 

The ID of the catalog object to be deleted. When an object is deleted, other
objects in the graph that depend on that object will be deleted as well (for example, deleting a
catalog item will delete its catalog item variations).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Checkout PaymentLinks
<details><summary><code>client.checkout.payment_links.<a href="src/square/checkout/payment_links/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all payment links.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.checkout.payment_links.list(
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
If a cursor is not provided, the endpoint returns the first page of the results.
For more  information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

A limit on the number of results to return per page. The limit is advisory and
the implementation might return more or less results. If the supplied limit is negative, zero, or
greater than the maximum limit of 1000, it is ignored.

Default value: `100`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.checkout.payment_links.<a href="src/square/checkout/payment_links/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Square-hosted checkout page. Applications can share the resulting payment link with their buyer to pay for goods and services.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.checkout.payment_links.create(
    idempotency_key="cd9e25dc-d9f2-4430-aedb-61605070e95f",
    quick_pay={
        "name": "Auto Detailing",
        "price_money": {"amount": 10000, "currency": "USD"},
        "location_id": "A9Y43N9ABXZBP",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique string that identifies this `CreatePaymentLinkRequest` request.
If you do not provide a unique string (or provide an empty string as the value),
the endpoint treats each request as independent.

For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

A description of the payment link. You provide this optional description that is useful in your
application context. It is not used anywhere.
    
</dd>
</dl>

<dl>
<dd>

**quick_pay:** `typing.Optional[QuickPayParams]` 

Describes an ad hoc item and price for which to generate a quick pay checkout link.
For more information,
see [Quick Pay Checkout](https://developer.squareup.com/docs/checkout-api/quick-pay-checkout).
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderParams]` 

Describes the `Order` for which to create a checkout link.
For more information,
see [Square Order Checkout](https://developer.squareup.com/docs/checkout-api/square-order-checkout).
    
</dd>
</dl>

<dl>
<dd>

**checkout_options:** `typing.Optional[CheckoutOptionsParams]` 

Describes optional fields to add to the resulting checkout page.
For more information,
see [Optional Checkout Configurations](https://developer.squareup.com/docs/checkout-api/optional-checkout-configurations).
    
</dd>
</dl>

<dl>
<dd>

**pre_populated_data:** `typing.Optional[PrePopulatedDataParams]` 

Describes fields to prepopulate in the resulting checkout page.
For more information, see [Prepopulate the shipping address](https://developer.squareup.com/docs/checkout-api/optional-checkout-configurations#prepopulate-the-shipping-address).
    
</dd>
</dl>

<dl>
<dd>

**payment_note:** `typing.Optional[str]` — A note for the payment. After processing the payment, Square adds this note to the resulting `Payment`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.checkout.payment_links.<a href="src/square/checkout/payment_links/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a payment link.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.checkout.payment_links.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of link to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.checkout.payment_links.<a href="src/square/checkout/payment_links/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a payment link. You can update the `payment_link` fields such as
`description`, `checkout_options`, and  `pre_populated_data`.
You cannot update other fields such as the `order_id`, `version`, `URL`, or `timestamp` field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.checkout.payment_links.update(
    id="id",
    payment_link={
        "version": 1,
        "checkout_options": {"ask_for_shipping_address": True},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the payment link to update.
    
</dd>
</dl>

<dl>
<dd>

**payment_link:** `PaymentLinkParams` 

The `payment_link` object describing the updates to apply.
For more information, see [Update a payment link](https://developer.squareup.com/docs/checkout-api/manage-checkout#update-a-payment-link).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.checkout.payment_links.<a href="src/square/checkout/payment_links/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a payment link.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.checkout.payment_links.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the payment link to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customers CustomAttributeDefinitions
<details><summary><code>client.customers.custom_attribute_definitions.<a href="src/square/customers/custom_attribute_definitions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the customer-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.

When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that
seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.customers.custom_attribute_definitions.list(
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory.
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint.
Provide this cursor to retrieve the next page of results for your original request.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.custom_attribute_definitions.<a href="src/square/customers/custom_attribute_definitions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a customer-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to define a custom attribute that can be associated with customer profiles.

A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
for a custom attribute. After the definition is created, you can call
[UpsertCustomerCustomAttribute](api-endpoint:CustomerCustomAttributes-UpsertCustomerCustomAttribute) or
[BulkUpsertCustomerCustomAttributes](api-endpoint:CustomerCustomAttributes-BulkUpsertCustomerCustomAttributes)
to set the custom attribute for customer profiles in the seller's Customer Directory.

Sellers can view all custom attributes in exported customer data, including those set to
`VISIBILITY_HIDDEN`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.custom_attribute_definitions.create(
    custom_attribute_definition={
        "key": "favoritemovie",
        "schema": {
            "$ref": "https://developer-production-s.squarecdn.com/schemas/v1/common.json#squareup.common.String"
        },
        "name": "Favorite Movie",
        "description": "The favorite movie of the customer.",
        "visibility": "VISIBILITY_HIDDEN",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition to create. Note the following:
- With the exception of the `Selection` data type, the `schema` is specified as a simple URL to the JSON schema
definition hosted on the Square CDN. For more information, including supported values and constraints, see
[Specifying the schema](https://developer.squareup.com/docs/customer-custom-attributes-api/custom-attribute-definitions#specify-schema).
- If provided, `name` must be unique (case-sensitive) across all visible customer-related custom attribute definitions for the seller.
- All custom attributes are visible in exported customer data, including those set to `VISIBILITY_HIDDEN`.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.custom_attribute_definitions.<a href="src/square/customers/custom_attribute_definitions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a customer-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.

To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.custom_attribute_definitions.get(
    key="key",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute definition to retrieve. If the requesting application
is not the definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the custom attribute definition, which is used for strongly consistent
reads to guarantee that you receive the most up-to-date data. When included in the request,
Square returns the specified version or a higher version if one exists. If the specified version
is higher than the current version, Square returns a `BAD_REQUEST` error.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.custom_attribute_definitions.<a href="src/square/customers/custom_attribute_definitions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a customer-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.

Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
`schema` for a `Selection` data type.

Only the definition owner can update a custom attribute definition. Note that sellers can view
all custom attributes in exported customer data, including those set to `VISIBILITY_HIDDEN`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.custom_attribute_definitions.update(
    key="key",
    custom_attribute_definition={
        "description": "Update the description as desired.",
        "visibility": "VISIBILITY_READ_ONLY",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to update.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition that contains the fields to update. This endpoint
supports sparse updates, so only new or changed fields need to be included in the request.
Only the following fields can be updated:

- `name`
- `description`
- `visibility`
- `schema` for a `Selection` data type. Only changes to the named options or the maximum number of allowed
selections are supported.

For more information, see
[Updatable definition fields](https://developer.squareup.com/docs/customer-custom-attributes-api/custom-attribute-definitions#updatable-definition-fields).

To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency) 
control, include the optional `version` field and specify the current version of the custom attribute definition.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.custom_attribute_definitions.<a href="src/square/customers/custom_attribute_definitions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a customer-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.

Deleting a custom attribute definition also deletes the corresponding custom attribute from
all customer profiles in the seller's Customer Directory.

Only the definition owner can delete a custom attribute definition.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.custom_attribute_definitions.delete(
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.custom_attribute_definitions.<a href="src/square/customers/custom_attribute_definitions/client.py">batch_upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates [custom attributes](entity:CustomAttribute) for customer profiles as a bulk operation.

Use this endpoint to set the value of one or more custom attributes for one or more customer profiles.
A custom attribute is based on a custom attribute definition in a Square seller account, which is
created using the [CreateCustomerCustomAttributeDefinition](api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition) endpoint.

This `BulkUpsertCustomerCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides a customer ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.custom_attribute_definitions.batch_upsert(
    values={
        "id1": {
            "customer_id": "N3NCVYY3WS27HF0HKANA3R9FP8",
            "custom_attribute": {"key": "favoritemovie", "value": "Dune"},
        },
        "id2": {
            "customer_id": "SY8EMWRNDN3TQDP2H4KS1QWMMM",
            "custom_attribute": {"key": "ownsmovie", "value": False},
        },
        "id3": {
            "customer_id": "SY8EMWRNDN3TQDP2H4KS1QWMMM",
            "custom_attribute": {"key": "favoritemovie", "value": "Star Wars"},
        },
        "id4": {
            "customer_id": "N3NCVYY3WS27HF0HKANA3R9FP8",
            "custom_attribute": {
                "key": "square:a0f1505a-2aa1-490d-91a8-8d31ff181808",
                "value": "10.5",
            },
        },
        "id5": {
            "customer_id": "70548QG1HN43B05G0KCZ4MMC1G",
            "custom_attribute": {
                "key": "sq0ids-0evKIskIGaY45fCyNL66aw:backupemail",
                "value": "fake-email@squareup.com",
            },
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**values:** `typing.Dict[
    str,
    BatchUpsertCustomerCustomAttributesRequestCustomerCustomAttributeUpsertRequestParams,
]` 

A map containing 1 to 25 individual upsert requests. For each request, provide an
arbitrary ID that is unique for this `BulkUpsertCustomerCustomAttributes` request and the
information needed to create or update a custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customers Groups
<details><summary><code>client.customers.groups.<a href="src/square/customers/groups/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the list of customer groups of a business.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.customers.groups.list(
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
If the limit is less than 1 or greater than 50, Square returns a `400 VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default value is 50.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.groups.<a href="src/square/customers/groups/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new customer group for a business.

The request must include the `name` value of the group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.groups.create(
    group={"name": "Loyal Customers"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group:** `CustomerGroupParams` — The customer group to create.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — The idempotency key for the request. For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.groups.<a href="src/square/customers/groups/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific customer group as identified by the `group_id` value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.groups.get(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — The ID of the customer group to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.groups.<a href="src/square/customers/groups/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a customer group as identified by the `group_id` value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.groups.update(
    group_id="group_id",
    group={"name": "Loyal Customers"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — The ID of the customer group to update.
    
</dd>
</dl>

<dl>
<dd>

**group:** `CustomerGroupParams` — The `CustomerGroup` object including all the updates you want to make.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.groups.<a href="src/square/customers/groups/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a customer group as identified by the `group_id` value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.groups.delete(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — The ID of the customer group to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.groups.<a href="src/square/customers/groups/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a group membership to a customer.

The customer is identified by the `customer_id` value
and the customer group is identified by the `group_id` value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.groups.add(
    customer_id="customer_id",
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to add to a group.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — The ID of the customer group to add the customer to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.groups.<a href="src/square/customers/groups/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a group membership from a customer.

The customer is identified by the `customer_id` value
and the customer group is identified by the `group_id` value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.groups.remove(
    customer_id="customer_id",
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer to remove from the group.
    
</dd>
</dl>

<dl>
<dd>

**group_id:** `str` — The ID of the customer group to remove the customer from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customers Segments
<details><summary><code>client.customers.segments.<a href="src/square/customers/segments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the list of customer segments of a business.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.customers.segments.list(
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by previous calls to `ListCustomerSegments`.
This cursor is used to retrieve the next set of query results.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
If the specified limit is less than 1 or greater than 50, Square returns a `400 VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default value is 50.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.segments.<a href="src/square/customers/segments/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific customer segment as identified by the `segment_id` value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.segments.get(
    segment_id="segment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**segment_id:** `str` — The Square-issued ID of the customer segment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customers Cards
<details><summary><code>client.customers.cards.<a href="src/square/customers/cards/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a card on file to an existing customer.

As with charges, calls to `CreateCustomerCard` are idempotent. Multiple
calls with the same card nonce return the same card record that was created
with the provided nonce during the _first_ call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.cards.create(
    customer_id="customer_id",
    card_nonce="YOUR_CARD_NONCE",
    billing_address={
        "address_line1": "500 Electric Ave",
        "address_line2": "Suite 600",
        "locality": "New York",
        "administrative_district_level1": "NY",
        "postal_code": "10003",
        "country": "US",
    },
    cardholder_name="Amelia Earhart",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The Square ID of the customer profile the card is linked to.
    
</dd>
</dl>

<dl>
<dd>

**card_nonce:** `str` 

A card nonce representing the credit card to link to the customer.

Card nonces are generated by the Square payment form when customers enter
their card information. For more information, see
[Walkthrough: Integrate Square Payments in a Website](https://developer.squareup.com/docs/web-payments/take-card-payment).

__NOTE:__ Card nonces generated by digital wallets (such as Apple Pay)
cannot be used to create a customer card.
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[AddressParams]` 

Address information for the card on file.

__NOTE:__ If a billing address is provided in the request, the
`CreateCustomerCardRequest.billing_address.postal_code` must match
the postal code encoded in the card nonce.
    
</dd>
</dl>

<dl>
<dd>

**cardholder_name:** `typing.Optional[str]` — The full name printed on the credit card.
    
</dd>
</dl>

<dl>
<dd>

**verification_token:** `typing.Optional[str]` 

An identifying token generated by [Payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
Verification tokens encapsulate customer device information and 3-D Secure
challenge results to indicate that Square has verified the buyer identity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.cards.<a href="src/square/customers/cards/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a card on file from a customer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.cards.delete(
    customer_id="customer_id",
    card_id="card_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the customer that the card on file belongs to.
    
</dd>
</dl>

<dl>
<dd>

**card_id:** `str` — The ID of the card on file to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customers CustomAttributes
<details><summary><code>client.customers.custom_attributes.<a href="src/square/customers/custom_attributes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the [custom attributes](entity:CustomAttribute) associated with a customer profile.

You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.

When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.customers.custom_attributes.list(
    customer_id="customer_id",
    limit=1,
    cursor="cursor",
    with_definitions=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the target [customer profile](entity:Customer).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory.
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint.
Provide this cursor to retrieve the next page of results for your original request. For more
information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**with_definitions:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each
custom attribute. Set this parameter to `true` to get the name and description of each custom
attribute, information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.custom_attributes.<a href="src/square/customers/custom_attributes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a [custom attribute](entity:CustomAttribute) associated with a customer profile.

You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.

To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.custom_attributes.get(
    customer_id="customer_id",
    key="key",
    with_definition=True,
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the target [customer profile](entity:Customer).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to retrieve. This key must match the `key` of a custom
attribute definition in the Square seller account. If the requesting application is not the
definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**with_definition:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of
the custom attribute. Set this parameter to `true` to get the name and description of the custom
attribute, information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the custom attribute, which is used for strongly consistent reads to
guarantee that you receive the most up-to-date data. When included in the request, Square
returns the specified version or a higher version if one exists. If the specified version is
higher than the current version, Square returns a `BAD_REQUEST` error.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.custom_attributes.<a href="src/square/customers/custom_attributes/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates a [custom attribute](entity:CustomAttribute) for a customer profile.

Use this endpoint to set the value of a custom attribute for a specified customer profile.
A custom attribute is based on a custom attribute definition in a Square seller account, which
is created using the [CreateCustomerCustomAttributeDefinition](api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition) endpoint.

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.custom_attributes.upsert(
    customer_id="customer_id",
    key="key",
    custom_attribute={"value": "Dune"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the target [customer profile](entity:Customer).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to create or update. This key must match the `key` of a
custom attribute definition in the Square seller account. If the requesting application is not
the definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute:** `CustomAttributeParams` 

The custom attribute to create or update, with the following fields:

- `value`. This value must conform to the `schema` specified by the definition. 
For more information, see [Value data types](https://developer.squareup.com/docs/customer-custom-attributes-api/custom-attributes#value-data-types).

- `version`. To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control for an update operation, include this optional field and specify the current version
of the custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.custom_attributes.<a href="src/square/customers/custom_attributes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a [custom attribute](entity:CustomAttribute) associated with a customer profile.

To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.customers.custom_attributes.delete(
    customer_id="customer_id",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — The ID of the target [customer profile](entity:Customer).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to delete. This key must match the `key` of a custom
attribute definition in the Square seller account. If the requesting application is not the
definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Devices Codes
<details><summary><code>client.devices.codes.<a href="src/square/devices/codes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all DeviceCodes associated with the merchant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.devices.codes.list(
    cursor="cursor",
    location_id="location_id",
    status="UNKNOWN",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.

See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

If specified, only returns DeviceCodes of the specified location.
Returns DeviceCodes of all locations if empty.
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[ProductType]` 

If specified, only returns DeviceCodes targeting the specified product type.
Returns DeviceCodes of all product types if empty.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[DeviceCodeStatus]` 

If specified, returns DeviceCodes with the specified statuses.
Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.devices.codes.<a href="src/square/devices/codes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected
terminal mode.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.devices.codes.create(
    idempotency_key="01bb00a6-0c86-4770-94ed-f5fca973cd56",
    device_code={
        "name": "Counter 1",
        "product_type": "TERMINAL_API",
        "location_id": "B5E4484SHHNYH",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this CreateDeviceCode request. Keys can
be any valid string but must be unique for every CreateDeviceCode request.

See [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**device_code:** `DeviceCodeParams` — The device code to create.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.devices.codes.<a href="src/square/devices/codes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves DeviceCode with the associated ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.devices.codes.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the device code.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Disputes Evidence
<details><summary><code>client.disputes.evidence.<a href="src/square/disputes/evidence/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of evidence associated with a dispute.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.disputes.evidence.list(
    dispute_id="dispute_id",
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.evidence.<a href="src/square/disputes/evidence/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the metadata for the evidence specified in the request URL path.

You must maintain a copy of any evidence uploaded if you want to reference it later. Evidence cannot be downloaded after you upload it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.disputes.evidence.get(
    dispute_id="dispute_id",
    evidence_id="evidence_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute from which you want to retrieve evidence metadata.
    
</dd>
</dl>

<dl>
<dd>

**evidence_id:** `str` — The ID of the evidence to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.disputes.evidence.<a href="src/square/disputes/evidence/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes specified evidence from a dispute.
Square does not send the bank any evidence that is removed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.disputes.evidence.delete(
    dispute_id="dispute_id",
    evidence_id="evidence_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dispute_id:** `str` — The ID of the dispute from which you want to remove evidence.
    
</dd>
</dl>

<dl>
<dd>

**evidence_id:** `str` — The ID of the evidence you want to remove.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## GiftCards Activities
<details><summary><code>client.gift_cards.activities.<a href="src/square/gift_cards/activities/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists gift card activities. By default, you get gift card activities for all
gift cards in the seller's account. You can optionally specify query parameters to
filter the list. For example, you can get a list of gift card activities for a gift card,
for all gift cards in a specific region, or for activities within a time window.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.gift_cards.activities.list(
    gift_card_id="gift_card_id",
    type="type",
    location_id="location_id",
    begin_time="begin_time",
    end_time="end_time",
    limit=1,
    cursor="cursor",
    sort_order="sort_order",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**gift_card_id:** `typing.Optional[str]` 

If a gift card ID is provided, the endpoint returns activities related 
to the specified gift card. Otherwise, the endpoint returns all gift card activities for 
the seller.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 

If a [type](entity:GiftCardActivityType) is provided, the endpoint returns gift card activities of the specified type. 
Otherwise, the endpoint returns all types of gift card activities.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

If a location ID is provided, the endpoint returns gift card activities for the specified location. 
Otherwise, the endpoint returns gift card activities for all locations.
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

The timestamp for the beginning of the reporting period, in RFC 3339 format.
This start time is inclusive. The default value is the current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

The timestamp for the end of the reporting period, in RFC 3339 format.
This end time is inclusive. The default value is the current time.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

If a limit is provided, the endpoint returns the specified number 
of results (or fewer) per page. The maximum value is 100. The default value is 50.
For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
If a cursor is not provided, the endpoint returns the first page of the results.
For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[str]` 

The order in which the endpoint returns the activities, based on `created_at`.
- `ASC` - Oldest to newest.
- `DESC` - Newest to oldest (default).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gift_cards.activities.<a href="src/square/gift_cards/activities/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a gift card activity to manage the balance or state of a [gift card](entity:GiftCard).
For example, create an `ACTIVATE` activity to activate a gift card with an initial balance before first use.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.gift_cards.activities.create(
    idempotency_key="U16kfr-kA70er-q4Rsym-7U7NnY",
    gift_card_activity={
        "type": "ACTIVATE",
        "location_id": "81FN9BNFZTKS4",
        "gift_card_id": "gftc:6d55a72470d940c6ba09c0ab8ad08d20",
        "activate_activity_details": {
            "order_id": "jJNGHm4gLI6XkFbwtiSLqK72KkAZY",
            "line_item_uid": "eIWl7X0nMuO9Ewbh0ChIx",
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` — A unique string that identifies the `CreateGiftCardActivity` request.
    
</dd>
</dl>

<dl>
<dd>

**gift_card_activity:** `GiftCardActivityParams` 

The activity to create for the gift card. This activity must specify `gift_card_id` or `gift_card_gan` for the target
gift card, the `location_id` where the activity occurred, and the activity `type` along with the corresponding activity details.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Labor BreakTypes
<details><summary><code>client.labor.break_types.<a href="src/square/labor/break_types/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `BreakType` instances for a business.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.labor.break_types.list(
    location_id="location_id",
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `typing.Optional[str]` 

Filter the returned `BreakType` results to only those that are associated with the
specified location.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of `BreakType` results to return per page. The number can range between 1
and 200. The default is 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A pointer to the next page of `BreakType` results to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.break_types.<a href="src/square/labor/break_types/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new `BreakType`.

A `BreakType` is a template for creating `Break` objects.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `break_name`
- `expected_duration`
- `is_paid`

You can only have three `BreakType` instances per location. If you attempt to add a fourth
`BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit of 3 breaks per location."
is returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.break_types.create(
    idempotency_key="PAD3NG5KSN2GL",
    break_type={
        "location_id": "CGJN03P1D08GF",
        "break_name": "Lunch Break",
        "expected_duration": "PT30M",
        "is_paid": True,
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**break_type:** `BreakTypeParams` — The `BreakType` to be created.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique string value to ensure the idempotency of the operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.break_types.<a href="src/square/labor/break_types/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single `BreakType` specified by `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.break_types.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID for the `BreakType` being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.break_types.<a href="src/square/labor/break_types/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing `BreakType`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.break_types.update(
    id="id",
    break_type={
        "location_id": "26M7H24AZ9N6R",
        "break_name": "Lunch",
        "expected_duration": "PT50M",
        "is_paid": True,
        "version": 1,
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` —  The UUID for the `BreakType` being updated.
    
</dd>
</dl>

<dl>
<dd>

**break_type:** `BreakTypeParams` — The updated `BreakType`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.break_types.<a href="src/square/labor/break_types/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing `BreakType`.

A `BreakType` can be deleted even if it is referenced from a `Shift`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.break_types.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID for the `BreakType` being deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Labor EmployeeWages
<details><summary><code>client.labor.employee_wages.<a href="src/square/labor/employee_wages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `EmployeeWage` instances for a business.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.labor.employee_wages.list(
    employee_id="employee_id",
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**employee_id:** `typing.Optional[str]` — Filter the returned wages to only those that are associated with the specified employee.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of `EmployeeWage` results to return per page. The number can range between
1 and 200. The default is 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A pointer to the next page of `EmployeeWage` results to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.employee_wages.<a href="src/square/labor/employee_wages/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single `EmployeeWage` specified by `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.employee_wages.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID for the `EmployeeWage` being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Labor Shifts
<details><summary><code>client.labor.shifts.<a href="src/square/labor/shifts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new `Shift`.

A `Shift` represents a complete workday for a single team member.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `team_member_id`
- `start_at`

An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when:
- The `status` of the new `Shift` is `OPEN` and the team member has another
shift with an `OPEN` status.
- The `start_at` date is in the future.
- The `start_at` or `end_at` date overlaps another shift for the same team member.
- The `Break` instances are set in the request and a break `start_at`
is before the `Shift.start_at`, a break `end_at` is after
the `Shift.end_at`, or both.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.shifts.create(
    idempotency_key="HIDSNG5KS478L",
    shift={
        "location_id": "PAA1RJZZKXBFG",
        "start_at": "2019-01-25T03:11:00-05:00",
        "end_at": "2019-01-25T13:11:00-05:00",
        "wage": {
            "title": "Barista",
            "hourly_rate": {"amount": 1100, "currency": "USD"},
            "tip_eligible": True,
        },
        "breaks": [
            {
                "start_at": "2019-01-25T06:11:00-05:00",
                "end_at": "2019-01-25T06:16:00-05:00",
                "break_type_id": "REGS1EQR1TPZ5",
                "name": "Tea Break",
                "expected_duration": "PT5M",
                "is_paid": True,
            }
        ],
        "team_member_id": "ormj0jJJZ5OZIzxrZYJI",
        "declared_cash_tip_money": {"amount": 500, "currency": "USD"},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**shift:** `ShiftParams` — The `Shift` to be created.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique string value to ensure the idempotency of the operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.shifts.<a href="src/square/labor/shifts/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `Shift` records for a business.
The list to be returned can be filtered by:
- Location IDs
- Team member IDs
- Shift status (`OPEN` or `CLOSED`)
- Shift start
- Shift end
- Workday details

The list can be sorted by:
- `START_AT`
- `END_AT`
- `CREATED_AT`
- `UPDATED_AT`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.labor.shifts.search(
    query={
        "filter": {
            "workday": {
                "date_range": {
                    "start_date": "2019-01-20",
                    "end_date": "2019-02-03",
                },
                "match_shifts_by": "START_AT",
                "default_timezone": "America/Los_Angeles",
            }
        }
    },
    limit=100,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[ShiftQueryParams]` — Query filters.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of resources in a page (200 by default).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — An opaque cursor for fetching the next page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.shifts.<a href="src/square/labor/shifts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single `Shift` specified by `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.shifts.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID for the `Shift` being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.shifts.<a href="src/square/labor/shifts/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing `Shift`.

When adding a `Break` to a `Shift`, any earlier `Break` instances in the `Shift` have
the `end_at` property set to a valid RFC-3339 datetime string.

When closing a `Shift`, all `Break` instances in the `Shift` must be complete with `end_at`
set on each `Break`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.shifts.update(
    id="id",
    shift={
        "location_id": "PAA1RJZZKXBFG",
        "start_at": "2019-01-25T03:11:00-05:00",
        "end_at": "2019-01-25T13:11:00-05:00",
        "wage": {
            "title": "Bartender",
            "hourly_rate": {"amount": 1500, "currency": "USD"},
            "tip_eligible": True,
        },
        "breaks": [
            {
                "id": "X7GAQYVVRRG6P",
                "start_at": "2019-01-25T06:11:00-05:00",
                "end_at": "2019-01-25T06:16:00-05:00",
                "break_type_id": "REGS1EQR1TPZ5",
                "name": "Tea Break",
                "expected_duration": "PT5M",
                "is_paid": True,
            }
        ],
        "version": 1,
        "team_member_id": "ormj0jJJZ5OZIzxrZYJI",
        "declared_cash_tip_money": {"amount": 500, "currency": "USD"},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the object being updated.
    
</dd>
</dl>

<dl>
<dd>

**shift:** `ShiftParams` — The updated `Shift` object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.shifts.<a href="src/square/labor/shifts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a `Shift`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.shifts.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID for the `Shift` being deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Labor TeamMemberWages
<details><summary><code>client.labor.team_member_wages.<a href="src/square/labor/team_member_wages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of `TeamMemberWage` instances for a business.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.labor.team_member_wages.list(
    team_member_id="team_member_id",
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `typing.Optional[str]` 

Filter the returned wages to only those that are associated with the
specified team member.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of `TeamMemberWage` results to return per page. The number can range between
1 and 200. The default is 200.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A pointer to the next page of `EmployeeWage` results to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.team_member_wages.<a href="src/square/labor/team_member_wages/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single `TeamMemberWage` specified by `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.team_member_wages.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID for the `TeamMemberWage` being retrieved.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Labor WorkweekConfigs
<details><summary><code>client.labor.workweek_configs.<a href="src/square/labor/workweek_configs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `WorkweekConfig` instances for a business.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.labor.workweek_configs.list(
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of `WorkweekConfigs` results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — A pointer to the next page of `WorkweekConfig` results to fetch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.labor.workweek_configs.<a href="src/square/labor/workweek_configs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a `WorkweekConfig`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.labor.workweek_configs.get(
    id="id",
    workweek_config={
        "start_of_week": "MON",
        "start_of_day_local_time": "10:00",
        "version": 10,
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The UUID for the `WorkweekConfig` object being updated.
    
</dd>
</dl>

<dl>
<dd>

**workweek_config:** `WorkweekConfigParams` — The updated `WorkweekConfig` object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Locations CustomAttributeDefinitions
<details><summary><code>client.locations.custom_attribute_definitions.<a href="src/square/locations/custom_attribute_definitions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the location-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.
When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.locations.custom_attribute_definitions.list(
    visibility_filter="ALL",
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**visibility_filter:** `typing.Optional[VisibilityFilter]` — Filters the `CustomAttributeDefinition` results by their `visibility` values.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory.
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint.
Provide this cursor to retrieve the next page of results for your original request.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.custom_attribute_definitions.<a href="src/square/locations/custom_attribute_definitions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a location-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to define a custom attribute that can be associated with locations.
A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
for a custom attribute. After the definition is created, you can call
[UpsertLocationCustomAttribute](api-endpoint:LocationCustomAttributes-UpsertLocationCustomAttribute) or
[BulkUpsertLocationCustomAttributes](api-endpoint:LocationCustomAttributes-BulkUpsertLocationCustomAttributes)
to set the custom attribute for locations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.custom_attribute_definitions.create(
    custom_attribute_definition={
        "key": "bestseller",
        "schema": {
            "$ref": "https://developer-production-s.squarecdn.com/schemas/v1/common.json#squareup.common.String"
        },
        "name": "Bestseller",
        "description": "Bestselling item at location",
        "visibility": "VISIBILITY_READ_WRITE_VALUES",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition to create. Note the following:
- With the exception of the `Selection` data type, the `schema` is specified as a simple URL to the JSON schema
definition hosted on the Square CDN. For more information, including supported values and constraints, see
[Supported data types](https://developer.squareup.com/docs/devtools/customattributes/overview#supported-data-types).
- `name` is required unless `visibility` is set to `VISIBILITY_HIDDEN`.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.custom_attribute_definitions.<a href="src/square/locations/custom_attribute_definitions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a location-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.custom_attribute_definitions.get(
    key="key",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute definition to retrieve. If the requesting application
is not the definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the custom attribute definition, which is used for strongly consistent
reads to guarantee that you receive the most up-to-date data. When included in the request,
Square returns the specified version or a higher version if one exists. If the specified version
is higher than the current version, Square returns a `BAD_REQUEST` error.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.custom_attribute_definitions.<a href="src/square/locations/custom_attribute_definitions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a location-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
`schema` for a `Selection` data type.
Only the definition owner can update a custom attribute definition.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.custom_attribute_definitions.update(
    key="key",
    custom_attribute_definition={
        "description": "Update the description as desired.",
        "visibility": "VISIBILITY_READ_ONLY",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to update.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition that contains the fields to update. This endpoint
supports sparse updates, so only new or changed fields need to be included in the request.
Only the following fields can be updated:
- `name`
- `description`
- `visibility`
- `schema` for a `Selection` data type. Only changes to the named options or the maximum number of allowed
selections are supported.

For more information, see
[Update a location custom attribute definition](https://developer.squareup.com/docs/location-custom-attributes-api/custom-attribute-definitions#update-custom-attribute-definition).
To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control, specify the current version of the custom attribute definition. 
If this is not important for your application, `version` can be set to -1.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.custom_attribute_definitions.<a href="src/square/locations/custom_attribute_definitions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a location-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
Deleting a custom attribute definition also deletes the corresponding custom attribute from
all locations.
Only the definition owner can delete a custom attribute definition.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.custom_attribute_definitions.delete(
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Locations CustomAttributes
<details><summary><code>client.locations.custom_attributes.<a href="src/square/locations/custom_attributes/client.py">batch_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes [custom attributes](entity:CustomAttribute) for locations as a bulk operation.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.custom_attributes.batch_delete(
    values={
        "id1": {"key": "bestseller"},
        "id2": {"key": "bestseller"},
        "id3": {"key": "phone-number"},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**values:** `typing.Dict[
    str,
    BulkDeleteLocationCustomAttributesRequestLocationCustomAttributeDeleteRequestParams,
]` 

The data used to update the `CustomAttribute` objects.
The keys must be unique and are used to map to the corresponding response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.custom_attributes.<a href="src/square/locations/custom_attributes/client.py">batch_upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates [custom attributes](entity:CustomAttribute) for locations as a bulk operation.
Use this endpoint to set the value of one or more custom attributes for one or more locations.
A custom attribute is based on a custom attribute definition in a Square seller account, which is
created using the [CreateLocationCustomAttributeDefinition](api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition) endpoint.
This `BulkUpsertLocationCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides a location ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.custom_attributes.batch_upsert(
    values={
        "id1": {
            "location_id": "L0TBCBTB7P8RQ",
            "custom_attribute": {"key": "bestseller", "value": "hot cocoa"},
        },
        "id2": {
            "location_id": "L9XMD04V3STJX",
            "custom_attribute": {
                "key": "bestseller",
                "value": "berry smoothie",
            },
        },
        "id3": {
            "location_id": "L0TBCBTB7P8RQ",
            "custom_attribute": {
                "key": "phone-number",
                "value": "+12223334444",
            },
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**values:** `typing.Dict[
    str,
    BulkUpsertLocationCustomAttributesRequestLocationCustomAttributeUpsertRequestParams,
]` 

A map containing 1 to 25 individual upsert requests. For each request, provide an
arbitrary ID that is unique for this `BulkUpsertLocationCustomAttributes` request and the
information needed to create or update a custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.custom_attributes.<a href="src/square/locations/custom_attributes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the [custom attributes](entity:CustomAttribute) associated with a location.
You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.
When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.locations.custom_attributes.list(
    location_id="location_id",
    visibility_filter="ALL",
    limit=1,
    cursor="cursor",
    with_definitions=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the target [location](entity:Location).
    
</dd>
</dl>

<dl>
<dd>

**visibility_filter:** `typing.Optional[VisibilityFilter]` — Filters the `CustomAttributeDefinition` results by their `visibility` values.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory.
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint.
Provide this cursor to retrieve the next page of results for your original request. For more
information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**with_definitions:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each
custom attribute. Set this parameter to `true` to get the name and description of each custom
attribute, information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.custom_attributes.<a href="src/square/locations/custom_attributes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a [custom attribute](entity:CustomAttribute) associated with a location.
You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.
To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.custom_attributes.get(
    location_id="location_id",
    key="key",
    with_definition=True,
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the target [location](entity:Location).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to retrieve. This key must match the `key` of a custom
attribute definition in the Square seller account. If the requesting application is not the
definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**with_definition:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of
the custom attribute. Set this parameter to `true` to get the name and description of the custom
attribute, information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the custom attribute, which is used for strongly consistent reads to
guarantee that you receive the most up-to-date data. When included in the request, Square
returns the specified version or a higher version if one exists. If the specified version is
higher than the current version, Square returns a `BAD_REQUEST` error.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.custom_attributes.<a href="src/square/locations/custom_attributes/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates a [custom attribute](entity:CustomAttribute) for a location.
Use this endpoint to set the value of a custom attribute for a specified location.
A custom attribute is based on a custom attribute definition in a Square seller account, which
is created using the [CreateLocationCustomAttributeDefinition](api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition) endpoint.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.custom_attributes.upsert(
    location_id="location_id",
    key="key",
    custom_attribute={"value": "hot cocoa"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the target [location](entity:Location).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to create or update. This key must match the `key` of a
custom attribute definition in the Square seller account. If the requesting application is not
the definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute:** `CustomAttributeParams` 

The custom attribute to create or update, with the following fields:
- `value`. This value must conform to the `schema` specified by the definition.
For more information, see [Supported data types](https://developer.squareup.com/docs/devtools/customattributes/overview#supported-data-types).
- `version`. To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control for an update operation, include the current version of the custom attribute.
If this is not important for your application, version can be set to -1.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.custom_attributes.<a href="src/square/locations/custom_attributes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a [custom attribute](entity:CustomAttribute) associated with a location.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.custom_attributes.delete(
    location_id="location_id",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the target [location](entity:Location).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to delete. This key must match the `key` of a custom
attribute definition in the Square seller account. If the requesting application is not the
definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Locations Transactions
<details><summary><code>client.locations.transactions.<a href="src/square/locations/transactions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists transactions for a particular location.

Transactions include payment information from sales and exchanges and refund
information from returns and exchanges.

Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.transactions.list(
    location_id="location_id",
    begin_time="begin_time",
    end_time="end_time",
    sort_order="DESC",
    cursor="cursor",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the location to list transactions for.
    
</dd>
</dl>

<dl>
<dd>

**begin_time:** `typing.Optional[str]` 

The beginning of the requested reporting period, in RFC 3339 format.

See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

Default value: The current time minus one year.
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[str]` 

The end of the requested reporting period, in RFC 3339 format.

See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.

Default value: The current time.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SortOrder]` 

The order in which results are listed in the response (`ASC` for
oldest first, `DESC` for newest first).

Default value: `DESC`
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.

See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.transactions.<a href="src/square/locations/transactions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details for a single transaction.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.transactions.get(
    location_id="location_id",
    transaction_id="transaction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — The ID of the transaction's associated location.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — The ID of the transaction to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.transactions.<a href="src/square/locations/transactions/client.py">capture</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Captures a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
endpoint with a `delay_capture` value of `true`.


See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.transactions.capture(
    location_id="location_id",
    transaction_id="transaction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.locations.transactions.<a href="src/square/locations/transactions/client.py">void</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
endpoint with a `delay_capture` value of `true`.


See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.locations.transactions.void(
    location_id="location_id",
    transaction_id="transaction_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**location_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Loyalty Accounts
<details><summary><code>client.loyalty.accounts.<a href="src/square/loyalty/accounts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a loyalty account. To create a loyalty account, you must provide the `program_id` and a `mapping` with the `phone_number` of the buyer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.accounts.create(
    loyalty_account={
        "program_id": "d619f755-2d17-41f3-990d-c04ecedd64dd",
        "mapping": {"phone_number": "+14155551234"},
    },
    idempotency_key="ec78c477-b1c3-4899-a209-a4e71337c996",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**loyalty_account:** `LoyaltyAccountParams` — The loyalty account to create.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `CreateLoyaltyAccount` request. 
Keys can be any valid string, but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.accounts.<a href="src/square/loyalty/accounts/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for loyalty accounts in a loyalty program.

You can search for a loyalty account using the phone number or customer ID associated with the account. To return all loyalty accounts, specify an empty `query` object or omit it entirely.

Search results are sorted by `created_at` in ascending order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.loyalty.accounts.search(
    query={"mappings": [{"phone_number": "+14155551234"}]},
    limit=10,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[SearchLoyaltyAccountsRequestLoyaltyAccountQueryParams]` — The search criteria for the request.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to include in the response. The default value is 30.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to 
this endpoint. Provide this to retrieve the next set of 
results for the original query.

For more information, 
see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.accounts.<a href="src/square/loyalty/accounts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a loyalty account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.accounts.get(
    account_id="account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID of the [loyalty account](entity:LoyaltyAccount) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.accounts.<a href="src/square/loyalty/accounts/client.py">accumulate_points</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds points earned from a purchase to a [loyalty account](entity:LoyaltyAccount).

- If you are using the Orders API to manage orders, provide the `order_id`. Square reads the order
to compute the points earned from both the base loyalty program and an associated
[loyalty promotion](entity:LoyaltyPromotion). For purchases that qualify for multiple accrual
rules, Square computes points based on the accrual rule that grants the most points.
For purchases that qualify for multiple promotions, Square computes points based on the most
recently created promotion. A purchase must first qualify for program points to be eligible for promotion points.

- If you are not using the Orders API to manage orders, provide `points` with the number of points to add.
You must first perform a client-side computation of the points earned from the loyalty program and
loyalty promotion. For spend-based and visit-based programs, you can call [CalculateLoyaltyPoints](api-endpoint:Loyalty-CalculateLoyaltyPoints)
to compute the points earned from the base loyalty program. For information about computing points earned from a loyalty promotion, see
[Calculating promotion points](https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.accounts.accumulate_points(
    account_id="account_id",
    accumulate_points={"order_id": "RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY"},
    idempotency_key="58b90739-c3e8-4b11-85f7-e636d48d72cb",
    location_id="P034NEENMD09F",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID of the target [loyalty account](entity:LoyaltyAccount).
    
</dd>
</dl>

<dl>
<dd>

**accumulate_points:** `LoyaltyEventAccumulatePointsParams` 

The points to add to the account. 
If you are using the Orders API to manage orders, specify the order ID.
Otherwise, specify the points to add.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies the `AccumulateLoyaltyPoints` request. 
Keys can be any valid string but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The [location](entity:Location) where the purchase was made.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.accounts.<a href="src/square/loyalty/accounts/client.py">adjust</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds points to or subtracts points from a buyer's account.

Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call
[AccumulateLoyaltyPoints](api-endpoint:Loyalty-AccumulateLoyaltyPoints)
to add points when a buyer pays for the purchase.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.accounts.adjust(
    account_id="account_id",
    idempotency_key="bc29a517-3dc9-450e-aa76-fae39ee849d1",
    adjust_points={"points": 10, "reason": "Complimentary points"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str` — The ID of the target [loyalty account](entity:LoyaltyAccount).
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `AdjustLoyaltyPoints` request. 
Keys can be any valid string, but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**adjust_points:** `LoyaltyEventAdjustPointsParams` 

The points to add or subtract and the reason for the adjustment. To add points, specify a positive integer.
To subtract points, specify a negative integer.
    
</dd>
</dl>

<dl>
<dd>

**allow_negative_balance:** `typing.Optional[bool]` 

Indicates whether to allow a negative adjustment to result in a negative balance. If `true`, a negative
balance is allowed when subtracting points. If `false`, Square returns a `BAD_REQUEST` error when subtracting
the specified number of points would result in a negative balance. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Loyalty Programs
<details><summary><code>client.loyalty.programs.<a href="src/square/loyalty/programs/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of loyalty programs in the seller's account.
Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).


Replaced with [RetrieveLoyaltyProgram](api-endpoint:Loyalty-RetrieveLoyaltyProgram) when used with the keyword `main`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.programs.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.programs.<a href="src/square/loyalty/programs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword `main`.

Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.programs.get(
    program_id="program_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `str` — The ID of the loyalty program or the keyword `main`. Either value can be used to retrieve the single loyalty program that belongs to the seller.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.programs.<a href="src/square/loyalty/programs/client.py">calculate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculates the number of points a buyer can earn from a purchase. Applications might call this endpoint
to display the points to the buyer.

- If you are using the Orders API to manage orders, provide the `order_id` and (optional) `loyalty_account_id`.
Square reads the order to compute the points earned from the base loyalty program and an associated
[loyalty promotion](entity:LoyaltyPromotion).

- If you are not using the Orders API to manage orders, provide `transaction_amount_money` with the
purchase amount. Square uses this amount to calculate the points earned from the base loyalty program,
but not points earned from a loyalty promotion. For spend-based and visit-based programs, the `tax_mode`
setting of the accrual rule indicates how taxes should be treated for loyalty points accrual.
If the purchase qualifies for program points, call
[ListLoyaltyPromotions](api-endpoint:Loyalty-ListLoyaltyPromotions) and perform a client-side computation
to calculate whether the purchase also qualifies for promotion points. For more information, see
[Calculating promotion points](https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.programs.calculate(
    program_id="program_id",
    order_id="RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY",
    loyalty_account_id="79b807d2-d786-46a9-933b-918028d7a8c5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `str` — The ID of the [loyalty program](entity:LoyaltyProgram), which defines the rules for accruing points.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `typing.Optional[str]` 

The [order](entity:Order) ID for which to calculate the points.
Specify this field if your application uses the Orders API to process orders.
Otherwise, specify the `transaction_amount_money`.
    
</dd>
</dl>

<dl>
<dd>

**transaction_amount_money:** `typing.Optional[MoneyParams]` 

The purchase amount for which to calculate the points. 
Specify this field if your application does not use the Orders API to process orders.
Otherwise, specify the `order_id`.
    
</dd>
</dl>

<dl>
<dd>

**loyalty_account_id:** `typing.Optional[str]` 

The ID of the target [loyalty account](entity:LoyaltyAccount). Optionally specify this field
if your application uses the Orders API to process orders.

If specified, the `promotion_points` field in the response shows the number of points the buyer would
earn from the purchase. In this case, Square uses the account ID to determine whether the promotion's
`trigger_limit` (the maximum number of times that a buyer can trigger the promotion) has been reached.
If not specified, the `promotion_points` field shows the number of points the purchase qualifies
for regardless of the trigger limit.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Loyalty Rewards
<details><summary><code>client.loyalty.rewards.<a href="src/square/loyalty/rewards/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a loyalty reward. In the process, the endpoint does following:

- Uses the `reward_tier_id` in the request to determine the number of points
to lock for this reward.
- If the request includes `order_id`, it adds the reward and related discount to the order.

After a reward is created, the points are locked and
not available for the buyer to redeem another reward.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.rewards.create(
    reward={
        "loyalty_account_id": "5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd",
        "reward_tier_id": "e1b39225-9da5-43d1-a5db-782cdd8ad94f",
        "order_id": "RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY",
    },
    idempotency_key="18c2e5ea-a620-4b1f-ad60-7b167285e451",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reward:** `LoyaltyRewardParams` — The reward to create.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `CreateLoyaltyReward` request. 
Keys can be any valid string, but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.rewards.<a href="src/square/loyalty/rewards/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches for loyalty rewards. This endpoint accepts a request with no query filters and returns results for all loyalty accounts.
If you include a `query` object, `loyalty_account_id` is required and `status` is  optional.

If you know a reward ID, use the
[RetrieveLoyaltyReward](api-endpoint:Loyalty-RetrieveLoyaltyReward) endpoint.

Search results are sorted by `updated_at` in descending order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.loyalty.rewards.search(
    query={"loyalty_account_id": "5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd"},
    limit=10,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[SearchLoyaltyRewardsRequestLoyaltyRewardQueryParams]` 

The search criteria for the request. 
If empty, the endpoint retrieves all loyalty rewards in the loyalty program.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return in the response. The default value is 30.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to 
this endpoint. Provide this to retrieve the next set of 
results for the original query.
For more information, 
see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.rewards.<a href="src/square/loyalty/rewards/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a loyalty reward.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.rewards.get(
    reward_id="reward_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reward_id:** `str` — The ID of the [loyalty reward](entity:LoyaltyReward) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.rewards.<a href="src/square/loyalty/rewards/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a loyalty reward by doing the following:

- Returns the loyalty points back to the loyalty account.
- If an order ID was specified when the reward was created
(see [CreateLoyaltyReward](api-endpoint:Loyalty-CreateLoyaltyReward)),
it updates the order by removing the reward and related
discounts.

You cannot delete a reward that has reached the terminal state (REDEEMED).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.rewards.delete(
    reward_id="reward_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reward_id:** `str` — The ID of the [loyalty reward](entity:LoyaltyReward) to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.rewards.<a href="src/square/loyalty/rewards/client.py">redeem</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Redeems a loyalty reward.

The endpoint sets the reward to the `REDEEMED` terminal state.

If you are using your own order processing system (not using the
Orders API), you call this endpoint after the buyer paid for the
purchase.

After the reward reaches the terminal state, it cannot be deleted.
In other words, points used for the reward cannot be returned
to the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.rewards.redeem(
    reward_id="reward_id",
    idempotency_key="98adc7f7-6963-473b-b29c-f3c9cdd7d994",
    location_id="P034NEENMD09F",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reward_id:** `str` — The ID of the [loyalty reward](entity:LoyaltyReward) to redeem.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `RedeemLoyaltyReward` request. 
Keys can be any valid string, but must be unique for every request.
    
</dd>
</dl>

<dl>
<dd>

**location_id:** `str` — The ID of the [location](entity:Location) where the reward is redeemed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Loyalty Programs Promotions
<details><summary><code>client.loyalty.programs.promotions.<a href="src/square/loyalty/programs/promotions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the loyalty promotions associated with a [loyalty program](entity:LoyaltyProgram).
Results are sorted by the `created_at` date in descending order (newest to oldest).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.loyalty.programs.promotions.list(
    program_id="program_id",
    status="ACTIVE",
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `str` 

The ID of the base [loyalty program](entity:LoyaltyProgram). To get the program ID,
call [RetrieveLoyaltyProgram](api-endpoint:Loyalty-RetrieveLoyaltyProgram) using the `main` keyword.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[LoyaltyPromotionStatus]` 

The status to filter the results by. If a status is provided, only loyalty promotions
with the specified status are returned. Otherwise, all loyalty promotions associated with
the loyalty program are returned.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint.
Provide this cursor to retrieve the next page of results for your original request.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response.
The minimum value is 1 and the maximum value is 30. The default value is 30.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.programs.promotions.<a href="src/square/loyalty/programs/promotions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a loyalty promotion for a [loyalty program](entity:LoyaltyProgram). A loyalty promotion
enables buyers to earn points in addition to those earned from the base loyalty program.

This endpoint sets the loyalty promotion to the `ACTIVE` or `SCHEDULED` status, depending on the
`available_time` setting. A loyalty program can have a maximum of 10 loyalty promotions with an
`ACTIVE` or `SCHEDULED` status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.programs.promotions.create(
    program_id="program_id",
    loyalty_promotion={
        "name": "Tuesday Happy Hour Promo",
        "incentive": {
            "type": "POINTS_MULTIPLIER",
            "points_multiplier_data": {"multiplier": "3.0"},
        },
        "available_time": {
            "time_periods": [
                "BEGIN:VEVENT\nDTSTART:20220816T160000\nDURATION:PT2H\nRRULE:FREQ=WEEKLY;BYDAY=TU\nEND:VEVENT"
            ]
        },
        "trigger_limit": {"times": 1, "interval": "DAY"},
        "minimum_spend_amount_money": {"amount": 2000, "currency": "USD"},
        "qualifying_category_ids": ["XTQPYLR3IIU9C44VRCB3XD12"],
    },
    idempotency_key="ec78c477-b1c3-4899-a209-a4e71337c996",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `str` 

The ID of the [loyalty program](entity:LoyaltyProgram) to associate with the promotion.
To get the program ID, call [RetrieveLoyaltyProgram](api-endpoint:Loyalty-RetrieveLoyaltyProgram)
using the `main` keyword.
    
</dd>
</dl>

<dl>
<dd>

**loyalty_promotion:** `LoyaltyPromotionParams` — The loyalty promotion to create.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `str` 

A unique identifier for this request, which is used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.programs.promotions.<a href="src/square/loyalty/programs/promotions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a loyalty promotion.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.programs.promotions.get(
    program_id="program_id",
    promotion_id="promotion_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `str` 

The ID of the base [loyalty program](entity:LoyaltyProgram). To get the program ID,
call [RetrieveLoyaltyProgram](api-endpoint:Loyalty-RetrieveLoyaltyProgram) using the `main` keyword.
    
</dd>
</dl>

<dl>
<dd>

**promotion_id:** `str` — The ID of the [loyalty promotion](entity:LoyaltyPromotion) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.loyalty.programs.promotions.<a href="src/square/loyalty/programs/promotions/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a loyalty promotion. Use this endpoint to cancel an `ACTIVE` promotion earlier than the
end date, cancel an `ACTIVE` promotion when an end date is not specified, or cancel a `SCHEDULED` promotion.
Because updating a promotion is not supported, you can also use this endpoint to cancel a promotion before
you create a new one.

This endpoint sets the loyalty promotion to the `CANCELED` state
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.loyalty.programs.promotions.cancel(
    program_id="program_id",
    promotion_id="promotion_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `str` — The ID of the base [loyalty program](entity:LoyaltyProgram).
    
</dd>
</dl>

<dl>
<dd>

**promotion_id:** `str` 

The ID of the [loyalty promotion](entity:LoyaltyPromotion) to cancel. You can cancel a
promotion that has an `ACTIVE` or `SCHEDULED` status.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants CustomAttributeDefinitions
<details><summary><code>client.merchants.custom_attribute_definitions.<a href="src/square/merchants/custom_attribute_definitions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the merchant-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.
When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.merchants.custom_attribute_definitions.list(
    visibility_filter="ALL",
    limit=1,
    cursor="cursor",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**visibility_filter:** `typing.Optional[VisibilityFilter]` — Filters the `CustomAttributeDefinition` results by their `visibility` values.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory.
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint.
Provide this cursor to retrieve the next page of results for your original request.
For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.custom_attribute_definitions.<a href="src/square/merchants/custom_attribute_definitions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to define a custom attribute that can be associated with a merchant connecting to your application.
A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
for a custom attribute. After the definition is created, you can call
[UpsertMerchantCustomAttribute](api-endpoint:MerchantCustomAttributes-UpsertMerchantCustomAttribute) or
[BulkUpsertMerchantCustomAttributes](api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes)
to set the custom attribute for a merchant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.custom_attribute_definitions.create(
    custom_attribute_definition={
        "key": "alternative_seller_name",
        "schema": {
            "$ref": "https://developer-production-s.squarecdn.com/schemas/v1/common.json#squareup.common.String"
        },
        "name": "Alternative Merchant Name",
        "description": "This is the other name this merchant goes by.",
        "visibility": "VISIBILITY_READ_ONLY",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition to create. Note the following:
- With the exception of the `Selection` data type, the `schema` is specified as a simple URL to the JSON schema
definition hosted on the Square CDN. For more information, including supported values and constraints, see
[Supported data types](https://developer.squareup.com/docs/devtools/customattributes/overview#supported-data-types).
- `name` is required unless `visibility` is set to `VISIBILITY_HIDDEN`.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.custom_attribute_definitions.<a href="src/square/merchants/custom_attribute_definitions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.custom_attribute_definitions.get(
    key="key",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute definition to retrieve. If the requesting application
is not the definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the custom attribute definition, which is used for strongly consistent
reads to guarantee that you receive the most up-to-date data. When included in the request,
Square returns the specified version or a higher version if one exists. If the specified version
is higher than the current version, Square returns a `BAD_REQUEST` error.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.custom_attribute_definitions.<a href="src/square/merchants/custom_attribute_definitions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
`schema` for a `Selection` data type.
Only the definition owner can update a custom attribute definition.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.custom_attribute_definitions.update(
    key="key",
    custom_attribute_definition={
        "description": "Update the description as desired.",
        "visibility": "VISIBILITY_READ_ONLY",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to update.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition that contains the fields to update. This endpoint
supports sparse updates, so only new or changed fields need to be included in the request.
Only the following fields can be updated:
- `name`
- `description`
- `visibility`
- `schema` for a `Selection` data type. Only changes to the named options or the maximum number of allowed
selections are supported.
For more information, see
[Update a merchant custom attribute definition](https://developer.squareup.com/docs/merchant-custom-attributes-api/custom-attribute-definitions#update-custom-attribute-definition).
The version field must match the current version of the custom attribute definition to enable
[optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
If this is not important for your application, version can be set to -1. For any other values, the request fails with a BAD_REQUEST error.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.custom_attribute_definitions.<a href="src/square/merchants/custom_attribute_definitions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
Deleting a custom attribute definition also deletes the corresponding custom attribute from
the merchant.
Only the definition owner can delete a custom attribute definition.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.custom_attribute_definitions.delete(
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants CustomAttributes
<details><summary><code>client.merchants.custom_attributes.<a href="src/square/merchants/custom_attributes/client.py">batch_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes [custom attributes](entity:CustomAttribute) for a merchant as a bulk operation.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.custom_attributes.batch_delete(
    values={
        "id1": {"key": "alternative_seller_name"},
        "id2": {"key": "has_seen_tutorial"},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**values:** `typing.Dict[
    str,
    BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestParams,
]` 

The data used to update the `CustomAttribute` objects.
The keys must be unique and are used to map to the corresponding response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.custom_attributes.<a href="src/square/merchants/custom_attributes/client.py">batch_upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates [custom attributes](entity:CustomAttribute) for a merchant as a bulk operation.
Use this endpoint to set the value of one or more custom attributes for a merchant.
A custom attribute is based on a custom attribute definition in a Square seller account, which is
created using the [CreateMerchantCustomAttributeDefinition](api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition) endpoint.
This `BulkUpsertMerchantCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides a merchant ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.custom_attributes.batch_upsert(
    values={
        "id1": {
            "merchant_id": "DM7VKY8Q63GNP",
            "custom_attribute": {
                "key": "alternative_seller_name",
                "value": "Ultimate Sneaker Store",
            },
        },
        "id2": {
            "merchant_id": "DM7VKY8Q63GNP",
            "custom_attribute": {"key": "has_seen_tutorial", "value": True},
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**values:** `typing.Dict[
    str,
    BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestParams,
]` 

A map containing 1 to 25 individual upsert requests. For each request, provide an
arbitrary ID that is unique for this `BulkUpsertMerchantCustomAttributes` request and the
information needed to create or update a custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.custom_attributes.<a href="src/square/merchants/custom_attributes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the [custom attributes](entity:CustomAttribute) associated with a merchant.
You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.
When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.merchants.custom_attributes.list(
    merchant_id="merchant_id",
    visibility_filter="ALL",
    limit=1,
    cursor="cursor",
    with_definitions=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — The ID of the target [merchant](entity:Merchant).
    
</dd>
</dl>

<dl>
<dd>

**visibility_filter:** `typing.Optional[VisibilityFilter]` — Filters the `CustomAttributeDefinition` results by their `visibility` values.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory.
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.
The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint.
Provide this cursor to retrieve the next page of results for your original request. For more
information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**with_definitions:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each
custom attribute. Set this parameter to `true` to get the name and description of each custom
attribute, information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.custom_attributes.<a href="src/square/merchants/custom_attributes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a [custom attribute](entity:CustomAttribute) associated with a merchant.
You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.
To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.custom_attributes.get(
    merchant_id="merchant_id",
    key="key",
    with_definition=True,
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — The ID of the target [merchant](entity:Merchant).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to retrieve. This key must match the `key` of a custom
attribute definition in the Square seller account. If the requesting application is not the
definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**with_definition:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of
the custom attribute. Set this parameter to `true` to get the name and description of the custom
attribute, information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

The current version of the custom attribute, which is used for strongly consistent reads to
guarantee that you receive the most up-to-date data. When included in the request, Square
returns the specified version or a higher version if one exists. If the specified version is
higher than the current version, Square returns a `BAD_REQUEST` error.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.custom_attributes.<a href="src/square/merchants/custom_attributes/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates a [custom attribute](entity:CustomAttribute) for a merchant.
Use this endpoint to set the value of a custom attribute for a specified merchant.
A custom attribute is based on a custom attribute definition in a Square seller account, which
is created using the [CreateMerchantCustomAttributeDefinition](api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition) endpoint.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.custom_attributes.upsert(
    merchant_id="merchant_id",
    key="key",
    custom_attribute={"value": "Ultimate Sneaker Store"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — The ID of the target [merchant](entity:Merchant).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to create or update. This key must match the `key` of a
custom attribute definition in the Square seller account. If the requesting application is not
the definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute:** `CustomAttributeParams` 

The custom attribute to create or update, with the following fields:
- `value`. This value must conform to the `schema` specified by the definition.
For more information, see [Supported data types](https://developer.squareup.com/docs/devtools/customattributes/overview#supported-data-types).
- The version field must match the current version of the custom attribute definition to enable
[optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
If this is not important for your application, version can be set to -1. For any other values, the request fails with a BAD_REQUEST error.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. For more information,
see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.custom_attributes.<a href="src/square/merchants/custom_attributes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a [custom attribute](entity:CustomAttribute) associated with a merchant.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.merchants.custom_attributes.delete(
    merchant_id="merchant_id",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — The ID of the target [merchant](entity:Merchant).
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 

The key of the custom attribute to delete. This key must match the `key` of a custom
attribute definition in the Square seller account. If the requesting application is not the
definition owner, you must use the qualified key.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Orders CustomAttributeDefinitions
<details><summary><code>client.orders.custom_attribute_definitions.<a href="src/square/orders/custom_attribute_definitions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the order-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.

When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that
seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.orders.custom_attribute_definitions.list(
    visibility_filter="ALL",
    cursor="cursor",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**visibility_filter:** `typing.Optional[VisibilityFilter]` — Requests that all of the custom attributes be returned, or only those that are read-only or read-write.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint. 
Provide this cursor to retrieve the next page of results for your original request. 
For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory. 
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. 
The default value is 20.
For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.custom_attribute_definitions.<a href="src/square/orders/custom_attribute_definitions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an order-related custom attribute definition.  Use this endpoint to
define a custom attribute that can be associated with orders.

After creating a custom attribute definition, you can set the custom attribute for orders
in the Square seller account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.custom_attribute_definitions.create(
    custom_attribute_definition={
        "key": "cover-count",
        "schema": {
            "$ref": "https://developer-production-s.squarecdn.com/schemas/v1/common.json#squareup.common.Number"
        },
        "name": "Cover count",
        "description": "The number of people seated at a table",
        "visibility": "VISIBILITY_READ_WRITE_VALUES",
    },
    idempotency_key="IDEMPOTENCY_KEY",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition to create. Note the following:
- With the exception of the `Selection` data type, the `schema` is specified as a simple URL to the JSON schema
definition hosted on the Square CDN. For more information, including supported values and constraints, see
[Specifying the schema](https://developer.squareup.com/docs/customer-custom-attributes-api/custom-attribute-definitions#specify-schema).
- If provided, `name` must be unique (case-sensitive) across all visible customer-related custom attribute definitions for the seller.
- All custom attributes are visible in exported customer data, including those set to `VISIBILITY_HIDDEN`.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. 
For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.custom_attribute_definitions.<a href="src/square/orders/custom_attribute_definitions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an order-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.

To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.custom_attribute_definitions.get(
    key="key",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control, include this optional field and specify the current version of the custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.custom_attribute_definitions.<a href="src/square/orders/custom_attribute_definitions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an order-related custom attribute definition for a Square seller account.

Only the definition owner can update a custom attribute definition. Note that sellers can view all custom attributes in exported customer data, including those set to `VISIBILITY_HIDDEN`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.custom_attribute_definitions.update(
    key="key",
    custom_attribute_definition={
        "key": "cover-count",
        "visibility": "VISIBILITY_READ_ONLY",
        "version": 1,
    },
    idempotency_key="IDEMPOTENCY_KEY",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to update.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_definition:** `CustomAttributeDefinitionParams` 

The custom attribute definition that contains the fields to update. This endpoint supports sparse updates, 
so only new or changed fields need to be included in the request.  For more information, see 
[Updatable definition fields](https://developer.squareup.com/docs/orders-custom-attributes-api/custom-attribute-definitions#updatable-definition-fields).

To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency) control, include the optional `version` field and specify the current version of the custom attribute definition.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. 
For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.custom_attribute_definitions.<a href="src/square/orders/custom_attribute_definitions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an order-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.

Only the definition owner can delete a custom attribute definition.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.custom_attribute_definitions.delete(
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` — The key of the custom attribute definition to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Orders CustomAttributes
<details><summary><code>client.orders.custom_attributes.<a href="src/square/orders/custom_attributes/client.py">batch_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes order [custom attributes](entity:CustomAttribute) as a bulk operation.

Use this endpoint to delete one or more custom attributes from one or more orders.
A custom attribute is based on a custom attribute definition in a Square seller account.  (To create a
custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

This `BulkDeleteOrderCustomAttributes` endpoint accepts a map of 1 to 25 individual delete
requests and returns a map of individual delete responses. Each delete request has a unique ID
and provides an order ID and custom attribute. Each delete response is returned with the ID
of the corresponding request.

To delete a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.custom_attributes.batch_delete(
    values={
        "cover-count": {
            "key": "cover-count",
            "order_id": "7BbXGEIWNldxAzrtGf9GPVZTwZ4F",
        },
        "table-number": {
            "key": "table-number",
            "order_id": "7BbXGEIWNldxAzrtGf9GPVZTwZ4F",
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**values:** `typing.Dict[
    str, BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeParams
]` — A map of requests that correspond to individual delete operations for custom attributes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.custom_attributes.<a href="src/square/orders/custom_attributes/client.py">batch_upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates order [custom attributes](entity:CustomAttribute) as a bulk operation.

Use this endpoint to delete one or more custom attributes from one or more orders.
A custom attribute is based on a custom attribute definition in a Square seller account.  (To create a
custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

This `BulkUpsertOrderCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides an order ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.custom_attributes.batch_upsert(
    values={
        "cover-count": {
            "custom_attribute": {
                "key": "cover-count",
                "value": "6",
                "version": 2,
            },
            "order_id": "7BbXGEIWNldxAzrtGf9GPVZTwZ4F",
        },
        "table-number": {
            "custom_attribute": {
                "key": "table-number",
                "value": "11",
                "version": 4,
            },
            "order_id": "7BbXGEIWNldxAzrtGf9GPVZTwZ4F",
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**values:** `typing.Dict[
    str, BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeParams
]` — A map of requests that correspond to individual upsert operations for custom attributes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.custom_attributes.<a href="src/square/orders/custom_attributes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the [custom attributes](entity:CustomAttribute) associated with an order.

You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.

When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.orders.custom_attributes.list(
    order_id="order_id",
    visibility_filter="ALL",
    cursor="cursor",
    limit=1,
    with_definitions=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the target [order](entity:Order).
    
</dd>
</dl>

<dl>
<dd>

**visibility_filter:** `typing.Optional[VisibilityFilter]` — Requests that all of the custom attributes be returned, or only those that are read-only or read-write.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

The cursor returned in the paged response from the previous call to this endpoint. 
Provide this cursor to retrieve the next page of results for your original request. 
For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to return in a single paged response. This limit is advisory. 
The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. 
The default value is 20.
For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    
</dd>
</dl>

<dl>
<dd>

**with_definitions:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each
custom attribute. Set this parameter to `true` to get the name and description of each custom attribute, 
information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.custom_attributes.<a href="src/square/orders/custom_attributes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a [custom attribute](entity:CustomAttribute) associated with an order.

You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.

To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.custom_attributes.get(
    order_id="order_id",
    custom_attribute_key="custom_attribute_key",
    version=1,
    with_definition=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the target [order](entity:Order).
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_key:** `str` 

The key of the custom attribute to retrieve.  This key must match the key of an
existing custom attribute definition.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 

To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control, include this optional field and specify the current version of the custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**with_definition:** `typing.Optional[bool]` 

Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each 
custom attribute. Set this parameter to `true` to get the name and description of each custom attribute, 
information about the data type, or other definition details. The default value is `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.custom_attributes.<a href="src/square/orders/custom_attributes/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates a [custom attribute](entity:CustomAttribute) for an order.

Use this endpoint to set the value of a custom attribute for a specific order.
A custom attribute is based on a custom attribute definition in a Square seller account. (To create a
custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.custom_attributes.upsert(
    order_id="order_id",
    custom_attribute_key="custom_attribute_key",
    custom_attribute={"key": "table-number", "value": "42", "version": 1},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the target [order](entity:Order).
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_key:** `str` 

The key of the custom attribute to create or update.  This key must match the key 
of an existing custom attribute definition.
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute:** `CustomAttributeParams` 

The custom attribute to create or update, with the following fields:

- `value`. This value must conform to the `schema` specified by the definition. 
For more information, see [Value data types](https://developer.squareup.com/docs/customer-custom-attributes-api/custom-attributes#value-data-types).

- `version`. To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
control, include this optional field and specify the current version of the custom attribute.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

A unique identifier for this request, used to ensure idempotency. 
For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.custom_attributes.<a href="src/square/orders/custom_attributes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a [custom attribute](entity:CustomAttribute) associated with a customer profile.

To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.orders.custom_attributes.delete(
    order_id="order_id",
    custom_attribute_key="custom_attribute_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The ID of the target [order](entity:Order).
    
</dd>
</dl>

<dl>
<dd>

**custom_attribute_key:** `str` 

The key of the custom attribute to delete.  This key must match the key of an
existing custom attribute definition.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TeamMembers WageSetting
<details><summary><code>client.team_members.wage_setting.<a href="src/square/team_members/wage_setting/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a `WageSetting` object for a team member specified
by `TeamMember.id`. For more information, see
[Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).

Square recommends using [RetrieveTeamMember](api-endpoint:Team-RetrieveTeamMember) or [SearchTeamMembers](api-endpoint:Team-SearchTeamMembers)
to get this information directly from the `TeamMember.wage_setting` field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team_members.wage_setting.get(
    team_member_id="team_member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member for which to retrieve the wage setting.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.team_members.wage_setting.<a href="src/square/team_members/wage_setting/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates a `WageSetting` object. The object is created if a
`WageSetting` with the specified `team_member_id` doesn't exist. Otherwise,
it fully replaces the `WageSetting` object for the team member.
The `WageSetting` is returned on a successful update. For more information, see
[Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting).

Square recommends using [CreateTeamMember](api-endpoint:Team-CreateTeamMember) or [UpdateTeamMember](api-endpoint:Team-UpdateTeamMember)
to manage the `TeamMember.wage_setting` field directly.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.team_members.wage_setting.update(
    team_member_id="team_member_id",
    wage_setting={
        "job_assignments": [
            {
                "job_title": "Manager",
                "pay_type": "SALARY",
                "annual_rate": {"amount": 3000000, "currency": "USD"},
                "weekly_hours": 40,
            },
            {
                "job_title": "Cashier",
                "pay_type": "HOURLY",
                "hourly_rate": {"amount": 2000, "currency": "USD"},
            },
        ],
        "is_overtime_exempt": True,
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_member_id:** `str` — The ID of the team member for which to update the `WageSetting` object.
    
</dd>
</dl>

<dl>
<dd>

**wage_setting:** `WageSettingParams` 

The complete `WageSetting` object. For all job assignments, specify one of the following:
- `job_id` (recommended) - If needed, call [ListJobs](api-endpoint:Team-ListJobs) to get a list of all jobs.
Requires Square API version 2024-12-18 or later.
- `job_title` - Use the exact, case-sensitive spelling of an existing title unless you want to create a new job.
This value is ignored if `job_id` is also provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Terminal Actions
<details><summary><code>client.terminal.actions.<a href="src/square/terminal/actions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Terminal action request and sends it to the specified device.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.actions.create(
    idempotency_key="thahn-70e75c10-47f7-4ab6-88cc-aaa4076d065e",
    action={
        "device_id": "{{DEVICE_ID}}",
        "deadline_duration": "PT5M",
        "type": "SAVE_CARD",
        "save_card_options": {
            "customer_id": "{{CUSTOMER_ID}}",
            "reference_id": "user-id-1",
        },
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `CreateAction` request. Keys can be any valid string
but must be unique for every `CreateAction` request.

See [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more
information.
    
</dd>
</dl>

<dl>
<dd>

**action:** `TerminalActionParams` — The Action to create.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.actions.<a href="src/square/terminal/actions/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a filtered list of Terminal action requests created by the account making the request. Terminal action requests are available for 30 days.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.terminal.actions.search(
    query={
        "filter": {"created_at": {"start_at": "2022-04-01T00:00:00.000Z"}},
        "sort": {"sort_order": "DESC"},
    },
    limit=2,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[TerminalActionQueryParams]` 

Queries terminal actions based on given conditions and sort order.
Leaving this unset will return all actions with the default sort order.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for the original query.
See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more
information.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of results returned for a single request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.actions.<a href="src/square/terminal/actions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a Terminal action request by `action_id`. Terminal action requests are available for 30 days.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.actions.get(
    action_id="action_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `str` — Unique ID for the desired `TerminalAction`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.actions.<a href="src/square/terminal/actions/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a Terminal action request if the status of the request permits it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.actions.cancel(
    action_id="action_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `str` — Unique ID for the desired `TerminalAction`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Terminal Checkouts
<details><summary><code>client.terminal.checkouts.<a href="src/square/terminal/checkouts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Terminal checkout request and sends it to the specified device to take a payment
for the requested amount.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.checkouts.create(
    idempotency_key="28a0c3bc-7839-11ea-bc55-0242ac130003",
    checkout={
        "amount_money": {"amount": 2610, "currency": "USD"},
        "reference_id": "id11572",
        "note": "A brief note",
        "device_options": {"device_id": "dbb5d83a-7838-11ea-bc55-0242ac130003"},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `CreateCheckout` request. Keys can be any valid string but
must be unique for every `CreateCheckout` request.

See [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**checkout:** `TerminalCheckoutParams` — The checkout to create.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.checkouts.<a href="src/square/terminal/checkouts/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a filtered list of Terminal checkout requests created by the application making the request. Only Terminal checkout requests created for the merchant scoped to the OAuth token are returned. Terminal checkout requests are available for 30 days.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.terminal.checkouts.search(
    query={"filter": {"status": "COMPLETED"}},
    limit=2,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[TerminalCheckoutQueryParams]` 

Queries Terminal checkouts based on given conditions and the sort order.
Leaving these unset returns all checkouts with the default sort order.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the number of results returned for a single request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.checkouts.<a href="src/square/terminal/checkouts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a Terminal checkout request by `checkout_id`. Terminal checkout requests are available for 30 days.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.checkouts.get(
    checkout_id="checkout_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**checkout_id:** `str` — The unique ID for the desired `TerminalCheckout`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.checkouts.<a href="src/square/terminal/checkouts/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a Terminal checkout request if the status of the request permits it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.checkouts.cancel(
    checkout_id="checkout_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**checkout_id:** `str` — The unique ID for the desired `TerminalCheckout`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Terminal Refunds
<details><summary><code>client.terminal.refunds.<a href="src/square/terminal/refunds/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a request to refund an Interac payment completed on a Square Terminal. Refunds for Interac payments on a Square Terminal are supported only for Interac debit cards in Canada. Other refunds for Terminal payments should use the Refunds API. For more information, see [Refunds API](api:Refunds).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.refunds.create(
    idempotency_key="402a640b-b26f-401f-b406-46f839590c04",
    refund={
        "payment_id": "5O5OvgkcNUhl7JBuINflcjKqUzXZY",
        "amount_money": {"amount": 111, "currency": "CAD"},
        "reason": "Returning items",
        "device_id": "f72dfb8e-4d65-4e56-aade-ec3fb8d33291",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` 

A unique string that identifies this `CreateRefund` request. Keys can be any valid string but
must be unique for every `CreateRefund` request.

See [Idempotency keys](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) for more information.
    
</dd>
</dl>

<dl>
<dd>

**refund:** `typing.Optional[TerminalRefundParams]` — The refund to create.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.refunds.<a href="src/square/terminal/refunds/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request. Terminal refund requests are available for 30 days.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.terminal.refunds.search(
    query={"filter": {"status": "COMPLETED"}},
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `typing.Optional[TerminalRefundQueryParams]` 

Queries the Terminal refunds based on given conditions and the sort order. Calling
`SearchTerminalRefunds` without an explicit query parameter returns all available
refunds with the default sort order.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this cursor to retrieve the next set of results for the original query.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limits the number of results returned for a single request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.refunds.<a href="src/square/terminal/refunds/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an Interac Terminal refund object by ID. Terminal refund objects are available for 30 days.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.refunds.get(
    terminal_refund_id="terminal_refund_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**terminal_refund_id:** `str` — The unique ID for the desired `TerminalRefund`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.terminal.refunds.<a href="src/square/terminal/refunds/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.terminal.refunds.cancel(
    terminal_refund_id="terminal_refund_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**terminal_refund_id:** `str` — The unique ID for the desired `TerminalRefund`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks EventTypes
<details><summary><code>client.webhooks.event_types.<a href="src/square/webhooks/event_types/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all webhook event types that can be subscribed to.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.webhooks.event_types.list(
    api_version="api_version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — The API version for which to list event types. Setting this field overrides the default version used by the application.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks Subscriptions
<details><summary><code>client.webhooks.subscriptions.<a href="src/square/webhooks/subscriptions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all webhook subscriptions owned by your application.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.webhooks.subscriptions.list(
    cursor="cursor",
    include_disabled=True,
    sort_order="DESC",
    limit=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 

A pagination cursor returned by a previous call to this endpoint.
Provide this to retrieve the next set of results for your original query.

For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    
</dd>
</dl>

<dl>
<dd>

**include_disabled:** `typing.Optional[bool]` 

Includes disabled [Subscription](entity:WebhookSubscription)s.
By default, all enabled [Subscription](entity:WebhookSubscription)s are returned.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SortOrder]` 

Sorts the returned list by when the [Subscription](entity:WebhookSubscription) was created with the specified order.
This field defaults to ASC.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The maximum number of results to be returned in a single page.
It is possible to receive fewer results than the specified limit on a given page.
The default value of 100 is also the maximum allowed value.

Default: 100
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.subscriptions.<a href="src/square/webhooks/subscriptions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a webhook subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.webhooks.subscriptions.create(
    idempotency_key="63f84c6c-2200-4c99-846c-2670a1311fbf",
    subscription={
        "name": "Example Webhook Subscription",
        "event_types": ["payment.created", "payment.updated"],
        "notification_url": "https://example-webhook-url.com",
        "api_version": "2021-12-15",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription:** `WebhookSubscriptionParams` — The [Subscription](entity:WebhookSubscription) to create.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique string that identifies the [CreateWebhookSubscription](api-endpoint:WebhookSubscriptions-CreateWebhookSubscription) request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.subscriptions.<a href="src/square/webhooks/subscriptions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a webhook subscription identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.webhooks.subscriptions.get(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.subscriptions.<a href="src/square/webhooks/subscriptions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a webhook subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.webhooks.subscriptions.update(
    subscription_id="subscription_id",
    subscription={
        "name": "Updated Example Webhook Subscription",
        "enabled": False,
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update.
    
</dd>
</dl>

<dl>
<dd>

**subscription:** `typing.Optional[WebhookSubscriptionParams]` — The [Subscription](entity:WebhookSubscription) to update.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.subscriptions.<a href="src/square/webhooks/subscriptions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a webhook subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.webhooks.subscriptions.delete(
    subscription_id="subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.subscriptions.<a href="src/square/webhooks/subscriptions/client.py">update_signature_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a webhook subscription by replacing the existing signature key with a new one.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.webhooks.subscriptions.update_signature_key(
    subscription_id="subscription_id",
    idempotency_key="ed80ae6b-0654-473b-bbab-a39aee89a60d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique string that identifies the [UpdateWebhookSubscriptionSignatureKey](api-endpoint:WebhookSubscriptions-UpdateWebhookSubscriptionSignatureKey) request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.subscriptions.<a href="src/square/webhooks/subscriptions/client.py">test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tests a webhook subscription by sending a test event to the notification URL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
client.webhooks.subscriptions.test(
    subscription_id="subscription_id",
    event_type="payment.created",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**subscription_id:** `str` — [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to test.
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[str]` 

The event type that will be used to test the [Subscription](entity:WebhookSubscription). The event type must be
contained in the list of event types in the [Subscription](entity:WebhookSubscription).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

