# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .time_range import TimeRange
import pydantic
import typing
from .segment_filter import SegmentFilter
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchAvailabilityFilter(UncheckedBaseModel):
    """
    A query filter to search for buyer-accessible availabilities by.
    """

    start_at_range: TimeRange = pydantic.Field()
    """
    The query expression to search for buy-accessible availabilities with their starting times falling within the specified time range.
    The time range must be at least 24 hours and at most 32 days long.
    For waitlist availabilities, the time range can be 0 or more up to 367 days long.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The query expression to search for buyer-accessible availabilities with their location IDs matching the specified location ID.
    This query expression cannot be set if `booking_id` is set.
    """

    segment_filters: typing.Optional[typing.List[SegmentFilter]] = pydantic.Field(default=None)
    """
    The query expression to search for buyer-accessible availabilities matching the specified list of segment filters.
    If the size of the `segment_filters` list is `n`, the search returns availabilities with `n` segments per availability.
    
    This query expression cannot be set if `booking_id` is set.
    """

    booking_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The query expression to search for buyer-accessible availabilities for an existing booking by matching the specified `booking_id` value.
    This is commonly used to reschedule an appointment.
    If this expression is set, the `location_id` and `segment_filters` expressions cannot be set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
