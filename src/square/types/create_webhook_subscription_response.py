# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .webhook_subscription import WebhookSubscription
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateWebhookSubscriptionResponse(UncheckedBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [CreateWebhookSubscription](api-endpoint:WebhookSubscriptions-CreateWebhookSubscription) endpoint.

    Note: if there are errors processing the request, the [Subscription](entity:WebhookSubscription) will not be
    present.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information on errors encountered during the request.
    """

    subscription: typing.Optional[WebhookSubscription] = pydantic.Field(default=None)
    """
    The new [Subscription](entity:WebhookSubscription).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
