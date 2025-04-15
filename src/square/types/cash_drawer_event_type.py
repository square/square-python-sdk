# This file was auto-generated by Fern from our API Definition.

import typing

CashDrawerEventType = typing.Union[
    typing.Literal[
        "NO_SALE",
        "CASH_TENDER_PAYMENT",
        "OTHER_TENDER_PAYMENT",
        "CASH_TENDER_CANCELLED_PAYMENT",
        "OTHER_TENDER_CANCELLED_PAYMENT",
        "CASH_TENDER_REFUND",
        "OTHER_TENDER_REFUND",
        "PAID_IN",
        "PAID_OUT",
    ],
    typing.Any,
]
