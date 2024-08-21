# O Auth

```python
o_auth_api = client.o_auth
```

## Class Name

`OAuthApi`

## Methods

* [Revoke Token](../../doc/api/o-auth.md#revoke-token)
* [Obtain Token](../../doc/api/o-auth.md#obtain-token)
* [Retrieve Token Status](../../doc/api/o-auth.md#retrieve-token-status)


# Revoke Token

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

:information_source: **Note** This endpoint does not require authentication.

```python
def revoke_token(self,
                body,
                authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Revoke Token Request`](../../doc/models/revoke-token-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| `authorization` | `str` | Header, Required | Client APPLICATION_SECRET |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Revoke Token Response`](../../doc/models/revoke-token-response.md).

## Example Usage

```python
body = {
    'client_id': 'CLIENT_ID',
    'access_token': 'ACCESS_TOKEN'
}

authorization = 'Client CLIENT_SECRET'

result = o_auth_api.revoke_token(
    body,
    authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Obtain Token

Returns an OAuth access token and a refresh token unless the
`short_lived` parameter is set to `true`, in which case the endpoint
returns only an access token.

The `grant_type` parameter specifies the type of OAuth request. If
`grant_type` is `authorization_code`, you must include the authorization
code you received when a seller granted you authorization. If `grant_type`
is `refresh_token`, you must provide a valid refresh token. If you're using
an old version of the Square APIs (prior to March 13, 2019), `grant_type`
can be `migration_token` and you must provide a valid migration token.

You can use the `scopes` parameter to limit the set of permissions granted
to the access token and refresh token. You can use the `short_lived` parameter
to create an access token that expires in 24 hours.

__Note:__ OAuth tokens should be encrypted and stored on a secure server.
Application clients should never interact directly with OAuth tokens.

:information_source: **Note** This endpoint does not require authentication.

```python
def obtain_token(self,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Obtain Token Request`](../../doc/models/obtain-token-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Obtain Token Response`](../../doc/models/obtain-token-response.md).

## Example Usage

```python
body = {
    'client_id': 'APPLICATION_ID',
    'grant_type': 'authorization_code',
    'client_secret': 'APPLICATION_SECRET',
    'code': 'CODE_FROM_AUTHORIZE'
}

result = o_auth_api.obtain_token(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Token Status

Returns information about an [OAuth access token](https://developer.squareup.com/docs/build-basics/access-tokens#get-an-oauth-access-token) or an application’s [personal access token](https://developer.squareup.com/docs/build-basics/access-tokens#get-a-personal-access-token).

Add the access token to the Authorization header of the request.

__Important:__ The `Authorization` header you provide to this endpoint must have the following format:

```
Authorization: Bearer ACCESS_TOKEN
```

where `ACCESS_TOKEN` is a
[valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

If the access token is expired or not a valid access token, the endpoint returns an `UNAUTHORIZED` error.

```python
def retrieve_token_status(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Token Status Response`](../../doc/models/retrieve-token-status-response.md).

## Example Usage

```python
result = o_auth_api.retrieve_token_status()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

