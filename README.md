# Square Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fsquare%2Fsquare-python-sdk)
[![pypi](https://img.shields.io/pypi/v/squareup)](https://pypi.org/project/squareup)

The Square Python library provides convenient access to the Square API from Python.

## Installation

```sh
pip install squareup
```

## Requirements

Use of the Square Python SDK requires:

* Python 3.8+

## Usage

Instantiate and use the client with the following:

```python
from square import Square

client = Square(
    # This is the default and can be omitted.
    token=os.environ.get("SQUARE_TOKEN"),
)
client.payments.create(
    source_id="ccof:GaJGNaZa8x4OgDJn4GB",
    idempotency_key="7b0f3ec5-086a-4871-8f13-3c81b3875218",
    amount_money={
        "amount": 1000,
        "currency": "USD"
    },
    app_fee_money={
        "amount": 10,
        "currency": "USD"
    },
    autocomplete=True,
    customer_id="W92WH6P11H4Z77CTET0RNTGFW8",
    location_id="L88917AVBK2S5",
    reference_id="123456",
    note="Brief description"
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from square import AsyncSquare

async def main() -> None:
    client = AsyncSquare(
        # This is the default and can be omitted.
        token=os.environ.get("SQUARE_TOKEN"),
    )
    await client.payments.create(
        source_id="ccof:GaJGNaZa8x4OgDJn4GB",
        idempotency_key="7b0f3ec5-086a-4871-8f13-3c81b3875218",
        amount_money={
            "amount": 1000,
            "currency": "USD"
        },
        app_fee_money={
            "amount": 10,
            "currency": "USD"
        },
        autocomplete=True,
        customer_id="W92WH6P11H4Z77CTET0RNTGFW8",
        location_id="L88917AVBK2S5",
        reference_id="123456",
        note="Brief description"
    )


asyncio.run(main())
```

## Legacy SDK

While the new SDK has a lot of improvements, we at Square understand that it takes time
to upgrade when there are breaking changes. To make the migration easier, the old SDK
is published as `squareup_legacy` so that the two SDKs can be used side-by-side in the
same project.

Check out the [example](./example/README.md) for a full demonstration, but the gist is
shown below:

```python
from square import Square
from square_legacy.client import Client as LegacySquare


def main():
    client = Square(token=os.environ.get("SQUARE_TOKEN"))
    legacy_client = LegacySquare(access_token=os.environ.get("SQUARE_TOKEN"))

    ...
```

We recommend migrating to the new SDK using the following steps:

1. Upgrade the PyPi package to ^42.0.0
2. Run `pip install squareup_legacy`
3. Search and replace all requires and imports from `square` to `square_legacy`
4. Gradually move over to use the new SDK by importing it from the `square` module

## Versioning

By default, the SDK is pinned to the latest version. If you would like
to override this version you can specify it like so:

```python
client = Square(
    version="2025-03-19"
)
```

## Automatic Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used
as generators for the underlying object.

```python
from square import Square

client = Square()
response = client.payments.list()
for item in response:
    yield item
# Alternatively, you can paginate page-by-page.
for page in response.iter_pages():
    yield page
```

## File Uploads

Files are uploaded with the [File](./src/square/core/file.py) type, which is constructed as a tuple in
a variety of formats. You can customize the filename and `Content-Type` of the individual `multipart/form-data`
part like so:

```python
invoice_pdf = client.invoices.create_invoice_attachment(
    invoice_id="inv:0-ChA4-3sU9GPd-uOC3HgvFjMWEL4N",
    image_file=(
         os.path.basename(pdf_filepath), # The filename to include in the `multipart/form-data` part.
         open(pdf_filepath, "rb"),       # The file stream, read as binary data.
         "application/pdf"               # The Content-Type for this particular file.
    ),
    request={
        "idempotency_key": str(uuid.uuid4()),
        "description": f"Invoice-{pdf_filepath}",
    }
)
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of
the following error will be thrown.

```python
from square.core.api_error import ApiError

try:
    client.payments.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Webhook Signature Verification

The SDK provides utility methods that allow you to verify webhook signatures and ensure
that all webhook events originate from Square. The `verify_signature` method will verify
the signature.

```python
from square.utils.webhooks_helper import verify_signature

is_valid = verify_signature(
    request_body=request_body,
    signature_header=request.headers['x-square-hmacsha256-signature'],
    signature_key="YOUR_SIGNATURE_KEY",
    notification_url="https://example.com/webhook", # The URL where event notifications are sent.
)
```

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retriable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
from square.core.request_options import RequestOptions

client.payments.create(
    ...,
    request_options=RequestOptions(
        max_retries=1
    )
)
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from square import Square

client = Square(
    ...,
    timeout=20.0,
)

# Override timeout for a specific method
client.payments.create(
    ...,
    request_options=RequestOptions(
        timeout_in_seconds=20
    )
)
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases
include support for proxies and transports.

```python
import httpx
from square import Square

client = Square(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
