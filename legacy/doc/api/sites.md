# Sites

```python
sites_api = client.sites
```

## Class Name

`SitesApi`


# List Sites

Lists the Square Online sites that belong to a seller. Sites are listed in descending order by the `created_at` date.

__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

```python
def list_sites(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List Sites Response`](../../doc/models/list-sites-response.md).

## Example Usage

```python
result = sites_api.list_sites()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

