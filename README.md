# Square Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fsquare%2Fsquare-python-sdk)
[![pypi](https://img.shields.io/pypi/v/squareup)](https://pypi.python.org/pypi/squareup)

The Square Python library provides convenient access to the Square API from Python.

## Requirements

Use of the Python SDK requires:

* Python 3 version 3.7 or higher

## Installation

```sh
pip install squareup
```

## Reference

A full reference for this library is available [here](./reference.md).

## Quickstart

For more information, see [Square Python SDK Quickstart](https://developer.squareup.com/docs/sdks/python/quick-start).

## Usage

Instantiate and use the client with the following:

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

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from square import AsyncSquare

client = AsyncSquare(
    token="YOUR_TOKEN",
)


async def main() -> None:
    await client.payments.create(
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


asyncio.run(main())
```

## Tests

First, clone the repo locally and `cd` into the directory.

```sh
git clone https://github.com/square/square-python-sdk.git
cd square-python-sdk
```

Next, install dependencies.

```sh
python3 -m pip install .
```

Before running the tests, find a sandbox token in your [Developer Dashboard] and set a `SQUARE_SANDBOX_TOKEN` environment variable.

```sh
export SQUARE_SANDBOX_TOKEN="YOUR SANDBOX TOKEN HERE"
```

Ensure you have `pytest` installed:

```
python3 -m pip install pytest
```

And lastly, run the tests.

```sh
pytest
```

## SDK Reference

### Payments
* [Payments]
* [Refunds]
* [Disputes]
* [Checkout]
* [Apple Pay]
* [Cards]
* [Payouts]

### Terminal
* [Terminal]

### Orders
* [Orders]
* [Order Custom Attributes]

### Subscriptions
* [Subscriptions]

### Invoices
* [Invoices]

### Items
* [Catalog]
* [Inventory]

### Customers
* [Customers]
* [Customer Groups]
* [Customer Segments]

### Loyalty
* [Loyalty]

### Gift Cards
* [Gift Cards]
* [Gift Card Activities]

### Bookings
* [Bookings]
* [Booking Custom Attributes]

### Business
* [Merchants]
* [Merchant Custom Attributes]
* [Locations]
* [Location Custom Attributes]
* [Devices]
* [Cash Drawers]

### Team
* [Team]
* [Labor]

### Financials
* [Bank Accounts]

### Online
* [Sites]
* [Snippets]

### Authorization
* [Mobile Authorization]
* [OAuth]

### Webhook Subscriptions
* [Webhook Subscriptions]
## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from square.core.api_error import ApiError

try:
    client.payments.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from square import Square

client = Square(
    token="YOUR_TOKEN",
)
response = client.bank_accounts.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.payments.create(..., request_options={
    "max_retries": 1
})
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
client.payments.create(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

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
