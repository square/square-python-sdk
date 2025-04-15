# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .subscription import Subscription
from .subscription_action import SubscriptionAction
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ResumeSubscriptionResponse(UncheckedBaseModel):
    """
    Defines output parameters in a response from the
    [ResumeSubscription](api-endpoint:Subscriptions-ResumeSubscription) endpoint.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Errors encountered during the request.
    """

    subscription: typing.Optional[Subscription] = pydantic.Field(default=None)
    """
    The resumed subscription.
    """

    actions: typing.Optional[typing.List[SubscriptionAction]] = pydantic.Field(default=None)
    """
    A list of `RESUME` actions created by the request and scheduled for the subscription.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
