# Bank Accounts

```python
bank_accounts_api = client.bank_accounts
```

## Class Name

`BankAccountsApi`

## Methods

* [List Bank Accounts](/doc/bank-accounts.md#list-bank-accounts)
* [Get Bank Account by V1 Id](/doc/bank-accounts.md#get-bank-account-by-v1-id)
* [Get Bank Account](/doc/bank-accounts.md#get-bank-account)

## List Bank Accounts

Returns a list of [BankAccount](#type-bankaccount) objects linked to a Square account. 
For more information, see 
[Bank Accounts API](https://developer.squareup.com/docs/docs/bank-accounts-api).

```python
def list_bank_accounts(self,
                      cursor=None,
                      limit=None,
                      location_id=None)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cursor` | `string` | Query, Optional | The pagination cursor returned by a previous call to this endpoint.<br>Use it in the next `ListBankAccounts` request to retrieve the next set <br>of results.<br><br>See the [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination) guide for more information. |
| `limit` | `int` | Query, Optional | Upper limit on the number of bank accounts to return in the response. <br>Currently, 1000 is the largest supported limit. You can specify a limit <br>of up to 1000 bank accounts. This is also the default limit. |
| `location_id` | `string` | Query, Optional | Location ID. You can specify this optional filter <br>to retrieve only the linked bank accounts belonging to a specific location. |

### Response Type

[`List Bank Accounts Response`](/doc/models/list-bank-accounts-response.md)

### Example Usage

```python
cursor = 'cursor6'
limit = 172
location_id = 'location_id4'

result = bank_accounts_api.list_bank_accounts(cursor, limit, location_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Bank Account by V1 Id

Returns details of a [BankAccount](#type-bankaccount) identified by V1 bank account ID. 
For more information, see 
[Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-the-v1-bank-accounts-api).

```python
def get_bank_account_by_v1_id(self,
                             v1_bank_account_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v1_bank_account_id` | `string` | Template, Required | Connect V1 ID of the desired `BankAccount`. For more information, see <br>[Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api). |

### Response Type

[`Get Bank Account by V1 Id Response`](/doc/models/get-bank-account-by-v1-id-response.md)

### Example Usage

```python
v1_bank_account_id = 'v1_bank_account_id8'

result = bank_accounts_api.get_bank_account_by_v1_id(v1_bank_account_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Get Bank Account

Returns details of a [BankAccount](#type-bankaccount) 
linked to a Square account. For more information, see 
[Bank Accounts API](https://developer.squareup.com/docs/docs/bank-accounts-api).

```python
def get_bank_account(self,
                    bank_account_id)
```

### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_id` | `string` | Template, Required | Square-issued ID of the desired `BankAccount`. |

### Response Type

[`Get Bank Account Response`](/doc/models/get-bank-account-response.md)

### Example Usage

```python
bank_account_id = 'bank_account_id0'

result = bank_accounts_api.get_bank_account(bank_account_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

