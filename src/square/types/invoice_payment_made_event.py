# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .invoice_payment_made_event_data import InvoicePaymentMadeEventData
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class InvoicePaymentMadeEvent(UncheckedBaseModel):
    """
    Published when a payment that is associated with an [invoice](entity:Invoice) is completed.
    For more information about invoice payments, see [Pay an invoice](https://developer.squareup.com/docs/invoices-api/pay-refund-invoices#pay-invoice).
    """

    merchant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the target merchant associated with the event.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of event this represents, `"invoice.payment_made"`.
    """

    event_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID for the event.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timestamp of when the event was created, in RFC 3339 format.
    """

    data: typing.Optional[InvoicePaymentMadeEventData] = pydantic.Field(default=None)
    """
    Data associated with the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
