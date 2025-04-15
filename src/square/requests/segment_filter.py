# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .filter_value import FilterValueParams


class SegmentFilterParams(typing_extensions.TypedDict):
    """
    A query filter to search for buyer-accessible appointment segments by.
    """

    service_variation_id: str
    """
    The ID of the [CatalogItemVariation](entity:CatalogItemVariation) object representing the service booked in this segment.
    """

    team_member_id_filter: typing_extensions.NotRequired[FilterValueParams]
    """
    A query filter to search for buyer-accessible appointment segments with service-providing team members matching the specified list of team member IDs.  Supported query expressions are
    - `ANY`: return the appointment segments with team members whose IDs match any member in this list.
    - `NONE`: return the appointment segments with team members whose IDs are not in this list.
    - `ALL`: not supported.
    
    When no expression is specified, any service-providing team member is eligible to fulfill the Booking.
    """
