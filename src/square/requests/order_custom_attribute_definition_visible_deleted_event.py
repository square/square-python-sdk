# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .custom_attribute_definition_event_data import CustomAttributeDefinitionEventDataParams


class OrderCustomAttributeDefinitionVisibleDeletedEventParams(typing_extensions.TypedDict):
    """
    Published when an order [custom attribute definition](entity:CustomAttributeDefinition) that is visible to the subscribing app is deleted.
    """

    merchant_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the target seller associated with the event.
    """

    type: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The type of this event. The value is `"order.custom_attribute_definition.visible.deleted"`.
    """

    event_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A unique ID for the event.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The timestamp of when the event was created, in RFC 3339 format.
    """

    data: typing_extensions.NotRequired[CustomAttributeDefinitionEventDataParams]
    """
    The data associated with the event.
    """
