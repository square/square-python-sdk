# Snippets

```python
snippets_api = client.snippets
```

## Class Name

`SnippetsApi`

## Methods

* [Delete Snippet](../../doc/api/snippets.md#delete-snippet)
* [Retrieve Snippet](../../doc/api/snippets.md#retrieve-snippet)
* [Upsert Snippet](../../doc/api/snippets.md#upsert-snippet)


# Delete Snippet

Removes your snippet from a Square Online site.

You can call [ListSites](../../doc/api/sites.md#list-sites) to get the IDs of the sites that belong to a seller.

__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

```python
def delete_snippet(self,
                  site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `str` | Template, Required | The ID of the site that contains the snippet. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Delete Snippet Response`](../../doc/models/delete-snippet-response.md).

## Example Usage

```python
site_id = 'site_id6'

result = snippets_api.delete_snippet(site_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retrieve Snippet

Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

You can call [ListSites](../../doc/api/sites.md#list-sites) to get the IDs of the sites that belong to a seller.

__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

```python
def retrieve_snippet(self,
                    site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `str` | Template, Required | The ID of the site that contains the snippet. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Retrieve Snippet Response`](../../doc/models/retrieve-snippet-response.md).

## Example Usage

```python
site_id = 'site_id6'

result = snippets_api.retrieve_snippet(site_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upsert Snippet

Adds a snippet to a Square Online site or updates the existing snippet on the site.
The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.

You can call [ListSites](../../doc/api/sites.md#list-sites) to get the IDs of the sites that belong to a seller.

__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

```python
def upsert_snippet(self,
                  site_id,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `str` | Template, Required | The ID of the site where you want to add or update the snippet. |
| `body` | [`Upsert Snippet Request`](../../doc/models/upsert-snippet-request.md) | Body, Required | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Upsert Snippet Response`](../../doc/models/upsert-snippet-response.md).

## Example Usage

```python
site_id = 'site_id6'

body = {
    'snippet': {
        'content': '<script>var js = 1;</script>'
    }
}

result = snippets_api.upsert_snippet(
    site_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

