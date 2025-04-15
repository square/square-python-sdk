# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .fulfillment_recipient import FulfillmentRecipient
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FulfillmentShipmentDetails(UncheckedBaseModel):
    """
    Contains the details necessary to fulfill a shipment order.
    """

    recipient: typing.Optional[FulfillmentRecipient] = pydantic.Field(default=None)
    """
    Information about the person to receive this shipment fulfillment.
    """

    carrier: typing.Optional[str] = pydantic.Field(default=None)
    """
    The shipping carrier being used to ship this fulfillment (such as UPS, FedEx, or USPS).
    """

    shipping_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note with additional information for the shipping carrier.
    """

    shipping_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the type of shipping product purchased from the carrier
    (such as First Class, Priority, or Express).
    """

    tracking_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reference number provided by the carrier to track the shipment's progress.
    """

    tracking_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the tracking webpage on the carrier's website.
    """

    placed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)
    indicating when the shipment was requested. The timestamp must be in RFC 3339 format
    (for example, "2016-09-04T23:59:33.123Z").
    """

    in_progress_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)
    indicating when this fulfillment was moved to the `RESERVED` state, which  indicates that preparation
    of this shipment has begun. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z").
    """

    packaged_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)
    indicating when this fulfillment was moved to the `PREPARED` state, which indicates that the
    fulfillment is packaged. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z").
    """

    expected_shipped_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)
    indicating when the shipment is expected to be delivered to the shipping carrier.
    The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z").
    """

    shipped_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)
    indicating when this fulfillment was moved to the `COMPLETED` state, which indicates that
    the fulfillment has been given to the shipping carrier. The timestamp must be in RFC 3339 format
    (for example, "2016-09-04T23:59:33.123Z").
    """

    canceled_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)
    indicating the shipment was canceled.
    The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z").
    """

    cancel_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of why the shipment was canceled.
    """

    failed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates)
    indicating when the shipment failed to be completed. The timestamp must be in RFC 3339 format
    (for example, "2016-09-04T23:59:33.123Z").
    """

    failure_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of why the shipment failed to be completed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
