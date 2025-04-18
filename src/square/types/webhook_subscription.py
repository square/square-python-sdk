# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class WebhookSubscription(UncheckedBaseModel):
    """
    Represents the details of a webhook subscription, including notification URL,
    event types, and signature key.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Square-generated unique ID for the subscription.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of this subscription.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the subscription is enabled (`true`) or not (`false`).
    """

    event_types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The event types associated with this subscription.
    """

    notification_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to which webhooks are sent.
    """

    api_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The API version of the subscription.
    This field is optional for `CreateWebhookSubscription`. 
    The value defaults to the API version used by the application.
    """

    signature_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated signature key used to validate the origin of the webhook event.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the subscription was created, in RFC 3339 format. For example, "2016-09-04T23:59:33.123Z".
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the subscription was last updated, in RFC 3339 format.
    For example, "2016-09-04T23:59:33.123Z".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
