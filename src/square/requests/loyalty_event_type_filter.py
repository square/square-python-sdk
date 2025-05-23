# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing
from ..types.loyalty_event_type import LoyaltyEventType


class LoyaltyEventTypeFilterParams(typing_extensions.TypedDict):
    """
    Filter events by event type.
    """

    types: typing.Sequence[LoyaltyEventType]
    """
    The loyalty event types used to filter the result.
    If multiple values are specified, the endpoint uses a 
    logical OR to combine them.
    See [LoyaltyEventType](#type-loyaltyeventtype) for possible values
    """
