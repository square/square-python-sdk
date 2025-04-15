# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class PaymentBalanceActivityDisputeDetailParams(typing_extensions.TypedDict):
    payment_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the payment associated with this activity.
    """

    dispute_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the dispute associated with this activity.
    """
