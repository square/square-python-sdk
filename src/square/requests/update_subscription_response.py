# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .subscription import SubscriptionParams


class UpdateSubscriptionResponseParams(typing_extensions.TypedDict):
    """
    Defines output parameters in a response from the
    [UpdateSubscription](api-endpoint:Subscriptions-UpdateSubscription) endpoint.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Errors encountered during the request.
    """

    subscription: typing_extensions.NotRequired[SubscriptionParams]
    """
    The updated subscription.
    """
