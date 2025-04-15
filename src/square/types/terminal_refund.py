# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .money import Money
from .action_cancel_reason import ActionCancelReason
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TerminalRefund(UncheckedBaseModel):
    """
    Represents a payment refund processed by the Square Terminal. Only supports Interac (Canadian debit network) payment refunds.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID for this `TerminalRefund`.
    """

    refund_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reference to the payment refund created by completing this `TerminalRefund`.
    """

    payment_id: str = pydantic.Field()
    """
    The unique ID of the payment being refunded.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reference to the Square order ID for the payment identified by the `payment_id`.
    """

    amount_money: Money = pydantic.Field()
    """
    The amount of money, inclusive of `tax_money`, that the `TerminalRefund` should return.
    This value is limited to the amount taken in the original payment minus any completed or
    pending refunds.
    """

    reason: str = pydantic.Field()
    """
    A description of the reason for the refund.
    """

    device_id: str = pydantic.Field()
    """
    The unique ID of the device intended for this `TerminalRefund`.
    The Id can be retrieved from /v2/devices api.
    """

    deadline_duration: typing.Optional[str] = pydantic.Field(default=None)
    """
    The RFC 3339 duration, after which the refund is automatically canceled.
    A `TerminalRefund` that is `PENDING` is automatically `CANCELED` and has a cancellation reason
    of `TIMED_OUT`.
    
    Default: 5 minutes from creation.
    
    Maximum: 5 minutes
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the `TerminalRefund`.
    Options: `PENDING`, `IN_PROGRESS`, `CANCEL_REQUESTED`, `CANCELED`, or `COMPLETED`.
    """

    cancel_reason: typing.Optional[ActionCancelReason] = pydantic.Field(default=None)
    """
    Present if the status is `CANCELED`.
    See [ActionCancelReason](#type-actioncancelreason) for possible values
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the `TerminalRefund` was created, as an RFC 3339 timestamp.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the `TerminalRefund` was last updated, as an RFC 3339 timestamp.
    """

    app_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the application that created the refund.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location of the device where the `TerminalRefund` was directed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
