# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .event import EventParams
from .event_metadata import EventMetadataParams


class SearchEventsResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields that are included in the response body of
    a request to the [SearchEvents](api-endpoint:Events-SearchEvents) endpoint.

    Note: if there are errors processing the request, the events field will not be
    present.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Information on errors encountered during the request.
    """

    events: typing_extensions.NotRequired[typing.Sequence[EventParams]]
    """
    The list of [Event](entity:Event)s returned by the search.
    """

    metadata: typing_extensions.NotRequired[typing.Sequence[EventMetadataParams]]
    """
    Contains the metadata of an event. For more information, see [Event](entity:Event).
    """

    cursor: typing_extensions.NotRequired[str]
    """
    When a response is truncated, it includes a cursor that you can use in a subsequent request to fetch the next set of events. If empty, this is the final response.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """
