![Square logo]

# Square Python SDK

[![Build](https://github.com/square/square-python-sdk/actions/workflows/python-package.yml/badge.svg)](https://github.com/square/square-python-sdk/actions/workflows/python-package.yml)
[![PyPi version](https://badge.fury.io/py/squareup.svg?new)](https://badge.fury.io/py/squareup)
[![Apache-2 license](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)

Use this library to integrate Square payments into your app and grow your business with Square APIs including Catalog, Customers, Employees, Inventory, Labor, Locations, and Orders.

* [Requirements](#requirements)
* [Installation](#installation)
* [Quickstart](#quickstart)
* [Usage](#usage)
* [Tests](#tests)
* [SDK Reference](#sdk-reference)
* [Deprecated APIs](#deprecated-apis)

## Requirements

Use of the Python SDK requires:

* Python 3 version 3.7 or higher

## Installation

For more information, see [Set Up Your Square SDK for a Python Project](https://developer.squareup.com/docs/sdks/python/setup-project).

## Quickstart

For more information, see [Square Python SDK Quickstart](https://developer.squareup.com/docs/sdks/python/quick-start).

## Usage
For more information, see [Using the Square Python SDK](https://developer.squareup.com/docs/sdks/python/using-python-sdk).

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
## Deprecated APIs

The following Square APIs are [deprecated](https://developer.squareup.com/docs/build-basics/api-lifecycle):

* [Employees] - replaced by the [Team] API. For more information, see [Migrate from the Employees API](https://developer.squareup.com/docs/team/migrate-from-v2-employees).

* [Transactions] - replaced by the [Orders] and [Payments] APIs.  For more information, see [Migrate from the Transactions API](https://developer.squareup.com/docs/payments-api/migrate-from-transactions-api).
 
[//]: # "Link anchor definitions"
[Square Logo]: https://docs.connect.squareup.com/images/github/github-square-logo.svg
[Developer Dashboard]: https://developer.squareup.com/apps
[Square API]: https://squareup.com/developers
[sign up for a developer account]: https://squareup.com/signup?v=developers
[Client]: doc/client.md
[Devices]: doc/api/devices.md
[Disputes]: doc/api/disputes.md
[Terminal]: doc/api/terminal.md
[Cash Drawers]: doc/api/cash-drawers.md
[Vendors]: doc/api/vendors.md
[Customer Groups]: doc/api/customer-groups.md
[Customer Custom Attributes]: doc/api/customer-custom-attributes.md
[Customer Segments]: doc/api/customer-segments.md
[Bank Accounts]: doc/api/bank-accounts.md
[Payments]: doc/api/payments.md
[Checkout]: doc/api/checkout.md
[Catalog]: doc/api/catalog.md
[Customers]: doc/api/customers.md
[Inventory]: doc/api/inventory.md
[Labor]: doc/api/labor.md
[Loyalty]: doc/api/loyalty.md
[Bookings]: doc/api/bookings.md
[Booking Custom Attributes]: doc/api/booking-custom-attributes.md
[Locations]: doc/api/locations.md
[Location Custom Attributes]: doc/api/location-custom-attributes.md
[Merchants]: doc/api/merchants.md
[Merchant Custom Attributes]: doc/api/merchant-custom-attributes.md
[Orders]: doc/api/orders.md
[Order Custom Attributes]: doc/api/order-custom-attributes.md
[Invoices]: doc/api/invoices.md
[Apple Pay]: doc/api/apple-pay.md
[Refunds]: doc/api/refunds.md
[Subscriptions]: doc/api/subscriptions.md
[Mobile Authorization]: doc/api/mobile-authorization.md
[OAuth]: doc/api/o-auth.md
[Team]: doc/api/team.md
[Python SDK]: https://github.com/square/square-python-sdk
[Locations overview]: https://developer.squareup.com/docs/locations-api/what-it-does
[OAuth overview]: https://developer.squareup.com/docs/oauth-api/what-it-does
[Sites]: doc/api/sites.md
[Snippets]: doc/api/snippets.md
[Cards]: doc/api/cards.md
[Payouts]: doc/api/payouts.md
[Gift Cards]: doc/api/gift-cards.md
[Gift Card Activities]: doc/api/gift-card-activities.md
[Employees]: doc/api/employees.md
[Transactions]: doc/api/transactions.md
[Webhook Subscriptions]: doc/api/webhook-subscriptions.md
