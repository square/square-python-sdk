# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .subscription import SubscriptionParams


class DeleteSubscriptionActionResponseParams(typing_extensions.TypedDict):
    """
    Defines output parameters in a response of the [DeleteSubscriptionAction](api-endpoint:Subscriptions-DeleteSubscriptionAction)
    endpoint.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Errors encountered during the request.
    """

    subscription: typing_extensions.NotRequired[SubscriptionParams]
    """
    The subscription that has the specified action deleted.
    """
