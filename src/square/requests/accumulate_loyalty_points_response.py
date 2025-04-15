# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .loyalty_event import LoyaltyEventParams


class AccumulateLoyaltyPointsResponseParams(typing_extensions.TypedDict):
    """
    Represents an [AccumulateLoyaltyPoints](api-endpoint:Loyalty-AccumulateLoyaltyPoints) response.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    event: typing_extensions.NotRequired[LoyaltyEventParams]
    """
    The resulting loyalty event. Starting in Square version 2022-08-17, this field is no longer returned.
    """

    events: typing_extensions.NotRequired[typing.Sequence[LoyaltyEventParams]]
    """
    The resulting loyalty events. If the purchase qualifies for points, the `ACCUMULATE_POINTS` event
    is always included. When using the Orders API, the `ACCUMULATE_PROMOTION_POINTS` event is included
    if the purchase also qualifies for a loyalty promotion.
    """
