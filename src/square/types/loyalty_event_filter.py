# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .loyalty_event_loyalty_account_filter import LoyaltyEventLoyaltyAccountFilter
import pydantic
from .loyalty_event_type_filter import LoyaltyEventTypeFilter
from .loyalty_event_date_time_filter import LoyaltyEventDateTimeFilter
from .loyalty_event_location_filter import LoyaltyEventLocationFilter
from .loyalty_event_order_filter import LoyaltyEventOrderFilter
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LoyaltyEventFilter(UncheckedBaseModel):
    """
    The filtering criteria. If the request specifies multiple filters,
    the endpoint uses a logical AND to evaluate them.
    """

    loyalty_account_filter: typing.Optional[LoyaltyEventLoyaltyAccountFilter] = pydantic.Field(default=None)
    """
    Filter events by loyalty account.
    """

    type_filter: typing.Optional[LoyaltyEventTypeFilter] = pydantic.Field(default=None)
    """
    Filter events by event type.
    """

    date_time_filter: typing.Optional[LoyaltyEventDateTimeFilter] = pydantic.Field(default=None)
    """
    Filter events by date time range. 
    For each range, the start time is inclusive and the end time 
    is exclusive.
    """

    location_filter: typing.Optional[LoyaltyEventLocationFilter] = pydantic.Field(default=None)
    """
    Filter events by location.
    """

    order_filter: typing.Optional[LoyaltyEventOrderFilter] = pydantic.Field(default=None)
    """
    Filter events by the order associated with the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
