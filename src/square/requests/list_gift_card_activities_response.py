# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .gift_card_activity import GiftCardActivityParams


class ListGiftCardActivitiesResponseParams(typing_extensions.TypedDict):
    """
    A response that contains a list of `GiftCardActivity` objects. If the request resulted in errors,
    the response contains a set of `Error` objects.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    gift_card_activities: typing_extensions.NotRequired[typing.Sequence[GiftCardActivityParams]]
    """
    The requested gift card activities or an empty object if none are found.
    """

    cursor: typing_extensions.NotRequired[str]
    """
    When a response is truncated, it includes a cursor that you can use in a
    subsequent request to retrieve the next set of activities. If a cursor is not present, this is
    the final response.
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """
