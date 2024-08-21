# Bank Accounts

```python
bank_accounts_api = client.bank_accounts
```

## Class Name

`BankAccountsApi`

## Methods

* [List Bank Accounts](../../doc/api/bank-accounts.md#list-bank-accounts)
* [Get Bank Account by V1 Id](../../doc/api/bank-accounts.md#get-bank-account-by-v1-id)
* [Get Bank Account](../../doc/api/bank-accounts.md#get-bank-account)


# List Bank Accounts

Returns a list of [BankAccount](../../doc/models/bank-account.md) objects linked to a Square account.

```python
def list_bank_accounts(self,
                      cursor=None,
                      limit=None,
                      location_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `str` | Query, Optional | The pagination cursor returned by a previous call to this endpoint.<br>Use it in the next `ListBankAccounts` request to retrieve the next set<br>of results.<br><br>See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. |
| `limit` | `int` | Query, Optional | Upper limit on the number of bank accounts to return in the response.<br>Currently, 1000 is the largest supported limit. You can specify a limit<br>of up to 1000 bank accounts. This is also the default limit. |
| `location_id` | `str` | Query, Optional | Location ID. You can specify this optional filter<br>to retrieve only the linked bank accounts belonging to a specific location. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Bank Accounts Response`](../../doc/models/list-bank-accounts-response.md).

## Example Usage

```python
result = bank_accounts_api.list_bank_accounts()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Bank Account by V1 Id

Returns details of a [BankAccount](../../doc/models/bank-account.md) identified by V1 bank account ID.

```python
def get_bank_account_by_v1_id(self,
                             v1_bank_account_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v1_bank_account_id` | `str` | Template, Required | Connect V1 ID of the desired `BankAccount`. For more information, see<br>[Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Get Bank Account by V1 Id Response`](../../doc/models/get-bank-account-by-v1-id-response.md).

## Example Usage

```python
v1_bank_account_id = 'v1_bank_account_id8'

result = bank_accounts_api.get_bank_account_by_v1_id(v1_bank_account_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Bank Account

Returns details of a [BankAccount](../../doc/models/bank-account.md)
linked to a Square account.

```python
def get_bank_account(self,
                    bank_account_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_id` | `str` | Template, Required | Square-issued ID of the desired `BankAccount`. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Get Bank Account Response`](../../doc/models/get-bank-account-response.md).

## Example Usage

```python
bank_account_id = 'bank_account_id0'

result = bank_accounts_api.get_bank_account(bank_account_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

