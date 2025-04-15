# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from .destination_details import DestinationDetails
from .money import Money
from .processing_fee import ProcessingFee
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PaymentRefund(UncheckedBaseModel):
    """
    Represents a refund of a payment made using Square. Contains information about
    the original payment and the amount of money refunded.
    """

    id: str = pydantic.Field()
    """
    The unique ID for this refund, generated by Square.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The refund's status:
    - `PENDING` - Awaiting approval.
    - `COMPLETED` - Successfully completed.
    - `REJECTED` - The refund was rejected.
    - `FAILED` - An error occurred.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location ID associated with the payment this refund is attached to.
    """

    unlinked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Flag indicating whether or not the refund is linked to an existing payment in Square.
    """

    destination_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The destination type for this refund.
    
    Current values include `CARD`, `BANK_ACCOUNT`, `WALLET`, `BUY_NOW_PAY_LATER`, `CASH`,
    `EXTERNAL`, and `SQUARE_ACCOUNT`.
    """

    destination_details: typing.Optional[DestinationDetails] = pydantic.Field(default=None)
    """
    Contains information about the refund destination. This field is populated only if
    `destination_id` is defined in the `RefundPayment` request.
    """

    amount_money: Money = pydantic.Field()
    """
    The amount of money refunded. This amount is specified in the smallest denomination
    of the applicable currency (for example, US dollar amounts are specified in cents).
    """

    app_fee_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount of money the application developer contributed to help cover the refunded amount.
    This amount is specified in the smallest denomination of the applicable currency (for example,
    US dollar amounts are specified in cents). For more information, see
    [Working with Monetary Amounts](https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts).
    """

    processing_fee: typing.Optional[typing.List[ProcessingFee]] = pydantic.Field(default=None)
    """
    Processing fees and fee adjustments assessed by Square for this refund.
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the payment associated with this refund.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the order associated with the refund.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason for the refund.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the refund was created, in RFC 3339 format.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the refund was last updated, in RFC 3339 format.
    """

    team_member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional ID of the team member associated with taking the payment.
    """

    terminal_refund_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional ID for a Terminal refund.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
