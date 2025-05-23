# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .subscription import SubscriptionParams
from .subscription_action import SubscriptionActionParams


class ResumeSubscriptionResponseParams(typing_extensions.TypedDict):
    """
    Defines output parameters in a response from the
    [ResumeSubscription](api-endpoint:Subscriptions-ResumeSubscription) endpoint.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Errors encountered during the request.
    """

    subscription: typing_extensions.NotRequired[SubscriptionParams]
    """
    The resumed subscription.
    """

    actions: typing_extensions.NotRequired[typing.Sequence[SubscriptionActionParams]]
    """
    A list of `RESUME` actions created by the request and scheduled for the subscription.
    """
