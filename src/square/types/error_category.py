# This file was auto-generated by Fern from our API Definition.

import typing

ErrorCategory = typing.Union[
    typing.Literal[
        "API_ERROR",
        "AUTHENTICATION_ERROR",
        "INVALID_REQUEST_ERROR",
        "RATE_LIMIT_ERROR",
        "PAYMENT_METHOD_ERROR",
        "REFUND_ERROR",
        "MERCHANT_SUBSCRIPTION_ERROR",
        "EXTERNAL_VENDOR_ERROR",
    ],
    typing.Any,
]
