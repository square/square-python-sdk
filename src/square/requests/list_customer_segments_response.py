# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .customer_segment import CustomerSegmentParams


class ListCustomerSegmentsResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields that are included in the response body for requests to the `ListCustomerSegments` endpoint.

    Either `errors` or `segments` is present in a given response (never both).
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    segments: typing_extensions.NotRequired[typing.Sequence[CustomerSegmentParams]]
    """
    The list of customer segments belonging to the associated Square account.
    """

    cursor: typing_extensions.NotRequired[str]
    """
    A pagination cursor to be used in subsequent calls to `ListCustomerSegments`
    to retrieve the next set of query results. The cursor is only present if the request succeeded and
    additional results are available.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """
