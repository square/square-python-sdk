# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .loyalty_account_deleted_event_object import LoyaltyAccountDeletedEventObjectParams


class LoyaltyAccountDeletedEventDataParams(typing_extensions.TypedDict):
    """
    The data associated with a `loyalty.account.deleted` event.
    """

    type: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The type of object affected by the event. For this event, the value is `loyalty_account`.
    """

    id: typing_extensions.NotRequired[str]
    """
    The ID of the affected loyalty account.
    """

    object: typing_extensions.NotRequired[LoyaltyAccountDeletedEventObjectParams]
    """
    An object that contains the loyalty account that was deleted.
    """
