# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .custom_attribute_event_data import CustomAttributeEventData
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CustomerCustomAttributeDeletedPublicEvent(UncheckedBaseModel):
    """
    Published when a customer [custom attribute](entity:CustomAttribute) that is visible
    to all applications is deleted. A notification is sent when any application deletes a custom attribute
    whose `visibility` is `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

    This event is replaced by
    [customer.custom_attribute.visible.deleted](webhook:customer.custom_attribute.visible.deleted),
    which applies to custom attributes that are visible to the subscribing application.
    """

    merchant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the seller associated with the event that triggered the event notification.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of this event. The value is `"customer.custom_attribute.public.deleted"`.
    """

    event_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID for the event notification.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp that indicates when the event notification was created, in RFC 3339 format.
    """

    data: typing.Optional[CustomAttributeEventData] = pydantic.Field(default=None)
    """
    The data associated with the event that triggered the event notification.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
