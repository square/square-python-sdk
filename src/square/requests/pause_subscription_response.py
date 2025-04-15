# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .subscription import SubscriptionParams
from .subscription_action import SubscriptionActionParams


class PauseSubscriptionResponseParams(typing_extensions.TypedDict):
    """
    Defines output parameters in a response from the
    [PauseSubscription](api-endpoint:Subscriptions-PauseSubscription) endpoint.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Errors encountered during the request.
    """

    subscription: typing_extensions.NotRequired[SubscriptionParams]
    """
    The subscription to be paused by the scheduled `PAUSE` action.
    """

    actions: typing_extensions.NotRequired[typing.Sequence[SubscriptionActionParams]]
    """
    The list of a `PAUSE` action and a possible `RESUME` action created by the request.
    """
