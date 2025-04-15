
# HttpResponse

Http response received.

## Parameters

| Name | Type | Description |
|  --- | --- | --- |
| status_code | int | The status code returned by the server. |
| reason_phrase | str | The reason phrase returned by the server. |
| headers | dict | Response headers. |
| text | str | Response body. |
| request | [`HttpRequest`](http-request.md) | The request that resulted in this response. |

